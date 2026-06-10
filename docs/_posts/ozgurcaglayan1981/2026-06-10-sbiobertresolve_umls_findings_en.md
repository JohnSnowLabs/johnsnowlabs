---
layout: model
title: Sentence Entity Resolver for UMLS CUI Codes (Findings)
author: John Snow Labs
name: sbiobertresolve_umls_findings
date: 2026-06-10
tags: [en, entity_resolution, licensed, clinical, umls, findings]
task: Entity Resolution
language: en
edition: Healthcare NLP 6.4.0
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical findings to UMLS CUI codes. It is trained on the 2026AA release of the Unified Medical Language System (UMLS) dataset. The training data covers the "Finding" (T033) semantic type, comprising approximately 736,000 name-CUI pairs. The model uses `sbiobert_base_cased_mli_onnx` embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_findings_en_6.4.0_3.4_1781134021603.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_findings_en_6.4.0_3.4_1781134021603.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_clinical","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("clinical_ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","clinical_ner"])\
    .setOutputCol("clinical_ner_chunk")\
    .setWhiteList(["PROBLEM"])

chunk2doc = Chunk2Doc()\
    .setInputCols("clinical_ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_findings","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
])

data = spark.createDataFrame([["The patient complained of headache, nausea, dizziness, and blurred vision following the injury.Physical examination revealed bilateral arm swelling, skin erythema, and tenderness around the ankle.The chest radiograph demonstrated pulmonary infiltrates and a small pleural effusion."]]).toDF("text")
result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

ner_model = medical.NerModel.pretrained("ner_clinical","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("clinical_ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","clinical_ner"])\
    .setOutputCol("clinical_ner_chunk")\
    .setWhiteList(["PROBLEM"])

chunk2doc = medical.Chunk2Doc()\
    .setInputCols("clinical_ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_findings","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
])

data = spark.createDataFrame([["The patient complained of headache, nausea, dizziness, and blurred vision following the injury.Physical examination revealed bilateral arm swelling, skin erythema, and tenderness around the ankle.The chest radiograph demonstrated pulmonary infiltrates and a small pleural effusion."]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel
    .pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel
    .pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel
    .pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("clinical_ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "clinical_ner"))
    .setOutputCol("clinical_ner_chunk")
    .setWhiteList(Array("PROBLEM"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("clinical_ner_chunk")
    .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings
    .pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("sbiobertresolve_umls_findings", "en", "clinical/models")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
))

val data = Seq("The patient complained of headache, nausea, dizziness, and blurred vision following the injury.Physical examination revealed bilateral arm swelling, skin erythema, and tenderness around the ankle.The chest radiograph demonstrated pulmonary infiltrates and a small pleural effusion.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk                   | entity   | umls_code   | resolution                               | all_k_results                                                                                                                                                                                                                                                         | all_k_distances                                                                                                                                                                                                                         | all_k_cosine_distances                                                                                                                                                                                                | all_k_resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:----------------------------|:---------|:------------|:-----------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| headache                    | PROBLEM  | C2029705    | headache lasting                         | C2029705:::C0751191:::C0037195:::C5880337:::C2363911:::C0232488:::C0423620:::C0458254:::C3842524:::C2015953:::C0162703:::C2015951:::C2015956:::C2675791:::C1821295:::C0038990:::C0423730                                                                              | 6.2163:::6.2773:::6.3668:::6.9818:::7.4093:::7.5417:::7.5784:::7.6078:::7.6736:::7.7007:::7.8193:::7.9487:::8.0083:::8.0105:::8.0144:::8.0201:::8.0477                                                                                  | 0.0566:::0.0585:::0.0602:::0.0719:::0.0810:::0.0829:::0.0871:::0.0869:::0.0870:::0.0877:::0.0901:::0.0925:::0.0946:::0.0964:::0.0946:::0.0944:::0.0957                                                                | headache lasting:::sharp headache:::sinus headache:::mouth pain:::exertional headache:::colicky pain:::location of headache:::pain cramping:::frequent or severe headaches:::nose pain:::sensitivity pain:::jaw pain:::throat pain:::headache, episodic:::pain distress:::sweating:::cough pain                                                                                                                                                                                                                                                                                                                                                                                    |
| nausea                      | PROBLEM  | C0423583    | nausea present                           | C0423583:::C3839628:::C4546083:::C1821227:::C1821223:::C5980104:::C3843946:::C5936462:::C0683369:::C1319170:::C0038990:::C0553721:::C0036973:::C4721445:::C0557910:::C0424491                                                                                         | 4.6504:::5.1830:::5.3363:::6.1696:::6.3720:::7.6242:::7.6626:::7.7772:::7.8199:::8.0071:::8.1649:::8.2745:::8.2972:::8.5342:::8.5447:::8.5543                                                                                           | 0.0317:::0.0400:::0.0423:::0.0567:::0.0607:::0.0860:::0.0866:::0.0887:::0.0903:::0.0945:::0.0976:::0.1018:::0.1023:::0.1068:::0.1075:::0.1079                                                                         | nausea present:::nausea level:::functional nausea:::intensity of nausea:::frequency of nausea:::bloating:::nausea or vomiting:::severe nausea:::confusion:::nausea and vomiting status:::sweating:::impaired sweating:::shiver:::torment:::shame:::face bloated                                                                                                                                                                                                                                                                                                                                                                                                                    |
| dizziness                   | PROBLEM  | C0427112    | dizziness present                        | C0427112:::C0234987:::C0859887:::C0234988:::C0522360:::C3280868:::C3842982:::C0013144:::C0553721:::C5885861:::C4060676:::C3842980:::C5983238                                                                                                                          | 5.0085:::5.0549:::5.5591:::5.9171:::6.0648:::6.6888:::6.8052:::6.8749:::6.9754:::6.9999:::7.1066:::7.1453:::7.1478                                                                                                                      | 0.0371:::0.0380:::0.0455:::0.0525:::0.0539:::0.0673:::0.0680:::0.0696:::0.0728:::0.0730:::0.0731:::0.0761:::0.0751                                                                                                    | dizziness present:::postural dizziness:::positional dizziness:::exertional dizziness (finding):::chronic subjective dizziness:::dizziness, episodic:::numbness or tingling:::drowsy (finding):::impaired sweating:::dizziness, vertigo observed:::feeling of discomfort:::lightheadedness, dizziness, or loss of balance:::emotional numbness                                                                                                                                                                                                                                                                                                                                      |
| blurred vision              | PROBLEM  | C0344232    | blurred vision                           | C0344232:::C3665347:::C4060946:::C0558171:::C0547030:::C1847840                                                                                                                                                                                                       | 0.0077:::5.4530:::5.7370:::6.3805:::6.5855:::6.6147                                                                                                                                                                                     | 0.0000:::0.0440:::0.0484:::0.0599:::0.0640:::0.0651                                                                                                                                                                   | blurred vision:::disturbed vision:::insufficient vision:::deteriorating vision:::impaired vision:::visual blurring                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| the injury                  | PROBLEM  | C3259076    | injury sequence                          | C3259076:::C2136899:::C0552510:::C4699601:::C4060696:::C0920744:::C2228400:::C2087083:::C3842029:::C0455586:::C4521243:::C2136639:::C2055637:::C2116669:::C0424366:::C2911673:::C0552513:::C3699703                                                                   | 6.6800:::6.7108:::6.8495:::6.8727:::7.1671:::7.2612:::7.3257:::7.3684:::7.5306:::7.6243:::7.8073:::7.9311:::8.0754:::8.0795:::8.1557:::8.1698:::8.2118:::8.3404                                                                         | 0.0701:::0.0690:::0.0701:::0.0731:::0.0795:::0.0825:::0.0806:::0.0826:::0.0877:::0.0889:::0.0926:::0.0957:::0.1017:::0.1002:::0.1021:::0.1015:::0.1042:::0.1054                                                       | injury sequence:::labial tissue injury:::causes injury:::covered injury:::injury agent:::injury stressor:::facial injury:::traumatic lesion:::injury-impaled object:::injury; history:::injury severity:::reported tissue injury:::tmj tissue injury:::tissue injury incision:::self-injury:::self-inflicted injury:::injury location:::additional cause of injury                                                                                                                                                                                                                                                                                                                 |
| Physical examination        | TEST     | C1509143    | physical examination                     | C1509143:::C2826729:::C2826940:::C0514231:::C0311392:::C4740269:::C0150618:::C1444665:::C5779771:::C1262869:::C1290908:::C0424545:::C5934489                                                                                                                          | 0.0067:::3.0793:::5.1247:::5.6881:::6.0999:::6.6409:::6.9446:::6.9801:::7.7974:::7.8692:::8.0038:::8.0804:::8.1243                                                                                                                      | 0.0000:::0.0141:::0.0391:::0.0476:::0.0544:::0.0673:::0.0727:::0.0732:::0.0899:::0.0915:::0.0952:::0.0962:::0.0968                                                                                                    | physical examination:::physical examination finding:::physical examination location:::physical exam performed:::physical findings:::estimated from physical examination:::history and physical examination:::physical examination completion status:::body posture (physical finding):::body position (physical finding):::patient status (physical finding):::general physical finding:::participates in physical care                                                                                                                                                                                                                                                            |
| bilateral arm swelling      | PROBLEM  | C2237077    | upper arm swelling bilateral             | C2237077:::C4751399:::C2237506:::C2038765:::C2038705:::C4751391:::C0745923:::C2055631:::C0281982:::C2109101:::C2220053:::C5678028:::C0151602:::C4272125:::C2038661:::C2176248:::C0542067:::C0241043                                                                   | 3.8840:::4.9540:::5.3837:::6.2611:::6.5139:::6.6447:::6.6737:::6.7749:::6.7940:::6.8931:::6.9050:::6.9250:::6.9338:::6.9378:::7.0035:::7.0052:::7.0643:::7.0827                                                                         | 0.0223:::0.0369:::0.0432:::0.0588:::0.0630:::0.0667:::0.0655:::0.0702:::0.0683:::0.0710:::0.0711:::0.0706:::0.0707:::0.0721:::0.0736:::0.0742:::0.0736:::0.0752                                                       | upper arm swelling bilateral:::swelling of bilateral arms:::bilateral wrist swelling:::upper arm swelling left:::forearm swelling:::localised swelling of bilateral hands:::lower extremity swollen bilateral:::tmj swelling bilateral:::skin swelling of:::bilateral ankle swelling:::bilateral swollen eyelids:::generalized cutaneous swelling:::facial swelling:::shoulder swelling bilateral extending to arm:::feet swelling bilaterally:::knee swelling localized bilateral:::large arm swelling:::shoulder swelling                                                                                                                                                        |
| skin erythema               | PROBLEM  | C1822297    | surrounding skin erythema                | C1822297:::C0239488:::C0748800:::C1720538:::C4551275:::C0239821:::C1857170:::C2176791:::C1536329:::C3277023:::C0239343:::C0241482:::C3670628:::C0239615:::C0240391:::C5883591:::C4313726:::C0241345:::C0857246:::C1536319:::C3805096:::C5545368:::C0240085:::C2957436 | 4.0162:::4.4316:::4.6203:::4.9075:::5.0336:::5.2348:::5.2955:::5.3848:::5.4148:::5.4844:::5.4986:::5.5274:::5.6170:::5.7583:::5.7613:::5.7669:::5.8197:::5.8777:::5.9639:::6.0067:::6.0341:::6.0777:::6.0808:::6.1042                   | 0.0246:::0.0297:::0.0319:::0.0364:::0.0386:::0.0419:::0.0418:::0.0440:::0.0442:::0.0457:::0.0454:::0.0467:::0.0482:::0.0510:::0.0508:::0.0492:::0.0521:::0.0528:::0.0542:::0.0555:::0.0557:::0.0560:::0.0563:::0.0570 | surrounding skin erythema:::facial erythema:::skin lesion erythematous:::persistent erythema of skin:::erythema of periwound skin:::hand erythema:::erythematous skin blotching:::buttock erythema:::forearm erythema:::erythema in affected areas:::extremity erythema:::trunk erythema:::interdigital erythema:::flank erythema:::mucous membrane erythema:::erythematous skin:::underlying erythema:::tendon erythema:::neck erythema:::back erythema:::puncture site erythema:::eyelid erythema:::joint erythema:::perineum erythema                                                                                                                                           |
| tenderness around the ankle | PROBLEM  | C0576208    | tenderness of ankle joint                | C0576208:::C2237508:::C2056534:::C0576209:::C2088020:::C0576389:::C2228033:::C0741051:::C0427280:::C2088499:::C2088049:::C0576273:::C4305063:::C2200485:::C0239933:::C2049086:::C2088023:::C2196505                                                                   | 3.2121:::6.2765:::7.0881:::7.3975:::7.4915:::7.5163:::7.5712:::7.5715:::7.6052:::7.7413:::7.8179:::7.8278:::7.8580:::7.8918:::7.9240:::7.9563:::7.9728:::8.0203                                                                         | 0.0152:::0.0585:::0.0749:::0.0805:::0.0837:::0.0838:::0.0845:::0.0865:::0.0872:::0.0892:::0.0914:::0.0909:::0.0926:::0.0931:::0.0927:::0.0947:::0.0954:::0.0960                                                       | tenderness of ankle joint:::bilateral ankle tenderness on palpation:::left anterior ankle tenderness on palpation:::ankle joint - painful on movement (finding):::right anterior ankle tenderness on palpation:::tenderness of toe joint:::pain of ankle elicited by motion:::inflammation ankle:::clicking ankle:::pain of ankle elicited at extreme limits of range of motion:::pain of ankle elicited by inversion:::tenderness of joint of foot:::somatic dysfunction of ankle region:::ankle tenderness on palpation right:::heel tenderness:::induration of ankle:::ankle tenderness on palpation right lateral:::ankle weakness right                                       |
| The chest radiograph        | TEST     | C2186568    | reported chest x-ray                     | C2186568:::C0742364:::C0150872:::C5934722:::C1821150:::C0426786:::C1406937:::C0577967:::C2087201:::C1287658:::C0425538:::C0577940:::C0742352:::C0424683:::C0436503:::C2157969:::C1405978                                                                              | 7.4864:::7.5510:::7.6581:::7.8670:::7.8984:::8.2289:::8.3773:::9.0401:::9.1218:::9.4676:::9.5903:::9.6108:::9.6379:::9.6735:::9.6932:::9.7075:::9.7161                                                                                  | 0.0901:::0.0919:::0.0908:::0.1012:::0.0986:::0.1059:::0.1136:::0.1323:::0.1295:::0.1434:::0.1454:::0.1471:::0.1498:::0.1482:::0.1448:::0.1500:::0.1480                                                                | reported chest x-ray:::chest x ray anatomy:::chest findings:::chest x-ray results:::chest x-ray findings:::chest appearance:::chest x-ray; examination:::named respiratory sign of chest (finding):::lesion of chest:::chest movement appearance finding (finding):::sounds within chest (finding):::respiratory finding of chest (finding):::mass of chest wall (finding):::circumference of chest:::abnormal chest radiograph:::nodule of chest:::radiology                                                                                                                                                                                                                      |
| pulmonary infiltrates       | PROBLEM  | C0235896    | pulmonary infiltrates                    | C0235896:::C3671959:::C0748143:::C4543700:::C0748144:::C6062441:::C5849031:::C4313225:::C4531104:::C3671964                                                                                                                                                           | 0.0065:::5.1313:::6.2408:::6.6056:::6.7248:::6.7477:::6.7600:::7.1274:::7.1864:::7.3210                                                                                                                                                 | 0.0000:::0.0393:::0.0582:::0.0652:::0.0677:::0.0688:::0.0682:::0.0766:::0.0776:::0.0815                                                                                                                               | pulmonary infiltrates:::pulmonary alveolar infiltration:::pulmonary infiltrate diffuse:::multilobar lung infiltrate:::pulmonary interstitial infiltrate:::bronchial infiltration:::pulmonary involvement:::interstitial infiltrates:::pulmonary opacity:::peribronchiolar infiltrate                                                                                                                                                                                                                                                                                                                                                                                               |
| a small pleural effusion    | PROBLEM  | C0747640    | pleural effusion loculated minor fissure | C0747640:::C0034079:::C4228911:::C4012096:::C5883598:::C4478245:::C2080416:::C2139069:::C5232995:::C4027629:::C6013452:::C2676513:::C0457094:::C4748643:::C4315136:::C5830253:::C0747710:::C5775626:::C5973472:::C3550696:::C1862763:::C0426436:::C3686623:::C2675021 | 8.5281:::9.5976:::9.7594:::9.7725:::9.8859:::9.9147:::10.0262:::10.1177:::10.2066:::10.2204:::10.2385:::10.2560:::10.3312:::10.3345:::10.3681:::10.3768:::10.3898:::10.3935:::10.3978:::10.4009:::10.4443:::10.4782:::10.5079:::10.5361 | 0.1168:::0.1396:::0.1485:::0.1481:::0.1518:::0.1512:::0.1572:::0.1608:::0.1634:::0.1598:::0.1644:::0.1640:::0.1652:::0.1624:::0.1670:::0.1701:::0.1731:::0.1697:::0.1682:::0.1648:::0.1650:::0.1686:::0.1696:::0.1738 | pleural effusion loculated minor fissure:::small mass of the lung:::small middle ear cavities:::pulmonary artery dilation, mild:::pericardial effusion, mild:::small pulmonary arteries:::soft mass of pharynx (physical finding):::soft mass of larynx (physical finding):::small localized cysts:::small nasal passages (physical finding):::small cysts:::small joint laxity:::thin sputum:::small lung volumes:::small pons:::bronchiectasis, mild:::pneumothorax small:::pulmonary artery dilation, mild to moderate:::narrow thoracic cavity (physical finding):::small thoracic cavity:::small airways:::small nostrils (finding):::small spleen:::small palpebral fissures |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_umls_findings|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bert_embeddings]|
|Output Labels:|[umls_code]|
|Language:|en|
|Size:|2.1 GB|
|Case sensitive:|false|