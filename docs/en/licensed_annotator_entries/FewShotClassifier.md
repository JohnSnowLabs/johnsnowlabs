{%- capture title -%}
FewShotClassifier
{%- endcapture -%}

{%- capture approach -%}
approach
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
`FewShotClassifier` annotators specifically target few-shot classification tasks, which involve training a model to make accurate predictions with limited labeled data.

These annotators provide a valuable capability for handling scenarios where labeled data is scarce or expensive to obtain. By effectively utilizing limited labeled examples, the few-shot classification approach enables the creation of models that can generalize and classify new instances accurately, even with minimal training data.

The FewShotClassifier is designed to process sentence embeddings as input. It generates category annotations, providing labels along with confidence scores that range from 0 to 1.
{%- endcapture -%}

{%- capture model_input_anno -%}
SENTENCE EMBEDDINGS
{%- endcapture -%}

{%- capture model_output_anno -%}
CATEGORY
{%- endcapture -%}

{%- capture model_python_medical -%}

from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

bert_sent = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence_embeddings")

few_shot_classifier = medical.FewShotClassifierModel.pretrained("few_shot_classifier_age_group_sbiobert_cased_mli", "en", "clinical/models")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("prediction")

clf_Pipeline = nlp.Pipeline(stages=[
    document_assembler,
    bert_sent,
    few_shot_classifier
])

data = spark.createDataFrame([
    ["""A patient presented with complaints of chest pain and shortness of breath. The medical history revealed the patient had a smoking habit for over 30 years, and was diagnosed with hypertension two years ago. After a detailed physical examination, the doctor found a noticeable wheeze on lung auscultation and prescribed a spirometry test, which showed irreversible airway obstruction. The patient was diagnosed with Chronic obstructive pulmonary disease (COPD) caused by smoking."""],
 ["""Hi, wondering if anyone has had a similar situation. My 1 year old daughter has the following; loose stools/ pale stools, elevated liver enzymes, low iron.  5 months and still no answers from drs. """],
 ["""Hi have chronic gastritis from 4 month(confirmed by endoscopy).I do not have acid reflux.Only dull ache above abdomen and left side of chest.I am on reberprozole and librax.My question is whether chronic gastritis is curable or is it a lifetime condition?I am loosing hope because this dull ache is not going away.Please please reply"""]
    ]).toDF("text")

result = clf_Pipeline.fit(data).transform(data)


# Show results
result.select('prediction.result','text').show(truncate=150)

+---------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|   result|                                                                                                                                                  text|
+---------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|  [Adult]|A patient presented with complaints of chest pain and shortness of breath. The medical history revealed the patient had a smoking habit for over 30...|
|  [Child]|Hi, wondering if anyone has had a similar situation. My 1 year old daughter has the following; loose stools/ pale stools, elevated liver enzymes, l...|
|[Unknown]|Hi have chronic gastritis from 4 month(confirmed by endoscopy).I do not have acid reflux.Only dull ache above abdomen and left side of chest.I am o...|
+---------+------------------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}


{%- capture model_scala_medical -%}

import spark.implicits._

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val bert_sent = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence_embeddings")

val few_shot_classifier = FewShotClassifierModel.pretrained("few_shot_classifier_age_group_sbiobert_cased_mli", "en", "clinical/models")
    .setInputCols("sentence_embeddings")
    .setOutputCol("prediction") 
    
val clf_Pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    bert_sent, 
    few_shot_classifier))

val data = Seq(
    ("""A patient presented with complaints of chest pain and shortness of breath. The medical history revealed the patient had a smoking habit for over 30 years, and was diagnosed with hypertension two years ago. After a detailed physical examination, the doctor found a noticeable wheeze on lung auscultation and prescribed a spirometry test, which showed irreversible airway obstruction. The patient was diagnosed with Chronic obstructive pulmonary disease (COPD) caused by smoking."""),
 ("""Hi, wondering if anyone has had a similar situation. My 1 year old daughter has the following; loose stools/ pale stools, elevated liver enzymes, low iron.  5 months and still no answers from drs. """),
 ("""Hi have chronic gastritis from 4 month(confirmed by endoscopy).I do not have acid reflux.Only dull ache above abdomen and left side of chest.I am on reberprozole and librax.My question is whether chronic gastritis is curable or is it a lifetime condition?I am loosing hope because this dull ache is not going away.Please please reply""")).toDF("text")
  
val result = clf_Pipeline.fit(data).transform(data)

// Show results


+---------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|   result|                                                                                                                                                  text|
+---------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|  [Adult]|A patient presented with complaints of chest pain and shortness of breath. The medical history revealed the patient had a smoking habit for over 30...|
|  [Child]|Hi, wondering if anyone has had a similar situation. My 1 year old daughter has the following; loose stools/ pale stools, elevated liver enzymes, l...|
|[Unknown]|Hi have chronic gastritis from 4 month(confirmed by endoscopy).I do not have acid reflux.Only dull ache above abdomen and left side of chest.I am o...|
+---------+------------------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}


{%- capture model_api_link -%}
[FewShotClassifierModel](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/classification/FewShotClassifierModel.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[FewShotClassifierModel](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/classification/few_shot_classifier/index.html#sparknlp_jsl.annotator.classification.few_shot_classifier.FewShotClassifierModel)
{%- endcapture -%}



{%- capture approach_description -%}
`FewShotClassifier` annotators specifically target few-shot classification tasks, which involve training a model to make accurate predictions with limited labeled data.

These annotators provide a valuable capability for handling scenarios where labeled data is scarce or expensive to obtain. By effectively utilizing limited labeled examples, the few-shot classification approach enables the creation of models that can generalize and classify new instances accurately, even with minimal training data.

The FewShotClassifier is designed to process sentence embeddings as input. It generates category annotations, providing labels along with confidence scores that range from 0 to 1.
{%- endcapture -%}

{%- capture approach_input_anno -%}
SENTENCE EMBEDDINGS
{%- endcapture -%}

{%- capture approach_output_anno -%}
CATEGORY
{%- endcapture -%}

{%- capture approach_python_medical -%}

from johnsnowlabs import nlp, medical 

document_asm = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("sentence")

sentence_embeddings = nlp.BertSentenceEmbeddings\
.pretrained("sbiobert_base_cased_mli","en","clinical/models")\
    .setInputCols(["sentence"])\
    .setOutputCol("sentence_embeddings")

graph_builder = medical.TFGraphBuilder()\
    .setModelName("fewshot_classifier")\
    .setInputCols(["sentence_embeddings"]) \
    .setLabelColumn("label")\
    .setGraphFolder("/tmp")\
    .setGraphFile("log_reg_graph.pb")\

few_shot_approach = medical.FewShotClassifierApproach()\
    .setLabelColumn("label")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("prediction")\
    .setModelFile(f"/tmp/log_reg_graph.pb")\
    .setEpochsNumber(10)\
    .setBatchSize(1)\
    .setLearningRate(0.001)

pipeline = nlp.Pipeline(
    stages=[
        document_asm,
        sentence_embeddings,
        graph_builder,
        few_shot_approach
    ])

model = pipeline.fit(train_data)
{%- endcapture -%}


{%- capture approach_scala_medical -%}

import spark.implicits._

val document_asm = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("sentence")

val sentence_embeddings = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
    .setInputCols("sentence")
    .setOutputCol("sentence_embeddings")

val few_shot_approach = new FewShotClassifierApproach()
    .setLabelColumn("label")
    .setInputCols("sentence_embeddings")
    .setOutputCol("prediction")
    .setModelFile("tmp/log_reg_graph.pb")
    .setEpochsNumber(10)
    .setBatchSize(1)
    .setLearningRate(0.001) 

val pipeline = new Pipeline().setStages(Array(
    document_asm, 
    sentence_embeddings, 
    few_shot_approach ))

val result = pipeline.fit(train_data).transform(test_data).cache()
{%- endcapture -%}


{%- capture approach_api_link -%}
[FewShotClassifierApproach](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/classification/FewShotClassifierApproach.html)
{%- endcapture -%}

{%- capture approach_python_api_link -%}
[FewShotClassifierApproach](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/classification/few_shot_classifier/index.html#sparknlp_jsl.annotator.classification.few_shot_classifier.FewShotClassifierApproach)
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
approach_description=approach_description
approach_input_anno=approach_input_anno
approach_output_anno=approach_output_anno
approach_python_medical=approach_python_medical
approach_scala_medical=approach_scala_medical
approach_api_link=approach_api_link
approach_python_api_link=approach_python_api_link
%}
