{%- capture title -%}
AssertionMerger
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}

Merges variety assertion columns coming from Assertion annotators like `sparknlp_jsl.annotator.assertion.AssertionDLModel`.
AssertionMerger can filter, prioritize and merge assertion annotations by using proper parameters.
See Also: `sparknlp_jsl.annotator.WhiteBlackListParams` for filtering options.

Parameters:

- `mergeOverlapping` *(Bool)*: Whether to merge overlapping matched assertions.

- `applyFilterBeforeMerge` *(Bool)*: Whether to apply filtering before merging.

- `assertionsConfidence` *(dict[str, float])*: Pairs (assertion,confidenceThreshold) to filter assertions which have confidence lower than the confidence threshold.

- `orderingFeatures` *(list[str])*: Specifies the ordering features to use for overlapping entities.
  Possible values include: 'begin', 'end', 'length', 'source', 'confidence'.
  Default: ['begin', 'length', 'source']

- `selectionStrategy` *(str)*: Determines the strategy for selecting annotations.
  Annotations can be selected either sequentially based on their order (Sequential) or using a more diverse strategy (DiverseLonger).
  Currently, only Sequential and DiverseLonger options are available. Default: Sequential.

- `defaultConfidence` *(float)*: When the confidence value is included in the orderingFeatures and a given annotation does not have any confidence,
  this parameter determines the value to be used. The default value is 0.

- `assertionSourcePrecedence` *(str)*: Specifies the assertion sources to use for prioritizing overlapping annotations when the 'source' ordering feature is utilized.
  This parameter contains a comma-separated list of assertion sources that drive the prioritization.
  Annotations will be prioritized based on the order of the given string.

- `sortByBegin` *(Bool)*: Whether to sort the annotations by begin at the end of the merge and filter process. Default: False.

- `blackList` *(list[str])*: If defined, list of entities to ignore. The rest will be processed.

- `whiteList` *(list[str])*:  If defined, list of entities to process. The rest will be ignored. Do not include IOB prefix on labels.

- `caseSensitive` *(Bool)*: Determines whether the definitions of the white listed and black listed entities are case sensitive. Default: True.

- `majorityVoting` *(Bool)*: Whether to use majority voting to resolve conflicts. Default: False.

{%- endcapture -%}

{%- capture model_input_anno -%}
ASSERTION
{%- endcapture -%}

{%- capture model_output_anno -%}
ASSERTION
{%- endcapture -%}

{%- capture model_python_medical -%}

from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_jsl = medical.NerModel.pretrained("ner_jsl", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner_jsl")\
    #.setIncludeAllConfidenceScores(False)

ner_jsl_converter = medical.NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner_jsl"]) \
    .setOutputCol("ner_jsl_chunk")\
    .setWhiteList(["SYMPTOM","VS_FINDING","DISEASE_SYNDROME_DISORDER","ADMISSION_DISCHARGE","PROCEDURE"])

assertion_jsl = medical.AssertionDLModel.pretrained("assertion_jsl_augmented", "en", "clinical/models") \
    .setInputCols(["sentence", "ner_jsl_chunk", "embeddings"]) \
    .setOutputCol("assertion_jsl")\
    .setEntityAssertionCaseSensitive(False)

ner_clinical = medical.NerModel.pretrained("ner_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner_clinical")\
    #.setIncludeAllConfidenceScores(False)

ner_clinical_converter = medical.NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner_clinical"]) \
    .setOutputCol("ner_clinical_chunk")\

assertion_dl = medical.AssertionDLModel.pretrained("assertion_dl", "en", "clinical/models") \
    .setInputCols(["sentence", "ner_clinical_chunk", "embeddings"]) \
    .setOutputCol("assertion_dl")

assertion_merger = medical.AssertionMerger() \
    .setInputCols("assertion_jsl", "assertion_dl") \
    .setOutputCol("assertion_merger") \
    .setMergeOverlapping(True) \
    .setSelectionStrategy("sequential") \
    .setAssertionSourcePrecedence("assertion_dl, assertion_jsl") \
    .setCaseSensitive(False) \
    .setAssertionsConfidence({"past": 0.70}) \
    .setOrderingFeatures(["length", "source", "confidence"]) \
    .setDefaultConfidence(0.50)\
    #.setBlackList(["HYPothetical"])

pipeline = Pipeline( stages =[document_assembler,
                              sentence_detector,
                              tokenizer,
                              word_embeddings,
                              ner_jsl,
                              ner_jsl_converter,
                              assertion_jsl,
                              ner_clinical,
                              ner_clinical_converter,
                              assertion_dl,
                              assertion_merger])

data = spark.createDataFrame([
                        """Patient had a headache for the last 2 weeks, and appears anxious when she walks fast. No alopecia noted. She denies pain. Her father is paralyzed and it is a stressor for her. She got antidepressant. We prescribed sleeping pills for her current insomnia."""], StringType()).toDF("text")


data = data.coalesce(1).withColumn("idx", F.monotonically_increasing_id())
results = pipeline.fit(data).transform(data)

## Result

+---+--------------+-----+---+---------+---------+----------------+----------+
|idx|ner_chunk     |begin|end|ner_label|assertion|assertion_source|confidence|
+---+--------------+-----+---+---------+---------+----------------+----------+
|0  |headache      |14   |21 |Symptom  |Past     |assertion_jsl   |0.9999    |
|0  |anxious       |57   |63 |PROBLEM  |present  |assertion_dl    |0.9392    |
|0  |alopecia      |89   |96 |PROBLEM  |absent   |assertion_dl    |0.9992    |
|0  |pain          |116  |119|PROBLEM  |absent   |assertion_dl    |0.9884    |
|0  |paralyzed     |136  |144|Symptom  |Family   |assertion_jsl   |0.9995    |
|0  |stressor      |158  |165|Symptom  |Family   |assertion_jsl   |1.0       |
|0  |antidepressant|184  |197|TREATMENT|present  |assertion_dl    |0.9628    |
|0  |sleeping pills|214  |227|TREATMENT|present  |assertion_dl    |0.998     |
|0  |insomnia      |245  |252|Symptom  |Past     |assertion_jsl   |0.9862    |
+---+--------------+-----+---+---------+---------+----------------+----------+

{%- endcapture -%}

{%- capture model_scala_medical -%}
import spark.implicits._

val document_assembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val sentence_detector = new SentenceDetector()
      .setInputCols(Array("document"))
      .setOutputCol("sentence")

val tokenizer = new Tokenizer()
      .setInputCols(Array("sentence"))
      .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
      .setInputCols(Array("sentence", "token"))
      .setOutputCol("embeddings")

val ner_jsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")
      .setInputCols(Array("sentence", "token", "embeddings"))
      .setOutputCol("ner_jsl")
    //.setIncludeAllConfidenceScores(false)

val ner_jsl_converter = new NerConverterInternal()
      .setInputCols(Array("sentence", "token", "ner_jsl"))
      .setOutputCol("ner_jsl_chunk")
      .setWhiteList(Array("SYMPTOM", "VS_FINDING", "DISEASE_SYNDROME_DISORDER", "ADMISSION_DISCHARGE", "PROCEDURE"))

val assertion_jsl = AssertionDLModel.pretrained("assertion_jsl_augmented", "en", "clinical/models")
      .setInputCols(Array("sentence", "ner_jsl_chunk", "embeddings"))
      .setOutputCol("assertion_jsl")
      .setEntityAssertionCaseSensitive(false)

val ner_clinical = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
      .setInputCols(Array("sentence", "token", "embeddings"))
      .setOutputCol("ner_clinical")
    //.setIncludeAllConfidenceScores(false)

val ner_clinical_converter = new NerConverterInternal()
      .setInputCols(Array("sentence", "token", "ner_clinical"))
      .setOutputCol("ner_clinical_chunk")

val assertion_dl = AssertionDLModel.pretrained("assertion_dl", "en", "clinical/models")
      .setInputCols(Array("sentence", "ner_clinical_chunk", "embeddings"))
      .setOutputCol("assertion_dl")

val assertion_merger = new AssertionMerger()
      .setInputCols("assertion_jsl", "assertion_dl")
      .setOutputCol("assertion_merger")
      .setMergeOverlapping(true)
      .setSelectionStrategy("sequential")
      .setAssertionSourcePrecedence("assertion_dl, assertion_jsl")
      .setCaseSensitive(false)
      .setAssertionsConfidence(Map("past"-> 0.70f))
      .setOrderingFeatures(Array("length", "source", "confidence"))
      .setDefaultConfidence(0.50f)
     // .setBlackList(("HYPothetical"))

val pipeline = new Pipeline().setStages(Array(document_assembler,
          sentence_detector,
          tokenizer,
          word_embeddings,
          ner_jsl,
          ner_jsl_converter,
          assertion_jsl,
          ner_clinical,
          ner_clinical_converter,
          assertion_dl,
          assertion_merger))

val text = "Patient had a headache for the last 2 weeks, and appears anxious when she walks fast. No alopecia noted. She denies pain. Her father is paralyzed and it is a stressor for her. She got antidepressant. We prescribed sleeping pills for her current insomnia."

val data = Seq(text).toDF("text")
//val data = data.coalesce(1).withColumn("idx", F.monotonically_increasing_id())

val results = pipeline.fit(data).transform(data)

// Result

+---+--------------+-----+---+---------+---------+----------------+----------+
|idx|ner_chunk     |begin|end|ner_label|assertion|assertion_source|confidence|
+---+--------------+-----+---+---------+---------+----------------+----------+
|0  |headache      |14   |21 |Symptom  |Past     |assertion_jsl   |0.9999    |
|0  |anxious       |57   |63 |PROBLEM  |present  |assertion_dl    |0.9392    |
|0  |alopecia      |89   |96 |PROBLEM  |absent   |assertion_dl    |0.9992    |
|0  |pain          |116  |119|PROBLEM  |absent   |assertion_dl    |0.9884    |
|0  |paralyzed     |136  |144|Symptom  |Family   |assertion_jsl   |0.9995    |
|0  |stressor      |158  |165|Symptom  |Family   |assertion_jsl   |1.0       |
|0  |antidepressant|184  |197|TREATMENT|present  |assertion_dl    |0.9628    |
|0  |sleeping pills|214  |227|TREATMENT|present  |assertion_dl    |0.998     |
|0  |insomnia      |245  |252|Symptom  |Past     |assertion_jsl   |0.9862    |
+---+--------------+-----+---+---------+---------+----------------+----------+

{%- endcapture -%}


{%- capture model_api_link -%}
[AssertionMerger](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/assertion/merger/AssertionMerger.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[AssertionMerger](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/assertion/assertion_merger/index.html)
{%- endcapture -%}



{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
model_api_link=model_api_link
model_python_api_link=model_python_api_link
%}
