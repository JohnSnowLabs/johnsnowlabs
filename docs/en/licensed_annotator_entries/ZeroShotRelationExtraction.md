{%- capture title -%}
ZeroShotRelationExtractionModel
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}

`ZeroShotRelationExtractionModel` implements zero-shot binary relations extraction by utilizing `BERT` transformer models trained on the NLI (Natural Language Inference) task. 

The model inputs consists of documents/sentences and paired NER chunks, usually obtained by `RENerChunksFilter`. The definitions of relations which are extracted is given by a dictionary structures, specifying a set of statements regarding the relationship of named entities. 

These statements are automatically appended to each document in the dataset and the NLI model is used to determine whether a particular relationship between entities.

Parametres:

- `relationalCategories`: A dictionary with definitions of relational categories. The keys of dictionary are the relation labels and the values are lists of hypothesis templates.

- `predictionThreshold`: Minimal confidence score to encode a relation (Default: `0.5`)

- `multiLabel`: Whether or not a pair of entities can be categorized by multiple relations (Default: `False`).

All the parameters can be set using the corresponding set method in camel case. For example, `.setMultiLabel()`.

For available pretrained models please see the [Models Hub](https://nlp.johnsnowlabs.com/models?language=en&q=zero_shot).

{%- endcapture -%}

{%- capture model_input_anno -%}
CHUNK, DOCUMENT 
{%- endcapture -%}

{%- capture model_output_anno -%}
CATEGORY
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

documenter = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentencer = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentences")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentences"])\
    .setOutputCol("tokens")

words_embedder = nlp.WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentences", "tokens"])\
    .setOutputCol("embeddings")

ner_clinical = medical.NerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentences", "tokens", "embeddings"])\
    .setOutputCol("ner_clinical")

ner_clinical_converter = medical.NerConverterInternal()\
    .setInputCols(["sentences", "tokens", "ner_clinical"])\
    .setOutputCol("ner_clinical_chunks")\
    .setWhiteList(["PROBLEM", "TEST"])  # PROBLEM-TEST-TREATMENT

ner_posology = medical.NerModel.pretrained("ner_posology", "en", "clinical/models")\
    .setInputCols(["sentences", "tokens", "embeddings"])\
    .setOutputCol("ner_posology")

ner_posology_converter = medical.NerConverterInternal()\
    .setInputCols(["sentences", "tokens", "ner_posology"])\
    .setOutputCol("ner_posology_chunks")\
    .setWhiteList(["DRUG"]) # DRUG-FREQUENCY-DOSAGE-DURATION-FORM-ROUTE-STRENGTH

chunk_merger = medical.ChunkMergeApproach()\
    .setInputCols("ner_clinical_chunks", "ner_posology_chunks")\
    .setOutputCol("merged_ner_chunks")

## ZERO-SHOT RE Starting...

pos_tagger = nlp.PerceptronModel().pretrained("pos_clinical", "en", "clinical/models")\
    .setInputCols(["sentences", "tokens"])\
    .setOutputCol("pos_tags")

dependency_parser = nlp.DependencyParserModel().pretrained("dependency_conllu", "en")\
    .setInputCols(["document", "pos_tags", "tokens"])\
    .setOutputCol("dependencies")

re_ner_chunk_filter = medical.RENerChunksFilter().setRelationPairs(["problem-test", "problem-drug"])\
    .setMaxSyntacticDistance(4)\
    .setDocLevelRelations(False)\
    .setInputCols(["merged_ner_chunks", "dependencies"])\
    .setOutputCol("re_ner_chunks")

re_model = medical.ZeroShotRelationExtractionModel.pretrained("re_zeroshot_biobert", "en", "clinical/models")\
    .setInputCols(["re_ner_chunks", "sentences"])\
    .setOutputCol("relations")\
    .setMultiLabel(True)\
    .setRelationalCategories(
        {
            "ADE": ["{DRUG} causes {PROBLEM}."],
            "IMPROVE": ["{DRUG} improves {PROBLEM}.", "{DRUG} cures {PROBLEM}."],
            "REVEAL": ["{TEST} reveals {PROBLEM}."],
        }
    )

pipeline = nlp.Pipeline(
    stages = [
        documenter,
        sentencer,
        tokenizer,
        words_embedder,
        ner_clinical,
        ner_clinical_converter,
        ner_posology,
        ner_posology_converter,
        chunk_merger,
        pos_tagger,
        dependency_parser,
        re_ner_chunk_filter,
        re_model
    ]
)

text = "Paracetamol can alleviate headache or sickness. An MRI test can be used to find cancer."

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

from pyspark.sql import functions as F

results.select(
    F.explode(F.arrays_zip(results.relations.metadata, results.relations.result)).alias("cols")).select(
    F.expr("cols['0']['sentence']").alias("sentence"),
    F.expr("cols['0']['entity1_begin']").alias("entity1_begin"),
    F.expr("cols['0']['entity1_end']").alias("entity1_end"),
    F.expr("cols['0']['chunk1']").alias("chunk1"),
    F.expr("cols['0']['entity1']").alias("entity1"),
    F.expr("cols['0']['entity2_begin']").alias("entity2_begin"),
    F.expr("cols['0']['entity2_end']").alias("entity2_end"),
    F.expr("cols['0']['chunk2']").alias("chunk2"),
    F.expr("cols['0']['entity2']").alias("entity2"),
    F.expr("cols['0']['hypothesis']").alias("hypothesis"),
    F.expr("cols['0']['nli_prediction']").alias("nli_prediction"),
    F.expr("cols['1']").alias("relation"),
    F.expr("cols['0']['confidence']").alias("confidence"),
).show(truncate=70)
+--------+-------------+-----------+-----------+-------+-------------+-----------+--------+-------+------------------------------+--------------+--------+----------+
sentence|entity1_begin|entity1_end|     chunk1|entity1|entity2_begin|entity2_end|  chunk2|entity2|                    hypothesis|nli_prediction|relation|confidence|
+--------+-------------+-----------+-----------+-------+-------------+-----------+--------+-------+------------------------------+--------------+--------+----------+
       0|            0|         10|Paracetamol|   DRUG|           38|         45|sickness|PROBLEM|Paracetamol improves sickness.|        entail| IMPROVE|0.98819494|
       0|            0|         10|Paracetamol|   DRUG|           26|         33|headache|PROBLEM|Paracetamol improves headache.|        entail| IMPROVE| 0.9929625|
       1|           48|         58|An MRI test|   TEST|           80|         85|  cancer|PROBLEM|   An MRI test reveals cancer.|        entail|  REVEAL| 0.9760039|
+--------+-------------+-----------+-----------+-------+-------------+-----------+--------+-------+------------------------------+--------------+--------+----------+

{%- endcapture -%}

{%- capture model_python_finance -%}
from johnsnowlabs import nlp, finance

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base", "en")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = finance.NerModel.pretrained("finner_financial_small", "en", "finance/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = finance.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

re_model = finance.ZeroShotRelationExtractionModel.pretrained("finre_zero_shot", "en", "finance/models")\
    .setInputCols(["ner_chunk", "sentence"])\
    .setOutputCol("relations")\
    .setMultiLabel(False)\
    .setRelationalCategories(
        {
            "profit_decline_by": [
                "{PROFIT_DECLINE} decreased by {AMOUNT} from",
                "{PROFIT_DECLINE} decreased by {AMOUNT} to",
            ],
            "profit_decline_by_per": [
                "{PROFIT_DECLINE} decreased by a {PERCENTAGE} from",
                "{PROFIT_DECLINE} decreased by a {PERCENTAGE} to",
            ],
            "profit_decline_from": [
                "{PROFIT_DECLINE} decreased from {AMOUNT}",
                "{PROFIT_DECLINE} decreased from {AMOUNT} for the year",
            ],
            "profit_decline_from_per": [
                "{PROFIT_DECLINE} decreased from {PERCENTAGE} to",
                "{PROFIT_DECLINE} decreased from {PERCENTAGE} to a total of",
            ],
            "profit_decline_to": ["{PROFIT_DECLINE} to {AMOUNT}"],
            "profit_increase_from": ["{PROFIT_INCREASE} from {AMOUNT}"],
            "profit_increase_to": ["{PROFIT_INCREASE} to {AMOUNT}"],
            "expense_decrease_by": ["{EXPENSE_DECREASE} decreased by {AMOUNT}"],
            "expense_decrease_by_per": ["{EXPENSE_DECREASE} decreased by a {PERCENTAGE}"],
            "expense_decrease_from": ["{EXPENSE_DECREASE} decreased from {AMOUNT}"],
            "expense_decrease_to": [
                "{EXPENSE_DECREASE} for a total of {AMOUNT} for the fiscal year"
            ],
            "has_date": [
                "{AMOUNT} for the fiscal year ended {FISCAL_YEAR}",
                "{PERCENTAGE} for the fiscal year ended {FISCAL_YEAR}",
            ],
        }
    )

pipeline = nlp.Pipeline(
    stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        embeddings,
        ner_model,
        ner_converter,
        re_model,
    ]
)

text = """License fees revenue decreased 40 %, or $ 0.5 million to $ 0.7 million for the year ended December 31, 2020 compared to $ 1.2 million for the year ended December 31, 2019. Services revenue increased 4 %, or $ 1.1 million, to $ 25.6 million for the year ended December 31, 2020 from $ 24.5 million for the year ended December 31, 2019. Costs of revenue, excluding depreciation and amortization increased by $ 0.1 million, or 2 %, to $ 8.8 million for the year ended December 31, 2020 from $ 8.7 million for the year ended December 31, 2019.  Also, a decrease in travel costs of $ 0.4 million due to travel restrictions caused by the global pandemic. As a percentage of revenue, cost of revenue, excluding depreciation and amortization was 34 % for each of the years ended December 31, 2020 and 2019. Sales and marketing expenses decreased 20 %, or $ 1.5 million, to $ 6.0 million for the year ended December 31, 2020 from $ 7.5 million for the year ended December 31, 2019."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

from pyspark.sql import functions as F

result.select(
    F.explode(F.arrays_zip(result.relations.metadata, result.relations.result)).alias("cols")).select(
    F.expr("cols['0']['sentence']").alias("sentence"),
    F.expr("cols['0']['entity1_begin']").alias("entity1_begin"),
    F.expr("cols['0']['entity1_end']").alias("entity1_end"),
    F.expr("cols['0']['chunk1']").alias("chunk1"),
    F.expr("cols['0']['entity1']").alias("entity1"),
    F.expr("cols['0']['entity2_begin']").alias("entity2_begin"),
    F.expr("cols['0']['entity2_end']").alias("entity2_end"),
    F.expr("cols['0']['chunk2']").alias("chunk2"),
    F.expr("cols['0']['entity2']").alias("entity2"),
    F.expr("cols['0']['hypothesis']").alias("hypothesis"),
    F.expr("cols['0']['nli_prediction']").alias("nli_prediction"),
    F.expr("cols['1']").alias("relation"),
    F.expr("cols['0']['confidence']").alias("confidence"),
).show(truncate=70)

+--------+-------------+-----------+----------------------------+----------------+-------------+-----------+-----------------+-----------+--------------------------------------------------------+--------------+---------------------+----------+
|sentence|entity1_begin|entity1_end|                      chunk1|         entity1|entity2_begin|entity2_end|           chunk2|    entity2|                                              hypothesis|nli_prediction|             relation|confidence|
+--------+-------------+-----------+----------------------------+----------------+-------------+-----------+-----------------+-----------+--------------------------------------------------------+--------------+---------------------+----------+
|       1|          227|        238|                25.6 million|          AMOUNT|          316|        332|December 31, 2019|FISCAL_YEAR|25.6 million for the fiscal year ended December 31, 2019|        entail|             has_date| 0.8744757|
|       0|           31|         32|                          40|      PERCENTAGE|          153|        169|December 31, 2019|FISCAL_YEAR|          40 for the fiscal year ended December 31, 2019|        entail|             has_date| 0.7889032|
|       5|          799|        826|Sales and marketing expenses|EXPENSE_DECREASE|          923|        933|      7.5 million|     AMOUNT| Sales and marketing expenses decreased from 7.5 million|        entail|expense_decrease_from| 0.9770538|
|       0|           59|         69|                 0.7 million|          AMOUNT|           90|        106|December 31, 2020|FISCAL_YEAR| 0.7 million for the fiscal year ended December 31, 2020|        entail|             has_date|0.67187774|
|       1|          172|        187|            Services revenue| PROFIT_INCREASE|          227|        238|     25.6 million|     AMOUNT|                        Services revenue to 25.6 million|        entail|   profit_increase_to| 0.9674029|
|       0|           31|         32|                          40|      PERCENTAGE|           90|        106|December 31, 2020|FISCAL_YEAR|          40 for the fiscal year ended December 31, 2020|        entail|             has_date|0.77800345|
|       5|          838|        839|                          20|      PERCENTAGE|          898|        914|December 31, 2020|FISCAL_YEAR|          20 for the fiscal year ended December 31, 2020|        entail|             has_date|0.85455483|
|       3|          561|        572|                travel costs|EXPENSE_DECREASE|          579|        589|      0.4 million|     AMOUNT|                   travel costs decreased by 0.4 million|        entail|  expense_decrease_by| 0.9946776|
|       0|           42|         52|                 0.5 million|          AMOUNT|          153|        169|December 31, 2019|FISCAL_YEAR| 0.5 million for the fiscal year ended December 31, 2019|        entail|             has_date| 0.7756689|
|       1|          172|        187|            Services revenue| PROFIT_INCREASE|          209|        219|      1.1 million|     AMOUNT|                       Services revenue from 1.1 million|        entail| profit_increase_from|0.96610945|
|       2|          408|        418|                 0.1 million|          AMOUNT|          521|        537|December 31, 2019|FISCAL_YEAR| 0.1 million for the fiscal year ended December 31, 2019|        entail|             has_date| 0.9083247|
|       5|          849|        859|                 1.5 million|          AMOUNT|          898|        914|December 31, 2020|FISCAL_YEAR| 1.5 million for the fiscal year ended December 31, 2020|        entail|             has_date| 0.7528142|
|       5|          849|        859|                 1.5 million|          AMOUNT|          954|        970|December 31, 2019|FISCAL_YEAR| 1.5 million for the fiscal year ended December 31, 2019|        entail|             has_date|0.80734617|
|       0|           42|         52|                 0.5 million|          AMOUNT|           90|        106|December 31, 2020|FISCAL_YEAR| 0.5 million for the fiscal year ended December 31, 2020|        entail|             has_date| 0.7157578|
|       1|          172|        187|            Services revenue| PROFIT_INCREASE|          284|        295|     24.5 million|     AMOUNT|                        Services revenue to 24.5 million|        entail|   profit_increase_to| 0.8597209|
|       0|           59|         69|                 0.7 million|          AMOUNT|          153|        169|December 31, 2019|FISCAL_YEAR| 0.7 million for the fiscal year ended December 31, 2019|        entail|             has_date|0.74845695|
|       1|          199|        199|                           4|      PERCENTAGE|          259|        275|December 31, 2020|FISCAL_YEAR|           4 for the fiscal year ended December 31, 2020|        entail|             has_date|0.84127575|
|       2|          424|        424|                           2|      PERCENTAGE|          465|        481|December 31, 2020|FISCAL_YEAR|           2 for the fiscal year ended December 31, 2020|        entail|             has_date| 0.8046481|
|       2|          424|        424|                           2|      PERCENTAGE|          521|        537|December 31, 2019|FISCAL_YEAR|           2 for the fiscal year ended December 31, 2019|        entail|             has_date| 0.8485104|
|       0|            0|         19|        License fees revenue|  PROFIT_DECLINE|           31|         32|               40| PERCENTAGE|               License fees revenue decreased by a 40 to|        entail|profit_decline_by_per| 0.9948003|
+--------+-------------+-----------+----------------------------+----------------+-------------+-----------+-----------------+-----------+--------------------------------------------------------+--------------+---------------------+----------+
only showing top 20 rows

{%- endcapture -%}

{%- capture model_python_legal -%}
from johnsnowlabs import nlp, legal

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = nlp.Tokenizer()\
    .setInputCols("document")\
    .setOutputCol("token")

tokenClassifier = legal.BertForTokenClassification.pretrained('legner_obligations','en', 'legal/models')\
    .setInputCols("token", "document")\
    .setOutputCol("ner")\
    .setMaxSentenceLength(512)\
    .setCaseSensitive(True)

ner_converter = legal.NerConverterInternal()\
    .setInputCols(["document", "token", "ner"])\
    .setOutputCol("ner_chunk")

re_model = legal.ZeroShotRelationExtractionModel.pretrained("legre_zero_shot", "en", "legal/models")\
    .setInputCols(["ner_chunk", "document"]) \
    .setOutputCol("relations")

re_model.setRelationalCategories({
    "GRANTS_TO": ["{OBLIGATION_SUBJECT} grants {OBLIGATION_INDIRECT_OBJECT}"],
    "GRANTS": ["{OBLIGATION_SUBJECT} grants {OBLIGATION_ACTION}"]
})

pipeline = nlp.Pipeline(stages = [
                document_assembler,  
                tokenizer,
                tokenClassifier, 
                ner_converter,
                re_model
               ])

text = """Arizona Copyright Grant. Subject to the terms and conditions of this Agreement, Arizona hereby grants to the Company a perpetual, non-exclusive, royalty-free license in, to and under the Arizona Licensed Copyrights for use in the Company Field throughout the world."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

from pyspark.sql import functions as F

result.select(
    F.explode(F.arrays_zip(result.relations.metadata, result.relations.result)).alias("cols")).select(
    F.expr("cols['0']['sentence']").alias("sentence"),
    F.expr("cols['0']['entity1_begin']").alias("entity1_begin"),
    F.expr("cols['0']['entity1_end']").alias("entity1_end"),
    F.expr("cols['0']['chunk1']").alias("chunk1"),
    F.expr("cols['0']['entity1']").alias("entity1"),
    F.expr("cols['0']['entity2_begin']").alias("entity2_begin"),
    F.expr("cols['0']['entity2_end']").alias("entity2_end"),
    F.expr("cols['0']['chunk2']").alias("chunk2"),
    F.expr("cols['0']['entity2']").alias("entity2"),
    F.expr("cols['0']['hypothesis']").alias("hypothesis"),
    F.expr("cols['0']['nli_prediction']").alias("nli_prediction"),
    F.expr("cols['1']").alias("relation"),
    F.expr("cols['0']['confidence']").alias("confidence"),
).show(truncate=70)

+--------+-------------+-----------+-------+------------------+-------------+-----------+-------------+--------------------------+----------------------------+--------------+---------+----------+
|sentence|entity1_begin|entity1_end| chunk1|           entity1|entity2_begin|entity2_end|       chunk2|                   entity2|                  hypothesis|nli_prediction| relation|confidence|
+--------+-------------+-----------+-------+------------------+-------------+-----------+-------------+--------------------------+----------------------------+--------------+---------+----------+
|       0|           80|         86|Arizona|OBLIGATION_SUBJECT|          109|        115|      Company|OBLIGATION_INDIRECT_OBJECT|      Arizona grants Company|        entail|GRANTS_TO| 0.9535338|
|       0|           80|         86|Arizona|OBLIGATION_SUBJECT|           88|        100|hereby grants|         OBLIGATION_ACTION|Arizona grants hereby grants|        entail|   GRANTS| 0.9873099|
+--------+-------------+-----------+-------+------------------+-------------+-----------+-------------+--------------------------+----------------------------+--------------+---------+----------+

{%- endcapture -%}

{%- capture model_scala_medical -%}

import spark.implicits._

val documenter = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentencer = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentences")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentences"))
    .setOutputCol("tokens")

val wordsEmbedder = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentences", "tokens"))
    .setOutputCol("embeddings")

val nerClinical = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentences", "tokens", "embeddings"))
    .setOutputCol("ner_clinical")

val nerClinicalConverter = new NerConverterInternal()
    .setInputCols(Array("sentences", "tokens", "ner_clinical"))
    .setOutputCol("ner_clinical_chunks")
    .setWhiteList(Array("PROBLEM", "TEST"))

val nerPosology = MedicalNerModel.pretrained("ner_posology", "en", "clinical/models")
    .setInputCols(Array("sentences", "tokens", "embeddings"))
    .setOutputCol("ner_posology")

val nerPosologyConverter = new NerConverterInternal()
    .setInputCols(Array("sentences", "tokens", "ner_posology"))
    .setOutputCol("ner_posology_chunks")
    .setWhiteList(Array("DRUG"))

val chunkMerger = new ChunkMergeApproach()
    .setInputCols(Array("ner_clinical_chunks", "ner_posology_chunks"))
    .setOutputCol("merged_ner_chunks")

val posTagger = PerceptronModel.pretrained("pos_clinical", "en", "clinical/models")
    .setInputCols(Array("sentences", "tokens"))
    .setOutputCol("pos_tags")

val dependencyParser = DependencyParserModel.pretrained("dependency_conllu", "en")
    .setInputCols(Array("document", "pos_tags", "tokens"))
    .setOutputCol("dependencies")

val reNerChunkFilter = new RENerChunksFilter()
    .setRelationPairs(Array("problem-test", "problem-drug"))
    .setMaxSyntacticDistance(4)
    .setDocLevelRelations(false)
    .setInputCols(Array("merged_ner_chunks", "dependencies"))
    .setOutputCol("re_ner_chunks")

val reModel = ZeroShotRelationExtractionModel.pretrained("re_zeroshot_biobert", "en", "clinical/models")
    .setInputCols(Array("re_ner_chunks", "sentences"))
    .setOutputCol("relations")
    .setMultiLabel(true)
    .setRelationalCategories(Map(
        "ADE" -> Array("{DRUG} causes {PROBLEM}."),
        "IMPROVE" -> Array("{DRUG} improves {PROBLEM}.", "{DRUG} cures {PROBLEM}."),
        "REVEAL" -> Array("{TEST} reveals {PROBLEM}.")
    ))

val pipeline = new Pipeline().setStages(Array(
    documenter,
    sentencer,
    tokenizer,
    wordsEmbedder,
    nerClinical,
    nerClinicalConverter,
    nerPosology,
    nerPosologyConverter,
    chunkMerger,
    posTagger,
    dependencyParser,
    reNerChunkFilter,
    reModel
))

val text = "Paracetamol can alleviate headache or sickness. An MRI test can be used to find cancer."

val data = Seq(text).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)

result.selectExpr("explode(arrays_zip(relations.metadata, relations.result)) as cols")
.selectExpr(
    "cols['0']['sentence'] as sentence",
    "cols['0']['entity1_begin'] as entity1_begin",
    "cols['0']['entity1_end'] as entity1_end",
    "cols['0']['chunk1'] as chunk1",
    "cols['0']['entity1'] as entity1",
    "cols['0']['entity2_begin'] as entity2_begin",
    "cols['0']['entity2_end'] as entity2_end",
    "cols['0']['chunk2'] as chunk2",
    "cols['0']['entity2'] as entity2",
    "cols['0']['hypothesis'] as hypothesis",
    "cols['0']['nli_prediction'] as nli_prediction",
    "cols['1'] as relation",
    "cols['0']['confidence'] as confidence").show(70)
 
+--------+-------------+-----------+-----------+-------+-------------+-----------+--------+-------+--------------------+--------------+--------+----------+
|sentence|entity1_begin|entity1_end|     chunk1|entity1|entity2_begin|entity2_end|  chunk2|entity2|          hypothesis|nli_prediction|relation|confidence|
+--------+-------------+-----------+-----------+-------+-------------+-----------+--------+-------+--------------------+--------------+--------+----------+
|       0|            0|         10|Paracetamol|   DRUG|           38|         45|sickness|PROBLEM|Paracetamol impro...|        entail| IMPROVE|0.98819494|
|       0|            0|         10|Paracetamol|   DRUG|           26|         33|headache|PROBLEM|Paracetamol impro...|        entail| IMPROVE| 0.9929625|
|       1|           48|         58|An MRI test|   TEST|           80|         85|  cancer|PROBLEM|An MRI test revea...|        entail|  REVEAL| 0.9760039|
+--------+-------------+-----------+-----------+-------+-------------+-----------+--------+-------+--------------------+--------------+--------+----------+

{%- endcapture -%}

{%- capture model_scala_finance -%}

import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val embeddings = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base", "en")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

val nerModel = FinanceNerModel.pretrained("finner_financial_small", "en", "finance/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner")

val nerConverter = new NerConverterInternal()
  .setInputCols(Array("sentence", "token", "ner"))
  .setOutputCol("ner_chunk")

val reModel = ZeroShotRelationExtractionModel.pretrained("finre_zero_shot", "en", "finance/models")
  .setInputCols(Array("ner_chunk", "sentence"))
  .setOutputCol("relations")
  .setMultiLabel(false)
  .setRelationalCategories(Map(
  "profit_decline_by" -> Array(
    "{PROFIT_DECLINE} decreased by {AMOUNT} from",
    "{PROFIT_DECLINE} decreased by {AMOUNT} to"
  ),
  "profit_decline_by_per" -> Array(
    "{PROFIT_DECLINE} decreased by a {PERCENTAGE} from",
    "{PROFIT_DECLINE} decreased by a {PERCENTAGE} to"
  ),
  "profit_decline_from" -> Array(
    "{PROFIT_DECLINE} decreased from {AMOUNT}",
    "{PROFIT_DECLINE} decreased from {AMOUNT} for the year"
  ),
  "profit_decline_from_per" -> Array(
    "{PROFIT_DECLINE} decreased from {PERCENTAGE} to",
    "{PROFIT_DECLINE} decreased from {PERCENTAGE} to a total of"
  ),
  "profit_decline_to" -> Array("{PROFIT_DECLINE} to {AMOUNT}"),
  "profit_increase_from" -> Array("{PROFIT_INCREASE} from {AMOUNT}"),
  "profit_increase_to" -> Array("{PROFIT_INCREASE} to {AMOUNT}"),
  "expense_decrease_by" -> Array("{EXPENSE_DECREASE} decreased by {AMOUNT}"),
  "expense_decrease_by_per" -> Array("{EXPENSE_DECREASE} decreased by a {PERCENTAGE}"),
  "expense_decrease_from" -> Array("{EXPENSE_DECREASE} decreased from {AMOUNT}"),
  "expense_decrease_to" -> Array("{EXPENSE_DECREASE} for a total of {AMOUNT} for the fiscal year"),
  "has_date" -> Array(
    "{AMOUNT} for the fiscal year ended {FISCAL_YEAR}",
    "{PERCENTAGE} for the fiscal year ended {FISCAL_YEAR}"
  )
))

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    embeddings,
    nerModel,
    nerConverter,
    reModel
  ))

val text = """License fees revenue decreased 40 %, or $ 0.5 million to $ 0.7 million for the year ended December 31, 2020 compared to $ 1.2 million for the year ended December 31, 2019. Services revenue increased 4 %, or $ 1.1 million, to $ 25.6 million for the year ended December 31, 2020 from $ 24.5 million for the year ended December 31, 2019. Costs of revenue, excluding depreciation and amortization increased by $ 0.1 million, or 2 %, to $ 8.8 million for the year ended December 31, 2020 from $ 8.7 million for the year ended December 31, 2019.  Also, a decrease in travel costs of $ 0.4 million due to travel restrictions caused by the global pandemic. As a percentage of revenue, cost of revenue, excluding depreciation and amortization was 34 % for each of the years ended December 31, 2020 and 2019. Sales and marketing expenses decreased 20 %, or $ 1.5 million, to $ 6.0 million for the year ended December 31, 2020 from $ 7.5 million for the year ended December 31, 2019."""

val data = Seq(text).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)

result.selectExpr("explode(arrays_zip(relations.metadata, relations.result)) as cols")
    .selectExpr(
    "cols['0']['sentence'] as sentence",
    "cols['0']['entity1_begin'] as entity1_begin",
    "cols['0']['entity1_end'] as entity1_end",
    "cols['0']['chunk1'] as chunk1",
    "cols['0']['entity1'] as entity1",
    "cols['0']['entity2_begin'] as entity2_begin",
    "cols['0']['entity2_end'] as entity2_end",
    "cols['0']['chunk2'] as chunk2",
    "cols['0']['entity2'] as entity2",
    "cols['0']['hypothesis'] as hypothesis",
    "cols['0']['nli_prediction'] as nli_prediction",
    "cols['1'] as relation",
    "cols['0']['confidence'] as confidence").show(70)

+--------+-------------+-----------+----------------------------+----------------+-------------+-----------+-----------------+-----------+--------------------------------------------------------+--------------+---------------------+----------+
|sentence|entity1_begin|entity1_end|                      chunk1|         entity1|entity2_begin|entity2_end|           chunk2|    entity2|                                              hypothesis|nli_prediction|             relation|confidence|
+--------+-------------+-----------+----------------------------+----------------+-------------+-----------+-----------------+-----------+--------------------------------------------------------+--------------+---------------------+----------+
|       1|          227|        238|                25.6 million|          AMOUNT|          316|        332|December 31, 2019|FISCAL_YEAR|25.6 million for the fiscal year ended December 31, 2019|        entail|             has_date| 0.8744757|
|       0|           31|         32|                          40|      PERCENTAGE|          153|        169|December 31, 2019|FISCAL_YEAR|          40 for the fiscal year ended December 31, 2019|        entail|             has_date| 0.7889032|
|       5|          799|        826|Sales and marketing expenses|EXPENSE_DECREASE|          923|        933|      7.5 million|     AMOUNT| Sales and marketing expenses decreased from 7.5 million|        entail|expense_decrease_from| 0.9770538|
|       0|           59|         69|                 0.7 million|          AMOUNT|           90|        106|December 31, 2020|FISCAL_YEAR| 0.7 million for the fiscal year ended December 31, 2020|        entail|             has_date|0.67187774|
|       1|          172|        187|            Services revenue| PROFIT_INCREASE|          227|        238|     25.6 million|     AMOUNT|                        Services revenue to 25.6 million|        entail|   profit_increase_to| 0.9674029|
|       0|           31|         32|                          40|      PERCENTAGE|           90|        106|December 31, 2020|FISCAL_YEAR|          40 for the fiscal year ended December 31, 2020|        entail|             has_date|0.77800345|
|       5|          838|        839|                          20|      PERCENTAGE|          898|        914|December 31, 2020|FISCAL_YEAR|          20 for the fiscal year ended December 31, 2020|        entail|             has_date|0.85455483|
|       3|          561|        572|                travel costs|EXPENSE_DECREASE|          579|        589|      0.4 million|     AMOUNT|                   travel costs decreased by 0.4 million|        entail|  expense_decrease_by| 0.9946776|
|       0|           42|         52|                 0.5 million|          AMOUNT|          153|        169|December 31, 2019|FISCAL_YEAR| 0.5 million for the fiscal year ended December 31, 2019|        entail|             has_date| 0.7756689|
|       1|          172|        187|            Services revenue| PROFIT_INCREASE|          209|        219|      1.1 million|     AMOUNT|                       Services revenue from 1.1 million|        entail| profit_increase_from|0.96610945|
|       2|          408|        418|                 0.1 million|          AMOUNT|          521|        537|December 31, 2019|FISCAL_YEAR| 0.1 million for the fiscal year ended December 31, 2019|        entail|             has_date| 0.9083247|
|       5|          849|        859|                 1.5 million|          AMOUNT|          898|        914|December 31, 2020|FISCAL_YEAR| 1.5 million for the fiscal year ended December 31, 2020|        entail|             has_date| 0.7528142|
|       5|          849|        859|                 1.5 million|          AMOUNT|          954|        970|December 31, 2019|FISCAL_YEAR| 1.5 million for the fiscal year ended December 31, 2019|        entail|             has_date|0.80734617|
|       0|           42|         52|                 0.5 million|          AMOUNT|           90|        106|December 31, 2020|FISCAL_YEAR| 0.5 million for the fiscal year ended December 31, 2020|        entail|             has_date| 0.7157578|
|       1|          172|        187|            Services revenue| PROFIT_INCREASE|          284|        295|     24.5 million|     AMOUNT|                        Services revenue to 24.5 million|        entail|   profit_increase_to| 0.8597209|
|       0|           59|         69|                 0.7 million|          AMOUNT|          153|        169|December 31, 2019|FISCAL_YEAR| 0.7 million for the fiscal year ended December 31, 2019|        entail|             has_date|0.74845695|
|       1|          199|        199|                           4|      PERCENTAGE|          259|        275|December 31, 2020|FISCAL_YEAR|           4 for the fiscal year ended December 31, 2020|        entail|             has_date|0.84127575|
|       2|          424|        424|                           2|      PERCENTAGE|          465|        481|December 31, 2020|FISCAL_YEAR|           2 for the fiscal year ended December 31, 2020|        entail|             has_date| 0.8046481|
|       2|          424|        424|                           2|      PERCENTAGE|          521|        537|December 31, 2019|FISCAL_YEAR|           2 for the fiscal year ended December 31, 2019|        entail|             has_date| 0.8485104|
|       0|            0|         19|        License fees revenue|  PROFIT_DECLINE|           31|         32|               40| PERCENTAGE|               License fees revenue decreased by a 40 to|        entail|profit_decline_by_per| 0.9948003|
+--------+-------------+-----------+----------------------------+----------------+-------------+-----------+-----------------+-----------+--------------------------------------------------------+--------------+---------------------+----------+
only showing top 20 rows

{%- endcapture -%}

{%- capture model_scala_legal -%}

import spark.implicits._

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols(Array("document"))
    .setOutputCol("token")

val tokenClassifier = LegalBertForTokenClassification.pretrained("legner_obligations", "en", "legal/models")
    .setInputCols(Array("token", "document"))
    .setOutputCol("ner")
    .setMaxSentenceLength(512)
    .setCaseSensitive(true)

val nerConverter = new NerConverterInternal()
    .setInputCols(Array("document", "token", "ner"))
    .setOutputCol("ner_chunk")

val reModel = ZeroShotRelationExtractionModel.pretrained("legre_zero_shot", "en", "legal/models")
    .setInputCols(Array("ner_chunk", "document"))
    .setOutputCol("relations")

reModel.setRelationalCategories(Map(
    "GRANTS_TO" -> Array("{OBLIGATION_SUBJECT} grants {OBLIGATION_INDIRECT_OBJECT}"),
    "GRANTS" -> Array("{OBLIGATION_SUBJECT} grants {OBLIGATION_ACTION}")
))

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    tokenizer,
    tokenClassifier,
    nerConverter,
    reModel
))

val text = """Arizona Copyright Grant. Subject to the terms and conditions of this Agreement, Arizona hereby grants to the Company a perpetual, non-exclusive, royalty-free license in, to and under the Arizona Licensed Copyrights for use in the Company Field throughout the world."""

val data = Seq(text).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)

result.select(explode(arrays_zip(result("relations")("metadata"), result("relations")("result"))).as("cols"))
.selectExpr(
    "cols['0']['sentence'] as sentence",
    "cols['0']['entity1_begin'] as entity1_begin",
    "cols['0']['entity1_end'] as entity1_end",
    "cols['0']['chunk1'] as chunk1",
    "cols['0']['entity1'] as entity1",
    "cols['0']['entity2_begin'] as entity2_begin",
    "cols['0']['entity2_end'] as entity2_end",
    "cols['0']['chunk2'] as chunk2",
    "cols['0']['entity2'] as entity2",
    "cols['0']['hypothesis'] as hypothesis",
    "cols['0']['nli_prediction'] as nli_prediction",
    "cols['1'] as relation",
    "cols['0']['confidence'] as confidence"
).show(70)

+--------+-------------+-----------+-------+------------------+-------------+-----------+-------------+--------------------------+----------------------------+--------------+---------+----------+
|sentence|entity1_begin|entity1_end| chunk1|           entity1|entity2_begin|entity2_end|       chunk2|                   entity2|                  hypothesis|nli_prediction| relation|confidence|
+--------+-------------+-----------+-------+------------------+-------------+-----------+-------------+--------------------------+----------------------------+--------------+---------+----------+
|       0|           80|         86|Arizona|OBLIGATION_SUBJECT|          109|        115|      Company|OBLIGATION_INDIRECT_OBJECT|      Arizona grants Company|        entail|GRANTS_TO| 0.9535338|
|       0|           80|         86|Arizona|OBLIGATION_SUBJECT|           88|        100|hereby grants|         OBLIGATION_ACTION|Arizona grants hereby grants|        entail|   GRANTS| 0.9873099|
+--------+-------------+-----------+-------+------------------+-------------+-----------+-------------+--------------------------+----------------------------+--------------+---------+----------+

{%- endcapture -%}

{%- capture model_api_link -%}
[ZeroShotRelationExtractionModel](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/finance/graph/relation_extraction/ZeroShotRelationExtractionModel.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[ZeroShotRelationExtractionModel](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/re/zero_shot_relation_extraction/index.html#sparknlp_jsl.annotator.re.zero_shot_relation_extraction.ZeroShotRelationExtractionModel)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[ZeroShotRelationExtractionModel](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ZeroShotRelationExtractionModel.ipynb)
{%- endcapture -%}


{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_python_finance=model_python_finance
model_python_legal=model_python_legal
model_scala_medical=model_scala_medical
model_scala_finance=model_scala_finance
model_scala_legal=model_scala_legal
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link
%}
