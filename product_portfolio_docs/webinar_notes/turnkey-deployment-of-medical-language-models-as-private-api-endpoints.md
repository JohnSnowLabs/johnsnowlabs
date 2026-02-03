# Turnkey Deployment of Medical Language Models as Private API Endpoints
Turnkey Deployment of Medical Language Models as Private API Endpoints

<https://www.johnsnowlabs.com/turnkey-deployment-of-medical-language-models-as-private-api-endpoints/>

<https://youtu.be/Z8WMKPsh5Ds>

<img src="/media/image.jpg" title="Video titled: Turnkey Deployment of Medical Language Models as Private API Endpoints" style="width:6.3125in;height:3.65625in" />

The speech provided in the transcript, "Turnkey Deployment of Medical Language Models as Private API Endpoints," was delivered by **CH sakya**, a software engineer and the lead engineer of the Integrations team at John Snow Labs.

The presentation focuses on the concept of medical language models (MLMs), the advantages of using them via API endpoints, and practical demonstrations of their deployment on major cloud infrastructure platforms: Amazon SageMaker, Databricks, and Snowflake.

### **1. What Are Medical Language Models (MLMs)?**

Medical Language Models are specialized **Natural Language Processing (NLP) models** specifically trained to understand, generate, and interpret text within the medical and healthcare domain. They are designed to manage the complex and specialized language found in clinical notes, medical literature, patient records, and other healthcare-related texts.

Common types of MLMs discussed include:

- **Named Entity Recognition (NER) models:** These identify and classify specific entities in medical text, such as symptoms, diseases, medications, and procedures.

- **Question Answering (QA) models:** These models are designed to answer particular medical questions, often using medical literature as their knowledge base.

- **Text Summarizing models:** These models summarize medical documents (e.g., research articles or patient records) to provide concise and relevant information.

### **2. Why Use API Endpoints for MLMs?**

Traditionally, utilizing an MLM was time-consuming and required technical expertise, involving environment setup, dependency installation, model download, and writing custom interaction code. API endpoints solve these challenges, offering significant advantages:

| **Benefit** | **Description** |
|:---|:---|
| **Interoperability & Integration** | Endpoints can be easily integrated with other applications and systems, facilitating seamless interoperability. |
| **Documentation** | They include comprehensive documentation and benchmarks, simplifying implementation. |
| **Control, Privacy, & Security** | Endpoints are deployed directly on **your cloud infrastructure**, giving you full control over the data and ensuring sensitive medical information remains private and secure. |
| **Speed of Development** | They are pre-built and ready to use; predictions can be made using simple API calls, drastically reducing the time required to develop applications. |
| **Reliability & Quality** | Built following best practices, ensuring reliable and high-quality performance. |
| **Monitoring** | Built-in cloud platform tools allow for consistent monitoring and management of the endpoints. |
| **Scalability** | Endpoints can be readily scaled up or down to handle large volumes of requests without issue. |
| **Maintenance** | Since they are managed by John Snow Labs, they are regularly maintained and updated, ensuring access to the latest features. |

### **3. Deploying and Using MLMs as API Endpoints**

The presentation demonstrated the discovery, deployment, and usage of private API endpoints across three major cloud platforms:

#### **A. Amazon SageMaker**

The deployment process begins by finding a model on the John Snow Labs website and clicking the "deploy to SageMaker" button, which directs the user to the AWS Marketplace listing.

**Deployment Steps:**

1.  **Subscription & Configuration:** Users subscribe, accept the offer, and navigate to configuration (using the SageMaker console, AWS CLI, or CloudFormation).

2.  **Model Creation:** A Deployable Model is created from the model package, requiring a model name and an IAM role with full SageMaker access.

3.  **Endpoint Creation:** A private API endpoint is configured (specifying instance type and number of instances) and created.

**Usage and Examples (Medical LLM Model):**

Once the endpoint is active, requests are made using AWS SDKs (like boto3 in Python).

- **Question Answering (Q&A):** The Medical LLM endpoint can answer complex clinical questions using a built-in prompt template (e.g., Open Book QA). The model provides concise responses based on the provided medical context. The model can also follow custom prompts, such as instructing it to answer a question simply enough for a 5-year-old child to understand.

- **Summarization:** The LLM can summarize clinical documents using a predefined summarizing template. It can handle single texts (e.g., a medical article on COVID) or an array of texts. Custom constraints can be applied, such as summarizing a document in less than 30 words.

- **Billing/Stopping:** This real-time inference is useful for quick responses to small data inputs. AWS automatically tracks usage, and endpoints should be deleted when use is complete to avoid charges.

#### **B. Databricks**

Deployment starts on the John Snow Labs website by selecting a model (such as one that detects oncology-specific entities and relations) and clicking "deploy to Databricks".

**Deployment Steps:**

1.  **Access:** After logging into Databricks and clicking "get instant access," the model becomes available in a Delta Share catalog.

2.  **Notebook:** Each model comes with a preview notebook that users import into their workspace to run the deployment.

3.  **Configuration:** The notebook requires input parameters: a **Databricks access token** (generated from the developer menu) and the **Databricks host URL**. It also requires a **JSL license** key, as the model uses a bring-your-own-license policy.

4.  **Deployment:** Running the notebook installs dependencies and uses the deploy function to create the private API endpoint.

**Usage and Examples (Oncology NER Model):**

Requests are sent using the NLP.query_endpoint function.

- **Entity Recognition:** The model detects and classifies oncological entities (e.g., identifying 'mastectomy' as a cancer surgery or 'list' as a direction). The results include a **confidence score**, indicating the model's certainty regarding the classification accuracy.

- **Multiple Documents:** The endpoint supports sending an array of clinical texts for processing, with results displayed in a data frame.

- **Billing/Stopping:** The JSL license tracks usage for billing. Endpoints must be stopped on the serving page when not in use.

#### **C. Snowflake**

Deployment starts on the John Snow Labs website by selecting a model (such as the clinical de-identification model) and clicking "deploy to Snowflake".

**Deployment Steps:**

1.  **Installation:** Users log into Snowflake Marketplace, click "get," select a warehouse, and choose a subscription option (trial or purchase) to begin installation.

2.  **Configuration:** A setup wizard requires selecting a warehouse and granting necessary permissions: one to bind the service to an endpoint, and one to start the compute pool that runs the service.

3.  **Activation:** Clicking "activate" launches the application.

4.  **Endpoint Start:** The start_app procedure is called to begin a compute pool and run the endpoint service.

**Usage and Examples (Clinical De-identification Model):**

Once the service is started, the prediction_UDF function is used to query the endpoint. This model is designed to recognize and anonymize a wide range of Protected Health Information (PHI) entities.

The endpoint supports four masking policies:

1.  **Mask Policy (Default):** Returns deidentified text where identified PHI entities are labeled.

2.  **Obfuscated Policy:** Returns fake PHI entities.

3.  **Mask Fixed Length with Chars:** Replaces PHI entities with ASC characters of a fixed length.

4.  **Mask with Chars:** Replaces PHI entities with ASC characters of uneven length.

The prediction_UDF can be called on **Snowflake tables** via a simple SELECT query, allowing users to perform de-identification on multiple documents stored in the database.

- **Billing/Stopping:** Endpoints use Snowflake container services, leveraging native scaling and resource allocation. Snowflake tracks usage and charges for both infrastructure and application costs. To stop billing, the user must call the stop_app procedure.