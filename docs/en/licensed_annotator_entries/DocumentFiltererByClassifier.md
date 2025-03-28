{%- capture model -%}
model
{%- endcapture -%}

{%- capture title -%}
DocumentFiltererByClassifier
{%- endcapture -%}

{%- capture model_description -%}
The DocumentFiltererByClassifier function is designed to filter documents based on the outcomes generated by classifier annotators. It operates using a white list and a black list. The white list comprises classifier results that meet the criteria to pass through the filter, while the black list includes results that are prohibited from passing through. This filtering process is sensitive to cases by default. However, by setting caseSensitive to False, the filter becomes case-insensitive, allowing for a broader range of matches based on the specified criteria. This function serves as an effective tool for systematically sorting and managing documents based on specific classifier outcomes, facilitating streamlined document handling and organization.

Parameters:

- `whiteList`: (list) If defined, list of entities to process. The rest will be ignored.

- `CaseSensitive`: (bool) Determines whether the definitions of the white listed entities are case sensitive.

{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT, CATEGORY
{%- endcapture -%}

{%- capture model_output_anno -%}
DOCUMENT
{%- endcapture -%}


{%- capture model_python_medical -%}

example = """Medical Specialty:
Cardiovascular / Pulmonary

Sample Name: Aortic Valve Replacement

Description: Aortic valve replacement using a mechanical valve and two-vessel coronary artery bypass grafting procedure using saphenous vein graft to the first obtuse marginal artery and left radial artery graft to the left anterior descending artery.
(Medical Transcription Sample Report)

DIAGNOSIS: Aortic valve stenosis with coronary artery disease associated with congestive heart failure. The patient has diabetes and is morbidly obese.

PROCEDURES: Aortic valve replacement using a mechanical valve and two-vessel coronary artery bypass grafting procedure using saphenous vein graft to the first obtuse marginal artery and left radial artery graft to the left anterior descending artery.

ANESTHESIA: General endotracheal

INCISION: Median sternotomy

INDICATIONS: The patient presented with severe congestive heart failure associated with the patient's severe diabetes. The patient was found to have moderately stenotic aortic valve. In addition, The patient had significant coronary artery disease consisting of a chronically occluded right coronary artery but a very important large obtuse marginal artery coming off as the main circumflex system. The patient also has a left anterior descending artery which has moderate disease and this supplies quite a bit of collateral to the patient's right system. It was decided to perform a valve replacement as well as coronary artery bypass grafting procedure.

FINDINGS: The left ventricle is certainly hypertrophied· The aortic valve leaflet is calcified and a severe restrictive leaflet motion. It is a tricuspid type of valve. The coronary artery consists of a large left anterior descending artery which is associated with 60% stenosis but a large obtuse marginal artery which has a tight proximal stenosis.

The radial artery was used for the left anterior descending artery. Flow was excellent. Looking at the targets in the posterior descending artery territory, there did not appear to be any large branches. On the angiogram these vessels appeared to be quite small. Because this is a chronically occluded vessel and the patient has limited conduit due to the patient's massive obesity, attempt to bypass to this area was not undertaken. The patient was brought to the operating room

PROCEDURE: The patient was brought to the operating room and placed in supine position. A median sternotomy incision was carried out and conduits were taken from the left arm as well as the right thigh. The patient weighs nearly three hundred pounds. There was concern as to taking down the left internal mammary artery. Because the radial artery appeared to be a good conduit The patient would have arterial graft to the left anterior descending artery territory. The patient was cannulated after the aorta and atrium were exposed and full heparinization.

The patient went on cardiopulmonary bypass and the aortic cross-clamp was applied Cardioplegia was delivered through the coronary sinuses in a retrograde manner. The patient was cooled to 32 degrees. Iced slush was applied to the heart. The aortic valve was then exposed through the aortic root by transverse incision. The valve leaflets were removed and the #23 St. Jude mechanical valve was secured into position by circumferential pledgeted sutures. At this point, aortotomy was closed.

The first obtuse marginal artery was a very large target and the vein graft to this target indeed produced an excellent amount of flow. Proximal anastomosis was then carried out to the foot of the aorta. The left anterior descending artery does not have severe disease but is also a very good target and the radial artery was anastomosed to this target in an end-to-side manner. The two proximal anastomoses were then carried out to the root of the aorta.

The patient came off cardiopulmonary bypass after aortic cross-clamp was released. The patient was adequately warmed. Protamine was given without adverse effect. Sternal closure was then done using wires. The subcutaneous layers were closed using Vicryl suture. The skin was approximated using staples.
"""

df = spark.createDataFrame([[example]]).toDF("text")

from johnsnowlabs import nlp, medical 

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")\

document_splitter = medical.InternalDocumentSplitter() \
    .setInputCols("document")\
    .setOutputCol("splits")\
    .setSplitMode("recursive")\
    .setChunkSize(100)\
    .setChunkOverlap(3)\
    .setExplodeSplits(True)\
    .setPatternsAreRegex(False)\
    .setSplitPatterns(["\n\n", "\n"])\
    .setKeepSeparators(False)\
    .setTrimWhitespace(True)
    #.setEnableSentenceIncrement(False)

sequenceClassifier = medical.BertForSequenceClassification\
    .pretrained('bert_sequence_classifier_clinical_sections', 'en', 'clinical/models')\
    .setInputCols(["splits", "token"])\
    .setOutputCol("prediction")\
    .setCaseSensitive(False)

document_filterer = medical.DocumentFiltererByClassifier()\
    .setInputCols(["splits", "prediction"])\
    .setOutputCol("filteredDocuments")\
    .setWhiteList(["Diagnostic and Laboratory Data"])\
    .setCaseSensitive(False)\


pipeline = nlp.Pipeline().setStages([
    document_assembler,
    tokenizer,
    document_splitter,
    sequenceClassifier,
    #document_filterer
])

result = pipeline.fit(df).transform(df)

# before filterer result

result.selectExpr("splits.result[0] as splits",
                  "prediction.result[0] as classes"
                  ).show(truncate=80)

+--------------------------------------------------------------------------------+------------------------------+
|                                                                          splits|                       classes|
+--------------------------------------------------------------------------------+------------------------------+
|Medical Specialty:\nCardiovascular / Pulmonary\n\nSample Name: Aortic Valve R...|                       History|
|Description: Aortic valve replacement using a mechanical valve and two-vessel...|Complications and Risk Factors|
|                                           (Medical Transcription Sample Report)|Complications and Risk Factors|
|DIAGNOSIS: Aortic valve stenosis with coronary artery disease associated with...|Diagnostic and Laboratory Data|
|PROCEDURES: Aortic valve replacement using a mechanical valve and two-vessel ...|                    Procedures|
|                 ANESTHESIA: General endotracheal\n\nINCISION: Median sternotomy|                    Procedures|
|INDICATIONS: The patient presented with severe congestive heart failure assoc...|     Consultation and Referral|
|FINDINGS: The left ventricle is certainly hypertrophied· The aortic valve lea...|Diagnostic and Laboratory Data|
|The radial artery was used for the left anterior descending artery. Flow was ...|Diagnostic and Laboratory Data|
|PROCEDURE: The patient was brought to the operating room and placed in supine...|                    Procedures|
|The patient went on cardiopulmonary bypass and the aortic cross-clamp was app...|                    Procedures|
|The first obtuse marginal artery was a very large target and the vein graft t...|Diagnostic and Laboratory Data|
|The patient came off cardiopulmonary bypass after aortic cross-clamp was rele...|                    Procedures|
+--------------------------------------------------------------------------------+------------------------------+


# after filterer result

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    tokenizer,
    document_splitter,
    sequenceClassifier,
    document_filterer
])

result = pipeline.fit(df).transform(df)
from pyspark.sql.functions import col
result.selectExpr("filteredDocuments.result[0] as splits",
                  "filteredDocuments.metadata[0].class_label as classes")\
                  .filter(col("classes").isNotNull()).show(truncate=80)

+--------------------------------------------------------------------------------+------------------------------+
|                                                                          splits|                       classes|
+--------------------------------------------------------------------------------+------------------------------+
|DIAGNOSIS: Aortic valve stenosis with coronary artery disease associated with...|Diagnostic and Laboratory Data|
|FINDINGS: The left ventricle is certainly hypertrophied· The aortic valve lea...|Diagnostic and Laboratory Data|
|The radial artery was used for the left anterior descending artery. Flow was ...|Diagnostic and Laboratory Data|
|The first obtuse marginal artery was a very large target and the vein graft t...|Diagnostic and Laboratory Data|
+--------------------------------------------------------------------------------+------------------------------+

{%- endcapture -%}


{%- capture model_scala_medical -%}
import spark.implicits._
 
val example = "Medical Specialty:
Cardiovascular / Pulmonary
Sample Name: Aortic Valve Replacement
Description: Aortic valve replacement using a mechanical valve and two-vessel coronary artery bypass grafting procedure using saphenous vein graft to the first obtuse marginal artery and left radial artery graft to the left anterior descending artery.
(Medical Transcription Sample Report)
DIAGNOSIS: Aortic valve stenosis with coronary artery disease associated with congestive heart failure. The patient has diabetes and is morbidly obese.
PROCEDURES: Aortic valve replacement using a mechanical valve and two-vessel coronary artery bypass grafting procedure using saphenous vein graft to the first obtuse marginal artery and left radial artery graft to the left anterior descending artery.
ANESTHESIA: General endotracheal
INCISION: Median sternotomy
INDICATIONS: The patient presented with severe congestive heart failure associated with the patient's severe diabetes. The patient was found to have moderately stenotic aortic valve. In addition, The patient had significant coronary artery disease consisting of a chronically occluded right coronary artery but a very important large obtuse marginal artery coming off as the main circumflex system. The patient also has a left anterior descending artery which has moderate disease and this supplies quite a bit of collateral to the patient's right system. It was decided to perform a valve replacement as well as coronary artery bypass grafting procedure.
FINDINGS: The left ventricle is certainly hypertrophied· The aortic valve leaflet is calcified and a severe restrictive leaflet motion. It is a tricuspid type of valve. The coronary artery consists of a large left anterior descending artery which is associated with 60% stenosis but a large obtuse marginal artery which has a tight proximal stenosis.
The radial artery was used for the left anterior descending artery. Flow was excellent. Looking at the targets in the posterior descending artery territory, there did not appear to be any large branches. On the angiogram these vessels appeared to be quite small. Because this is a chronically occluded vessel and the patient has limited conduit due to the patient's massive obesity, attempt to bypass to this area was not undertaken. The patient was brought to the operating room
PROCEDURE: The patient was brought to the operating room and placed in supine position. A median sternotomy incision was carried out and conduits were taken from the left arm as well as the right thigh. The patient weighs nearly three hundred pounds. There was concern as to taking down the left internal mammary artery. Because the radial artery appeared to be a good conduit The patient would have arterial graft to the left anterior descending artery territory. The patient was cannulated after the aorta and atrium were exposed and full heparinization.
The patient went on cardiopulmonary bypass and the aortic cross-clamp was applied Cardioplegia was delivered through the coronary sinuses in a retrograde manner. The patient was cooled to 32 degrees. Iced slush was applied to the heart. The aortic valve was then exposed through the aortic root by transverse incision. The valve leaflets were removed and the #23 St. Jude mechanical valve was secured into position by circumferential pledgeted sutures. At this point, aortotomy was closed.
The first obtuse marginal artery was a very large target and the vein graft to this target indeed produced an excellent amount of flow. Proximal anastomosis was then carried out to the foot of the aorta. The left anterior descending artery does not have severe disease but is also a very good target and the radial artery was anastomosed to this target in an end-to-side manner. The two proximal anastomoses were then carried out to the root of the aorta.
The patient came off cardiopulmonary bypass after aortic cross-clamp was released. The patient was adequately warmed. Protamine was given without adverse effect. Sternal closure was then done using wires. The subcutaneous layers were closed using Vicryl suture. The skin was approximated using staples.
"

val df = Seq(example).toDF("text") 

val document_assembler = new DocumentAssembler()
  .setInputCol("text") 
  .setOutputCol("document") 

val tokenizer = new Tokenizer()
  .setInputCols(Array("document")) 
  .setOutputCol("token")

val document_splitter = new InternalDocumentSplitter()
  .setInputCols("document") 
  .setOutputCol("splits") 
  .setSplitMode("recursive") 
  .setChunkSize(100) 
  .setChunkOverlap(3) 
  .setExplodeSplits(true) 
  .setPatternsAreRegex(false) 
  .setSplitPatterns(Array(" "," ")) 
  .setKeepSeparators(false) 
  .setTrimWhitespace(true) 
  //.setEnableSentenceIncrement(false) 

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_clinical_sections","en","clinical/models") 
  .setInputCols(Array("splits","token")) 
  .setOutputCol("prediction") 
  .setCaseSensitive(false) 

val document_filterer = new DocumentFiltererByClassifier()
  .setInputCols(Array("splits","prediction")) 
  .setOutputCol("filteredDocuments") 
  .setWhiteList(Array("Diagnostic and Laboratory Data")) 
  .setCaseSensitive(false) 

val pipeline = new Pipeline().setStages(Array( 
                                              document_assembler, 
                                              tokenizer, 
                                              document_splitter, 
                                              sequenceClassifier, 
                                              //document_filterer )) 

val result = pipeline.fit(df).transform(df) 

// before filterer result 

+--------------------------------------------------------------------------------+------------------------------+
|                                                                          splits|                       classes|
+--------------------------------------------------------------------------------+------------------------------+
|Medical Specialty:\nCardiovascular / Pulmonary\n\nSample Name: Aortic Valve R...|                       History|
|Description: Aortic valve replacement using a mechanical valve and two-vessel...|Complications and Risk Factors|
|                                           (Medical Transcription Sample Report)|Complications and Risk Factors|
|DIAGNOSIS: Aortic valve stenosis with coronary artery disease associated with...|Diagnostic and Laboratory Data|
|PROCEDURES: Aortic valve replacement using a mechanical valve and two-vessel ...|                    Procedures|
|                 ANESTHESIA: General endotracheal\n\nINCISION: Median sternotomy|                    Procedures|
|INDICATIONS: The patient presented with severe congestive heart failure assoc...|     Consultation and Referral|
|FINDINGS: The left ventricle is certainly hypertrophied· The aortic valve lea...|Diagnostic and Laboratory Data|
|The radial artery was used for the left anterior descending artery. Flow was ...|Diagnostic and Laboratory Data|
|PROCEDURE: The patient was brought to the operating room and placed in supine...|                    Procedures|
|The patient went on cardiopulmonary bypass and the aortic cross-clamp was app...|                    Procedures|
|The first obtuse marginal artery was a very large target and the vein graft t...|Diagnostic and Laboratory Data|
|The patient came off cardiopulmonary bypass after aortic cross-clamp was rele...|                    Procedures|
+--------------------------------------------------------------------------------+------------------------------+


// after filterer result

val pipeline = new Pipeline().setStages(Array( 
                                              document_assembler, 
                                              tokenizer, 
                                              document_splitter, 
                                              sequenceClassifier, 
                                              document_filterer )) 

val result = pipeline.fit(df) .transform(df) 

+--------------------------------------------------------------------------------+------------------------------+
|                                                                          splits|                       classes|
+--------------------------------------------------------------------------------+------------------------------+
|DIAGNOSIS: Aortic valve stenosis with coronary artery disease associated with...|Diagnostic and Laboratory Data|
|FINDINGS: The left ventricle is certainly hypertrophied· The aortic valve lea...|Diagnostic and Laboratory Data|
|The radial artery was used for the left anterior descending artery. Flow was ...|Diagnostic and Laboratory Data|
|The first obtuse marginal artery was a very large target and the vein graft t...|Diagnostic and Laboratory Data|
+--------------------------------------------------------------------------------+------------------------------+

{%- endcapture -%}


{%- capture model_notebook_link -%}
[DocumentFiltererByClassifierNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/DocumentFiltererByClassifier.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
model_notebook_link=model_notebook_link
%}
