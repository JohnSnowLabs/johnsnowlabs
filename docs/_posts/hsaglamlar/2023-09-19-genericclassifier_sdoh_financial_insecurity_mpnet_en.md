---
layout: model
title: SDOH Financial Insecurity For Classification
author: John Snow Labs
name: genericclassifier_sdoh_financial_insecurity_mpnet
date: 2023-09-19
tags: [sdoh, en, mpnet, social_determinants, public_health, licensed]
task: Text Classification
language: en
edition: Healthcare NLP 5.1.0
spark_version: 3.0
supported: true
annotator: GenericClassifierModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The Financial Insecurity classifier leverages [MPNET embeddings](https://sparknlp.org/2023/08/18/mpnet_embedding_nli_mpnet_base_v2_en.html) within a robust classifier architecture. Trained on a diverse dataset, this model offers precise label assignments along with confidence scores for its predictions. By incorporating MPNET embeddings, the model excels at comprehensively analyzing text, providing valuable insights into financial insecurity within the provided text. The model's primary objective is to classify text into two key labels: 'No_Financial_Insecurity_Or_Unknown' and 'Financial_Insecurity'.

- `No_Financial_Insecurity_Or_Unknown`: This category encompasses statements that indicate the absence of financial insecurity or situations where the information is either unknown or not provided.

- `Financial_Insecurity`: Statements falling into this category indicate instances of financial insecurity, where individuals may be struggling with economic instability, potentially affecting their ability to meet basic needs and achieve financial stability.

## Predicted Entities

`Financial_Insecurity`, `No_Financial_Insecurity_Or_Unknown`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/SOCIAL_DETERMINANT_CLASSIFICATION_GENERIC/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/SOCIAL_DETERMINANT_CLASSIFICATION.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/genericclassifier_sdoh_financial_insecurity_mpnet_en_5.1.0_3.0_1695125672777.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/genericclassifier_sdoh_financial_insecurity_mpnet_en_5.1.0_3.0_1695125672777.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")
        
sent_embd = MPNetEmbeddings.pretrained("mpnet_embedding_nli_mpnet_base_v2", 'en')\
    .setInputCols(["document"])\
    .setOutputCol("sentence_embeddings")\

features_asm = FeaturesAssembler()\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("features")
      
gen_clf = GenericClassifierModel.pretrained('genericclassifier_sdoh_financial_insecurity_mpnet', 'en', 'clinical/models')\
    .setInputCols("features")\
    .setOutputCol("prediction")\

pipeline = Pipeline(stages=[document_assembler,
                            sent_embd,
                            features_asm,
                            gen_clf])

text_list = ["Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatment plan that includes surgery, chemotherapy, and radiation therapy. ",
             "She reported occasional respiratory symptoms, such as wheezing and shortness of breath, but had no signs of a mental disorder. Her healthcare provider assessed her lung function, reviewed her medication regimen, and provided personalized asthma education. ",
             "she has Financial stability",
             "he doesn't experience Economic uncertainty",
             "The individual is managing their mental health challenges.",
             "the patient has  financial problems.",
             "she has Financial instability",
             
                "The patient a 35-year-old woman, visited her healthcare provider with concerns about her health. She bravely shared that she was facing financial difficultie, which was affecting her ability to afford necessary medical care and prescriptions. The caring healthcare provider listened attentively and discussed various options. They helped Sarah explore low-cost alternatives for her medications and connected her with local resources that could assist with healthcare expenses. By addressing the financial aspect, Sarah's healthcare provider ensured that she could receive the care she needed without further straining her finances. Leaving the appointment, Sarah felt relieved and grateful for the support in managing her health amidst her financial challenges.",
             """Case Study: Comprehensive Health Assessment

Patient Information:
Age: 40 years
Gender: Female
Occupation: Part-time administrative assistant
Marital Status: Married, with two school-aged children

Presenting Complaint:
The patient presented to the primary care clinic with concerns about her overall health and well-being. She reported feeling overwhelmed and stressed due to financial difficulties.

Medical History:
The patient has a history of well-managed asthma, which is controlled with an inhaler as needed. She reported occasional headaches, likely related to stress and tension.

Social Determinants of Health (SDOH):
One significant social determinant affecting the patient is financial instability. The patient and her husband have experienced a recent reduction in household income due to her husband's job loss. This has resulted in difficulties in meeting basic needs, including housing, utilities, and groceries. The patient expressed concerns about her ability to afford necessary medical care and medications for both herself and her children.

Family Support:
The patient's husband is actively seeking employment, but the financial strain has created additional stress for the family. They have limited support from extended family members, who are also facing their own financial challenges.

Mental Health:
The patient reported feeling anxious and experiencing occasional bouts of sadness related to the financial stressors. She expressed a desire to explore coping strategies and potentially seek counseling to help manage her emotional well-being.

Physical Examination Findings:
On physical examination, the patient appeared well-nourished but displayed signs of mild fatigue. Vital signs were within normal limits, and cardiovascular, respiratory, gastrointestinal, and musculoskeletal examinations revealed no abnormalities. Neurological examination findings were normal, with intact cranial nerves and normal motor and sensory functions.

Diagnostic Impression:
The patient's medical history and physical examination findings did not reveal any acute or chronic medical conditions. However, it was evident that her overall health was being significantly impacted by the current financial difficulties.

Treatment Recommendations:
1. Financial Assistance: Provide information on local resources and assistance programs available to help individuals and families facing financial hardships. This may include information on food assistance programs, housing support, and access to discounted healthcare services.

2. Coping Strategies and Counseling: Discuss and recommend strategies for coping with stress and anxiety related to financial difficulties. Provide information on local counseling services or support groups that can help the patient manage her emotional well-being.

3. Asthma Management: Review the patient's asthma action plan and ensure she has an adequate supply of inhalers. Discuss any concerns or questions she may have regarding her asthma management.

4. Follow-Up: Schedule regular follow-up appointments to monitor the patient's progress, provide ongoing support, and address any emerging challenges related to her health and financial circumstances."""]

df = spark.createDataFrame(text_list, StringType()).toDF("text")

result = pipeline.fit(df).transform(df)

result.select("text", "prediction.result").show(truncate=100)
```
```scala
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")
        
sent_emb = MPNetEmbeddings.pretrained("mpnet_embedding_nli_mpnet_base_v2", 'en')\
    .setInputCols(["document"])\
    .setOutputCol("sentence_embeddings")\

features_asm = FeaturesAssembler()\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("features")

generic_classifier = GenericClassifierModel.pretrained("genericclassifier_sdoh_financial_insecurity_mpnet", 'en', 'clinical/models')\
    .setInputCols(["features"])\
    .setOutputCol("prediction")

pipeline = Pipeline(stages=[
    document_assembler,
    sent_emb,
    features_asm,
    generic_classifier    
])

val data = Seq("Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatment plan that includes surgery, chemotherapy, and radiation therapy. ",
             "She reported occasional respiratory symptoms, such as wheezing and shortness of breath, but had no signs of a mental disorder. Her healthcare provider assessed her lung function, reviewed her medication regimen, and provided personalized asthma education. ",
             "she has Financial stability",
             "he doesn't experience Economic uncertainty",
             "The individual is managing their mental health challenges.",
             "the patient has  financial problems.",
             "she has Financial instability",
             
                "The patient a 35-year-old woman, visited her healthcare provider with concerns about her health. She bravely shared that she was facing financial difficultie, which was affecting her ability to afford necessary medical care and prescriptions. The caring healthcare provider listened attentively and discussed various options. They helped Sarah explore low-cost alternatives for her medications and connected her with local resources that could assist with healthcare expenses. By addressing the financial aspect, Sarah's healthcare provider ensured that she could receive the care she needed without further straining her finances. Leaving the appointment, Sarah felt relieved and grateful for the support in managing her health amidst her financial challenges.",
             """Case Study: Comprehensive Health Assessment

Patient Information:
Age: 40 years
Gender: Female
Occupation: Part-time administrative assistant
Marital Status: Married, with two school-aged children

Presenting Complaint:
The patient presented to the primary care clinic with concerns about her overall health and well-being. She reported feeling overwhelmed and stressed due to financial difficulties.

Medical History:
The patient has a history of well-managed asthma, which is controlled with an inhaler as needed. She reported occasional headaches, likely related to stress and tension.

Social Determinants of Health (SDOH):
One significant social determinant affecting the patient is financial instability. The patient and her husband have experienced a recent reduction in household income due to her husband's job loss. This has resulted in difficulties in meeting basic needs, including housing, utilities, and groceries. The patient expressed concerns about her ability to afford necessary medical care and medications for both herself and her children.

Family Support:
The patient's husband is actively seeking employment, but the financial strain has created additional stress for the family. They have limited support from extended family members, who are also facing their own financial challenges.

Mental Health:
The patient reported feeling anxious and experiencing occasional bouts of sadness related to the financial stressors. She expressed a desire to explore coping strategies and potentially seek counseling to help manage her emotional well-being.

Physical Examination Findings:
On physical examination, the patient appeared well-nourished but displayed signs of mild fatigue. Vital signs were within normal limits, and cardiovascular, respiratory, gastrointestinal, and musculoskeletal examinations revealed no abnormalities. Neurological examination findings were normal, with intact cranial nerves and normal motor and sensory functions.

Diagnostic Impression:
The patient's medical history and physical examination findings did not reveal any acute or chronic medical conditions. However, it was evident that her overall health was being significantly impacted by the current financial difficulties.

Treatment Recommendations:
1. Financial Assistance: Provide information on local resources and assistance programs available to help individuals and families facing financial hardships. This may include information on food assistance programs, housing support, and access to discounted healthcare services.

2. Coping Strategies and Counseling: Discuss and recommend strategies for coping with stress and anxiety related to financial difficulties. Provide information on local counseling services or support groups that can help the patient manage her emotional well-being.

3. Asthma Management: Review the patient's asthma action plan and ensure she has an adequate supply of inhalers. Discuss any concerns or questions she may have regarding her asthma management.

4. Follow-Up: Schedule regular follow-up appointments to monitor the patient's progress, provide ongoing support, and address any emerging challenges related to her health and financial circumstances.""").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+--------------------------------------------------------------------------------+------------------------------------+
|                                                                            text|                              result|
+--------------------------------------------------------------------------------+------------------------------------+
|Patient B is a 40-year-old female who was diagnosed with breast cancer. She h...|[No_Financial_Insecurity_Or_Unknown]|
|She reported occasional respiratory symptoms, such as wheezing and shortness ...|[No_Financial_Insecurity_Or_Unknown]|
|                                                     she has Financial stability|[No_Financial_Insecurity_Or_Unknown]|
|                                      he doesn't experience Economic uncertainty|[No_Financial_Insecurity_Or_Unknown]|
|                      The individual is managing their mental health challenges.|[No_Financial_Insecurity_Or_Unknown]|
|                                            the patient has  financial problems.|              [Financial_Insecurity]|
|                                                   she has Financial instability|              [Financial_Insecurity]|
|The patient a 35-year-old woman, visited her healthcare provider with concern...|              [Financial_Insecurity]|
|Case Study: Comprehensive Health Assessment\n\nPatient Information:\nAge: 40 ...|              [Financial_Insecurity]|
+--------------------------------------------------------------------------------+------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|genericclassifier_sdoh_financial_insecurity_mpnet|
|Compatibility:|Healthcare NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[features]|
|Output Labels:|[prediction]|
|Language:|en|
|Size:|3.4 MB|
|Dependencies:|mpnet_embedding_nli_mpnet_base_v2|

## References

Internal SDOH project

## Benchmarking

```bash
                             label  precision    recall  f1-score   support
              Financial_Insecurity       0.84      0.89      0.87       201
No_Financial_Insecurity_Or_Unknown       0.97      0.95      0.96       711
                          accuracy        -         -        0.94       912
                         macro-avg       0.91      0.92      0.91       912
                      weighted-avg       0.94      0.94      0.94       912
```