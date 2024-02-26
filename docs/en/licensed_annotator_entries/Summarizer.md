{%- capture title -%}
Summarizer
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
Summarizer annotator that uses a generative deep learning model to create summaries of medical, finance, and legal texts. This annotator helps to quickly summarize complex medical, finance, and legal information from related documents.

Parameters:

- `doSample`: Whether or not to use sampling, use greedy decoding otherwise (Default: false)

- `ignoreTokenIds`: A list of token ids which are ignored in the decoder's output (Default: Array())

- `maxNewTokens`: Maximum number of new tokens to be generated (Default: 30)

- `maxTextLength`: Maximum length of context text.

- `noRepeatNgramSize`: If set to int > 0, all ngrams of that size can only occur once (Default: 0)

- `randomSeed`: Optional Random seed for the model.

- `refineChunkSize`: How large should refined chunks Be.

- `refineMaxAttempts`: How many times should chunks be re-summarized while they are above SummaryTargetLength before stopping.

- `refineSummary`: Set true to perform refined summarization at increased computation cost.

- `refineSummaryTargetLength`: Target length for refined summary.

- `topK`: The number of highest probability vocabulary tokens to keep for top-k-filtering (Default: 50)

- `useCache`: Cache internal state of the model to improve performance

Available models can be found at the [Models Hub](https://nlp.johnsnowlabs.com/models?task=Summarization).

For more extended examples on document pre-processing see the [Spark NLP Workshop](https://github.com/JohnSnowLabs/spark-nlp-workshop)
{%- endcapture -%}

{%- capture model_input_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_output_anno -%}
CHUNK
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler()\
    .setInputCol('text')\
    .setOutputCol('document')

summarizer = medical.Summarizer.pretrained("summarizer_clinical_jsl", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("summary")\
    .setMaxTextLength(512)\
    .setMaxNewTokens(512)

pipeline = nlp.Pipeline(
    stages=[
        document_assembler,
        summarizer
])

text = """The patient is a pleasant 17-year-old gentleman who was playing basketball today in gym. Two hours prior to presentation, he started to fall and someone stepped on his ankle and kind of twisted his right ankle and he cannot bear weight on it now. It hurts to move or bear weight. No other injuries noted. He does not think he has had injuries to his ankle in the past.
SOCIAL HISTORY: He does not drink or smoke.
MEDICAL DECISION MAKING:
He had an x-ray of his ankle that showed a small ossicle versus avulsion fracture of the talonavicular joint on the lateral view. He has had no pain over the metatarsals themselves. This may be a fracture based upon his exam. He does want to have me to put him in a splint. He was given Motrin here. He will be discharged home to follow up with Dr. X from Orthopedics.
DISPOSITION: Crutches and splint were administered here. I gave him a prescription for Motrin and some Darvocet if he needs to length his sleep and if he has continued pain to follow up with Dr. X. Return if any worsening problems."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

result.select("summary.result").show(truncate=False)

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[A 17-year-old man fell and twisted his right ankle, causing pain to move or bear weight. An x-ray showed a small ossicle or avulsion fracture of the talonavicular joint on the lateral view, which may be a fracture based upon his exam. He was given Motrin and discharged home with crutches and a prescription for Motrin and Darvocet. He was advised to follow up with his doctor if pain worsens and return if any worsening problems worsen.]|
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_scala_medical -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val summarizer = Summarizer.pretrained("summarizer_clinical_jsl", "en", "clinical/models")
  .setInputCols(Array("document"))
  .setOutputCol("summary")
  .setMaxTextLength(512)
  .setMaxNewTokens(512)


val pipeline = new Pipeline().setStages(Array(documentAssembler, summarizer))

val text = """The patient is a pleasant 17-year-old gentleman who was playing basketball today in gym. Two hours prior to presentation, he started to fall and someone stepped on his ankle and kind of twisted his right ankle and he cannot bear weight on it now. It hurts to move or bear weight. No other injuries noted. He does not think he has had injuries to his ankle in the past.
SOCIAL HISTORY: He does not drink or smoke.
MEDICAL DECISION MAKING:
He had an x-ray of his ankle that showed a small ossicle versus avulsion fracture of the talonavicular joint on the lateral view. He has had no pain over the metatarsals themselves. This may be a fracture based upon his exam. He does want to have me to put him in a splint. He was given Motrin here. He will be discharged home to follow up with Dr. X from Orthopedics.
DISPOSITION: Crutches and splint were administered here. I gave him a prescription for Motrin and some Darvocet if he needs to length his sleep and if he has continued pain to follow up with Dr. X. Return if any worsening problems."""

val data = Seq(text).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)

{%- endcapture -%}

{%- capture model_python_legal -%}
from johnsnowlabs import nlp, legal

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

summarizer = legal.Summarizer().pretrained('legsum_flant5_legal_augmented','en','legal/models')\
    .setInputCols(["document"])\
    .setOutputCol("summary")\
    .setMaxNewTokens(1000)

pipeline = nlp.Pipeline(stages=[document_assembler, summarizer])

data = spark.createDataFrame([
  ["""NOW, THEREFORE, in consideration of the Company’s disclosure of information to the Recipient
and the promises set forth below, the parties agree as follows:

     1. Confidential Information. “Confidential Information” as used in this
Agreement means all information relating to the Company disclosed to the Recipient by the Company,
including without limitation any business, technical, marketing, financial or other information,
whether in written, electronic or oral form. Any and all reproductions, copies, notes, summaries,
reports, analyses or other material derived by the Recipient or its Representatives (as defined
below) in whole or in part from the Confidential Information in whatever form maintained shall be
considered part of the Confidential Information itself and shall be treated as such. Confidential
Information does not include information that (a) is or becomes part of the public domain other
than as a result of disclosure by the Recipient or its Representatives; (b) becomes available to
the Recipient on a nonconfidential basis from a source other than the Company, provided that source
is not bound with respect to that information by a confidentiality agreement with the Company or is
otherwise prohibited from transmitting that information by a contractual, legal or other
obligation; (c) can be proven by the Recipient to have been in the Recipient’s possession prior to
disclosure of the same by the Company; or (d) is independently developed by the Recipient without
reference to or reliance on any of the Company’s Confidential Information."""]
]).toDF('text')

result = pipeline.fit(data).transform(data)

result.select("summary.result").show(truncate=False)

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[This legal agreement states that the company has disclosed all information relating to the company to the recipient, including any business, technical, marketing, financial or other information. It also states that any reproductions, copies, notes, summaries, reports, analyses or other material derived from the confidential information must be treated as part of the confidential information. The confidential information does not include information that is or becomes part of the public domain other than as a result of disclosure by the recipient or its representatives, becomes available to the recipient on a nonconfidential basis from a source other than the company, can be proven by the recipient to have been in the recipient’s possession prior to disclosure, or is independently developed by the recipient without reference to or reliance on any of the company’s confidential information.]|
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_scala_legal -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val summarizer = Summarizer.pretrained("legsum_flant5_legal_augmented", "en", "legal/models")
  .setInputCols(Array("document"))
  .setOutputCol("summary")
  .setMaxNewTokens(1000)

val pipeline = new Pipeline()
  .setStages(Array(documentAssembler, summarizer))

val text = """NOW, THEREFORE, in consideration of the Company’s disclosure of information to the Recipient
and the promises set forth below, the parties agree as follows:

     1. Confidential Information. “Confidential Information” as used in this
Agreement means all information relating to the Company disclosed to the Recipient by the Company,
including without limitation any business, technical, marketing, financial or other information,
whether in written, electronic or oral form. Any and all reproductions, copies, notes, summaries,
reports, analyses or other material derived by the Recipient or its Representatives (as defined
below) in whole or in part from the Confidential Information in whatever form maintained shall be
considered part of the Confidential Information itself and shall be treated as such. Confidential
Information does not include information that (a) is or becomes part of the public domain other
than as a result of disclosure by the Recipient or its Representatives; (b) becomes available to
the Recipient on a nonconfidential basis from a source other than the Company, provided that source
is not bound with respect to that information by a confidentiality agreement with the Company or is
otherwise prohibited from transmitting that information by a contractual, legal or other
obligation; (c) can be proven by the Recipient to have been in the Recipient’s possession prior to
disclosure of the same by the Company; or (d) is independently developed by the Recipient without
reference to or reliance on any of the Company’s Confidential Information."""

val data = Seq(text).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[This legal agreement states that the company has disclosed all information relating to the company to the recipient, including any business, technical, marketing, financial or other information. It also states that any reproductions, copies, notes, summaries, reports, analyses or other material derived from the confidential information must be treated as part of the confidential information. The confidential information does not include information that is or becomes part of the public domain other than as a result of disclosure by the recipient or its representatives, becomes available to the recipient on a nonconfidential basis from a source other than the company, can be proven by the recipient to have been in the recipient’s possession prior to disclosure, or is independently developed by the recipient without reference to or reliance on any of the company’s confidential information.]|
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}

{%- capture model_python_finance -%}
from johnsnowlabs import nlp, finance

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

summarizer = finance.Summarizer().pretrained('finsum_flant5_base','en','finance/models')\
    .setInputCols(["document"])\
    .setOutputCol("summary")\
    .setMaxNewTokens(1000)

pipeline = nlp.Pipeline(stages=[document_assembler, summarizer])

data = spark.createDataFrame([["""Lost Time Incident Rate: 
The lost time incident rate per 200,000 hours worked in 2021 was 0.14, which decreased by 17.6% compared to 2020 (0.17) and decreased by 70.8% compared to 2019 (0.48). The decrease in the lost time incident rate can be attributed to the company's efforts to improve workplace safety and implement effective risk management strategies. 
The total Scope 2 GHG emissions in 2021 were 688,228 tonnes, which remained relatively stable compared to 2020. The company's efforts to transition to renewable energy sources have helped to minimize Scope 2 GHG emissions."""]]).toDF('text')

result = pipeline.fit(data).transform(data)

result.select("summary.result").show(truncate=False)

{%- endcapture -%}

{%- capture model_scala_finance -%}
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val summarizer = Summarizer.pretrained("finsum_flant5_base", "en", "finance/models")
  .setInputCols(Array("document"))
  .setOutputCol("summary")
  .setMaxNewTokens(1000)

val pipeline = new Pipeline().setStages(Array(documentAssembler, summarizer))

val text = """Lost Time Incident Rate: 
The lost time incident rate per 200,000 hours worked in 2021 was 0.14, which decreased by 17.6% compared to 2020 (0.17) and decreased by 70.8% compared to 2019 (0.48). The decrease in the lost time incident rate can be attributed to the company's efforts to improve workplace safety and implement effective risk management strategies. 
The total Scope 2 GHG emissions in 2021 were 688,228 tonnes, which remained relatively stable compared to 2020. The company's efforts to transition to renewable energy sources have helped to minimize Scope 2 GHG emissions."""

val data = Seq(text).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)

{%- endcapture -%}

{%- capture model_api_link -%}
[MedicalSummarizer](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/seq2seq/MedicalSummarizer.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[MedicalSummarizer](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/seq2seq/medical_summarizer/index.html#sparknlp_jsl.annotator.seq2seq.medical_summarizer.MedicalSummarizer)
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
%}
