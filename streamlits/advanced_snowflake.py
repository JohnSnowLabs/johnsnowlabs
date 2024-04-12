
# Import python packages
from pandas import json_normalize
import pandas as pd
import json
import streamlit as st
from snowflake.snowpark.context import get_active_session

st.set_page_config(
    layout="wide",
    initial_sidebar_state="auto",
    page_title="JSL Snowflake Model Services",
    page_icon="https://raw.githubusercontent.com/JohnSnowLabs/streamlit-demo-apps/master/resources/favicon.png",
)

st.sidebar.image(
    "https://nlp.johnsnowlabs.com/assets/images/logo.png", use_column_width=True
)

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem; margin-bottom: 2.5rem">{}</div>"""

st.title("❄️ John Snow Labs Snowflake on Container Services ❄️")

genre = st.sidebar.radio(
    "Choose your model service",
    [
        "SUMMARIZE_CLINICAL_QUESTIONS",
        "SUMMARIZE_BIOMEDICAL_PUBMED",
        "RESOLVE_MEDICATION",
        "EXPLAIN_CLINICAL_DOC_ERA",
        "DEIDENTIFY_CLINICAL",
        "MED_NER_VOP_LANGTEST",
    ],
)

st.sidebar.image(
    "https://upload.wikimedia.org/wikipedia/commons/f/ff/Snowflake_Logo.svg", use_column_width=True
)


links = {
    "DEIDENTIFY_CLINICAL": """
[Demo](https://demo.johnsnowlabs.com/healthcare/DEID_PHI_TEXT_MULTI/)
[Models Hub Page](https://nlp.johnsnowlabs.com/2023/07/11/clinical_deidentification_en.html)
""",
    "EXPLAIN_CLINICAL_DOC_ERA": """[Demo](https://demo.johnsnowlabs.com/healthcare/RE_BODYPART_ENT/)
    [Models Hub Page](https://nlp.johnsnowlabs.com/2023/06/17/explain_clinical_doc_era_en.html)""",
    "RESOLVE_MEDICATION": """
    [Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes)
    [Models Hub Page](https://nlp.johnsnowlabs.com/2023/06/21/medication_resolver_pipeline_en.html)
    """,
    "SUMMARIZE_BIOMEDICAL_PUBMED": """
[Demo](https://demo.johnsnowlabs.com/healthcare/MEDICAL_LLM/)
[Models Hub Page](https://nlp.johnsnowlabs.com/2023/06/22/summarizer_biomedical_pubmed_pipeline_en.html)
""",
    "SUMMARIZE_CLINICAL_QUESTIONS": """
[Demo](https://demo.johnsnowlabs.com/healthcare/MEDICAL_LLM/)
[Models Hub Page](https://nlp.johnsnowlabs.com/2023/04/03/summarizer_clinical_questions_en.html)
""",
    "MED_NER_VOP_LANGTEST": """[Demo](https://nlp.johnsnowlabs.com/recognize_entitie)
    [Models Hub Page](https://sparknlp.org/2019/07/13/wikiner_6B_100_de.html)""",
}


examples = {
    "DEIDENTIFY_CLINICAL": """Record date : 2093-01-13,
Name : Hendrickson, ORA,
25 years-old,
#719435. IP: 203.120.223.13,
the driver's license no:A334455B.
The SSN: 324598674 and e-mail: hale@gmail.com.
Patient's VIN : 1HGBH41JXMN109286. Date : 01/13/93, PCP : David Hale.
""",
    "EXPLAIN_CLINICAL_DOC_ERA": """She is admitted to The John Hopkins Hospital 2 days ago with a history of gestational diabetes mellitus diagnosed.
She denied pain and any headache.
She was seen by the endocrinology service and she was discharged on 03/02/2018 on 40 units of insulin glargine, 12 units of insulin lispro, and metformin 1000 mg two times a day.
She had close follow-up with endocrinology post discharge.
    """,
    "RESOLVE_MEDICATION": "The patient was prescribed Amlodopine Vallarta 10-320mg, Eviplera. The other patient is given Lescol 40 MG and Everolimus 1.5 mg tablet",
    "SUMMARIZE_BIOMEDICAL_PUBMED": """Residual disease after initial surgery for ovarian cancer is the strongest prognostic factor for survival.
However, the extent of surgical resection required to achieve optimal cytoreduction is controversial.
Our goal was to estimate the effect of aggressive surgical resection on ovarian cancer patient survival.\n
A retrospective cohort study of consecutive patients with International Federation of Gynecology and Obstetrics stage IIIC ovarian cancer undergoing primary surgery
was conducted between January 1, 1994, and December 31, 1998.
The main outcome measures were residual disease after cytoreduction, frequency of radical surgical resection, and 5-year disease-specific survival.\n
The study comprised 194 patients, including 144 with carcinomatosis.
The mean patient age and follow-up time were 64.4 and 3.5 years, respectively.
After surgery, 131 (67.5%) of the 194 patients had less than 1 cm of residual disease (definition of optimal cytoreduction).
Considering all patients, residual disease was the only independent predictor of survival;
the need to perform radical procedures to achieve optimal cytoreduction was not associated with a decrease in survival.
For the subgroup of patients with carcinomatosis, residual disease and the performance of radical surgical procedures were the only independent predictors.
Disease-specific survival was markedly improved for patients with carcinomatosis operated on by surgeons who most frequently used radical procedures compared with those least likely to use radical procedures (44% versus 17%, P < .001).
Overall, residual disease was the only independent predictor of survival.
Minimizing residual disease through aggressive surgical resection was beneficial, especially in patients with carcinomatosis.
    """,
    "SUMMARIZE_CLINICAL_QUESTIONS": """Hello,I'm 20 year old girl.
I'm diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss, from 4 months.
Because of this, I stayed in the hospital and just discharged from hospital.
I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem.
Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal .
Also i have b12 deficiency and vitamin D deficiency so I'm taking weekly supplement of vitamin D and 1000 mcg b12 daily.
I'm taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now.
I feel a little bit relief from weakness and depression but I'm facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate.
I just want to know if i should start allopathy medicine or homeopathy is okay?
Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time.
Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.
Sorry for my poor english😐Thank you.

    """,
    "MED_NER_VOP_LANGTEST": """John Smith, the CEO of XYZ Corporation, traveled to Paris last week to attend a conference organized by the International Business Forum. During his stay, he visited the Eiffel Tower and met with representatives from various companies, including the United Nations. Meanwhile, an innovative startup called Tech Innovators was making headlines in Silicon Valley with its breakthrough technology.""",
    "MED_NER_RISK_FACTORS": """Smith is 55 years old, living in New York, a divorced Mexcian American woman with financial problems. She speaks Spanish and Portuguese. She lives in an apartment. She has been struggling with diabetes for the past 10 years and has recently been experiencing frequent hospitalizations due to uncontrolled blood sugar levels. Smith works as a cleaning assistant and cannot access health insurance or paid sick leave. She has a son, a student at college. Pt with likely long-standing depression. She is aware she needs rehab. Pt reports having her catholic faith as a means of support as well.  She has a long history of etoh abuse, beginning in her teens. She reports she has been a daily drinker for 30 years, most recently drinking beer daily. She smokes a pack of cigarettes a day. She had DUI in April and was due to court this week.""",
}

o_levels = {
    "EXPLAIN_CLINICAL_DOC_ERA": {
        "relation": [
            "clinical_relations",
            "clinical_relations_confidence",
            "clinical_relations_entity1",
            "clinical_relations_entity1_begin",
            "clinical_relations_entity1_class",
            "clinical_relations_entity1_end",
            "clinical_relations_entity2",
            "clinical_relations_entity2_begin",
            "clinical_relations_entity2_class",
            "clinical_relations_entity2_end",
            "clinical_relations_origin_sentence",
            # "sentence_pragmatic",
        ],
        "chunk": [
            "assertion",
            "assertion_confidence",
            "entities_clinical_ner_chunks",
            "entities_clinical_ner_chunks_class",
            "entities_clinical_ner_chunks_confidence",
            "entities_clinical_ner_chunks_origin_chunk",
            "entities_clinical_ner_chunks_origin_sentence",
            # "sentence_pragmatic",
        ],
        "token": [
            "pos",
            "unlabeled_dependency",
            # "sentence_pragmatic",
        ],
    },
    "DEIDENTIFY_CLINICAL": {
        "chunk": [
            "de_identified",
        ],
        "matched": [
            "matched_pos",
        ],
        "sentence": [
            "sentence_dl",
        ],
    },
    "RESOLVE_MEDICATION": {
        "chunk": [
            # "RxNorm_Chunk_result",
            "mapped_entity_ADE",
            "mapped_entity_ADE_all_relations",
            "mapped_entity_ADE_origin_entity",
            "mapped_entity_ADE_origin_sentence_id",
            "mapped_entity_Action",
            "mapped_entity_Action_origin_entity",
            "mapped_entity_Action_origin_sentence_id",
            "mapped_entity_NDC_Package",
            "mapped_entity_NDC_Package_all_relations",
            "mapped_entity_NDC_Package_origin_entity",
            "mapped_entity_NDC_Package_origin_sentence_id",
            "mapped_entity_NDC_Product",
            "mapped_entity_NDC_Product_all_relations",
            "mapped_entity_NDC_Product_origin_entity",
            "mapped_entity_NDC_Product_origin_sentence_id",
            "mapped_entity_SNOMED_CT",
            "mapped_entity_SNOMED_CT_all_relations",
            "mapped_entity_SNOMED_CT_origin_entity",
            "mapped_entity_SNOMED_CT_origin_sentence_id",
            "mapped_entity_Treatment",
            "mapped_entity_Treatment_origin_entity",
            "mapped_entity_Treatment_origin_sentence_id",
            "mapped_entity_UMLS",
            # "mapped_entity_UMLS_all_relations",
            "mapped_entity_UMLS_origin_entity",
            "mapped_entity_UMLS_origin_sentence_id",
        ],
        "matched": [
            "matched_pos",
        ],
        "sentence": [
            "sentence_dl",
        ],
    },
    "SUMMARIZE_CLINICAL_QUESTIONS": {
        "sentence": [
            "sentence",
        ],
        "document": [
            "document",
            "summary_summary",
        ],
    },
    "SUMMARIZE_BIOMEDICAL_PUBMED": {
        "sentence": [
            "sentence",
        ],
        "document": [
            "document",
            "summary_summary",
        ],
    },
    "MED_NER_VOP_LANGTEST": {
        "chunk": [
            "entities_wikiner_glove_840B_300",
            "entities_wikiner_glove_840B_300_class",
            "entities_wikiner_glove_840B_300_confidence",
            "entities_wikiner_glove_840B_300_origin_chunk",
            "entities_wikiner_glove_840B_300_origin_sentence",
        ],
        "sentence": [
            "sentence",
        ],
    },
}

st.write(links[genre])

TEXT = examples[genre]
textTyped = st.text_area("Type Your Text", value=TEXT, height=200)






def get_model_response_json(model, input):
    session = get_active_session()
    # max len chars 255
    input = input.replace("'",'')[:250]
    cmd = f"""SELECT JSL_{model}('{input}')"""
    data = session.sql(cmd).collect()[0].as_dict()
    data = data[list(data.keys())[0]]
    return json.loads(data)


def get_model_response_df(model, input):
    session = get_active_session()
    input = input.replace("'",'')[:250]
    cmd = f"""SELECT JSL_{model}('{input}')"""
    data = session.sql(cmd).collect()[0].as_dict()
    data = data[list(data.keys())[0]]
    data = json.loads(data)
    data = json_normalize(data)
    return pd.DataFrame(data).set_index("index")



st.subheader("Model Response DF")
df = get_model_response_df(genre, textTyped)
st.dataframe(df)
# st.json(get_model_response_json(genre, textTyped))
print("cols", df.columns)
if "relation" in o_levels[genre]:
    st.subheader("Model Response DF-Relation")
    df.explode(o_levels[genre]["relation"])[o_levels[genre]["relation"]]


if "chunk" in o_levels[genre]:
    st.subheader("Model Response DF-Entities")
    df.explode(o_levels[genre]["chunk"])[o_levels[genre]["chunk"]]

if "document" in o_levels[genre]:
    st.subheader("Model Response DF-Document Features")
    df.explode(o_levels[genre]["document"])[o_levels[genre]["document"]]


if "sentence" in o_levels[genre]:
    st.subheader("Model Response DF-Sentence Features")
    df.explode(o_levels[genre]["sentence"])[o_levels[genre]["sentence"]]


if "token" in o_levels[genre]:
    st.subheader("Model Response DF-Tokens")
    df.explode(o_levels[genre]["token"])[o_levels[genre]["token"]]
st.subheader("Model Response JSON")
st.json(get_model_response_json(genre, textTyped))
