{%- capture title -%}
RelationExtraction
{%- endcapture -%}

{%- capture approach -%}
approach
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
Extracts and classifies instances of relations between named entities.

Parameters:

- `predictionThreshold` *(Float)*: Sets minimal activation of the target unit to encode a new relation instance.

- `relationPairs` *(List[Str])*: List of dash-separated pairs of named entities. For example, [“Biomarker-RelativeDay”] will process all relations between entities of type “Biomarker” and “RelativeDay”.

- `relationPairsCaseSensitive` *(Bool)*: Determines whether relation pairs are case sensitive.

- `relationTypePerPair` *dict[str, list[str]]*: List of entity pairs per relations which limit the entities can form a relation. For example, {“CAUSE”: [“PROBLEM”, “SYMPTOM”]} which only let a “CAUSE” relation to hold between a problem (“PROBLEM) and a symptom (“SYMTOM”).

- `maxSyntacticDistance` *(Int)*: Maximal syntactic distance, as threshold (Default: 0). Determine how far the “from entity” can be from the “to entity” in the text. Increasing this value will increase recall, but also increase the number of false positives.

- `customLabels` *(dict[str, str])*: Custom relation labels.

- `multiClass` *(Bool)*: If multiClass is set, the model will return all the labels with corresponding scores (Default: False)

For pretrained models please see the
[Models Hub](https://nlp.johnsnowlabs.com/models?task=Relation+Extraction) for available models.

{%- endcapture -%}

{%- capture model_input_anno -%}
WORD_EMBEDDINGS, POS, CHUNK, DEPENDENCY
{%- endcapture -%}

{%- capture model_output_anno -%}
CATEGORY
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

documenter = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentencer = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentences")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentences"])\
    .setOutputCol("tokens")

words_embedder = nlp.WordEmbeddingsModel()\
    .pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentences", "tokens"])\
    .setOutputCol("embeddings")

pos_tagger = nlp.PerceptronModel()\
    .pretrained("pos_clinical", "en", "clinical/models") \
    .setInputCols(["sentences", "tokens"])\
    .setOutputCol("pos_tags")

ner_tagger = medical.NerModel()\
    .pretrained("ner_posology", "en", "clinical/models")\
    .setInputCols("sentences", "tokens", "embeddings")\
    .setOutputCol("ner_tags")

ner_chunker = medical.NerConverterInternal()\
    .setInputCols(["sentences", "tokens", "ner_tags"])\
    .setOutputCol("ner_chunks")

dependency_parser = nlp.DependencyParserModel()\
    .pretrained("dependency_conllu", "en")\
    .setInputCols(["sentences", "pos_tags", "tokens"])\
    .setOutputCol("dependencies")

reModel = medical.RelationExtractionModel()\
    .pretrained("posology_re")\
    .setInputCols(["embeddings", "pos_tags", "ner_chunks", "dependencies"])\
    .setOutputCol("relations")\
    .setMaxSyntacticDistance(4)

pipeline = nlp.Pipeline(stages=[
    documenter,
    sentencer,
    tokenizer,
    words_embedder,
    pos_tagger,
    ner_tagger,
    ner_chunker,
    dependency_parser,
    reModel
])

text = """
The patient was prescribed 1 unit of Advil for 5 days after meals. The patient was also
given 1 unit of Metformin daily.
He was seen by the endocrinology service and she was discharged on 40 units of insulin glargine at night ,
12 units of insulin lispro with meals , and metformin 1000 mg two times a day.
"""
df = spark.createDataFrame([[text]]).toDF("text")
result = pipeline.fit(df).transform(df)

# Show results
result.select(F.explode(F.arrays_zip(
                              result.relations.result,
                              result.relations.metadata)).alias("cols"))\
.select(
    F.expr("cols['1']['chunk1']").alias("chunk1"),
    F.expr("cols['1']['chunk2']").alias("chunk2"),
    F.expr("cols['1']['entity1']").alias("entity1"),
    F.expr("cols['1']['entity2']").alias("entity2"),
    F.expr("cols['0']").alias("relations"),
    F.expr("cols['1']['confidence']").alias("confidence")).show(5, truncate=False)

+---------+----------------+-------+---------+--------------+----------+
|chunk1   |chunk2          |entity1|entity2  |relations     |confidence|
+---------+----------------+-------+---------+--------------+----------+
|1 unit   |Advil           |DOSAGE |DRUG     |DOSAGE-DRUG   |1.0       |
|Advil    |for 5 days      |DRUG   |DURATION |DRUG-DURATION |1.0       |
|1 unit   |Metformin       |DOSAGE |DRUG     |DOSAGE-DRUG   |1.0       |
|Metformin|daily           |DRUG   |FREQUENCY|DRUG-FREQUENCY|1.0       |
|40 units |insulin glargine|DOSAGE |DRUG     |DOSAGE-DRUG   |1.0       |
+---------+----------------+-------+---------+--------------+----------+

{%- endcapture -%}

{%- capture model_scala_medical -%}
import spark.implicits._

val documenter = new DocumentAssembler()
    .setInputCol("text") 
    .setOutputCol("document") 

val sentencer = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentences") 

val tokenizer = new Tokenizer()
    .setInputCols("sentences") 
    .setOutputCol("tokens") 

val words_embedder = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models") 
    .setInputCols(Array("sentences","tokens")) 
    .setOutputCol("embeddings") 

val pos_tagger = PerceptronModel.pretrained("pos_clinical","en","clinical/models") 
    .setInputCols(Array("sentences","tokens")) 
    .setOutputCol("pos_tags") 

val ner_tagger = MedicalNerModel.pretrained("ner_posology","en","clinical/models") 
    .setInputCols("sentences","tokens","embeddings") 
    .setOutputCol("ner_tags") 

val ner_chunker = new NerConverterInternal()
    .setInputCols(Array("sentences","tokens","ner_tags")) 
    .setOutputCol("ner_chunks") 

val dependency_parser = DependencyParserModel.pretrained("dependency_conllu","en") 
    .setInputCols(Array("sentences","pos_tags","tokens")) 
    .setOutputCol("dependencies") 

val reModel = RelationExtractionModel.pretrained("posology_re") 
    .setInputCols(Array("embeddings","pos_tags","ner_chunks","dependencies")) 
    .setOutputCol("relations") 
    .setMaxSyntacticDistance(4) 

val pipeline = new Pipeline().setStages(Array(
                                             documenter, 
                                             sentencer, 
                                             tokenizer,
                                             words_embedder, 
                                             pos_tagger, 
                                             ner_tagger, 
                                             ner_chunker, 
                                             dependency_parser, 
                                             reModel )) 

val text = " The patient was prescribed 1 unit of Advil for 5 days after meals. The patient was also given 1 unit of Metformin daily. He was seen by the endocrinology service and she was discharged on 40 units of insulin glargine at night , 12 units of insulin lispro with meals ,and metformin 1000 mg two times a day. " 

val df = Seq(text) .toDF("text") 
val result = pipeline.fit(df) .transform(df) 

// Show results

+---------+----------------+-------+---------+--------------+----------+
|chunk1   |chunk2          |entity1|entity2  |relations     |confidence|
+---------+----------------+-------+---------+--------------+----------+
|1 unit   |Advil           |DOSAGE |DRUG     |DOSAGE-DRUG   |1.0       |
|Advil    |for 5 days      |DRUG   |DURATION |DRUG-DURATION |1.0       |
|1 unit   |Metformin       |DOSAGE |DRUG     |DOSAGE-DRUG   |1.0       |
|Metformin|daily           |DRUG   |FREQUENCY|DRUG-FREQUENCY|1.0       |
|40 units |insulin glargine|DOSAGE |DRUG     |DOSAGE-DRUG   |1.0       |
+---------+----------------+-------+---------+--------------+----------+

{%- endcapture -%}


{%- capture model_api_link -%}
[RelationExtractionModel](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/re/RelationExtractionModel.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[RelationExtractionModel](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/re/relation_extraction/index.html#sparknlp_jsl.annotator.re.relation_extraction.RelationExtractionModel)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[RelationExtractionModelNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/RelationExtractionModel.ipynb)
{%- endcapture -%}

{%- capture approach_description -%}
Trains a TensorFlow model for relation extraction. 

To train a custom relation extraction model, you need to first creat a Tensorflow graph using either the `TfGraphBuilder` annotator or the `tf_graph` module. Then, set the path to the Tensorflow graph using the method `.setModelFile("path/to/tensorflow_graph.pb")`.

If the parameter `relationDirectionCol` is set, the model will be trained using the direction information (see the parameter decription for details). Otherwise, the model won't have direction between the relation of the entities.

After training a model (using the `.fit()` method), the resulting object is of class `RelationExtractionModel`.

Parameters:

- `FromEntity`: (begin_col: str, end_col: str, label_col: str) Sets from entity

- `begin_col` Column that has a reference of where the chunk begins 

- `end_col`: Column that has a reference of where the chunk ends

- `label_col`: Column that has a reference what are the type of chunk

- `ToEntity`: (begin_col: str, end_col: str, label_col: str) Sets to entity

- `begin_col` Column that has a reference of where the chunk begins 

- `end_col`: Column that has a reference of where the chunk ends

- `label_col`: Column that has a reference what are the type of chunk

- `CustomLabels`: (labels: dict[str, str]) Sets custom relation labels

- `labels`: Dictionary which maps old to new labels

- `RelationDirectionCol`: (col: str) Relation direction column (possible values are: "none", "left" or "right"). If this parameter is not set, the model will not have direction between the relation of the entities

- `col` Column contains the relation direction values

- `PretrainedModelPath` (value: str) Path to an already trained model saved to disk, which is used as a starting point for training the new model

- `ОverrideExistingLabels` (bool) Whether to override already learned labels when using a pretrained model to initialize the new model. Default is ‘true’

- `batchSize`: (Int) Size for each batch in the optimization process

- `EpochsNumber` (Int) Maximum number of epochs to train

- `Dropout`: (Float) Dropout at the output of each layer

- `LearningRate`: (Float) Learning rate for the optimization process

- `OutputLogsPath`: (Str) Folder path to save training logs. If no path is specified, the logs won't be stored in disk. The path can be a local file path, a distributed file path (HDFS, DBFS), or a cloud storage (S3).

- `ModelFile`: (Str) The path to the Tensorflow graph

- `FixImbalance` (Float) Fix the imbalance in the training set by replicating examples of under represented categories

- `ValidationSplit` (Float) The proportion of training dataset to be used as validation set

- `OverrideExistingLabels` (Boolean) Controls whether to override already learned lebels when using a pretrained model to initialize the new model. A value of true will override existing labels

- `MultiClass` (Boolean) If multiClass is set, the model will return all the labels with corresponding scores. By default, multiClass is false.

- `ModelFile` (Str) Location of file of the model used for classification

- `MaxSyntacticDistance` (Int) Maximal syntactic distance, as threshold (Default: 0)
{%- endcapture -%}

{%- capture approach_input_anno -%}
WORD_EMBEDDINGS, POS, CHUNK, DEPENDENCY
{%- endcapture -%}

{%- capture approach_output_anno -%}
NONE
{%- endcapture -%}

{%- capture approach_python_medical -%}
from johnsnowlabs import nlp, medical
# Defining pipeline stages to extract entities first
documentAssembler = nlp.DocumentAssembler() \
  .setInputCol("text") \
  .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
  .setInputCols(["document"]) \
  .setOutputCol("tokens")

embedder = nlp.WordEmbeddingsModel \
  .pretrained("embeddings_clinical", "en", "clinical/models") \
  .setInputCols(["document", "tokens"]) \
  .setOutputCol("embeddings")

posTagger = nlp.PerceptronModel \
  .pretrained("pos_clinical", "en", "clinical/models") \
  .setInputCols(["document", "tokens"]) \
  .setOutputCol("posTags")

nerTagger = nlp.MedicalNerModel \
  .pretrained("ner_events_clinical", "en", "clinical/models") \
  .setInputCols(["document", "tokens", "embeddings"]) \
  .setOutputCol("ner_tags")

nerConverter = nlp.NerConverter() \
  .setInputCols(["document", "tokens", "ner_tags"]) \
  .setOutputCol("nerChunks")

depencyParser = nlp.DependencyParserModel \
  .pretrained("dependency_conllu", "en") \
  .setInputCols(["document", "posTags", "tokens"]) \
  .setOutputCol("dependencies")

# Then define `RelationExtractionApproach` and training parameters
re = medical.RelationExtractionApproach() \
  .setInputCols(["embeddings", "posTags", "train_ner_chunks", "dependencies"]) \
  .setOutputCol("relations_t") \
  .setLabelColumn("target_rel") \
  .setEpochsNumber(300) \
  .setBatchSize(200) \
  .setLearningRate(0.001) \
  .setModelFile("path/to/graph_file.pb") \
  .setFixImbalance(True) \
  .setValidationSplit(0.05) \
  .setFromEntity("from_begin", "from_end", "from_label") \
  .setToEntity("to_begin", "to_end", "to_label")

finisher = nlp.Finisher() \
  .setInputCols(["relations_t"]) \
  .setOutputCols(["relations"]) \
  .setCleanAnnotations(False) \
  .setValueSplitSymbol(",") \
  .setAnnotationSplitSymbol(",") \
  .setOutputAsArray(False)

# Define complete pipeline and start training
pipeline = nlp.Pipeline(stages=[
    documentAssembler,
    tokenizer,
    embedder,
    posTagger,
    nerTagger,
    nerConverter,
    depencyParser,
    re,
    finisher])

model = pipeline.fit(trainData)

{%- endcapture -%}

{%- capture approach_scala_medical -%}
import spark.implicits._

// Defining pipeline stages to extract entities first
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("tokens")

val embedder = WordEmbeddingsModel
  .pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("document", "tokens"))
  .setOutputCol("embeddings")

val posTagger = PerceptronModel
  .pretrained("pos_clinical", "en", "clinical/models")
  .setInputCols(Array("document", "tokens"))
  .setOutputCol("posTags")

val nerTagger = MedicalNerModel
  .pretrained("ner_events_clinical", "en", "clinical/models")
  .setInputCols(Array("document", "tokens", "embeddings"))
  .setOutputCol("ner_tags")

val nerConverter = new NerConverter()
  .setInputCols(Array("document", "tokens", "ner_tags"))
  .setOutputCol("nerChunks")

val depencyParser = DependencyParserModel
  .pretrained("dependency_conllu", "en")
  .setInputCols(Array("document", "posTags", "tokens"))
  .setOutputCol("dependencies")

// Then define `RelationExtractionApproach` and training parameters
val re = new RelationExtractionApproach()
  .setInputCols(Array("embeddings", "posTags", "train_ner_chunks", "dependencies"))
  .setOutputCol("relations_t")
  .setLabelColumn("target_rel")
  .setEpochsNumber(300)
  .setBatchSize(200)
  .setlearningRate(0.001f)
  .setModelFile("path/to/graph_file.pb")
  .setFixImbalance(true)
  .setValidationSplit(0.05f)
  .setFromEntity("from_begin", "from_end", "from_label")
  .setToEntity("to_begin", "to_end", "to_label")

val finisher = new Finisher()
  .setInputCols(Array("relations_t"))
  .setOutputCols(Array("relations"))
  .setCleanAnnotations(false)
  .setValueSplitSymbol(",")
  .setAnnotationSplitSymbol(",")
  .setOutputAsArray(false)

// Define complete pipeline and start training
val pipeline = new Pipeline()
  .setStages(Array(
    documentAssembler,
    tokenizer,
    embedder,
    posTagger,
    nerTagger,
    nerConverter,
    depencyParser,
    re,
    finisher))

val model = pipeline.fit(trainData)

{%- endcapture -%}


{%- capture approach_api_link -%}
[RelationExtractionApproach](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/re/RelationExtractionApproach.html)
{%- endcapture -%}

{%- capture approach_python_api_link -%}
[RelationExtractionApproach](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/re/relation_extraction/index.html#sparknlp_jsl.annotator.re.relation_extraction.RelationExtractionApproach)
{%- endcapture -%}

{%- capture approach_notebook_link -%}
[RelationExtractionApproachNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/RelationExtractionApproach.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
approach=approach
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link
approach_description=approach_description
approach_input_anno=approach_input_anno
approach_output_anno=approach_output_anno
approach_python_medical=approach_python_medical
approach_scala_medical=approach_scala_medical
approach_api_link=approach_api_link
approach_python_api_link=approach_python_api_link
approach_notebook_link=approach_notebook_link
%}
