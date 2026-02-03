Ai \- Automating Clinical Data Abstraction From Unstructured Documents Using Spark NLP with John Snow Labs

The speech delivered by David Dalby, CTO of John Snow Labs, focuses on the challenges of clinical data abstraction from unstructured documents and how modern Natural Language Processing \(NLP\), specifically Spark NLP, provides state\-of\-the\-art solutions\.

## __Detailed Summary of the Speech__

### __The Challenge of Clinical Data Abstraction__

The fundamental task in healthcare is taking diverse documents—which could include images, tables, academic papers, audiology reports, and lab reports—and transforming them into a structured format that can be analyzed, summarized, visualized, and treated like classic relational data\. Currently, this abstraction is __mostly done manually__, making the data too slow and expensive to access, meaning much of it is never utilized\.

A major hurdle is that in many medical specialties, such as oncology, the majority of clinically relevant data resides only in __free text__\. One study involving a top\-five pharmaceutical company found that out of approximately 300 data points required to apply clinical guidelines, only 40% were available in structured data; the rest was completely unstructured, specific text\.

To manage this volume, U\.S\. hospitals typically employ dozens, if not hundreds, of clinical data abstractors manually\. This is often driven by participation in patient registries, which are disease\-specific databases that may require 300 to 600 structured fields per patient event\. The challenge is inherently an NLP problem because understanding basic clinical information \(like blood pressure or cholesterol levels\) often requires complex contextual understanding of unstructured text\.

Clinical trials face similar issues, generating hundreds of thousands of documents that require rapid data collection, summarization, and analysis to determine drug efficacy and safety\. This process is plagued by manual difficulties related to handwriting, multilingual data, and inconsistent jargon\.

### __NLP as a Foundational Technology__

Due to the vast availability of digital text and the significant improvements in NLP technologies, automation is now accurate enough for certain tasks, often for the first time in history\. A March 2021 industry survey highlighted that NLP is becoming foundational in health IT technology, ranking alongside data integration, business intelligence, and data warehousing, but being the only new technology among those core four\.

### __John Snow Labs and State\-of\-the\-Art \(SOTA\) Standards__

David Dalby introduced John Snow Labs \(JSL\) as an AI NLP company focused exclusively on natural language processing in healthcare and life science\. JSL is best known for __Spark NLP__, an open\-source library used widely in the enterprise, supporting over 200 languages and deep learning models\. __Spark NLP for Healthcare__ is their main product, used by __54% of healthcare AI teams__ to structure clinical or biomedical data, making it the most commonly used library in the industry\.

JSL defines "State of the Art" \(SOTA\) rigorously, requiring:

1. __Academic Excellence:__ A peer\-reviewed paper that measures accuracy against a publicly reproducible academic benchmark\.
2. __Real\-World Production:__ The system must be in production in multiple places, demonstrating that it generalizes and is reusable across different organizations and use cases\.
3. __Open Code:__ Some code must be open source or open core, ensuring the solution is based on verifiable software\.

### __Core NLP Tasks for Clinical Data Abstraction__

The speech detailed several essential NLP tasks required for clinical data abstraction:

#### __1\. Named Entity Recognition \(NER\)__

NER identifies clinical entities such as medical problems, medical treatments, and medical tests within free text\. JSL states that Spark NLP is the top result \(most accurate peer\-reviewed outcome\) on __8 out of 11 medical NER benchmarks__ tracked by the website Papers with Code\. Crucially, JSL focuses on ensuring these models work on noisy, real\-world data within high\-compliance, scalable environments, not just nice academic datasets\.

JSL demonstrated massive speed\-ups with the release of __Spark NLP 3__, which was optimized for modern compute platforms \(Spark 3\)\. Compared to the previous version, JSL reported being almost __eight times faster__ in calculating entity resolution and about __three times faster__ in calculating NER \(using deep learning on GPUs\)\.

#### __2\. Clinical Assertion Status Detection__

This is a separate task that determines what is being asserted about a recognized entity\. This is vital for clinical decisions\. Examples include identifying if a condition is:

- __Present__ \(the patient has it\)\.
- __Absent__ \(the patient does not have it, e\.g\., "shows no stomach pain"\)\.
- __Conditional__ \(only occurs under specific circumstances, e\.g\., "short of breath when climbing stairs"\)\.
- __Associated with someone else__ \(e\.g\., "father with Alzheimer"\)\. JSL reported achieving new SOTA accuracy on the main academic benchmark for assertion status\.

#### __3\. Relation Extraction__

Relation extraction is used to find connections between different entities\. Examples include temporal relations \(did the symptom start before or after the drug?\) or physical relations \(linking symptoms to body parts\)\. JSL ships over 30 pre\-trained relation extraction models, which are also trainable\. New SOTA accuracy was reported in key areas like relations between symptoms/procedures/treatments, and biomedical relations between genes/phenotypes\.

#### __4\. De\-identification__

De\-identification \(De\-ID\) is necessary to mask or obfuscate sensitive data like patient names, ages, birth locations, and hospitals \(PHI\) found in text, PDFs, or DICOM images\. JSL prefers __obfuscation__ \(replacing PHI with random, realistic values\) over deletion or simple masking, as it is more readable and protects against compliance failure if a single entity is missed\. JSL recently achieved a new SOTA accuracy on the 2014 i2b2 challenge de\-identification benchmark\.

### __Tips and Lessons Learned__

1. __Production vs\. Academic:__ An academic result is usually years away from a practical, real\-world healthcare solution that accounts for privacy, security, scalability, customization, and explainability\.
2. __Healthcare is Not Monolithic:__ Healthcare involves hundreds of different domain\-specific "languages" \(e\.g\., dentistry, oncology, cardiology, next\-generation sequencing\)\. Projects often require training custom models, meaning the software must be trainable and often requires medical professionals to annotate and label data\.
3. __The Active Learning Loop:__ For projects requiring near\-perfect accuracy \(like clinical trials\), humans must be kept __in the loop__\. The software performs the automated extraction, and a human expert validates or corrects the data in a user interface\. These corrections are then used as new labeled data to retrain and improve the model via an active learning loop, which is typically the fastest and most effective way to begin a clinical data abstraction project\.

In conclusion, the speaker noted that achievable accuracy has changed significantly in the last two years, making tasks that were previously impractical now possible\.

