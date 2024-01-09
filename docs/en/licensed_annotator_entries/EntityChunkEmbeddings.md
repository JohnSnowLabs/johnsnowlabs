{%- capture title -%}
EntityChunkEmbeddings
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
Weighted average embeddings of multiple named entities chunk annotations.

Entity Chunk Embeddings uses BERT Sentence embeddings to compute a weighted average vector represention of related entity chunks.  The input the model consists of chunks of recognized named entities. One or more entities are selected as target entities and for each of them a list of related entities is specified (if empty, all other entities are assumed to be related).

The model looks for chunks of the target entities and then tries to pair each target entity (e.g. DRUG)  with other related entities (e.g. DOSAGE, STRENGTH, FORM, etc). The criterion for pairing a target entity with another related entity is that they appear in the same sentence and the maximal syntactic distance is below a predefined threshold.

The relationship between target and related entities is one-to-many, meaning that if there multiple instances of the same target entity (e.g.) within a sentence, the model will map a related entity (e.g. DOSAGE) to at most one of the instances of the target entity. For example, if there is a sentence "The patient was given 125 mg of paracetamol and metformin", the model will pair "125 mg" to "paracetamol", but not to "metformin".

The output of the model is an average embeddings of the chunks of each of the target entities and their related entities. It is possible to specify a particular weight for each entity type.

An entity can be defined both as target a entity and as a related entity for some other target entity. For example, we may want to compute the embeddings of SYMPTOMs and their related entities, as well as the embeddings of DRUGs and their related entities, one of each is also SYMPTOM. In such cases, it is possible to use the TARGET_ENTITY:RELATED_ENTITY notation to specify the weight of an related entity (e.g. "DRUG:SYMPTOM" to set the weight of SYMPTOM when it appears as an related entity to target entity DRUG). The relative weights of entities for particular entity chunk embeddings are available in the annotations metadata.

This model is a subclass of `BertSentenceEmbeddings` and shares all parameters
with it. It can load any pretrained `BertSentenceEmbeddings` model.

Parametres:

- `targetEntities`: (dict) The target entities mapped to lists of their related entities. A target entity with an empty list of related entities means all other entities are assumed to be related to it. Entity names are case insensitive. *Mandatory to set at least one entity*

- `entityWeights`: (dict) The relative weights of drug related entities. If not set, all entities have equal weights. If the list is non-empty and some entity is not in it, then its weight is set to 0. The notation TARGET_ENTITY:RELATED_ENTITY can be used to specify the weight of a entity which is related to specific target entity (e.g. "DRUG:SYMPTOM" -> 0.3f). Entity names are case insensitive.

- `maxSyntacticDistance`: (Int) Maximal syntactic distance between the drug entity and the other drug related entities. Default value is 2.


The default model is `"sbiobert_base_cased_mli"` from `clinical/models`.
Other available models can be found at [Models Hub](https://nlp.johnsnowlabs.com/models?task=Embeddings).

{%- endcapture -%}

{%- capture model_input_anno -%}
DEPENDENCY, CHUNK
{%- endcapture -%}

{%- capture model_output_anno -%}
SENTENCE_EMBEDDINGS
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

documenter = nlp.DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

sentence_detector =  nlp.SentenceDetector()\
    .setInputCols("document")\
    .setOutputCol("sentence")\

tokenizer = nlp.Tokenizer()\
    .setInputCols("sentence")\
    .setOutputCol("token")

embeddings = nlp.WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

posology_ner_model = medical.NerModel().pretrained("ner_posology_large", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols("sentence", "token", "ner")\
    .setOutputCol("ner_chunk")

pos_tager = nlp.PerceptronModel().pretrained("pos_clinical", "en", "clinical/models")\
    .setInputCols("sentence", "token")\
    .setOutputCol("pos_tag")

dependency_parser = nlp.DependencyParserModel().pretrained("dependency_conllu", "en")\
    .setInputCols(["sentence", "pos_tag", "token"])\
    .setOutputCol("dependencies")

entity_chunk_embeddings = medical.EntityChunkEmbeddings().pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk", "dependencies"])\
    .setOutputCol("drug_chunk_embeddings")

entity_chunk_embeddings.setTargetEntities({"DRUG": ["STRENGTH", "ROUTE", "FORM"]})

rxnorm_re = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_rxnorm_augmented_re", "en", "clinical/models")\
    .setInputCols(["drug_chunk_embeddings"])\
    .setOutputCol("rxnorm_code")\
    .setDistanceFunction("EUCLIDEAN")

rxnorm_pipeline_re = nlp.Pipeline(
    stages=[
        documenter,
        sentence_detector,
        tokenizer,
        embeddings,
        posology_ner_model,
        ner_converter,
        pos_tager,
        dependency_parser,
        entity_chunk_embeddings,
        rxnorm_re,
    ]
)

rxnorm_model = rxnorm_pipeline_re.fit(spark.createDataFrame([[""]]).toDF("text"))

data_df = spark.createDataFrame(
    [
        [
            "The patient was given metformin 500 mg tablet, 2.5 mg of coumadin and then ibuprofen."
        ],
        [
            "The patient was given metformin 400 mg, coumadin 5 mg, coumadin, amlodipine 10 MG tablet"
        ],
    ]
).toDF("text")

results = rxnorm_model.transform(data_df)
results.select("drug_chunk_embeddings.result", "drug_chunk_embeddings.embeddings").show(truncate=200)

+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                              result|                                                                                                                                                                                              embeddings|
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|               [metformin 500 mg tablet, 2.5 mg coumadin, ibuprofen]|[[0.13060866, 0.26946265, -0.50702775, 0.7724293, 0.7356907, 0.0962475, -0.5546377, 0.0534295, -0.55345106, 0.48484787, -0.35735086, 0.49109104, 0.84404886, 0.30384326, -0.9923568, -0.24454081, 0.3...|
|[metformin 400 mg, coumadin 5 mg, coumadin, amlodipine 10 MG tablet]|[[-0.177948, 0.25489503, -0.5724586, 0.8031439, 0.9211674, 0.3558219, -0.37258363, -0.194855, -0.7407244, 0.48175216, 0.040639203, 0.6822441, 0.5768623, -0.19830275, -1.1513872, -0.32279214, 0.6181...|
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}

{%- capture model_scala_medical -%}
import spark.implicits._

val documenter = new DocumentAssembler()
    .setInputCol("text") 
    .setOutputCol("document") 

val sentence_detector = new SentenceDetector()
    .setInputCols("document") 
    .setOutputCol("sentence") 

val tokenizer = new Tokenizer()
    .setInputCols("sentence") 
    .setOutputCol("token") 

val embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models") 
    .setInputCols(Array("sentence","token")) 
    .setOutputCol("embeddings") 

val posology_ner_model = MedicalNerModel.pretrained("ner_posology_large","en","clinical/models") 
    .setInputCols(Array("sentence","token","embeddings")) 
    .setOutputCol("ner") 

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence","token","ner")) 
    .setOutputCol("ner_chunk") 

val pos_tager = PerceptronModel.pretrained("pos_clinical","en","clinical/models") 
    .setInputCols(Array("sentence","token")) 
    .setOutputCol("pos_tag") 

val dependency_parser = DependencyParserModel.pretrained("dependency_conllu","en") 
    .setInputCols(Array("sentence","pos_tag","token")) 
    .setOutputCol("dependencies") 

val entity_chunk_embeddings = EntityChunkEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models") 
    .setInputCols(Array("ner_chunk","dependencies")) 
    .setOutputCol("drug_chunk_embeddings") 

val entity_chunk_embeddings.setTargetEntities(Map("DRUG" -> "Array("STRENGTH","ROUTE","FORM")")) 

val rxnorm_re = SentenceEntityResolverModel.pretrained("sbiobertresolve_rxnorm_augmented_re","en","clinical/models")
    .setInputCols("drug_chunk_embeddings")
    .setOutputCol("rxnorm_code") 
    .setDistanceFunction("EUCLIDEAN") 

val rxnorm_pipeline_re = new Pipeline().setStages(Array( 
    documenter, 
    sentence_detector, 
    tokenizer, 
    embeddings, 
    posology_ner_model, 
    ner_converter, 
    pos_tager, 
    dependency_parser, 
    entity_chunk_embeddings,
    rxnorm_re)) 

val rxnorm_model = Seq(( "The patient was given metformin 500 mg tablet,2.5 mg of coumadin and then ibuprofen." ), ( "The patient was given metformin 400 mg,coumadin 5 mg,coumadin,amlodipine 10 MG tablet" )).toDF("text")

val results = rxnorm_model.fit(rxnorm_model).transform(rxnorm_model) 


+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                              result|                                                                                                                                                                                              embeddings|
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|               [metformin 500 mg tablet, 2.5 mg coumadin, ibuprofen]|[[0.13060866, 0.26946265, -0.50702775, 0.7724293, 0.7356907, 0.0962475, -0.5546377, 0.0534295, -0.55345106, 0.48484787, -0.35735086, 0.49109104, 0.84404886, 0.30384326, -0.9923568, -0.24454081, 0.3...|
|[metformin 400 mg, coumadin 5 mg, coumadin, amlodipine 10 MG tablet]|[[-0.177948, 0.25489503, -0.5724586, 0.8031439, 0.9211674, 0.3558219, -0.37258363, -0.194855, -0.7407244, 0.48175216, 0.040639203, 0.6822441, 0.5768623, -0.19830275, -1.1513872, -0.32279214, 0.6181...|
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}

{%- capture model_api_link -%}
[EntityChunkEmbeddingsModel](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/embeddings/EntityChunkEmbeddings.html)
{%- endcapture -%}


{%- capture model_python_api_link -%}
[EntityChunkEmbeddingsModel](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/embeddings/entity_chunk_embeddings/index.html#sparknlp_jsl.annotator.embeddings.entity_chunk_embeddings.EntityChunkEmbeddings)
{%- endcapture -%}

{%- capture model_notebook_link -%}
[EntityChunkEmbeddingsModelNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/EntityChunkEmbeddings.ipynb)
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
model_notebook_link=model_notebook_link
%}
