{%- capture title -%}
FeaturesAssembler
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
The FeaturesAssembler is used to collect features from different columns. It can collect features from single value
columns (anything which can be cast to a float, if casts fails then the value is set to 0), array columns or
SparkNLP annotations (if the annotation is an embedding, it takes the embedding, otherwise tries to cast the
`result` field). The output of the transformer is a `FEATURE_VECTOR` annotation (the numeric vector is in the
`embeddings` field).

The parameters below are used for `FeaturesAssembler`.

- `inputCols`: The name of the columns containing the input annotations. It can read either a String column name or an Array of strings (column names).
- `outputCol`: The name of the column in Document type that is generated. We can specify only one column here.


All the parameters can be set using the corresponding set method in the camel case. For example, `.setInputcols()`.
{%- endcapture -%}

{%- capture model_input_anno -%}
NONE
{%- endcapture -%}

{%- capture model_output_anno -%}
FEATURE_VECTOR
{%- endcapture -%}

{%- capture model_api_link -%}
[FeaturesAssembler](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/FeaturesAssembler.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[FeaturesAssembler](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/feature_assembler/index.html#sparknlp_jsl.annotator.feature_assembler.FeaturesAssembler.name)
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import medical, nlp 

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_healthcare_100d","en","clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("word_embeddings")

sentence_embeddings = nlp.SentenceEmbeddings() \
    .setInputCols(["document", "word_embeddings"]) \
    .setOutputCol("sentence_embeddings") \
    .setPoolingStrategy("AVERAGE")

features_asm = medical.FeaturesAssembler()\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("features")

embeddings_pipeline = nlp.Pipeline(
    stages = [
        document_assembler,
        tokenizer,
        word_embeddings,
        sentence_embeddings,
        features_asm
    ])

data_df = spark.createDataFrame(
    [
        [
            "PROCEDURES PERFORMED: Colonoscopy. INDICATIONS: Renewed symptoms likely consistent with active flare of Inflammatory Bowel Disease, not responsive to conventional therapy including sulfasalazine, cortisone, local therapy. PROCEDURE: Informed consent was obtained prior to the procedure with special attention to benefits, risks, alternatives. Risks explained as bleeding, infection, bowel perforation, aspiration pneumonia, or reaction to the medications. Vital signs were monitored by blood pressure, heart rate, and oxygen saturation. Supplemental O2 given. Specifics discussed. Preprocedure physical exam performed. Stable vital signs. Lungs clear. Cardiac exam showed regular rhythm. Abdomen soft. Her past history, her past workup, her past visitation with me for Inflammatory Bowel Disease, well responsive to sulfasalazine reviewed. She currently has a flare and is not responding, therefore, likely may require steroid taper. At the same token, her symptoms are mild. She has rectal bleeding, essentially only some rusty stools. There is not significant diarrhea, just some lower stools. No significant pain. Therefore, it is possible that we are just dealing with a hemorrhoidal bleed, therefore, colonoscopy now needed. Past history reviewed. Specifics of workup, need for followup, and similar discussed. All questions answered. A normal digital rectal examination was performed. The PCF-160 AL was inserted into the anus and advanced to the cecum without difficulty, as identified by the ileocecal valve, cecal stump, and appendical orifice. All mucosal aspects thoroughly inspected, including a retroflexed examination. Withdrawal time was greater than six minutes. Unfortunately, the terminal ileum could not be intubated despite multiple attempts. Findings were those of a normal cecum, right colon, transverse colon, descending colon. A small cecal polyp was noted, this was biopsy-removed, placed in bottle #1. Random biopsies from the cecum obtained, bottle #2; random biopsies from the transverse colon obtained, as well as descending colon obtained, bottle #3. There was an area of inflammation in the proximal sigmoid colon, which was biopsied, placed in bottle #4. There was an area of relative sparing, with normal sigmoid lining, placed in bottle #5, randomly biopsied, and then inflammation again in the distal sigmoid colon and rectum biopsied, bottle #6, suggesting that we may be dealing with Crohn disease, given the relative sparing of the sigmoid colon and junk lesion. Retroflexed showed hemorrhoidal disease. Scope was then withdrawn, patient left in good condition. IMPRESSION: Active flare of Inflammatory Bowel Disease, question of Crohn disease. PLAN: I will have the patient follow up with me, will follow up on histology, follow up on the polyps. She will be put on a steroid taper and make an appointment and hopefully steroids alone will do the job. If not, she may be started on immune suppressive medication, such as azathioprine, or similar. All of this has been reviewed with the patient. All questions answered."
        ],
    ]
).toDF("text")

result = embeddings_pipeline.fit(data_df).transform(data_df)
result.select("features").show(truncate=False)

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|features                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[{feature_vector, 0, 0, , {sentence -> 0}, [-0.00896873, 0.011731416, 0.12154201, 0.1149235, -0.14689414, 0.0103584975, 0.053073216, -0.056412186, -0.05143186, -0.0118978135, -0.12175384, -0.035894137, 0.11812756, 0.094671555, 0.15838866, 0.15260744, -0.004094441, -0.13675772, -0.07472433, -0.035856977, -0.026730005, -0.21840473, 0.029632289, -0.011515695, -0.20407394, -0.07848257, 0.040990185, 0.23028605, 0.077140555, 0.066990435, 0.015219222, -0.10295644, 0.038072545, 0.10786369, 0.121525764, -0.09569349, -0.06309264, 0.2778952, 0.06462455, -0.10851931, -0.14370486, -0.1466352, 0.08354363, -0.078758985, -0.08377953, 0.12384644, -0.23281692, -0.25607574, 0.16399069, -0.07780675, -0.18302177, -0.18325584, -0.12128636, -0.0010129504, 0.0070792097, 0.20506753, 0.034964647, 0.058425985, 0.19572404, -0.103953235, -0.20159312, -0.099047214, -0.07337802, -0.03713124, -0.055443633, 0.11107734, 0.048563413, -0.038048305, -0.020617828, 0.17082842, 0.069010496, 0.08457101, -0.038229663, 0.073144384, -0.092326105, -0.10054428, -4.3286112E-4, -0.046703782, -0.080231875, 0.02524295, 0.01368699, -0.19783853, -0.03501917, 0.13324805, 0.09053264, -0.0958231, -0.0032442473, 0.19218525, -0.027179888, 0.030672349, 0.12848215, -0.014700146, -0.089054875, 0.13839856, -0.15778734, 0.07103226, -0.060303356, 0.20854644, -0.008389737, -0.1473986]}]|
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}

{%- capture model_python_legal -%}
from johnsnowlabs import nlp, legal 

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained()\
    .setInputCols(["document","token"])\
    .setOutputCol("word_embeddings")

sentence_embeddings = nlp.SentenceEmbeddings() \
    .setInputCols(["document", "word_embeddings"]) \
    .setOutputCol("sentence_embeddings") \
    .setPoolingStrategy("AVERAGE")

features_asm =legal.FeaturesAssembler()\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("features")

embeddings_pipeline = nlp.Pipeline(
    stages = [
        document_assembler,
        tokenizer,
        word_embeddings,
        sentence_embeddings,
        features_asm
    ])

data_df = spark.createDataFrame(
    [
        [
            "This is an Intellectual Property Agreement between Amazon Inc. and Atlantic Inc."
        ],
    ]
).toDF("text")

result = embeddings_pipeline.fit(data_df).transform(data_df)
result.select("features").show(truncate=False)

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|features                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[{feature_vector, 0, 0, , {sentence -> 0}, [0.02474357, -0.08310143, 0.4801927, -0.070223466, 0.33147717, -0.18737249, -0.048361354, -0.052325998, 0.053252153, -0.0067390013, 0.2836935, -0.25569317, 0.3415577, -0.19251995, 0.051623292, -0.25131556, 0.3472208, -0.036604006, -0.35653928, 0.13225944, 0.18795085, -0.09561886, 0.4695179, 0.22093144, 0.32058474, 0.057281215, 0.082858086, -0.3714214, -0.19219379, -0.26751986, -0.148075, 0.6410107, -0.07821157, -0.06398429, 6.32831E-5, 0.21222909, 0.33145514, 0.2575328, 0.009346781, -0.21482512, -0.22197871, -0.14005142, 0.04592571, -0.2919176, 0.011854073, -0.14047821, 0.22201888, -0.13500921, -0.101019345, -0.31175214, -0.0031539474, 0.07841865, 0.23760447, 0.8622971, -0.21095662, -1.9944092, -0.090888076, -0.45743433, 1.5815442, 0.4848822, -0.12528154, 0.33802572, -0.16203907, -0.09874586, 0.63106954, -0.21860953, 0.39005432, 0.25023165, 0.66769457, -0.13867687, 0.02832079, -0.17432508, -0.05764636, -0.44529453, 0.032839067, -0.2266792, -0.002856281, 0.007823931, -1.0165309, 0.08553613, 0.38090998, 0.011592574, -0.18031952, 0.37968582, -0.77948713, -0.068393, -0.029594865, -0.2165647, 0.1665183, -0.23963346, -0.017649503, -0.24768801, -0.2725593, 0.14533372, -0.36786577, 0.23388086, -0.20129707, -0.33582142, 0.5970527, 0.12596472]}]|
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}

{%- capture model_python_finance -%}
from johnsnowlabs import nlp, finance 

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained()\
    .setInputCols(["document","token"])\
    .setOutputCol("word_embeddings")

sentence_embeddings = nlp.SentenceEmbeddings() \
    .setInputCols(["document", "word_embeddings"]) \
    .setOutputCol("sentence_embeddings") \
    .setPoolingStrategy("AVERAGE")

features_asm =finance.FeaturesAssembler()\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("features")

embeddings_pipeline = nlp.Pipeline(
    stages = [
        document_assembler,
        tokenizer,
        word_embeddings,
        sentence_embeddings,
        features_asm
    ])

data_df = spark.createDataFrame(
    [
        [
            "Our competitors include the following by general category: legacy antivirus product providers, such as McAfee LLC and Broadcom Inc."
        ],
    ]
).toDF("text")

result = embeddings_pipeline.fit(data_df).transform(data_df)
result.select("features").show(truncate=False)

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|features                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[{feature_vector, 0, 0, , {sentence -> 0}, [-0.05989722, 0.10907035, 0.25595385, -0.21656203, 0.20777024, -0.17276664, -0.045803867, -0.14506632, -0.16928527, -0.10008922, 0.18800992, -0.36529806, 0.22592439, -0.118487455, 0.006129823, -0.2674002, 0.37149927, 0.12375746, -0.30488327, 0.2507765, -0.060471725, -0.22705032, 0.39436466, 0.40368417, 0.15569581, 0.083455965, 0.11193783, -0.2783573, -0.23566169, -0.12444999, 0.22503565, 0.43343276, -0.3165808, -0.057086047, 0.050554093, 0.3512633, 0.17572127, 0.19258633, -0.09170296, -0.25344467, 0.018219033, -0.117947415, -0.03234701, -0.1549039, -0.0147800855, 0.076972865, 0.08612865, -0.14120182, -0.18348631, -0.4500436, 0.038739346, 0.12991442, -0.032128494, 0.7483725, -0.09843177, -1.6700389, 0.0060545397, -0.1044135, 1.2469376, 0.32064447, -0.17263599, 0.31999183, 0.0077194544, 0.15370668, 0.59472036, -0.16953614, 0.3042488, 0.25355336, 0.60402286, 0.07441569, -0.12468894, 0.03140718, -0.2630037, -0.37703836, 0.034783553, -0.058904923, 0.022686867, 0.07962498, -0.7945683, -0.21051218, 0.6615892, -0.18747853, -0.25412843, 0.26003888, -1.0803214, -0.026889319, -0.11805089, -0.14200646, -0.019682527, -0.2372327, 0.0090960255, -0.071929, -0.115089305, 0.21781716, -0.3569975, 0.07799677, -0.096894525, -0.34368798, 0.66465, 0.14913023]}]|
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_scala_medical -%}
import spark.implicits._

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer() 
    .setInputCols("document")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_healthcare_100d","en","clinical/models")
    .setInputCols(Array("document","token"))
    .setOutputCol("word_embeddings")

val sentence_embeddings = new SentenceEmbeddings() 
    .setInputCols(Array("document", "word_embeddings")) 
    .setOutputCol("sentence_embeddings") 
    .setPoolingStrategy("AVERAGE")

val features_asm = new FeaturesAssembler()
    .setInputCols("sentence_embeddings")
    .setOutputCol("features")

val nlpPipeline = new Pipeline().setStages(Array(
        document_assembler,
        tokenizer,
        word_embeddings,
        sentence_embeddings,
        features_asm
))

val data = Seq(
  "PROCEDURES PERFORMED: Colonoscopy. INDICATIONS: Renewed symptoms likely consistent with active flare of Inflammatory Bowel Disease, not responsive to conventional therapy including sulfasalazine, cortisone, local therapy. PROCEDURE: Informed consent was obtained prior to the procedure with special attention to benefits, risks, alternatives. Risks explained as bleeding, infection, bowel perforation, aspiration pneumonia, or reaction to the medications. Vital signs were monitored by blood pressure, heart rate, and oxygen saturation. Supplemental O2 given. Specifics discussed. Preprocedure physical exam performed. Stable vital signs. Lungs clear. Cardiac exam showed regular rhythm. Abdomen soft. Her past history, her past workup, her past visitation with me for Inflammatory Bowel Disease, well responsive to sulfasalazine reviewed. She currently has a flare and is not responding, therefore, likely may require steroid taper. At the same token, her symptoms are mild. She has rectal bleeding, essentially only some rusty stools. There is not significant diarrhea, just some lower stools. No significant pain. Therefore, it is possible that we are just dealing with a hemorrhoidal bleed, therefore, colonoscopy now needed. Past history reviewed. Specifics of workup, need for followup, and similar discussed. All questions answered. A normal digital rectal examination was performed. The PCF-160 AL was inserted into the anus and advanced to the cecum without difficulty, as identified by the ileocecal valve, cecal stump, and appendical orifice. All mucosal aspects thoroughly inspected, including a retroflexed examination. Withdrawal time was greater than six minutes. Unfortunately, the terminal ileum could not be intubated despite multiple attempts. Findings were those of a normal cecum, right colon, transverse colon, descending colon. A small cecal polyp was noted, this was biopsy-removed, placed in bottle #1. Random biopsies from the cecum obtained, bottle #2; random biopsies from the transverse colon obtained, as well as descending colon obtained, bottle #3. There was an area of inflammation in the proximal sigmoid colon, which was biopsied, placed in bottle #4. There was an area of relative sparing, with normal sigmoid lining, placed in bottle #5, randomly biopsied, and then inflammation again in the distal sigmoid colon and rectum biopsied, bottle #6, suggesting that we may be dealing with Crohn disease, given the relative sparing of the sigmoid colon and junk lesion. Retroflexed showed hemorrhoidal disease. Scope was then withdrawn, patient left in good condition. IMPRESSION: Active flare of Inflammatory Bowel Disease, question of Crohn disease. PLAN: I will have the patient follow up with me, will follow up on histology, follow up on the polyps. She will be put on a steroid taper and make an appointment and hopefully steroids alone will do the job. If not, she may be started on immune suppressive medication, such as azathioprine, or similar. All of this has been reviewed with the patient. All questions answered."
).toDF("text")

val result = nlpPipeline.fit(data_df).transform(data_df)

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|features                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[{feature_vector, 0, 0, , {sentence -> 0}, [-0.00896873, 0.011731416, 0.12154201, 0.1149235, -0.14689414, 0.0103584975, 0.053073216, -0.056412186, -0.05143186, -0.0118978135, -0.12175384, -0.035894137, 0.11812756, 0.094671555, 0.15838866, 0.15260744, -0.004094441, -0.13675772, -0.07472433, -0.035856977, -0.026730005, -0.21840473, 0.029632289, -0.011515695, -0.20407394, -0.07848257, 0.040990185, 0.23028605, 0.077140555, 0.066990435, 0.015219222, -0.10295644, 0.038072545, 0.10786369, 0.121525764, -0.09569349, -0.06309264, 0.2778952, 0.06462455, -0.10851931, -0.14370486, -0.1466352, 0.08354363, -0.078758985, -0.08377953, 0.12384644, -0.23281692, -0.25607574, 0.16399069, -0.07780675, -0.18302177, -0.18325584, -0.12128636, -0.0010129504, 0.0070792097, 0.20506753, 0.034964647, 0.058425985, 0.19572404, -0.103953235, -0.20159312, -0.099047214, -0.07337802, -0.03713124, -0.055443633, 0.11107734, 0.048563413, -0.038048305, -0.020617828, 0.17082842, 0.069010496, 0.08457101, -0.038229663, 0.073144384, -0.092326105, -0.10054428, -4.3286112E-4, -0.046703782, -0.080231875, 0.02524295, 0.01368699, -0.19783853, -0.03501917, 0.13324805, 0.09053264, -0.0958231, -0.0032442473, 0.19218525, -0.027179888, 0.030672349, 0.12848215, -0.014700146, -0.089054875, 0.13839856, -0.15778734, 0.07103226, -0.060303356, 0.20854644, -0.008389737, -0.1473986]}]|
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

{%- endcapture -%}

{%- capture model_scala_legal -%}
import spark.implicits._

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer() 
    .setInputCols("document")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained()
    .setInputCols(Array("document","token"))
    .setOutputCol("word_embeddings")

val sentence_embeddings = new SentenceEmbeddings() 
    .setInputCols(Array("document", "word_embeddings")) 
    .setOutputCol("sentence_embeddings") 
    .setPoolingStrategy("AVERAGE")

val features_asm = new FeaturesAssembler()
    .setInputCols("sentence_embeddings")
    .setOutputCol("features")

val nlpPipeline = new Pipeline().setStages(Array(
        document_assembler,
        tokenizer,
        word_embeddings,
        sentence_embeddings,
        features_asm
))

val data = Seq(
  "This is an Intellectual Property Agreement between Amazon Inc. and Atlantic Inc."
).toDF("text")

val result = nlpPipeline.fit(data_df).transform(data_df)

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|features                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[{feature_vector, 0, 0, , {sentence -> 0}, [0.02474357, -0.08310143, 0.4801927, -0.070223466, 0.33147717, -0.18737249, -0.048361354, -0.052325998, 0.053252153, -0.0067390013, 0.2836935, -0.25569317, 0.3415577, -0.19251995, 0.051623292, -0.25131556, 0.3472208, -0.036604006, -0.35653928, 0.13225944, 0.18795085, -0.09561886, 0.4695179, 0.22093144, 0.32058474, 0.057281215, 0.082858086, -0.3714214, -0.19219379, -0.26751986, -0.148075, 0.6410107, -0.07821157, -0.06398429, 6.32831E-5, 0.21222909, 0.33145514, 0.2575328, 0.009346781, -0.21482512, -0.22197871, -0.14005142, 0.04592571, -0.2919176, 0.011854073, -0.14047821, 0.22201888, -0.13500921, -0.101019345, -0.31175214, -0.0031539474, 0.07841865, 0.23760447, 0.8622971, -0.21095662, -1.9944092, -0.090888076, -0.45743433, 1.5815442, 0.4848822, -0.12528154, 0.33802572, -0.16203907, -0.09874586, 0.63106954, -0.21860953, 0.39005432, 0.25023165, 0.66769457, -0.13867687, 0.02832079, -0.17432508, -0.05764636, -0.44529453, 0.032839067, -0.2266792, -0.002856281, 0.007823931, -1.0165309, 0.08553613, 0.38090998, 0.011592574, -0.18031952, 0.37968582, -0.77948713, -0.068393, -0.029594865, -0.2165647, 0.1665183, -0.23963346, -0.017649503, -0.24768801, -0.2725593, 0.14533372, -0.36786577, 0.23388086, -0.20129707, -0.33582142, 0.5970527, 0.12596472]}]|
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_scala_finance -%}
import spark.implicits._

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer() 
    .setInputCols("document")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained()
    .setInputCols(Array("document","token"))
    .setOutputCol("word_embeddings")

val sentence_embeddings = new SentenceEmbeddings() 
    .setInputCols(Array("document", "word_embeddings")) 
    .setOutputCol("sentence_embeddings") 
    .setPoolingStrategy("AVERAGE")

val features_asm = new FeaturesAssembler()
    .setInputCols("sentence_embeddings")
    .setOutputCol("features")

val nlpPipeline = new Pipeline().setStages(Array(
        document_assembler,
        tokenizer,
        word_embeddings,
        sentence_embeddings,
        features_asm
))

val data = Seq(
  "Our competitors include the following by general category: legacy antivirus product providers, such as McAfee LLC and Broadcom Inc."
).toDF("text")

val result = nlpPipeline.fit(data_df).transform(data_df)

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|features                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|[{feature_vector, 0, 0, , {sentence -> 0}, [-0.05989722, 0.10907035, 0.25595385, -0.21656203, 0.20777024, -0.17276664, -0.045803867, -0.14506632, -0.16928527, -0.10008922, 0.18800992, -0.36529806, 0.22592439, -0.118487455, 0.006129823, -0.2674002, 0.37149927, 0.12375746, -0.30488327, 0.2507765, -0.060471725, -0.22705032, 0.39436466, 0.40368417, 0.15569581, 0.083455965, 0.11193783, -0.2783573, -0.23566169, -0.12444999, 0.22503565, 0.43343276, -0.3165808, -0.057086047, 0.050554093, 0.3512633, 0.17572127, 0.19258633, -0.09170296, -0.25344467, 0.018219033, -0.117947415, -0.03234701, -0.1549039, -0.0147800855, 0.076972865, 0.08612865, -0.14120182, -0.18348631, -0.4500436, 0.038739346, 0.12991442, -0.032128494, 0.7483725, -0.09843177, -1.6700389, 0.0060545397, -0.1044135, 1.2469376, 0.32064447, -0.17263599, 0.31999183, 0.0077194544, 0.15370668, 0.59472036, -0.16953614, 0.3042488, 0.25355336, 0.60402286, 0.07441569, -0.12468894, 0.03140718, -0.2630037, -0.37703836, 0.034783553, -0.058904923, 0.022686867, 0.07962498, -0.7945683, -0.21051218, 0.6615892, -0.18747853, -0.25412843, 0.26003888, -1.0803214, -0.026889319, -0.11805089, -0.14200646, -0.019682527, -0.2372327, 0.0090960255, -0.071929, -0.115089305, 0.21781716, -0.3569975, 0.07799677, -0.096894525, -0.34368798, 0.66465, 0.14913023]}]|
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
{%- endcapture -%}

{%- capture model_notebook_link -%}
[Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/FeaturesAssembler.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_python_legal=model_python_legal
model_python_finance=model_python_finance
model_scala_medical=model_scala_medical
model_scala_legal=model_scala_legal
model_scala_finance=model_scala_finance
model_api_link=model_api_link
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link
%}
