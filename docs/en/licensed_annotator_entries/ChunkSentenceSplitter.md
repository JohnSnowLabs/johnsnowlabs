{%- capture title -%}
ChunkSentenceSplitter
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}

`ChunkSentenceSplitter` annotator can split the documents into chunks according to separators given as `CHUNK` columns. It is useful when you need to perform different models or analysis in different sections of your document (for example, for different headers, clauses, items, etc.). The given separator chunk can be the output from, for example, [RegexMatcher](https://nlp.johnsnowlabs.com/docs/en/annotators#regexmatcher) or [NerModel](https://nlp.johnsnowlabs.com/docs/en/licensed_annotators#nermodel).

Parametres;

- `GroupBySentences`: (boolean) Sets the groupBySentences that allow split the paragraphs grouping the chunks by sentences.

- `InsertChunk`: (boolean) Whether to insert the chunk in the paragraph or not.

- `DefaultEntity`: (str) Sets the key in the metadata dictionary that you want to filter (by default "entity")

For detailed usage of this annotator, visit [this notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/18.Chunk_Sentence_Splitter.ipynb) from our `Spark NLP Workshop`.

{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_python_medical -%}

# Defining the pipeline
documentAssembler = nlp.DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
        .setInputCols(["document"])\
        .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
      .setInputCols(["sentence"])\
      .setOutputCol("token")\

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
      .setInputCols(["sentence", "token"])\
      .setOutputCol("embeddings")

clinical_ner = medical.NerModel.pretrained("ner_jsl_slim", "en", "clinical/models") \
      .setInputCols(["sentence", "token", "embeddings"]) \
      .setOutputCol("ner")

ner_converter = medical.NerConverterInternal() \
      .setInputCols(["sentence", "token", "ner"]) \
      .setOutputCol("ner_chunk")\
      .setWhiteList(["Header"])

#applying ChunkSentenceSplitter
chunkSentenceSplitter = medical.ChunkSentenceSplitter()\
    .setInputCols("document","ner_chunk")\
    .setOutputCol("paragraphs")\
    .setGroupBySentences(False)

pipeline_model = nlp.Pipeline(
    stages = [
        documentAssembler,
        sentenceDetector,
        tokenizer,
        word_embeddings,
        clinical_ner,
        ner_converter,
        chunkSentenceSplitter
    ])


sentences = [["""Sample Name: Mesothelioma - Pleural Biopsy
Description: Right pleural effusion and suspected malignant mesothelioma. (Medical Transcription Sample Report)
PREOPERATIVE DIAGNOSIS:  Right pleural effusion and suspected malignant mesothelioma.
POSTOPERATIVE DIAGNOSIS: Right pleural effusion, suspected malignant mesothelioma.
ANESTHESIA: General double-lumen endotracheal.
DESCRIPTION OF FINDINGS:  Right pleural effusion, firm nodules, diffuse scattered throughout the right pleura and diaphragmatic surface.
SPECIMEN:  Pleural biopsies for pathology and microbiology.
INDICATIONS:  Briefly, this is a 66-year-old gentleman who has been transferred from an outside hospital after a pleural effusion had been drained and biopsies taken from the right chest that were thought to be consistent with mesothelioma. Upon transfer, he had a right pleural effusion demonstrated on x-ray as well as some shortness of breath and dyspnea on exertion. The risks, benefits, and alternatives to right VATS pleurodesis and pleural biopsy were discussed with the patient and his family and they wished to proceed.
Dr. X was present for the entire procedure which was right VATS pleurodesis and pleural biopsies.The counts were correct x2 at the end of the case."""]]

df = spark.createDataFrame(sentences).toDF("text")
paragraphs = pipeline_model.fit(df).transform(df)

paragraphs.selectExpr("explode(paragraphs) as result")\
          .selectExpr("result.result","result.metadata.entity", "result.metadata.splitter_chunk").show(truncate=80)

+--------------------------------------------------------------------------------+------------+------------------------+
|                                                                          result|      entity|          splitter_chunk|
+--------------------------------------------------------------------------------+------------+------------------------+
|                                     Sample Name: Mesothelioma - Pleural Biopsy |introduction|                     UNK|
|Description: Right pleural effusion and suspected malignant mesothelioma. (Me...|      Header|            Description:|
|PREOPERATIVE DIAGNOSIS:  Right pleural effusion and suspected malignant mesot...|      Header| PREOPERATIVE DIAGNOSIS:|
|POSTOPERATIVE DIAGNOSIS: Right pleural effusion, suspected malignant mesothel...|      Header|POSTOPERATIVE DIAGNOSIS:|
|                                 ANESTHESIA: General double-lumen endotracheal. |      Header|             ANESTHESIA:|
|DESCRIPTION OF FINDINGS:  Right pleural effusion, firm nodules, diffuse scatt...|      Header|DESCRIPTION OF FINDINGS:|
|                    SPECIMEN:  Pleural biopsies for pathology and microbiology. |      Header|               SPECIMEN:|
|INDICATIONS:  Briefly, this is a 66-year-old gentleman who has been transferr...|      Header|            INDICATIONS:|
+--------------------------------------------------------------------------------+------------+------------------------+

{%- endcapture -%}

{%- capture model_scala_medical -%}

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val clinical_ner = MedicalNerModel.pretrained("ner_jsl_slim", "en", "clinical/models") \
    .setInputCols(Array("sentence", "token", "embeddings")) 
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal() 
    .setInputCols(Array("sentence", "token", "ner")) 
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("Header"))

//applying ChunkSentenceSplitter
val chunkSentenceSplitter = new ChunkSentenceSplitter()
    .setInputCols("document","ner_chunk")
    .setOutputCol("paragraphs")
    .setGroupBySentences(false)

val pipeline_model = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    word_embeddings,
    clinical_ner,
    ner_converter,
    chunkSentenceSplitter
))


val sentences = ("""Sample Name: Mesothelioma - Pleural Biopsy
Description: Right pleural effusion and suspected malignant mesothelioma. (Medical Transcription Sample Report)
PREOPERATIVE DIAGNOSIS:  Right pleural effusion and suspected malignant mesothelioma.
POSTOPERATIVE DIAGNOSIS: Right pleural effusion, suspected malignant mesothelioma.
ANESTHESIA: General double-lumen endotracheal.
DESCRIPTION OF FINDINGS:  Right pleural effusion, firm nodules, diffuse scattered throughout the right pleura and diaphragmatic surface.
SPECIMEN:  Pleural biopsies for pathology and microbiology.
INDICATIONS:  Briefly, this is a 66-year-old gentleman who has been transferred from an outside hospital after a pleural effusion had been drained and biopsies taken from the right chest that were thought to be consistent with mesothelioma. Upon transfer, he had a right pleural effusion demonstrated on x-ray as well as some shortness of breath and dyspnea on exertion. The risks, benefits, and alternatives to right VATS pleurodesis and pleural biopsy were discussed with the patient and his family and they wished to proceed.
Dr. X was present for the entire procedure which was right VATS pleurodesis and pleural biopsies.The counts were correct x2 at the end of the case.""")

val data = Seq(sentences).toDF("text")
val paragraphs = pipeline_model.fit(df).transform(df)

paragraphs.selectExpr("explode(paragraphs) as result")
          .selectExpr("result.result","result.metadata.entity", "result.metadata.splitter_chunk").show(truncate=80)

+--------------------------------------------------------------------------------+------------+------------------------+
|                                                                          result|      entity|          splitter_chunk|
+--------------------------------------------------------------------------------+------------+------------------------+
|                                     Sample Name: Mesothelioma - Pleural Biopsy |introduction|                     UNK|
|Description: Right pleural effusion and suspected malignant mesothelioma. (Me...|      Header|            Description:|
|PREOPERATIVE DIAGNOSIS:  Right pleural effusion and suspected malignant mesot...|      Header| PREOPERATIVE DIAGNOSIS:|
|POSTOPERATIVE DIAGNOSIS: Right pleural effusion, suspected malignant mesothel...|      Header|POSTOPERATIVE DIAGNOSIS:|
|                                 ANESTHESIA: General double-lumen endotracheal. |      Header|             ANESTHESIA:|
|DESCRIPTION OF FINDINGS:  Right pleural effusion, firm nodules, diffuse scatt...|      Header|DESCRIPTION OF FINDINGS:|
|                    SPECIMEN:  Pleural biopsies for pathology and microbiology. |      Header|               SPECIMEN:|
|INDICATIONS:  Briefly, this is a 66-year-old gentleman who has been transferr...|      Header|            INDICATIONS:|
+--------------------------------------------------------------------------------+------------+------------------------+

{%- endcapture -%}

{%- capture model_python_legal -%}

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")
        
sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") \
        .setInputCols(["sentence", "token"]) \
        .setOutputCol("embeddings")

ner_model = legal.NerModel.pretrained("legner_headers", "en", "legal/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = nlp.NerConverter()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")

chunkSentenceSplitter = legal.ChunkSentenceSplitter()\
    .setInputCols("document","ner_chunk")\
    .setOutputCol("paragraphs")\
    .setGroupBySentences(False)

    
nlp_pipeline = nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter,
    chunkSentenceSplitter])


text = """AGREEMENT

NOW, THEREFORE, for good and valuable consideration, and in consideration of the mutual covenants and conditions herein contained, the Parties agree as follows:

2. Definitions. For purposes of this Agreement, the following terms have the meanings ascribed thereto in this Section 1. 2. Appointment as Reseller.

2.1 Appointment. The Company hereby [***]. Allscripts may also disclose Company"s pricing information relating to its Merchant Processing Services and facilitate procurement of Merchant Processing Services on behalf of Sublicensed Customers, including, without limitation by references to such pricing information and Merchant Processing Services in Customer Agreements. 6

2.2 Customer Agreements.

a) Subscriptions. Allscripts and its Affiliates may sell Subscriptions for terms no less than one year and no greater than four (4) years on a subscription basis to Persons who subsequently execute a Customer Agreement, provided that Allscripts may enter into Customer Agreements with terms longer than four (4) years with large organizations, provided that Phreesia consents in each instance in writing in advance, which consent will not be unreasonably withheld."""

sdf = spark.createDataFrame([[text]]).toDF("text")
paragraphs = nlp_pipeline.fit(sdf).transform(sdf)

paragraphs.selectExpr("explode(paragraphs) as result")\
          .selectExpr("result.result","result.metadata.entity").show(truncate=50)

+----------------------------------------------------------------------------------------------------+---------+
|                                                                                              result|   entity|
+----------------------------------------------------------------------------------------------------+---------+
|AGREEMENT  NOW, THEREFORE, for good and valuable consideration, and in consideration of the mutua...|SUBHEADER|
|                                                                          Appointment as Reseller.  |SUBHEADER|
|                                                                                   2.1 Appointment. |SUBHEADER|
|The Company hereby [***]. Allscripts may also disclose Company"s pricing information relating to ...|SUBHEADER|
|                                                                       6 2.2 Customer Agreements.   |   HEADER|
|a) Subscriptions. Allscripts and its Affiliates may sell Subscriptions for terms no less than one...|SUBHEADER|
+----------------------------------------------------------------------------------------------------+---------+

{%- endcapture -%}

{%- capture model_scala_legal -%}

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
        
val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val embeddings = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") 
    .setInputCols(Array("sentence", "token")) 
    .setOutputCol("embeddings")

val ner_model = LegalNerModel.pretrained("legner_headers", "en", "legal/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence","token","ner"))
    .setOutputCol("ner_chunk")

val chunkSentenceSplitter = new ChunkSentenceSplitter()
    .setInputCols("document","ner_chunk")
    .setOutputCol("paragraphs")
    .setGroupBySentences(false)
    
val nlp_pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter,
    chunkSentenceSplitter))


val text = """AGREEMENT

NOW, THEREFORE, for good and valuable consideration, and in consideration of the mutual covenants and conditions herein contained, the Parties agree as follows:

2. Definitions. For purposes of this Agreement, the following terms have the meanings ascribed thereto in this Section 1. 2. Appointment as Reseller.

2.1 Appointment. The Company hereby [***]. Allscripts may also disclose Company"s pricing information relating to its Merchant Processing Services and facilitate procurement of Merchant Processing Services on behalf of Sublicensed Customers, including, without limitation by references to such pricing information and Merchant Processing Services in Customer Agreements. 6

2.2 Customer Agreements.

a) Subscriptions. Allscripts and its Affiliates may sell Subscriptions for terms no less than one year and no greater than four (4) years on a subscription basis to Persons who subsequently execute a Customer Agreement, provided that Allscripts may enter into Customer Agreements with terms longer than four (4) years with large organizations, provided that Phreesia consents in each instance in writing in advance, which consent will not be unreasonably withheld."""

val data = Seq(text).toDF("text")
val paragraphs = nlp_pipeline.fit(data).transform(data)

paragraphs.selectExpr("explode(paragraphs) as result")
          .selectExpr("result.result","result.metadata.entity").show(truncate=50)

+----------------------------------------------------------------------------------------------------+---------+
|                                                                                              result|   entity|
+----------------------------------------------------------------------------------------------------+---------+
|AGREEMENT  NOW, THEREFORE, for good and valuable consideration, and in consideration of the mutua...|SUBHEADER|
|                                                                          Appointment as Reseller.  |SUBHEADER|
|                                                                                   2.1 Appointment. |SUBHEADER|
|The Company hereby [***]. Allscripts may also disclose Company"s pricing information relating to ...|SUBHEADER|
|                                                                       6 2.2 Customer Agreements.   |   HEADER|
|a) Subscriptions. Allscripts and its Affiliates may sell Subscriptions for terms no less than one...|SUBHEADER|
+----------------------------------------------------------------------------------------------------+---------+

{%- endcapture -%}


{%- capture model_python_finance -%}

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

ner_model = finance.NerModel.pretrained("finner_headers", "en", "finance/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = finance.NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")

chunkSentenceSplitter = legal.ChunkSentenceSplitter()\
    .setInputCols("document","ner_chunk")\
    .setOutputCol("paragraphs")\
    .setGroupBySentences(False)

nlp_pipeline = nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter,
    chunkSentenceSplitter])


text = """2. DEFINITION. 

For purposes of this Agreement, the following terms have the meanings ascribed thereto in this Section 1 and 2 Appointment as Reseller.

2.1 Appointment. 

The Company hereby [***]. Allscripts may also disclose Company"s pricing information relating to its Merchant Processing Services and facilitate procurement of Merchant Processing Services on behalf of Sublicensed Customers, including, without limitation by references to such pricing information and Merchant Processing Services in Customer Agreements. 6

2.2 Customer Agreements."""

sdf = spark.createDataFrame([[text]]).toDF("text")
paragraphs = nlp_pipeline.fit(sdf).transform(sdf)

paragraphs.selectExpr("explode(paragraphs) as result")\
          .selectExpr("result.result","result.metadata.entity").show(truncate=50)

+----------------------------------------------------------------------------------------------------+---------+
|                                                                                              result|   entity|
+----------------------------------------------------------------------------------------------------+---------+
|                                                                                                 2. |   HEADER|
|DEFINITION.   For purposes of this Agreement, the following terms have the meanings ascribed ther...|SUBHEADER|
|                                                                                 2.1 Appointment.   |SUBHEADER|
|The Company hereby [***]. Allscripts may also disclose Company"s pricing information relating to ...|SUBHEADER|
|                                                                          6  2.2 Customer Agreements|   HEADER|
+----------------------------------------------------------------------------------------------------+---------+

{%- endcapture -%}

{%- capture model_scala_legal -%}

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
        
val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val embeddings = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") 
    .setInputCols(Array("sentence", "token")) 
    .setOutputCol("embeddings")

val ner_model = FinanceNerModel.pretrained("finner_headers", "en", "finance/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence","token","ner"))
    .setOutputCol("ner_chunk")

val chunkSentenceSplitter = new ChunkSentenceSplitter()
    .setInputCols("document","ner_chunk")
    .setOutputCol("paragraphs")
    .setGroupBySentences(false)

val nlp_pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter,
    chunkSentenceSplitter))


val text = """2. DEFINITION. 

For purposes of this Agreement, the following terms have the meanings ascribed thereto in this Section 1 and 2 Appointment as Reseller.

2.1 Appointment. 

The Company hereby [***]. Allscripts may also disclose Company"s pricing information relating to its Merchant Processing Services and facilitate procurement of Merchant Processing Services on behalf of Sublicensed Customers, including, without limitation by references to such pricing information and Merchant Processing Services in Customer Agreements. 6

2.2 Customer Agreements."""

val data = Seq(text).toDF("text")
val paragraphs = nlp_pipeline.fit(data).transform(data)

paragraphs.selectExpr("explode(paragraphs) as result")
          .selectExpr("result.result","result.metadata.entity").show(truncate=50)

+----------------------------------------------------------------------------------------------------+---------+
|                                                                                              result|   entity|
+----------------------------------------------------------------------------------------------------+---------+
|                                                                                                 2. |   HEADER|
|DEFINITION.   For purposes of this Agreement, the following terms have the meanings ascribed ther...|SUBHEADER|
|                                                                                 2.1 Appointment.   |SUBHEADER|
|The Company hereby [***]. Allscripts may also disclose Company"s pricing information relating to ...|SUBHEADER|
|                                                                          6  2.2 Customer Agreements|   HEADER|
+----------------------------------------------------------------------------------------------------+---------+

{%- endcapture -%}


{%- capture model_api_link -%}
[ChunkSentenceSplitter](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/chunker/ChunkSentenceSplitter.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[ChunkSentenceSplitter](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/chunker/chunk_sentence_splitter/index.html#sparknlp_jsl.annotator.chunker.chunk_sentence_splitter.ChunkSentenceSplitter)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[ChunkSentenceSplitter](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ChunkSentenceSplitter.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
model_python_legal=model_python_legal
model_scala_legal=model_scala_legal
model_python_finance=model_python_finance
model_scala_finance=model_scala_finance
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link
%}
