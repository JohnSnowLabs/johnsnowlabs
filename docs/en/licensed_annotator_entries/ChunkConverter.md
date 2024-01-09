{%- capture title -%}
ChunkConverter
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
Convert chunks from [RegexMatcher](https://nlp.johnsnowlabs.com/docs/en/annotators#regexmatcher) to chunks with a entity in the metadata.

This annotator is important when the user wants to merge entities identified by NER models together with rules-based matching used by the RegexMathcer annotator. In the following steps of the pipeline, all the identified entities can be treated in a unified field.

Parameters:

- `inputCols`: The name of the columns containing the input annotations. It can read either a String column or an Array.

- `outputCol`: The name of the column in Document type that is generated. We can specify only one column here.


All the parameters can be set using the corresponding set method in camel case. For example, `.setInputcols()`.

{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

# Creating the pipeline
rules = '''
\b[A-Z]+(\s+[A-Z]+)*:\b, SECTION_HEADER
'''

with open('regex_rules.txt', 'w') as f:
    f.write(rules)

sample_text = """
POSTOPERATIVE DIAGNOSIS: Cervical lymphadenopathy.
PROCEDURE:  Excisional biopsy of right cervical lymph node.
ANESTHESIA:  General endotracheal anesthesia.
Specimen:  Right cervical lymph node.
EBL: 10 cc.
COMPLICATIONS:  None.
FINDINGS: Enlarged level 2 lymph node was identified and removed and sent for pathologic examination.
FLUIDS:  Please see anesthesia report.
URINE OUTPUT:  None recorded during the case.
INDICATIONS FOR PROCEDURE:  This is a 43-year-old female with a several-year history of persistent cervical lymphadenopathy. She reports that it is painful to palpation on the right and has had multiple CT scans as well as an FNA which were all nondiagnostic. After risks and benefits of surgery were discussed with the patient, an informed consent was obtained. She was scheduled for an excisional biopsy of the right cervical lymph node.
PROCEDURE IN DETAIL:  The patient was taken to the operating room and placed in the supine position. She was anesthetized with general endotracheal anesthesia. The neck was then prepped and draped in the sterile fashion. Again, noted on palpation there was an enlarged level 2 cervical lymph node.A 3-cm horizontal incision was made over this lymph node. Dissection was carried down until the sternocleidomastoid muscle was identified. The enlarged lymph node that measured approximately 2 cm in diameter was identified and was removed and sent to Pathology for touch prep evaluation. The area was then explored for any other enlarged lymph nodes. None were identified, and hemostasis was achieved with electrocautery. A quarter-inch Penrose drain was placed in the wound.The wound was then irrigated and closed with 3-0 interrupted Vicryl sutures for a deep closure followed by a running 4-0 Prolene subcuticular suture. Mastisol and Steri-Strip were placed over the incision, and sterile bandage was applied. The patient tolerated this procedure well and was extubated without complications and transported to the recovery room in stable condition. She will return to the office tomorrow in followup to have the Penrose drain removed.
"""

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = medical.NerModel.pretrained("ner_clinical_large","en","clinical/models") \
    .setInputCols("sentence","token","embeddings") \
    .setOutputCol("ner")

ner_converter= medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\

regex_matcher = nlp.RegexMatcher()\
    .setInputCols('document')\
    .setStrategy("MATCH_ALL")\
    .setOutputCol("regex_matches")\
    .setExternalRules(path='/content/regex_rules.txt', delimiter=',')

chunkConverter = medical.ChunkConverter()\
    .setInputCols("regex_matches")\
    .setOutputCol("regex_chunk")

merger= medical.ChunkMergeApproach()\
    .setInputCols(["regex_chunk", "ner_chunk"])\
    .setOutputCol("merged_chunks")\
    .setMergeOverlapping(True)\
    .setChunkPrecedence("field")

pipeline= nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    word_embeddings,
    ner_model,
    ner_converter,
    regex_matcher,
    chunkConverter,
    merger
])

data= spark.createDataFrame([[sample_text]]).toDF("text")
result = pipeline.fit(data).transform(data)

# Results
result.select(F.explode(F.arrays_zip(result.merged_chunks.result, 
                                     result.merged_chunks.metadata)).alias("cols"))\
                  .select(F.expr("cols['0']").alias("chunk"),
                          F.expr("cols['1']['entity']").alias("merged_entity")).show(15, truncate=100)

+----------------------------------------------+--------------+
|                                         chunk| merged_entity|
+----------------------------------------------+--------------+
|                      POSTOPERATIVE DIAGNOSIS:|SECTION_HEADER|
|                      Cervical lymphadenopathy|       PROBLEM|
|                                    PROCEDURE:|SECTION_HEADER|
|Excisional biopsy of right cervical lymph node|          TEST|
|                                   ANESTHESIA:|SECTION_HEADER|
|               General endotracheal anesthesia|     TREATMENT|
|                     Right cervical lymph node|       PROBLEM|
|                                          EBL:|SECTION_HEADER|
|                                COMPLICATIONS:|SECTION_HEADER|
|                                     FINDINGS:|SECTION_HEADER|
|                   Enlarged level 2 lymph node|       PROBLEM|
|                        pathologic examination|          TEST|
|                                       FLUIDS:|SECTION_HEADER|
|                                 URINE OUTPUT:|SECTION_HEADER|
|                    INDICATIONS FOR PROCEDURE:|SECTION_HEADER|
+----------------------------------------------+--------------+

{%- endcapture -%}

{%- capture model_scala_medical -%}
// val rules = """\b[A-Z]+(\s+[A-Z]+)*:\b, SECTION_HEADER""" 
// with open("regex_rules.txt","w") as f: 
//    f.write(rules) 


import spark.implicits._

val documentAssembler = new DocumentAssembler()
    .setInputCol("text") 
    .setOutputCol("document") 

val sentenceDetector = new SentenceDetector()
    .setInputCols(Array("document")) 
    .setOutputCol("sentence") 

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence")) 
    .setOutputCol("token") 

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
    .setInputCols(Array("sentence","token"))
    .setOutputCol("embeddings") 

val ner_model = MedicalNerModel.pretrained("ner_clinical_large","en","clinical/models")
    .setInputCols("sentence","token","embeddings") 
    .setOutputCol("ner") 

val ner_converter= new NerConverterInternal() 
    .setInputCols(Array("sentence","token","ner")) 
    .setOutputCol("ner_chunk") 

val regex_matcher = new RegexMatcher()
    .setInputCols("document") 
    .setStrategy("MATCH_ALL") 
    .setOutputCol("regex_matches") 
    .setExternalRules(path="/content/regex_rules.txt",delimiter=",") 

val chunkConverter = new ChunkConverter()
    .setInputCols("regex_matches") 
    .setOutputCol("regex_chunk") 

val merger= new ChunkMergeApproach() 
    .setInputCols(Array("regex_chunk","ner_chunk")) 
    .setOutputCol("merged_chunks") 
    .setMergeOverlapping(true) 
    .setChunkPrecedence("field") 

val pipeline= new Pipeline().setStages(Array( 
    documentAssembler, 
    sentenceDetector, 
    tokenizer, 
    word_embeddings,
    ner_model, 
    ner_converter, 
    regex_matcher, 
    chunkConverter, 
    merger )) 

val data = Seq(("POSTOPERATIVE DIAGNOSIS: Cervical lymphadenopathy. PROCEDURE: Excisional biopsy of right cervical lymph node. ANESTHESIA: General endotracheal anesthesia. Specimen: Right cervical lymph node. EBL: 10 cc. COMPLICATIONS: None. FINDINGS: Enlarged level 2 lymph node was identified and removed and sent for pathologic examination. FLUIDS: Please see anesthesia report. URINE OUTPUT: None recorded during the case. INDICATIONS FOR PROCEDURE: This is a 43-year-old female with a several-year history of persistent cervical lymphadenopathy. She reports that it is painful to palpation on the right and has had multiple CT scans as well as an FNA which were all nondiagnostic. After risks and benefits of surgery were discussed with the patient,an informed consent was obtained. She was scheduled for an excisional biopsy of the right cervical lymph node. PROCEDURE IN DETAIL: The patient was taken to the operating room and placed in the supine position. She was anesthetized with general endotracheal anesthesia. The neck was then prepped and draped in the sterile fashion. Again,noted on palpation there was an enlarged level 2 cervical lymph node.A 3-cm horizontal incision was made over this lymph node. Dissection was carried down until the sternocleidomastoid muscle was identified. The enlarged lymph node that measured approximately 2 cm in diameter was identified and was removed and sent to Pathology for touch prep evaluation. The area was then explored for any other enlarged lymph nodes. None were identified,and hemostasis was achieved with electrocautery. A quarter-inch Penrose drain was placed in the wound.The wound was then irrigated and closed with 3-0 interrupted Vicryl sutures for a deep closure followed by a running 4-0 Prolene subcuticular suture. Mastisol and Steri-Strip were placed over the incision,and sterile bandage was applied. The patient tolerated this procedure well and was extubated without complications and transported to the recovery room in stable condition. She will return to the office tomorrow in followup to have the Penrose drain removed.")).toDF("text")

val result = pipeline.fit(data).transform(data)

+----------------------------------------------+--------------+
|                                         chunk| merged_entity|
+----------------------------------------------+--------------+
|                      POSTOPERATIVE DIAGNOSIS:|SECTION_HEADER|
|                      Cervical lymphadenopathy|       PROBLEM|
|                                    PROCEDURE:|SECTION_HEADER|
|Excisional biopsy of right cervical lymph node|          TEST|
|                                   ANESTHESIA:|SECTION_HEADER|
|               General endotracheal anesthesia|     TREATMENT|
|                     Right cervical lymph node|       PROBLEM|
|                                          EBL:|SECTION_HEADER|
|                                COMPLICATIONS:|SECTION_HEADER|
|                                     FINDINGS:|SECTION_HEADER|
|                   Enlarged level 2 lymph node|       PROBLEM|
|                        pathologic examination|          TEST|
|                                       FLUIDS:|SECTION_HEADER|
|                                 URINE OUTPUT:|SECTION_HEADER|
|                    INDICATIONS FOR PROCEDURE:|SECTION_HEADER|
+----------------------------------------------+--------------+
{%- endcapture -%}

{%- capture model_python_finance -%}
from johnsnowlabs import nlp, finance

# Creating the pipeline
rules = '''
\b[A-Z]+(\s+[A-Z]+)*:\b, SECTION_HEADER
'''

with open('regex_rules.txt', 'w') as f:
    f.write(rules)

sample_text="""AWA Group LP intends to pay dividends on the Common Units on a quarterly basis at an annual rate of 8.00% of the Offering Price. """

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

ner_model = finance.NerModel.pretrained("finner_orgs_prods_alias", "en", "finance/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter= nlp.NerConverter()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")
    # .setWhiteList(["ORG"]) # Return only ORG entities

regex_matcher = nlp.RegexMatcher()\
    .setInputCols('document')\
    .setStrategy("MATCH_ALL")\
    .setOutputCol("regex_matches")\
    .setExternalRules(path='/content/regex_rules.txt', delimiter=',')

chunkConverter = finance.ChunkConverter()\
    .setInputCols("regex_matches")\
    .setOutputCol("regex_chunk")

merger= finance.ChunkMergeApproach()\
    .setInputCols(["regex_chunk", "ner_chunk"])\
    .setOutputCol("merged_chunks")\
    .setMergeOverlapping(True)\
    .setChunkPrecedence("field")

pipeline= nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    word_embeddings,
    ner_model,
    ner_converter,
    regex_matcher,
    chunkConverter,
    merger
])

data= spark.createDataFrame([[sample_text]]).toDF("text")
result = pipeline.fit(data).transform(data)

# Results
result.select(F.explode(F.arrays_zip(result.merged_chunks.result, 
                                     result.merged_chunks.metadata)).alias("cols"))\
                  .select(F.expr("cols['0']").alias("chunk"),
                          F.expr("cols['1']['entity']").alias("merged_entity")).show(15, truncate=100)

+--------+-------------+
|   chunk|merged_entity|
+--------+-------------+
|Group LP|          ORG|
+--------+-------------+


{%- endcapture -%}

{%- capture model_scala_finance -%}
// val rules = """\b[A-Z]+(\s+[A-Z]+)*:\b, SECTION_HEADER""" 
// with open("regex_rules.txt","w") as f: 
//    f.write(rules) 

import spark.implicits._

val documentAssembler = new DocumentAssembler()
    .setInputCol("text") 
    .setOutputCol("document") 

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
    .setInputCols(Array("document")) 
    .setOutputCol("sentence") 

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence")) 
    .setOutputCol("token") 

val word_embeddings = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en")
    .setInputCols(Array("sentence","token")) 
    .setOutputCol("embeddings") 

val ner_model = FinanceNerModel.pretrained("finner_orgs_prods_alias","en","finance/models")
    .setInputCols(Array("sentence","token","embeddings")) 
    .setOutputCol("ner") 

val ner_converter= new NerConverterInternal()  
    .setInputCols(Array("sentence","token","ner")) 
    .setOutputCol("ner_chunk") 
    // .setWhiteList(Array("ORG")) 

// Return only ORG entities 
val regex_matcher = new RegexMatcher()
    .setInputCols("document") 
    .setStrategy("MATCH_ALL") 
    .setOutputCol("regex_matches") 
    .setExternalRules(path="/content/regex_rules.txt",delimiter=",") 

val chunkConverter = new ChunkConverter()
    .setInputCols("regex_matches") 
    .setOutputCol("regex_chunk") 
 
val merger= new ChunkMergeApproach() 
    .setInputCols(Array("regex_chunk","ner_chunk")) 
    .setOutputCol("merged_chunks") 
    .setMergeOverlapping(true) 
    .setChunkPrecedence("field") 

val pipeline= new Pipeline().setStages(Array( 
    documentAssembler, 
    sentenceDetector, 
    tokenizer, 
    word_embeddings, 
    ner_model, 
    ner_converter, 
    regex_matcher, 
    chunkConverter, 
    merger )) 
    
val data = Seq(("AWA Group LP intends to pay dividends on the Common Units on a quarterly basis at an annual rate of 8.00% of the Offering Price.")).toDF("text")

val result = pipeline.fit(data).transform(data)

+--------+-------------+
|   chunk|merged_entity|
+--------+-------------+
|Group LP|          ORG|
+--------+-------------+

{%- endcapture -%}

{%- capture model_python_legal -%}
from johnsnowlabs import nlp, legal

# Creating the pipeline
rules = '''
\b[A-Z]+(\s+[A-Z]+)*:\b, SECTION_HEADER
'''

with open('regex_rules.txt', 'w') as f:
    f.write(rules)

sample_text="""AWA Group LP intends to pay dividends on the Common Units on a quarterly basis at an annual rate of 8.00% of the Offering Price. """

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

ner_model = legal.NerModel.pretrained("legner_org_per_role_date", "en", "legal/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter= nlp.NerConverter()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")
    # .setWhiteList(["ORG"]) # Return only ORG entities

regex_matcher = nlp.RegexMatcher()\
    .setInputCols('document')\
    .setStrategy("MATCH_ALL")\
    .setOutputCol("regex_matches")\
    .setExternalRules(path='/content/regex_rules.txt', delimiter=',')

chunkConverter = legal.ChunkConverter()\
    .setInputCols("regex_matches")\
    .setOutputCol("regex_chunk")

merger= legal.ChunkMergeApproach()\
    .setInputCols(["regex_chunk", "ner_chunk"])\
    .setOutputCol("merged_chunks")\
    .setMergeOverlapping(True)\
    .setChunkPrecedence("field")

pipeline= nlp.Pipeline(stages=[
    documentAssembler,
    sentenceDetector,
    tokenizer,
    word_embeddings,
    ner_model,
    ner_converter,
    regex_matcher,
    chunkConverter,
    merger
])

data= spark.createDataFrame([[sample_text]]).toDF("text")
result = pipeline.fit(data).transform(data)

# Results
result.select(F.explode(F.arrays_zip(result.merged_chunks.result, 
                                     result.merged_chunks.metadata)).alias("cols"))\
                  .select(F.expr("cols['0']").alias("chunk"),
                          F.expr("cols['1']['entity']").alias("merged_entity")).show(15, truncate=100)

+--------+-------------+
|   chunk|merged_entity|
+--------+-------------+
|Group LP|          ORG|
+--------+-------------+


{%- endcapture -%}

{%- capture model_scala_legal -%}
// val rules = """[A-Z]+[\s+[A-Z]+]*,SECTION_HEADER """ 
// with open("regex_rules.txt","w") as f: 
//    f.write(rules) 

import spark.implicits._

val documentAssembler = new DocumentAssembler()
    .setInputCol("text") 
    .setOutputCol("document") 

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
    .setInputCols(Array("document")) 
    .setOutputCol("sentence") 

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence")) 
    .setOutputCol("token") 

val word_embeddings = BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en")
    .setInputCols(Array("sentence","token")) 
    .setOutputCol("embeddings") 

val ner_model = LegalNerModel.pretrained("legner_org_per_role_date", "en", "legal/models")
    .setInputCols(Array("sentence","token","embeddings")) 
    .setOutputCol("ner") 

val ner_converter= new NerConverterInternal()  
    .setInputCols(Array("sentence","token","ner")) 
    .setOutputCol("ner_chunk") 
    // .setWhiteList(Array("ORG")) 

// Return only ORG entities 
val regex_matcher = new RegexMatcher()
    .setInputCols("document") 
    .setStrategy("MATCH_ALL") 
    .setOutputCol("regex_matches") 
    .setExternalRules(path="/content/regex_rules.txt",delimiter=",") 

val chunkConverter = new ChunkConverter()
    .setInputCols("regex_matches") 
    .setOutputCol("regex_chunk") 
 
val merger= new ChunkMergeApproach() 
    .setInputCols(Array("regex_chunk","ner_chunk")) 
    .setOutputCol("merged_chunks") 
    .setMergeOverlapping(true) 
    .setChunkPrecedence("field") 

val pipeline= new Pipeline().setStages(Array( 
    documentAssembler, 
    sentenceDetector, 
    tokenizer, 
    word_embeddings, 
    ner_model, 
    ner_converter, 
    regex_matcher, 
    chunkConverter, 
    merger )) 
    
val data = Seq(("AWA Group LP intends to pay dividends on the Common Units on a quarterly basis at an annual rate of 8.00% of the Offering Price.")).toDF("text")

val result = pipeline.fit(data).transform(data)
                          
+--------+-------------+
|   chunk|merged_entity|
+--------+-------------+
|Group LP|          ORG|
+--------+-------------+
{%- endcapture -%}

{%- capture model_api_link -%}
[ChunkConverter](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/chunker/ChunkConverter.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[ChunkConverter](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/chunker/chunk_converter/index.html#sparknlp_jsl.annotator.chunker.chunk_converter.ChunkConverter.html)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[ChunkConverterNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ChunkConverter.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
model_python_finance=model_python_finance
model_scala_finance=model_scala_finance
model_python_legal=model_python_legal
model_scala_legal=model_scala_legal
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link
%}
