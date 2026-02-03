Turning Medical Expert Knowledge into Responsible Language Models by John Snow Labs' Dr\. David Talby

The speech delivered by Dr\. David Talby focuses on the process of transforming specialized __medical expert knowledge into responsible language models \(LMs\)__, particularly addressing the unique challenges of healthcare data and the necessity of maintaining high ethical and accuracy standards\.

### __The Context and Initial Healthcare NLP Pipeline__

Healthcare data involves a wide variety of non\-structural modalities, including clinical documents, pathology reports, radiology reports, lab reports, MRI imaging, and vital sign reports\. The ultimate goal is to convert this complex data into a structured table of features for models used in tasks such as prognosis prediction or recommending the next course of action\.

A standard production NLP pipeline in this domain is extensive, often containing 40, 50, or 60 steps\. Key steps include:

1. __OCR/Computer Vision:__ Processing documents that are images\.
2. __De\-identification:__ Essential to avoid data leakage of sensitive data into the model; for instance, preventing the model from learning to associate a specific patient name with a disease\.
3. __Document Classification:__ Necessary because different document types \(e\.g\., pathology reports\) use distinct language, requiring specialized NLP models for each type\.
4. __Named Entity Extraction \(NER\):__ Extracting hundreds of diverse entities, such as lab results, social determinants of health, and radiological findings\.
5. __Assertion Status and Context:__ Crucially understanding the meaning *associated* with each entity\. This involves differentiating states like: 
	1. Patient is diabetic vs\. Patient is *not* diabetic vs\. Patient *shows symptoms* of diabetes\.
	2. Past events \("had surgery 10 years ago"\) vs\. Future plans \("surgery planned for next month"\)\.
6. __Coreference Resolution and Normalization:__ Grouping disparate terms \(e\.g\., "diabetes," "t2dm," "type 2 diabetes mellitus," "glucose intolerant"\) into the same concept and normalizing them into codes\. Failure to do this means studies may erroneously split one concept into several, leading to inaccurate conclusions\.

### __The Importance of Expert Agreement and Annotation__

To build these highly contextualized models, the process must begin manually, where __actual medical doctors__ define the clinical semantics and achieve agreement on definitions\. This step is challenging because agreement is often hard to achieve, even on standardized concepts like cancer staging or gender classification\. The first crucial action is to __write down the annotation guidelines__\. Due to the variety and specialization within medical language, the speaker emphasizes that the process of defining these guidelines is never truly finished\.

### __Automated and Responsible Model Building__

To overcome the slow pace of manual annotation, an __augmented process__ is used that automates about 90% of the work\.

This process involves:

- Starting with a __pre\-trained model__ \(like a general treatment model\) to pre\-annotate documents based on specific clinical definitions\.
- Domain experts \(medical doctors\) review and refine these pre\-annotations\.
- The model is __automatically retrained in the background__ as more data is annotated, eventually stabilizing\.
- This approach is typically __four to five times faster__ than non\-automated processes and allows domain experts to build and publish models __without data scientists__ being involved\.

The tool used for this process is __completely free__, includes scaling and security features, and is designed for high\-compliance environments, allowing deployment on\-premise without sharing data\.

__Responsible AI in Healthcare__ The healthcare industry is unique in that responsible AI procedures are often implemented *before* the first model is deployed\. The process requires:

- __Audit Trails and Versioning:__ Regulators must be able to ask which model was used on a specific patient at a specific time and why\.
- __Human Oversight:__ Differentiating between the model's predictions/completions and the human expert’s acceptance or rejection of those proposals\.

The speaker highlights five key areas for building reliable models, inspired by open\-source projects like Checklist and Cleanlab:

1. __Perturbation Testing:__ Testing how stable the model is when subjected to small changes, such as typos, replacing synonyms with similar words \(especially drugs or symptoms from the same class\), or altering capitalization and punctuation\. This helps detect model fragility\.
2. __Generating Alternate Data:__ Automatically generating labeled alternate data to re\-train the model and improve stability\.
3. __Noise Level Detection \(Identifying Bad Labels\):__ Recognizing that a significant portion of remaining classification errors \(e\.g\., the last 10% toward 100% accuracy\) often results from incorrect human labels\. Heuristics identify suspect labels by comparing them to a zero\-shot model or checking if the model’s own inference strongly disagrees with the input label\. A ranked list of suspect labels is generated for human review and automatic correction/retraining\.
4. __Bias Detection:__ Since patient notes often include features like gender, age group, and race/ethnicity, the tool can automatically classify these attributes and generate performance scores \(e\.g\., F\-scores\) based on these demographics\. It is also critical to ensure there are __enough examples__ for a specific sub\-population \(e\.g\., age group or ethnicity\) before applying the model to them\.

### __The Distinct Nature of Medical Language__

Medical language is functionally a __different language__ from common language\. It has a unique vocabulary, grammar, and meaning\. The speaker suggests that the time required to learn to interpret a radiology report is comparable to the time needed to learn Russian or Portuguese\. This complexity necessitates specialized models and benchmarks\.

### __Exciting Use Cases__

The use cases in healthcare are varied and often directly help people:

- __Identifying high\-risk patients__ \(e\.g\., chronic disease\) months in advance to prevent emergency room visits\.
- Applications in __mental health__ \(depression, suicide ideation\)\.
- __Oncology:__ Extracting details like cancer staging and tumor histology from pathology reports \(which structural data often lacks\) to match patients to clinical trials and treatment plans\.
- Monitoring social media for __adverse events__ related to medications\.
- __Life\-saving classification:__ Automatically detecting clinically __urgent messages__ \(1% to 2% of messages sent by patients to doctors\) within minutes, potentially saving hundreds of people daily\.

### __Ethics and Accuracy__

Healthcare is described as an industry that prioritizes ethics\. Accuracy in this field depends not only on the model but also on the application; for example, NLP models are generally __not used to automatically adjust drug dosage__\. Furthermore, since healthcare systems are known to be imperfect \(e\.g\., blood tests being redone because previous records might be wrong\), the human system has checks built in\. The most critical factor for accuracy is achieving __agreement between experts__ on definitions, especially since many clinical definitions remain controversial or undecided \(e\.g\., defining high\-risk pregnancy\)\. The tools support this by providing features for auditing, versioning, comparing expert annotations, and updating guidelines\.

