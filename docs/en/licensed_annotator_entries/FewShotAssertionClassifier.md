{%- capture title -%}
FewShotAssertionClassifierModel
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}

FewShotAssertionClassifierModel does assertion classification using can run large (LLMS based)
few shot classifiers based on the SetFit approach.

Parameters:

- `batchSize` *(Int)*: Batch size

- `caseSensitive` *(Bool)*: Whether the classifier is sensitive to text casing

- `maxSentenceLength` *(Int)*: The maximum length of the input text


{%- endcapture -%}

{%- capture model_input_anno -%} 
DOCUMENT, CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
ASSERTION
{%- endcapture -%}

{%- capture model_python_medical -%}

from johnsnowlabs import nlp, medical

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")\
    .setSplitChars(["-", "\/"])

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

# ner_oncology
ner_oncology = MedicalNerModel.pretrained("ner_oncology","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_oncology")

ner_oncology_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner_oncology"])\
    .setOutputCol("ner_chunk")

few_shot_assertion_converter = FewShotAssertionSentenceConverter()\
    .setInputCols(["sentence", "token", "ner_chunk"])\
    .setOutputCol("assertion_sentence")

e5_embeddings = E5Embeddings.pretrained("e5_base_v2_embeddings_medical_assertion_oncology", "en", "clinical/models")\
    .setInputCols(["assertion_sentence"])\
    .setOutputCol("assertion_embedding")

few_shot_assertion_classifier = FewShotAssertionClassifierModel()\
    .pretrained("fewhot_assertion_oncology_e5_base_v2_oncology", "en", "clinical/models")\
    .setInputCols(["assertion_embedding"])\
    .setOutputCol("assertion_fewshot")

assertion_pipeline = Pipeline(
    stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        word_embeddings,
        ner_oncology,
        ner_oncology_converter,
        few_shot_assertion_converter,
        e5_embeddings,
        few_shot_assertion_classifier
    ])

sample_text= [
    """The patient is suspected to have colorectal cancer. Her family history is positive for other cancers. The result of the biopsy was positive. A CT scan was ordered to rule out metastases."""
    ]

data = spark.createDataFrame([sample_text]).toDF("text")

result = assertion_pipeline.fit(data).transform(data)

## Result

+-----------------+-----+---+----------------+---------+----------+
|ner_chunk        |begin|end|ner_label       |assertion|confidence|
+-----------------+-----+---+----------------+---------+----------+
|colorectal cancer|33   |49 |Cancer_Dx       |Possible |0.5812815 |
|Her              |52   |54 |Gender          |Present  |0.9562998 |
|cancers          |93   |99 |Cancer_Dx       |Family   |0.23465642|
|biopsy           |120  |125|Pathology_Test  |Past     |0.95732147|
|positive         |131  |138|Pathology_Result|Present  |0.9564386 |
|CT scan          |143  |149|Imaging_Test    |Past     |0.9571699 |
|metastases       |175  |184|Metastasis      |Possible |0.54986554|
+-----------------+-----+---+----------------+---------+----------+

{%- endcapture -%}

{%- capture model_scala_medical -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel
    .pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")
    .setSplitChars(Array("-", "/"))

val wordEmbeddings = WordEmbeddingsModel
    .pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val nerOncology = MedicalNerModel
    .pretrained("ner_oncology", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner_oncology")

val nerOncologyConverter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner_oncology"))
    .setOutputCol("ner_chunk")

val fewShotAssertionConverter = new FewShotAssertionSentenceConverter()
    .setInputCols(Array("sentence", "token", "ner_chunk"))
    .setOutputCol("assertion_sentence")

val e5Embeddings = E5Embeddings
    .pretrained("e5_base_v2_embeddings_medical_assertion_oncology", "en", "clinical/models")
    .setInputCols(Array("assertion_sentence"))
    .setOutputCol("assertion_embedding")

val fewShotAssertionClassifier = FewShotAssertionClassifierModel
    .pretrained("fewhot_assertion_oncology_e5_base_v2_oncology", "en", "clinical/models")
    .setInputCols(Array("assertion_embedding"))
    .setOutputCol("assertion_fewshot")

val pipeline = new Pipeline()
    .setStages(Array(
        documentAssembler,
        sentenceDetector,
        tokenizer,
        wordEmbeddings,
        nerOncology,
        nerOncologyConverter,
        fewShotAssertionConverter,
        e5Embeddings,
        fewShotAssertionClassifier
    ))

val sampleText = Seq("The patient is suspected to have colorectal cancer. Her family history is positive for other cancers.
The result of the biopsy was positive. A CT scan was ordered to rule out metastases.")

val data = spark.createDataFrame(sampleText).toDF("text")

val result = pipeline.fit(data).transform(data)

result.show(false)

// Result       

+-----------------+-----+---+----------------+---------+----------+
|ner_chunk        |begin|end|ner_label       |assertion|confidence|
+-----------------+-----+---+----------------+---------+----------+
|colorectal cancer|33   |49 |Cancer_Dx       |Possible |0.5812815 |
|Her              |52   |54 |Gender          |Present  |0.9562998 |
|cancers          |93   |99 |Cancer_Dx       |Family   |0.23465642|
|biopsy           |120  |125|Pathology_Test  |Past     |0.95732147|
|positive         |131  |138|Pathology_Result|Present  |0.9564386 |
|CT scan          |143  |149|Imaging_Test    |Past     |0.9571699 |
|metastases       |175  |184|Metastasis      |Possible |0.54986554|
+-----------------+-----+---+----------------+---------+----------+

{%- endcapture -%}

{%- capture model_api_link -%}
[FewShotAssertionClassifierModel](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/classification/FewShotAssertionClassifierModel.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[FewShotAssertionClassifierModel](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/classification/few_shot_assertion_classifier/index.html)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[FewShotAssertionClassifierModel](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/2.2.FewShot_Assertion_Classifier.ipynb)
{%- endcapture -%}

{%- capture approach_description -%}
Trains a TensorFlow model for few shot assertion classifier.

To train a custom few shot assertion classifier model, you need to first create a Tensorflow graph using either the `TfGraphBuilder` annotator or the `tf_graph` module. Then, set the path to the Tensorflow graph using the method `.setModelFile("path/to/tensorflow_graph.pb")`.



Parameters:


- `batchSize`: (int) Batch size

- `dropout`: (float) Dropout coefficient

- `epochsN`: (int) Maximum number of epochs to train

- `featureScaling`: (str) Feature scaling method. Possible values are 'zscore', 'minmax' or empty (no scaling)

- `fixImbalance`: (boolean) Fix the imbalance in the training set by replicating examples of under represented categories

- `labelColumn`: (str) Column with label per each document

- `learningRate`: (float) Learning Rate

- `modelFile`: (str) Location of file of the model used for classification

- `multiClass`: (boolean) If multiClass is set, the model will return all the labels with corresponding scores. By default, multiClass is false.

- `outputLogsPath`: (str) Folder path to save training logs. If no path is specified, the logs won't be stored in disk. The path can be a local file path, a distributed file path (HDFS, DBFS), or a cloud storage (S3).

- `validationSplit`: (float) The proportion of training dataset to be used as validation set.The model will be validated against this dataset on each Epoch and will not be used for training. The value should be between 0.0 and 1.0.

- `datasetInfo` *(Str)*: Descriptive information about the dataset being used.

  {%- endcapture -%}

{%- capture approach_input_anno -%}
SENTENCE_EMBEDDINGS
{%- endcapture -%}

{%- capture approach_output_anno -%}
ASSERTION
{%- endcapture -%}

{%- capture approach_python_medical -%}
from johnsnowlabs import nlp, medical

from sparknlp_jsl.annotator import TFGraphBuilder

graph_folder = "./tf_graphs"
graph_name = "assertion_graph.pb"

assertion_graph_builder = TFGraphBuilder()\
    .setModelName("fewshot_assertion")\
    .setInputCols(["assertion_embedding"]) \
    .setLabelColumn("label")\
    .setGraphFolder(graph_folder)\
    .setGraphFile(graph_name)\
    .setHiddenUnitsNumber(100)

fewshot_assertion_approach = FewShotAssertionClassifierApproach()\
    .setInputCols("assertion_embedding")\
    .setOutputCol("assertion")\
    .setLabelCol("label")\
    .setBatchSize(32)\
    .setDropout(0.1)\
    .setLearningRate(0.001)\
    .setEpochsNumber(40)\
    .setValidationSplit(0.2)\
    .setModelFile(f"{graph_folder}/{graph_name}")

clinical_assertion_pipeline = Pipeline(
    stages = [
        assertion_graph_builder,
        fewshot_assertion_approach
    ])

assertion_model = clinical_assertion_pipeline.fit(assertion_train_data)

{%- endcapture -%}

{%- capture approach_scala_medical -%}
import spark.implicits._

// Defining pipeline stages to extract entities first
val documentAssembler = new MultiDocumentAssembler()
    .setInputCols(Array("text", "span"))
    .setOutputCols(Array("document", "span_document"))

val tokenizer = new Tokenizer()
    .setInputCols(Array("document"))
    .setOutputCol("token")

val chunker = new Doc2Chunk()
    .setInputCols(Array("span_document"))
    .setOutputCol("span_chunk")

val assertionConverter = new FewShotAssertionSentenceConverter()
    .setInputCols(Array("document", "span_chunk", "token"))
    .setOutputCol("assertion_sentence")

val sentenceEmbeddings = MPNetEmbeddings
    .pretrained()
    .setInputCols(Array("assertion_sentence"))
    .setOutputCol("assertion_embedding")

val fewShotAssertionApproach = FewShotAssertionClassifierApproach
    .setInputCols(Array("assertion_embedding"))
    .setOutputCol("prediction")
    .setLabelColumn("label")
    .setEpochsNumber(10)
    .setBatchSize(1)
    .setMultiClass(false)
    .setlearningRate(0.01f)

val pipeline = new Pipeline().setStages(
  Array(
    documentAssembler,
    tokenizer,
    chunker,
    assertionConverter,
    sentenceEmbeddings,
    fewShotAssertionApproach))

val model = pipeline.fit(trainData)


{%- endcapture -%}


{%- capture approach_api_link -%}
[FewShotAssertionClassifierApproach](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/classification/FewShotAssertionClassifierApproach.html)
{%- endcapture -%}

{%- capture approach_python_api_link -%}
[FewShotAssertionClassifierApproach](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/classification/few_shot_assertion_classifier/index.html)
{%- endcapture -%}

{%- capture approach_notebook_link -%}
[FewShotAssertionClassifierNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/2.2.FewShot_Assertion_Classifier.ipynb)
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
