---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Healthcare NLP v7.0.0 Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_7_0_0
key: docs-licensed-release-notes
modify_date: 2026-10-01
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 7.0.0

#### Highlights

We are delighted to announce notable enhancements and updates in Healthcare NLP 7.0.0. This is a **major release**, and the headline addition is **native support for Apache Spark 4.x, delivered alongside the existing Spark 3.x line**. In practice, this means Healthcare NLP now runs on the newest cloud runtimes: you can move to the **latest Databricks runtimes — including 17, 18.1, 18.2, and 19** — and keep using the same John Snow Labs JAR you already know. Spark 3.x users are fully supported as before, so upgrading is a choice you make when your platform is ready, not something forced on you by this release.

Beyond the Spark 4 milestone, 7.0.0 brings a **new HL7 v2.x de-identification annotator**, several significant **de-identification enhancements** (nationality-aware obfuscation, ID-based obfuscation, encrypted mappings columns, entity-level date-to-year conversion, state-format-aware obfuscation and refreshed faker resources), and a major overhaul of **TensorFlow-based training** that **ships 1,171 ready-to-use training graphs inside the JAR** so classifier, relation extraction and assertion training no longer require a local TensorFlow installation. The release is rounded out by a set of stability and memory-management bug fixes.

This release also delivers an update of the medical terminology models: 81 updated and 73 new Entity Resolver, ChunkMapper, and pretrained pipeline models across 16 medical coding systems, each trained on the latest official release of its terminology, from SNOMED CT (US Edition 20260901), LOINC 2.83, and ICD-11 (WHO 2026-01) to RxNorm, ICD-10-CM, CPT, HCPCS, HPO, HGNC, MeSH, and NCIt. Updated models of several systems now carry the source release in their names, so a pipeline can stay pinned to the terminology release it was built for.

Two new benchmarks come with the release. On medical terminology mapping, the resolvers reach 87.3% to 96.4% top-1 accuracy and score highest on all four coding systems tested against five general-purpose LLMs, and a CPU speed benchmark reports end-to-end timings for oncology NER and resolver pipelines on 1,000 clinical documents. New blog posts cover clinical term mapping and the 2026 clinical de-identification benchmarks, where Healthcare NLP reaches 0.96 PHI F1 on expert-annotated clinical notes.

- **Apache Spark 4.x support alongside Spark 3.x**, unlocking the latest cloud runtimes (including Databricks 17, 18.1, 18.2, and 19) with automatic artifact selection so `sparknlp_jsl.start()` just works
- **`Hl7v2DeIdentification`** — a new, dependency-free annotator for de-identifying HL7 v2.x messages (structured fields and free-text narratives)
- **De-Identification enhancements** — nationality-aware name obfuscation, ID-based obfuscation, encrypted mappings (aux) column, `dateToYearEntities`, state-format-aware STATE obfuscation, and cleaned/expanded faker resources
- **Train TensorFlow-based annotators without TensorFlow** — 1,171 embedded training graphs for Classifier, Relation Extraction and Assertion training, selected automatically
- Updated 81 and Introduced 73 New Entity Resolver, ChunkMapper, and Pretrained Pipeline Models Across 16 Medical Coding Systems
- Medical Terminology Mapping Benchmark: Healthcare NLP Resolvers vs. General-Purpose LLMs
- Oncology NER and Entity Resolver Pipelines Speed Benchmark
- New Blog Posts & Technical Deep Dives
- Updated Notebooks And Demonstrations For Making Healthcare NLP Easier To Navigate And Understand
  - New [HL7 v2 De-Identification](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.15.HL7v2_DeIdentification.ipynb) Notebook
- **Bug fixes** — memory/temp-file cleanup on model loading, ONNX CUDA preload recovery, batched ZeroShotNer decoding, empty-input handling, and multi-task NER fixes
- The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

These enhancements will elevate your experience with Healthcare NLP, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.


<div class="h3-box" markdown="1">

#### 🌟 Spotlight: Apache Spark 4.x Support & the Latest Cloud Runtimes

For a long time, staying on Healthcare NLP meant staying on Apache Spark 3.x. As cloud providers moved their newest runtimes to Spark 4, that gap became a real blocker: teams wanting the newest Databricks runtime had to choose between upgrading their platform and keeping Healthcare NLP.

**Healthcare NLP 7.0.0 closes that gap.** The library now runs natively on **Apache Spark 4.x** in addition to Spark 3.x, so you can move to the **latest cloud runtimes and keep everything you already have** — the same annotators, the same pretrained models, the same pipelines. Concretely, this means the newest **Databricks runtimes — 17, 18.1, 18.2, and 19 — are now supported**, and the same applies to any Spark 4.x cluster you run yourself.

The best part: **you usually don't have to think about any of this.** When you install Healthcare NLP with `pip` and call `sparknlp_jsl.start()`, it detects the Spark version on your cluster and pulls the matching build automatically. Spark 3.x clusters keep getting the Spark 3 build; Spark 4.x clusters get the Spark 4 build. No configuration changes, no manual coordinates.

```python
import sparknlp_jsl

# Works the same on Spark 3.x and Spark 4.x clusters — the right build is chosen for you.
spark = sparknlp_jsl.start(secret=SECRET)
```

**Choosing a build manually (`spark.jars`)**

If you attach the JAR manually — for example on a cluster where you set `spark.jars` yourself — pick the build that matches your runtime:

{:.table-model-big}

| Your runtime | Use this build | GPU / Apple Silicon / AArch64 |
| --- | --- | --- |
| Spark 3.x (Databricks 13–16) | `spark-nlp-jsl-7.0.0.jar` | supported, as before |
| Spark 4.x — the common case (Databricks 17, 18.1, 18.2, 19 and other Spark 4 clusters) | `spark-nlp-jsl_2.13-7.0.0.jar` | supported |
| Plain, **unpatched** Spark 4.0.0 (a self-managed cluster on the original 4.0.0 build) | `spark-nlp-jsl-spark400_2.13-7.0.0.jar` | supported |

**A note for Databricks 17+ users:** these runtimes report themselves as Spark `4.0.0`, but they already include an important upstream fix, so they use the **regular Spark 4 build** (`spark-nlp-jsl_2.13-...`) — **not** the `spark400` one. The dedicated `spark400` build is only for a plain, unpatched Spark 4.0.0 that you manage yourself. If you ever see a `NoSuchMethodError` mentioning Spark's `Param` class, it almost always means the wrong one of these two Spark 4 builds was selected — switch to the regular `_2.13` build. When in doubt, let `sparknlp_jsl.start()` choose for you.

Your existing Spark 3.x workloads keep working unchanged — Spark 4 support is added next to Spark 3, not on top of it.

</div><div class="h3-box" markdown="1">

#### HL7 v2.x De-Identification with `Hl7v2DeIdentification`

`Hl7v2DeIdentification` is a **new Spark Transformer for de-identifying HL7 v2.x messages** — the classic pipe/hat delimited "vertical bar" format (e.g. `ADT^A01`, `ORU^R01`). It performs field-level obfuscation using a **lightweight, dependency-free delimiter parser**.

**What are HL7 v2 messages?** HL7 v2.x is the messaging standard hospital systems have used for decades to exchange clinical events — patient admissions (`ADT`), lab results (`ORU`), orders (`ORM`/`RDE`), and more. A message is a block of text where each line is a **segment** (identified by a 3-letter code such as `MSH`, `PID`, or `OBX`), and every segment is built from **fields** separated by `|`, which split further into **components** (`^`), **repetitions** (`~`) and **subcomponents** (`&`). PHI is scattered throughout these fields — a patient's name in `PID-5`, date of birth in `PID-7`, phone in `PID-13` — and can also sit inside free-text narrative fields such as `OBX-5` (observation value) and `NTE-3` (notes). Because these messages are still ubiquitous in real hospital integrations, de-identifying them safely — without corrupting the delimiter structure that downstream systems depend on — is a common and demanding requirement.

Because the HL7 v2 wire format (segments, fields, components, repetitions, subcomponents and the escape character declared in `MSH-1`/`MSH-2`) is identical across all v2.x versions, a single **Terser-style path notation** targets PHI uniformly **from v2.1 through v2.9** without any version-specific structure libraries.

**Path Notation**

```text
"PID-5"       -> segment PID, field 5 (all components / repetitions)
"PID-5-1"     -> field 5, component 1 (family name)
"PID-5-1-2"   -> field 5, component 1, subcomponent 2
"PID(2)-5-1"  -> the 2nd PID segment occurrence, field 5, component 1
```

Field numbers match the HL7 specification exactly, including the `MSH` off-by-one convention (`MSH-1` is the field separator, `MSH-2` the encoding characters). Obfuscated replacements are sanitized so they can never inject an HL7 delimiter or control character and break the message structure.

**Pretrained HL7 v2 de-identification models**

Two ready-to-use models ship with this release. Both bake in a comprehensive default PHI map covering HIPAA Safe Harbor identifiers (names, dates, addresses, phones, SSNs, MRN/account/member/license/device IDs and clinician names) across the common HL7 v2 segments (`MSH`, `EVN`, `PID`, `PD1`, `MRG`, `NK1`, `PV1`, `PV2`, `GT1`, `IN1`/`IN2`, `AL1`, `DG1`, `PR1`, `ROL`, `ACC`, `UB1`/`UB2`, `TXA`, `SCH`/`AIP`/`AIS`, `ORC`, `OBR`, `OBX`, `SPM`, `RXA`, `RXE`). Segments absent from a message are simply skipped, so the same model works on any HL7 v2 feed.

- **`hl7v2_deidentification_base`** de-identifies only the structured PHI fields and leaves narrative fields untouched.
- **`hl7v2_deidentification_free_text`** applies the same structured map and additionally routes the narrative fields `OBX-5` and `NTE-3` through a Healthcare NLP de-identification pipeline (set with `setPipeline()`), so PHI written in prose is de-identified too.

**Example**

Take a short, synthetic `ORU^R01` lab-result message that carries PHI both in structured fields and in a free-text narrative (`OBX-5`, `NTE-3`):

```python
hl7_v2_message = """YOUR_HL7_HERE"""

# The free-text model routes OBX-5 / NTE-3 through a clinical de-identification pipeline,
# so we load one first. It returns its de-identified text in the "obfuscated" column.
deid_pipeline = PretrainedPipeline(
    "clinical_deidentification_docwise_benchmark_optimized_v2", "en", "clinical/models"
)

deid = (
    Hl7v2DeIdentification.pretrained("hl7v2_deidentification_free_text", "en", "clinical/models")
        .setInputCol("text")
        .setOutputCol("deid")
        .setMode("obfuscate")
        .setDays(20)
        .setSeed(88)
        .setPipeline(spark, deid_pipeline, "obfuscated")
)

obfuscated = deid.deidentify(hl7_v2_message)
```

Running this on the message below (`hl7_v2_message`):

```text
MSH|^~\&|LAB|GOOD HEALTH LAB|EHR|GOOD HEALTH HOSPITAL|20240108090000||ORU^R01|MSG00002|P|2.4
PID|1||MRN123456^^^GHH^MR||DOE^JOHN^MICHAEL||19800101|M|||123 Main Street^^Boston^MA^02108^USA||617-555-1122
OBR|1|ORD123|FILL456|CBC^Complete Blood Count|||20240108083000|||||||||004777^SMITH^ROBERT
OBX|1|TX|NARR^Narrative||Patient John Doe was seen on 01/08/2024 at Good Health Hospital and reports mild fatigue. He lives at 123 Main Street, Boston and can be reached at 617-555-1122.||||||F
NTE|1||Follow up with Dr. Robert Smith at 617-555-9000 in two weeks.
```

De-identifying it with the free-text model obfuscates the structured PHI **and** routes the narrative fields through the NLP pipeline, while leaving the message structure, segment codes and clinical content intact:

```text
MSH|^~\&|LAB|GOOD HEALTH LAB|EHR|GOOD HEALTH HOSPITAL|20240128090000||ORU^R01|MSG00002|P|2.4
PID|1||TMC678901^^^GHH^MR||CEASE^MYLENE^ANOLA||19800121|M|||1011 North Cooper Street^^Allenchester^VA^57653^USA||162-000-6677
OBR|1|ORD123|FILL456|CBC^Complete Blood Count|||20240128083000|||||||||559222^LITTER^DERREK
OBX|1|TX|NARR^Narrative||Patient Valerie Ates was seen on 18/09/2024 at Medical Center Of Trinity and reports mild fatigue. He lives at 2001 Ladbrook Drive, Winder and can be reached at 839-777-3344.||||||F
NTE|1||Follow up with Dr. Elidia Plump at 839-777-1222 in two weeks.
```

Notice that the patient name (`PID-5`), MRN (`PID-3`), date of birth (`PID-7`), address (`PID-11`), phone (`PID-13`), message timestamp (`MSH-7`) and ordering physician (`OBR-16`) are all obfuscated in the structured fields, while the narrative in `OBX-5` and `NTE-3` is de-identified as natural language — with dates consistently shifted by the same offset across the whole message.

> For a feed without free text (or where narrative fields are handled elsewhere), use `hl7v2_deidentification_base` instead — it needs no pipeline and no `setPipeline()` call.

</div><div class="h3-box" markdown="1">

#### De-Identification Enhancements

This release extends the de-identification family with several new capabilities across the `DeIdentification`, `LightDeIdentification`, `StructuredDeidentification` and `ReIdentification` components.

**Nationality-aware name obfuscation (`setNationalityAwareness`)**

When enabled, the original name's nationality is detected from embedded, gender-separated nationality name lists (e.g. Arab, French, Spanish, German, Russian, Turkish, and more) and the fake name is generated from the **same nationality and gender**. This preserves the demographic character of the document while still removing the real identity. The feature is supported for **English** (`language == "en"`); for other languages it is automatically disabled, and if the nationality cannot be detected the obfuscation falls back to the regular behavior (gender-aware when `genderAwareness` is enabled, otherwise the default faker lists).

```python
deid.setNationalityAwareness(True)
```

**ID-based obfuscation (`setIdBasedObfuscation`)**

Makes name obfuscation depend on the document ID (read from the `id` metadata of the document), for name-related entities (`NAME`, `PATIENT`, `DOCTOR`, `SIGNING_PERSON`, `PERSON`, `CLIENT`, `FIRST_NAME`, `LAST_NAME`):

- Same document ID + same name → **same fake** (consistent within a document)
- Same document ID + different names → different fakes
- Different document IDs + same name → **different fakes** (a name is obfuscated differently across documents)

It works together with `genderAwareness` and `nationalityAwareness`, and falls back to seed-based selection when no document ID is available.

**Encrypted mappings (aux) column (`setAuxEncryptionKey`)**

The mappings/aux column carries the original values so that `ReIdentification` can restore the original text. Setting an encryption key now encrypts the sensitive fields of that column with **AES-256-GCM**, so it can be stored next to the de-identified data without exposing the originals. The **same key must be set on both sides** — on the de-identification annotator that produces the column and on `ReIdentification` that consumes it. The key is never persisted in clear text: it is wrapped before being stored in the annotator, so a saved pipeline never contains the raw passphrase. When no key is set, the mappings column keeps its plain, backward-compatible behavior.

```python
de_identification = DeIdentification() \
    .setReturnEntityMappings(True) \
    .setMappingsColumn("aux") \
    .setAuxEncryptionKey("my-secret-key")

re_identification = ReIdentification() \
    .setAuxEncryptionKey("my-secret-key")
```

**Entity-level date-to-year conversion (`setDateToYearEntities`)**

Previously the `dateToYear` flag governed all date entities globally. The new `dateToYearEntities` parameter lets you convert **only specific date entities** (e.g. `DOB`) to year-only, while every other date entity keeps the regular format-preserving date displacement. When the list is non-empty it overrides the global `dateToYear` flag for the listed entities; when empty (default), the global flag applies.

```python
deid.setDateToYearEntities(["DOB", "DOD"])
```

**State-format-aware STATE obfuscation**

STATE obfuscation is now format aware: a spelled-out state (e.g. "New York") is replaced by a spelled-out fake, and a two-letter abbreviation (e.g. "NY") is replaced by a two-letter fake, backed by two mirrored resources (`state/en.txt` and `state/abbreviation_en.txt`). The check is format-based rather than membership-based, so a two-letter STATE chunk is always replaced by a two-letter value — the obfuscated output never leaks whether the original was a real state — and the two formats interoperate correctly with the geographic-consistency path.

**Refreshed faker resources**

The faker resources were cleaned and expanded: offensive entries were removed from the faker name lists, US state abbreviations were added, and person-name and street/location lists were corrected and broadened across `en`, `de`, `es`, `fr`, `ro` and `ar`.

</div><div class="h3-box" markdown="1">

#### Train TensorFlow-Based Annotators Without TensorFlow: Embedded Graphs for Classifier, Relation Extraction and Assertion Training

Training the TensorFlow-based annotators of Healthcare NLP used to require you to **generate a TensorFlow graph yourself** before calling `fit()`:

```python
from sparknlp_jsl.training import tf_graph

tf_graph.build("relation_extraction",
               build_params={"input_dim": 1149, "output_dim": 13, "hidden_layers": [300, 200],
                             "hidden_act": "relu", "batch_norm": 1, "hidden_act_l2": 1},
               model_location="/dbfs/re_graphs/",
               model_filename="graph_with_re_13_1149.pb")

re_approach = RelationExtractionApproach() \
    .setModelFile("/dbfs/re_graphs/graph_with_re_13_1149.pb")   # was required
```

That graph builder only runs on `tensorflow==2.12.0` together with `tensorflow-addons`, and **those packages can no longer be installed on current environments**: TensorFlow 2.12 has no wheels for Python 3.12+, and `tensorflow-addons` reached its end of life in May 2024. On recent Databricks runtimes and on freshly created Python environments the graph generation step simply failed, which blocked custom training entirely.

Starting with this release, **1,171 ready-to-use training graphs are shipped inside the Healthcare NLP JAR** and the annotators pick the right one automatically. No TensorFlow installation, no `tf_graph.build`, no `setModelFile`:

```python
re_approach = RelationExtractionApproach() \
    .setInputCols(["embeddings", "pos_tags", "train_ner_chunks", "dependencies"]) \
    .setOutputCol("relations") \
    .setLabelColumn("rel") \
    .setEpochsNumber(70) \
    .setBatchSize(200) \
    .setlearningRate(0.001) \
    .setFromEntity("begin1i", "end1i", "label1") \
    .setToEntity("begin2i", "end2i", "label2")

# fit() selects a suitable embedded graph on its own
re_model = re_approach.fit(train_data)
```

The selected graph is logged during training, so you always know what was used:

```
Selected graph: generic_classifier_dl/gc_1536_13.pb (input_dim: 1536, output_dim: 13) for a dataset with 1149 features and 13 classes.
```

**Supported Annotators**

These annotators now train with the embedded graphs, and their graph parameters became optional:

{:.table-model-big}

| Annotator | Embedded graph family |
| --- | --- |
| `GenericClassifierApproach` | multi layer perceptron `[300, 200]`, relu, softmax, cross entropy |
| `RelationExtractionApproach` | same as above |
| `FewShotAssertionClassifierApproach` | same as above |
| `GenericLogRegClassifierApproach` | logistic regression (no hidden layer), sigmoid, cross entropy |
| `FewShotClassifierApproach` (including the Finance and Legal variants) | same as above |
| `GenericSVMClassifierApproach` | linear, sigmoid, hinge loss |
| `AssertionDLApproach` (including the Finance and Legal variants) | 3-layer stacked bidirectional LSTM, 34 units |

`MedicalNerApproach` and `MedicalNerDLGraphChecker` already trained from embedded graphs; this release completes the picture for the remaining TensorFlow-based trainable annotators.

**What Is Shipped**

{:.table-model-big}

| Graph family | Resource folder | Graphs | Variations |
| --- | --- | --- | --- |
| Generic classifier / Relation extraction / Few-shot assertion | `generic_classifier_dl` | 360 | 15 feature vector sizes x 24 class counts |
| Logistic regression / Few-shot classifier | `logreg_classifier_dl` | 360 | 15 feature vector sizes x 24 class counts |
| SVM classifier | `svm_classifier_dl` | 360 | 15 feature vector sizes x 24 class counts |
| AssertionDL | `assertion_dl` | 91 | 7 embeddings dimensions x 13 class counts |
| **Total** | | **1,171** | |

- **Feature vector sizes** (dense families): 64, 128, 256, 384, 512, 768, 1024, 1536, 2048, 3072, 4096, 6144, 8192, 12288, 16384
- **Class counts** (dense families): every value from 2 to 20, plus 24, 32, 48, 64 and 100
- **Embeddings dimensions** (AssertionDL): 100, 128, 200, 300, 512, 768, 1024
- **Class counts** (AssertionDL): every value from 2 to 12, plus 16 and 20

This covers, for example, relation extraction with word embeddings up to 3072 dimensions (a relation feature vector is roughly `5 x embeddings_dim + 149`), few-shot classification on any common sentence embeddings model, and assertion status training with `embeddings_clinical` (200), GloVe (100 / 300) or BERT-family word embeddings (768 / 1024).

**How the Best Graph Is Selected**

When no graph path is given, the annotator inspects the training data and resolves the graph itself.

- **Dense classifier families.** Feature vectors and one-hot labels are zero padded to the graph dimensions, which is mathematically neutral, so any graph that is *large enough* trains to the same result. The resolver picks the **smallest graph with `input_dim >= number of features` and `output_dim >= number of classes`**, and always prefers an **exact class count** so the reported metrics are computed on the real classes only.
- **AssertionDL.** Word embeddings and labels are fed with their real dimensions, so the resolver requires an **exact match of both the embeddings dimension and the number of labels**. The embedded graphs accept a **dynamic sequence length**, so a single graph works with any `setMaxSentLen()` value.
- **Custom graphs still win.** `setModelFile()` (dense families) and `setGraphFile()` (AssertionDL) keep overriding everything, so existing training scripts and custom topologies keep working unchanged.
- **New parameter `setGraphFolder()`** is now available on the generic classifier family as well (it already existed for AssertionDL and MedicalNer). Point it to a folder of your own graphs and the same "smallest suitable graph" logic is applied there.

If nothing fits, training fails fast with an actionable message that contains the exact `tf_graph.build` call needed to create the missing graph, instead of an obscure TensorFlow error.

**Additional Improvements and Fixes**

- **`modelFile` is optional now** and empty by default; the automatic resolution is used instead. Explicitly set values behave exactly as before.
- **AssertionDL graphs accept a dynamic sequence length**, and the trained `AssertionDLModel` now inherits `maxSentLen` and `scopeWindow` from the approach (fixing a prediction-time mismatch between approach and model defaults, 250 vs 256).
- **AssertionDL graphs are no longer pinned to the CPU**, so assertion training can use a GPU when available.
- **Padded output units can no longer be predicted.** `GenericClassifierModel` and `RelationExtractionModel` restrict predictions to the trained labels, both for the top label and for `setMultiClass(True)` scores.
- **`sparknlp_jsl.training.tf_graph` fixes** for users who still build custom graphs: `logreg_classifier`, `svm_classifier` and `fewshot_classifier` now carry their complete default parameters, each graph is exported once instead of twice, and `TFGraphBuilder` no longer passes an invalid `max_seq_len` value for `assertion_dl`.

> The embedded graphs add about 260 MB to the JAR. They contain topologies and initializers only, no trained weights.

</div><div class="h3-box" markdown="1">

#### Updated 81 and Introduced 73 New Entity Resolver, ChunkMapper, and Pretrained Pipeline Models Across 16 Medical Coding Systems

This release delivers a comprehensive refresh of the terminology models of Healthcare NLP: **154 models across 16 medical coding systems** — 98 Entity Resolver models, 37 ChunkMapper models and 19 pretrained pipelines, of which **81 are updated and 73 are new**. Each system is trained on its latest official release, from SNOMED CT (US Edition 20260901), LOINC 2.83 and ICD-11 (WHO 2026-01) to RxNorm, NDC, CPT, HCPCS, HPO, HGNC, MeSH and NCIt.

- **Release-versioned model names.** Updated models of several systems now carry the source release in their name (e.g. `_20260901`, `_2_83`, `_2026`, `_202601`), so a pipeline can stay pinned to the terminology release it was built for.
- **Mappers for fast exact lookup.** ChunkMapper models map entity text or codes to target codes by dictionary lookup, as a lighter alternative to the resolvers and for crosswalks between coding systems.
- **Pretrained pipelines** package each resolver or mapper with the stages it needs, so it runs as a single `PretrainedPipeline` call.

**SNOMED CT**

Trained on the SNOMED CT US Edition 20260901 release.

{:.table-model-big}

| Model Name | Type | Embeddings | Description | Status |
|---|---|---|---|---|
| `sbiobertresolve_snomed_20260901` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical entities to the full, domain-unrestricted set of active SNOMED CT concepts | New |
| `sbiobertresolve_snomed_auxConcepts_20260901` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical entities to SNOMED CT auxiliary/descriptive concept codes | Updated |
| `sbiobertresolve_snomed_bodyStructure_20260901` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical entities to SNOMED CT body structure codes | Updated |
| `sbiobertresolve_snomed_conditions_20260901` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical entities to SNOMED CT condition/disorder codes | Updated |
| `sbiobertresolve_snomed_drug_20260901` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical entities to SNOMED CT drug/substance codes | Updated |
| `sbiobertresolve_snomed_findings_20260901` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical entities to SNOMED CT clinical finding codes | Updated |
| `sbiobertresolve_snomed_no_class_20260901` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical entities to SNOMED CT concepts not assigned to a specific class | Updated |
| `sbiobertresolve_snomed_procedures_measurements_20260901` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical entities to SNOMED CT procedure and measurement codes | Updated |
| `biolordresolve_snomed_20260901` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps clinical entities to the full, domain-unrestricted set of active SNOMED CT concepts | New |
| `biolordresolve_snomed_auxConcepts_20260901` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps clinical entities to SNOMED CT auxiliary/descriptive concept codes | New |
| `biolordresolve_snomed_bodyStructure_20260901` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps clinical entities to SNOMED CT body structure codes | New |
| `biolordresolve_snomed_conditions_20260901` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps clinical entities to SNOMED CT condition/disorder codes | New |
| `biolordresolve_snomed_drug_20260901` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps clinical entities to SNOMED CT drug/substance codes | New |
| `biolordresolve_snomed_findings_20260901` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps clinical entities to SNOMED CT clinical finding codes | New |
| `biolordresolve_snomed_no_class_20260901` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps clinical entities to SNOMED CT concepts not assigned to a specific class | New |
| `biolordresolve_snomed_procedures_measurements_20260901` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps clinical entities to SNOMED CT procedure and measurement codes | New |
| `bgeresolve_snomed_20260901` | Resolver | `bge_base_en_v1_5_onnx` | Maps clinical entities to the full, domain-unrestricted set of active SNOMED CT concepts | Updated |
| `bgeresolve_snomed_auxConcepts_20260901` | Resolver | `bge_base_en_v1_5_onnx` | Maps clinical entities to SNOMED CT auxiliary/descriptive concept codes | New |
| `bgeresolve_snomed_bodyStructure_20260901` | Resolver | `bge_base_en_v1_5_onnx` | Maps clinical entities to SNOMED CT body structure codes | New |
| `bgeresolve_snomed_conditions_20260901` | Resolver | `bge_base_en_v1_5_onnx` | Maps clinical entities to SNOMED CT condition/disorder codes | New |
| `bgeresolve_snomed_drug_20260901` | Resolver | `bge_base_en_v1_5_onnx` | Maps clinical entities to SNOMED CT drug/substance codes | New |
| `bgeresolve_snomed_findings_20260901` | Resolver | `bge_base_en_v1_5_onnx` | Maps clinical entities to SNOMED CT clinical finding codes | New |
| `bgeresolve_snomed_no_class_20260901` | Resolver | `bge_base_en_v1_5_onnx` | Maps clinical entities to SNOMED CT concepts not assigned to a specific class | New |
| `bgeresolve_snomed_procedures_measurements_20260901` | Resolver | `bge_base_en_v1_5_onnx` | Maps clinical entities to SNOMED CT procedure and measurement codes | New |
| `icd10cm_snomed_mapper_20260901` | Mapper | - | Maps ICD-10-CM codes to their corresponding SNOMED CT codes via dictionary lookup | Updated |
| `icdo_snomed_mapper_20260901` | Mapper | - | Maps ICD-O codes to their corresponding SNOMED CT codes via dictionary lookup | Updated |
| `snomed_icd10cm_mapper_20260901` | Mapper | - | Maps SNOMED CT codes to their corresponding ICD-10-CM codes via dictionary lookup | Updated |
| `snomed_icdo_mapper_20260901` | Mapper | - | Maps SNOMED CT codes to their corresponding ICD-O codes via dictionary lookup | Updated |
| `snomed_mapper_20260901` | Mapper | - | Maps clinical entities to their corresponding SNOMED CT codes via dictionary lookup | Updated |
| `sbiobertresolve_snomed_auxConcepts_pipeline_20260901` | Pipeline | - | End-to-end pipeline mapping clinical entities to SNOMED CT auxiliary/descriptive concept codes | Updated |
| `sbiobertresolve_snomed_bodyStructure_pipeline_20260901` | Pipeline | - | End-to-end pipeline mapping clinical entities to SNOMED CT body structure codes | Updated |
| `sbiobertresolve_snomed_conditions_pipeline_20260901` | Pipeline | - | End-to-end pipeline mapping clinical entities to SNOMED CT condition/disorder codes | Updated |
| `sbiobertresolve_snomed_drug_pipeline_20260901` | Pipeline | - | End-to-end pipeline mapping clinical entities to SNOMED CT drug/substance codes | Updated |
| `sbiobertresolve_snomed_findings_pipeline_20260901` | Pipeline | - | End-to-end pipeline mapping clinical entities to SNOMED CT clinical finding codes | Updated |
| `sbiobertresolve_snomed_no_class_pipeline_20260901` | Pipeline | - | End-to-end pipeline mapping clinical entities to SNOMED CT concepts not assigned to a specific class | New |
| `sbiobertresolve_snomed_pipeline_20260901` | Pipeline | - | End-to-end pipeline mapping clinical entities to the full, domain-unrestricted set of active SNOMED CT concepts | Updated |
| `sbiobertresolve_snomed_procedures_measurements_pipeline_20260901` | Pipeline | - | End-to-end pipeline mapping clinical entities to SNOMED CT procedure and measurement codes | Updated |
| `biolordresolve_snomed_pipeline_20260901` | Pipeline | - | End-to-end pipeline mapping clinical entities to the full, domain-unrestricted set of active SNOMED CT concepts | New |
| `bgeresolve_snomed_pipeline_20260901` | Pipeline | - | End-to-end pipeline mapping clinical entities to the full, domain-unrestricted set of active SNOMED CT concepts | Updated |
| `icd10cm_snomed_mapping_pipeline_20260901` | Pipeline | - | End-to-end pipeline mapping ICD-10-CM codes to their corresponding SNOMED CT codes | Updated |
| `icdo_snomed_mapping_pipeline_20260901` | Pipeline | - | End-to-end pipeline mapping ICD-O codes to their corresponding SNOMED CT codes | Updated |
| `snomed_icd10cm_mapping_pipeline_20260901` | Pipeline | - | End-to-end pipeline mapping SNOMED CT codes to their corresponding ICD-10-CM codes | Updated |
| `snomed_icdo_mapping_pipeline_20260901` | Pipeline | - | End-to-end pipeline mapping SNOMED CT codes to their corresponding ICD-O codes | Updated |
| `snomed_mapping_pipeline_20260901` | Pipeline | - | End-to-end pipeline mapping clinical entities to their corresponding SNOMED CT codes | New |

**LOINC**

Trained on the official LOINC 2.83 dataset.

{:.table-model-big}

| Model Name | Type | Embeddings | Description | Status |
|---|---|---|---|---|
| `sbiobertresolve_loinc_2_83` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical entities to LOINC codes | Updated |
| `sbiobertresolve_loinc_augmented_2_83` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical entities to LOINC codes, including non-numeric Part/Answer/Panel/Survey codes | Updated |
| `sbiobertresolve_loinc_numeric_2_83` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical entities to numeric, directly orderable/reportable LOINC codes | Updated |
| `sbiobertresolve_loinc_numeric_augmented_2_83` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical entities to numeric LOINC codes, augmented training corpus | Updated |
| `biolordresolve_loinc_2_83` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps clinical entities to LOINC codes | New |
| `biolordresolve_loinc_augmented_2_83` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps clinical entities to LOINC codes, including non-numeric Part/Answer/Panel/Survey codes | Updated |
| `biolordresolve_loinc_numeric_2_83` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps clinical entities to numeric, directly orderable/reportable LOINC codes | New |
| `biolordresolve_loinc_numeric_augmented_2_83` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps clinical entities to numeric LOINC codes, augmented training corpus | New |
| `bgeresolve_loinc_2_83` | Resolver | `bge_base_en_v1_5_onnx` | Maps clinical entities to LOINC codes | New |
| `bgeresolve_loinc_augmented_2_83` | Resolver | `bge_base_en_v1_5_onnx` | Maps clinical entities to LOINC codes, including non-numeric Part/Answer/Panel/Survey codes | New |
| `bgeresolve_loinc_numeric_2_83` | Resolver | `bge_base_en_v1_5_onnx` | Maps clinical entities to numeric, directly orderable/reportable LOINC codes | New |
| `bgeresolve_loinc_numeric_augmented_2_83` | Resolver | `bge_base_en_v1_5_onnx` | Maps clinical entities to numeric LOINC codes, augmented training corpus | New |
| `loinc_mapper_2_83` | Mapper | - | Maps clinical entities to LOINC codes via dictionary lookup | New |
| `loinc_numeric_mapper_2_83` | Mapper | - | Maps clinical entities to numeric LOINC codes via dictionary lookup | New |
| `sbiobertresolve_loinc_augmented_pipeline_2_83` | Pipeline | - | End-to-end pipeline mapping clinical entities to LOINC codes, including non-numeric Part/Answer/Panel/Survey codes | Updated |
| `sbiobertresolve_loinc_numeric_augmented_pipeline_2_83` | Pipeline | - | End-to-end pipeline mapping clinical entities to numeric LOINC codes, augmented training corpus | Updated |
| `sbiobertresolve_loinc_numeric_pipeline_2_83` | Pipeline | - | End-to-end pipeline mapping clinical entities to numeric LOINC codes | New |
| `sbiobertresolve_loinc_pipeline_2_83` | Pipeline | - | End-to-end pipeline mapping clinical entities to LOINC codes | New |

**ICD-10-CM**

Trained on the ICD-10-CM 20260401 (FY2026, effective April 1, 2026) code set.

{:.table-model-big}

| Model Name | Type | Embeddings | Description | Status |
|---|---|---|---|---|
| `sbiobertresolve_icd10cm_augmented` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical entities to ICD-10-CM codes, augmented with synonyms | Updated |
| `sbiobertresolve_icd10cm_augmented_billable_hcc` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical entities to ICD-10-CM codes, augmented with synonyms, with billable status and HCC score | Updated |
| `sbiobertresolve_icd10cm_generalised` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical entities to 3-character ICD-10-CM categories | Updated |
| `sbiobertresolve_icd10cm_generalised_augmented` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical entities to 3-character ICD-10-CM categories, augmented with synonyms | Updated |
| `sbiobertresolve_icd10cm_slim_billable_hcc` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical entities to ICD-10-CM codes (slim version), with billable status and HCC score | Updated |
| `sbiobertresolve_icd10cm_slim_normalized` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical entities to ICD-10-CM codes (slim version, normalized) | Updated |
| `sbertresolve_icd10cm_augmented` | Resolver | `sbert_jsl_medium_uncased` | Maps clinical entities to ICD-10-CM codes, augmented with synonyms | Updated |
| `sbertresolve_icd10cm_augmented_billable_hcc` | Resolver | `sbert_jsl_medium_uncased` | Maps clinical entities to ICD-10-CM codes, augmented with synonyms, with billable status and HCC score | Updated |
| `sbertresolve_icd10cm_slim_billable_hcc` | Resolver | `sbert_jsl_medium_uncased` | Maps clinical entities to ICD-10-CM codes (slim version), with billable status and HCC score | Updated |
| `biolordresolve_icd10cm_augmented_billable_hcc` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps clinical entities to ICD-10-CM codes, augmented with synonyms, with billable status and HCC score | Updated |
| `bgeresolve_icd10cm` | Resolver | `bge_base_en_v1_5_onnx` | Maps clinical entities to ICD-10-CM codes, augmented with synonyms | Updated |
| `icd10cm_billable_hcc_mapper` | Mapper | - | Maps an ICD-10-CM code to its billable status and HCC score | Updated |
| `icd10cm_generalised_mapper` | Mapper | - | Maps an ICD-10-CM code to its 3-character generalised category and chapter name | Updated |
| `icd10cm_mapper` | Mapper | - | Maps clinical entities to their corresponding ICD-10-CM codes via dictionary lookup | Updated |

**ICD-10-PCS**

Trained on the ICD-10-PCS 20260401 (FY2026, effective April 1, 2026) code set.

{:.table-model-big}

| Model Name | Type | Embeddings | Description | Status |
|---|---|---|---|---|
| `sbiobertresolve_icd10pcs` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps procedure entities to ICD-10-PCS codes | Updated |
| `sbiobertresolve_icd10pcs_augmented` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps procedure entities to ICD-10-PCS codes, augmented with synonyms | Updated |

**CMS-HCC**

Trained on the ICD-10-CM 20260401 release, with CMS-HCC (ESRD V24, 2026 midyear final).

{:.table-model-big}

| Model Name | Type | Embeddings | Description | Status |
|---|---|---|---|---|
| `sbiobertresolve_hcc_augmented` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical entities to CMS-HCC ESRD V24 risk-adjustment category codes | Updated |
| `sbertresolve_hcc_augmented` | Resolver | `sbert_jsl_medium_uncased` | Maps clinical entities to CMS-HCC ESRD V24 risk-adjustment category codes | Updated |

**ICD-11**

Trained on the WHO ICD-11 2026-01 release.

{:.table-model-big}

| Model Name | Type | Embeddings | Description | Status |
|---|---|---|---|---|
| `sbiobertresolve_icd11_202601` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical entities to ICD-11 codes | New |
| `sbiobertresolve_icd11_augmented_202601` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical entities to ICD-11 codes, synonym-augmented | New |
| `icd10_icd11_mapper_202601` | Mapper | - | Maps ICD-10 codes to their corresponding ICD-11 code(s) and relation type | New |
| `icd11_icd10_mapper_202601` | Mapper | - | Maps ICD-11 codes to their corresponding ICD-10 codes | New |
| `icd11_mapper_202601` | Mapper | - | Maps clinical entities to ICD-11 codes via dictionary lookup | New |

**ICD-O**

Trained on the ICD-O-3.2 2026 update dataset.

{:.table-model-big}

| Model Name | Type | Embeddings | Description | Status |
|---|---|---|---|---|
| `sbiobertresolve_icdo_augmented_2026` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical/oncology entities to ICD-O morphology/topography codes | Updated |
| `biolordresolve_icdo_augmented_2026` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps clinical/oncology entities to ICD-O morphology/topography codes | New |
| `bgeresolve_icdo_augmented_2026` | Resolver | `bge_base_en_v1_5_onnx` | Maps clinical/oncology entities to ICD-O morphology/topography codes | New |
| `icdo_mapper` | Mapper | - | Maps oncology entities to ICD-O codes via dictionary lookup | New |

**RxNorm**

Trained on the RxNorm 20260601 release.

{:.table-model-big}

| Model Name | Type | Embeddings | Description | Status |
|---|---|---|---|---|
| `sbiobertresolve_rxnorm_augmented_v2` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps drug entities to RxNorm codes | Updated |
| `biolordresolve_avg_rxnorm_augmented_v2` | Resolver | `mpnet_embeddings_biolord_2023` | Maps drug entities to RxNorm codes | Updated |
| `biolordresolve_rxnorm_augmented_v2` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps drug entities to RxNorm codes | Updated |
| `bgeresolve_rxnorm` | Resolver | `bge_base_en_v1_5_onnx` | Maps drug entities to RxNorm codes | Updated |
| `medembed_base_rxnorm_augmented` | Resolver | `bge_medembed_base_v0_1` | Maps drug entities to RxNorm codes | Updated |
| `medembed_large_rxnorm_augmented` | Resolver | `bge_medembed_large_v0_1` | Maps drug entities to RxNorm codes | New |
| `rxnorm_mapper` | Mapper | - | Maps drug entities to RxNorm codes via dictionary lookup | Updated |

**NDC**

Trained on the openFDA NDC Directory (release 2026-07-22).

{:.table-model-big}

| Model Name | Type | Embeddings | Description | Status |
|---|---|---|---|---|
| `sbiobertresolve_ndc` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical drug entities to NDC codes | Updated |
| `biolordresolve_ndc` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps clinical drug entities to NDC codes | New |
| `bgeresolve_ndc` | Resolver | `bge_base_en_v1_5_onnx` | Maps clinical drug entities to NDC codes | New |
| `drug_brandname_ndc_mapper` | Mapper | - | Maps drug brand names to NDC codes | Updated |
| `hcpcs_ndc_mapper` | Mapper | - | Maps HCPCS codes to their corresponding NDC codes and brand names | Updated |
| `ndc_drug_brandname_mapper` | Mapper | - | Maps NDC codes to their corresponding drug brand names | Updated |
| `ndc_hcpcs_mapper` | Mapper | - | Maps NDC codes to their corresponding HCPCS codes and descriptions | Updated |
| `ndc_mapper` | Mapper | - | Maps drug entities extracted from clinical text to NDC codes | New |

**ATC**

Trained on the WHO ATC-DDD dataset (release 2026-04-25).

{:.table-model-big}

| Model Name | Type | Embeddings | Description | Status |
|---|---|---|---|---|
| `sbiobertresolve_atc` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps drug entities to ATC codes | Updated |
| `biolordresolve_atc` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps drug entities to ATC codes | New |
| `bgeresolve_atc` | Resolver | `bge_base_en_v1_5_onnx` | Maps drug entities to ATC codes | New |
| `atc_mapper` | Mapper | - | Maps drug entities to ATC codes via dictionary lookup | New |

**CPT**

Trained on CPT 2026 data, further augmented by John Snow Labs for broader coverage.

> ⚠️ CPT models are available only to users with a valid AMA license. Contact support@johnsnowlabs.com for access.

{:.table-model-big}

| Model Name | Type | Embeddings | Description | Status |
|---|---|---|---|---|
| `sbiobertresolve_cpt_augmented` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical procedure entities to CPT codes | Updated |
| `sbiobertresolve_cpt_procedures_measurements_augmented` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical procedure and measurement entities to CPT codes | Updated |
| `biolordresolve_cpt_augmented` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps clinical procedure entities to CPT codes | New |
| `biolordresolve_cpt_procedures_measurements_augmented` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps clinical procedure and measurement entities to CPT codes | Updated |
| `bgeresolve_cpt_augmented` | Resolver | `bge_base_en_v1_5_onnx` | Maps clinical procedure entities to CPT codes | New |
| `bgeresolve_cpt_procedures_measurements_augmented` | Resolver | `bge_base_en_v1_5_onnx` | Maps clinical procedure and measurement entities to CPT codes | New |
| `cpt_mapper` | Mapper | - | Maps procedure, test, and treatment entities to CPT codes via exact-match lookup | Updated |

**HCPCS**

Trained on the CMS HCPCS Level II Alpha-Numeric master file (release 20260701).

{:.table-model-big}

| Model Name | Type | Embeddings | Description | Status |
|---|---|---|---|---|
| `sbiobertresolve_hcpcs` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical entities to HCPCS codes | Updated |
| `biolordresolve_hcpcs` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps clinical entities to HCPCS codes | New |
| `bgeresolve_hcpcs` | Resolver | `bge_base_en_v1_5_onnx` | Maps clinical entities to HCPCS codes | New |
| `hcpcs_mapper` | Mapper | - | Maps clinical entities to HCPCS codes via dictionary lookup | New |

**HPO**

Trained on the Human Phenotype Ontology (HPO) 2026-06-23 release.

{:.table-model-big}

| Model Name | Type | Embeddings | Description | Status |
|---|---|---|---|---|
| `sbiobertresolve_HPO` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical phenotype entities to HPO codes | Updated |
| `biolordresolve_HPO` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps clinical phenotype entities to HPO codes | New |
| `bgeresolve_HPO` | Resolver | `bge_base_en_v1_5_onnx` | Maps clinical phenotype entities to HPO codes | New |
| `gene_hpo_code_mapper` | Mapper | - | Maps genes to their associated HPO code(s) | Updated |
| `hpo_code_eom_mapper` | Mapper | - | Maps HPO codes to their associated Elements of Morphology id(s) | Updated |
| `hpo_code_gene_disease_mapper` | Mapper | - | Maps HPO codes to associated genes and their related phenotypes | Updated |
| `hpo_code_gene_mapper` | Mapper | - | Maps HPO codes to their associated gene(s) | Updated |
| `hpo_disease_mapper` | Mapper | - | Maps HPO codes to their associated disease id(s) and name(s) (OMIM, Orphanet, DECIPHER) | New |
| `hpo_mapper` | Mapper | - | Maps phenotype entities to HPO codes via dictionary lookup | Updated |
| `hpo_parent_mapper` | Mapper | - | Maps HPO codes to their full ancestor chain in the HPO hierarchy | Updated |
| `hpo_synonym_mapper` | Mapper | - | Maps phenotype entities to their exact, related, broad, and narrow synonyms | Updated |

**HGNC**

Trained on the HGNC monthly release dated 2026-08-04.

{:.table-model-big}

| Model Name | Type | Embeddings | Description | Status |
|---|---|---|---|---|
| `sbiobertresolve_hgnc_2026` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps gene entities to HGNC codes using current approved gene symbols and names | Updated |
| `sbiobertresolve_hgnc_augmented_2026` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps gene entities to HGNC codes, including alias and previous gene symbols and names | New |
| `biolordresolve_hgnc_2026` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps gene entities to HGNC codes using current approved gene symbols and names | New |
| `biolordresolve_hgnc_augmented_2026` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps gene entities to HGNC codes, including alias and previous gene symbols and names | New |
| `bgeresolve_hgnc_2026` | Resolver | `bge_base_en_v1_5_onnx` | Maps gene entities to HGNC codes using current approved gene symbols and names | New |
| `bgeresolve_hgnc_augmented_2026` | Resolver | `bge_base_en_v1_5_onnx` | Maps gene entities to HGNC codes, including alias and previous gene symbols and names | New |
| `hgnc_code_symbol_mapper_2026` | Mapper | - | Maps HGNC codes to their current approved gene symbol | New |
| `hgnc_mapper_2026` | Mapper | - | Maps gene mentions to HGNC codes via dictionary lookup | New |
| `hgnc_mapper_augmented_2026` | Mapper | - | Maps gene mentions, including alias and previous symbols/names, to HGNC codes | New |
| `hgnc_symbol_code_mapper_2026` | Mapper | - | Maps current approved gene symbols to their HGNC code | New |

**MeSH**

Trained on the MeSH 2026 dataset.

{:.table-model-big}

| Model Name | Type | Embeddings | Description | Status |
|---|---|---|---|---|
| `sbiobertresolve_mesh_2026` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical/veterinary entities to MeSH codes | Updated |
| `sbiobertresolve_mesh_augmented_2026` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical/veterinary entities to MeSH codes (Athena-augmented) | Updated |
| `sbiobertresolve_mesh_veterinary_2026` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps veterinary-focused entities to MeSH codes | Updated |
| `biolordresolve_mesh_2026` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps clinical/veterinary entities to MeSH codes | New |
| `biolordresolve_mesh_augmented_2026` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps clinical/veterinary entities to MeSH codes (Athena-augmented) | New |
| `biolordresolve_mesh_veterinary_2026` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps veterinary-focused entities to MeSH codes | New |
| `bgeresolve_mesh_2026` | Resolver | `bge_base_en_v1_5_onnx` | Maps clinical/veterinary entities to MeSH codes | New |
| `bgeresolve_mesh_augmented_2026` | Resolver | `bge_base_en_v1_5_onnx` | Maps clinical/veterinary entities to MeSH codes (Athena-augmented) | New |
| `bgeresolve_mesh_veterinary_2026` | Resolver | `bge_base_en_v1_5_onnx` | Maps veterinary-focused entities to MeSH codes | New |
| `mesh_mapper_2026` | Mapper | - | Maps clinical/veterinary entities to MeSH codes via dictionary lookup | New |

**NCIt**

Trained on the NCI Thesaurus dataset (July 28, 2026 release).

{:.table-model-big}

| Model Name | Type | Embeddings | Description | Status |
|---|---|---|---|---|
| `sbiobertresolve_ncit` | Resolver | `sbiobert_base_cased_mli_onnx` | Maps clinical entities to NCIt codes | Updated |
| `biolordresolve_ncit` | Resolver | `mpnet_embeddings_biolord_2023_c` | Maps clinical entities to NCIt codes | New |
| `bgeresolve_ncit` | Resolver | `bge_base_en_v1_5_onnx` | Maps clinical entities to NCIt codes | New |
| `ncit_mapper` | Mapper | - | Maps clinical entities to NCIt codes via dictionary lookup | New |

*Example* (entity resolution — `sbiobertresolve_icd11_202601`):

```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("word_embeddings")

ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM"])

c2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

icd11_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd11_202601", "en", "clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(stages=[
    document_assembler, sentenceDetectorDL, tokenizer, word_embeddings,
    ner, ner_converter, c2doc, sbert_embedder, icd11_resolver
])

data = spark.createDataFrame([[
    "The patient has a history of type 2 diabetes mellitus and essential hypertension, "
    "and was recently diagnosed with Parkinson disease."
]]).toDF("text")

result = resolver_pipeline.fit(data).transform(data)
```

*Result*

| ner_chunk | entity | icd11_code | resolution |
|---|---|---|---|
| type 2 diabetes mellitus | PROBLEM | 5A11 | type 2 diabetes mellitus |
| essential hypertension | PROBLEM | BA00 | essential hypertension |
| Parkinson disease | PROBLEM | 8A00.0 | parkinson disease |

*Example* (code-level mapping — `icd11_mapper_202601`):

```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_clinical = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM"])

icd11_mapper = ChunkMapperModel.pretrained("icd11_mapper_202601", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["icd11_code"])\
    .setLowerCase(True)

pipeline = Pipeline(stages=[
    document_assembler, sentence_detector, tokenizer, word_embeddings,
    ner_clinical, ner_converter, icd11_mapper
])

data = spark.createDataFrame([
    ["cholera"], ["parkinson disease"], ["type 2 diabetes mellitus"],
    ["essential hypertension"], ["actinic keratosis"]
]).toDF("text")

result = pipeline.fit(data).transform(data)
```

*Result*

| text | icd11_code |
|---|---|
| cholera | 1A00 |
| parkinson disease | 8A00.0 |
| type 2 diabetes mellitus | 5A11 |
| essential hypertension | BA00 |
| actinic keratosis | EK90.0, XH36H6 |

`actinic keratosis` is a genuine WHO title collision — two different codes (`EK90.0`, a skin disease, and `XH36H6`, a chapter-X extension code) share the exact same official title, so the model correctly returns both rather than silently picking one.


</div><div class="h3-box" markdown="1">

#### Medical Terminology Mapping Benchmark: Healthcare NLP Resolvers vs. General-Purpose LLMs

Healthcare NLP resolvers were compared with five general-purpose LLMs on mapping clinical phrases to exact codes in SNOMED CT, RxNorm, ICD-10-CM, and ICD-O. Each system has 110 items: 100 terms whose gold codes were confirmed active in the current release, plus 10 currency items (5 codes added in the current release and 5 retired since the prior one). Every tool received the same bare phrase closed-book, with no tools, web search, or database access, and was scored on top-1 exact code match.

The resolvers under test were `sbiobertresolve_snomed_auxConcepts_20260901` (SNOMED CT 20260901), `sbiobertresolve_rxnorm_augmented_v2` (RxNorm 20260601), `sbiobertresolve_icd10cm_augmented` (ICD-10-CM 20260401), and `sbiobertresolve_icdo_augmented_2026` (ICD-O 3.2, 2026 update).

{:.table-model-big}

| Tool | SNOMED CT | RxNorm | ICD-10-CM | ICD-O 3.2 |
|---|---|---|---|---|
| Healthcare NLP | 87.3% | 91.8% | 95.5% | 96.4% |
| Claude Opus 5 | 76.4% | 63.6% | 94.5% | 93.6% |
| Claude Sonnet 5 | 55.5% | 52.7% | 87.3% | 90.9% |
| Claude Fable 5 | 80.0% | 82.7% | 93.6% | 92.7% |
| GPT-5.6 | 41.8% | 35.5% | 92.7% | 47.3% |
| Gemini 3.6 Flash | 51.8% | 40.9% | 90.9% | 90.9% |

The resolvers score highest on all four systems. The gap is largest where codes are long numeric identifiers: 7.3 points over the best LLM on SNOMED CT and 9.1 points on RxNorm. On ICD-10-CM and ICD-O, where codes are short and partly mnemonic, the best LLM comes within 1.0 and 2.8 points. The LLM errors fall into three groups: a related concept of the wrong type, codes added after the model's training cutoff, and codes that do not exist in the vocabulary.

The full methodology is on the [benchmark page](https://nlp.johnsnowlabs.com/docs/en/benchmark).

</div><div class="h3-box" markdown="1">

#### Oncology NER and Entity Resolver Pipelines Speed Benchmark

This benchmark times one clinical NER pipeline and five Sentence Entity Resolver pipelines end to end on the same input: 1,000 rows built from 220 i2b2 de-identification surrogate notes (4,360,197 characters, 780,532 tokens), repartitioned to 128. All runs used a Microsoft Azure Standard D64ds v5 VM (64 vCPUs, 256 GiB RAM, no GPU). The timer wraps the Parquet write, which is the action that runs the full pipeline.

{:.table-model-big}

| Pipeline | Type | Total chunks | Elapsed | Rows/sec | Tokens/sec |
|---|---|---|---|---|---|
| `ner_oncology_wip` | NER | 53,513 | 57.3 sec | 17.4 | 13,614.5 |
| `sbiobertresolve_icdo_base` | Resolver | 1,792 | 1 min 18.8 sec | 12.7 | 9,905.4 |
| `sbiobertresolve_atc` | Resolver | 13,814 | 1 min 26.3 sec | 11.6 | 9,049.0 |
| `sbiobertresolve_snomed_findings` | Resolver | 28,459 | 3 min 43.8 sec | 4.5 | 3,487.8 |
| `sbiobertresolve_hgnc_2026` | Resolver | 17,172 | 6 min 22.3 sec | 2.6 | 2,041.6 |
| `sbluebertresolve_loinc_uncased` | Resolver | 17,172 | 6 min 38.6 sec | 2.5 | 1,958.4 |

Each resolver pipeline runs the NER pass first and then embeds every extracted chunk before the nearest-neighbor lookup, so the sentence embedding stage accounts for most of the resolver time. The HGNC and LOINC pipelines resolve the same 17,172 chunks, which puts their resolver stages side by side at 382.3 and 398.6 seconds. For faster CPU runs, use the ONNX embeddings (`sbiobert_base_cased_mli_onnx`); the [CPU benchmarking](https://nlp.johnsnowlabs.com/docs/en/benchmark#cpu-benchmarking) results compare the TensorFlow, ONNX, and OpenVINO backends.

</div><div class="h3-box" markdown="1">

#### New Blog Posts & Technical Deep Dives

- [High-Accuracy Clinical Term Mapping to Standard Medical Terminologies (ICD-10, RxNorm, SNOMED, and 90+ vocabularies) with John Snow Labs' Medical Language Models](https://medium.com/john-snow-labs/high-accuracy-clinical-term-mapping-to-standard-medical-terminologies-icd-10-rxnorm-snomed-and-3a0333c95b4c): This post compares Healthcare NLP resolvers with Claude Opus 5, Claude Sonnet 5, Claude Fable 5, GPT-5.6, and Gemini 3.6 Flash on 110 closed-book items each for SNOMED CT, RxNorm, ICD-10-CM, and ICD-O. The resolvers reach 87.3%, 91.8%, 95.5%, and 96.4% top-1 accuracy, the highest score on every system. It also explains how the training data behind each resolver is built and how resolvers and their companion mapper models divide the work between free text and known codes.
- [Clinical de-identification benchmarks 2026: John Snow Labs against OpenAI, Databricks, Presidio, and LLM APIs](https://www.johnsnowlabs.com/clinical-de-identification-benchmarks-2026-john-snow-labs-against-openai-databricks-presidio-and-llm-apis/): This post collects the 2026 clinical de-identification comparisons in one place, each with its methodology and reproduction links. On 1,479 expert-annotated PHI chunks, Healthcare NLP reaches 0.96 PHI F1, against 0.91 for Claude Opus 4.8, 0.89 for GPT-5.5, 0.86 for Gemini 3.1 Pro, and 0.71 for Databricks `ai_mask()`. The same pipeline reaches 0.98 micro F1 on the official 2014 i2b2 test set, and the post adds published results for Presidio (0.60 to 0.85 F1 in two peer-reviewed studies) and the OpenAI Privacy Filter (0.55 F1).
- [Benchmarking Databricks ai_mask on clinical de-identification: 0.71 PHI F1](https://www.johnsnowlabs.com/benchmarking-databricks-ai_mask-on-clinical-de-identification-0-71-phi-f1/): This post scores the Databricks `ai_mask()` SQL function on the same expert-annotated corpus and evaluation code as the comparisons above. It reaches 0.71 PHI F1, with recall ranging from 0.35 on contact identifiers to 0.85 on ID numbers, and requesting the 18 labels of a HIPAA-aligned taxonomy lowers PHI F1 to 0.61. The post also compares output formats, cross-document consistency, and audit records with the Healthcare NLP de-identification pipeline, which runs on the same Databricks cluster through the Databricks Marketplace.

</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For Making Healthcare NLP Easier To Navigate And Understand

- New [HL7 v2 De-Identification](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.15.HL7v2_DeIdentification.ipynb) Notebook
  This notebook covers the two pretrained `Hl7v2DeIdentification` models: `hl7v2_deidentification_base` for structured PHI fields, and `hl7v2_deidentification_free_text`, which also de-identifies the `OBX-5` and `NTE-3` narrative fields through a de-identification pipeline. Both models ship with a default PHI map of 280 Terser paths. The examples run both models on synthetic `ADT^A01` and `ORU^R01` messages and cover obfuscate and mask modes, custom path rules with segment occurrences such as `NK1(2)-2-1`, extending the default map, and processing through Spark DataFrames, single messages and message lists. A final section de-identifies 4 real-world HL7 v2 sample files with each model.

</div><div class="h3-box" markdown="1">

#### Bug Fixes & Stability Improvements

- **Model-loading temp-file cleanup.** Model loading and archive extraction created temporary files and directories that were not always cleaned up. Previously, loading a 1 GB ONNX model could leave approximately 2 GB of temporary files on disk; ONNX temp files are now removed reliably.
- **ONNX CUDA preload recovery.** ONNX session creation is now delegated to the OS, making GPU/CUDA preload more robust and recovering gracefully from preload issues.
- **Batched ZeroShotNer decoding.** Fixed incorrect decoding of `ZeroShotNer` outputs when running in batches.
- **`DocumentFiltererByNER` empty inputs.** Fixed handling of empty inputs so the annotator no longer fails on documents without matching entities.
- **PretrainedZeroShotMultiTask fixes.** Corrected `begin`/`end` offsets and added enum support in `PretrainedZeroShotMultiTask`, fixed an empty getter/setter, and enabled lazy output typing in `MultiAnnotationSplitter`.

</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.

+ `sbiobertresolve_snomed_20260901`
+ `sbiobertresolve_snomed_auxConcepts_20260901`
+ `sbiobertresolve_snomed_bodyStructure_20260901`
+ `sbiobertresolve_snomed_conditions_20260901`
+ `sbiobertresolve_snomed_drug_20260901`
+ `sbiobertresolve_snomed_findings_20260901`
+ `sbiobertresolve_snomed_no_class_20260901`
+ `sbiobertresolve_snomed_procedures_measurements_20260901`
+ `biolordresolve_snomed_20260901`
+ `biolordresolve_snomed_auxConcepts_20260901`
+ `biolordresolve_snomed_bodyStructure_20260901`
+ `biolordresolve_snomed_conditions_20260901`
+ `biolordresolve_snomed_drug_20260901`
+ `biolordresolve_snomed_findings_20260901`
+ `biolordresolve_snomed_no_class_20260901`
+ `biolordresolve_snomed_procedures_measurements_20260901`
+ `bgeresolve_snomed_20260901`
+ `bgeresolve_snomed_auxConcepts_20260901`
+ `bgeresolve_snomed_bodyStructure_20260901`
+ `bgeresolve_snomed_conditions_20260901`
+ `bgeresolve_snomed_drug_20260901`
+ `bgeresolve_snomed_findings_20260901`
+ `bgeresolve_snomed_no_class_20260901`
+ `bgeresolve_snomed_procedures_measurements_20260901`
+ `icd10cm_snomed_mapper_20260901`
+ `icdo_snomed_mapper_20260901`
+ `snomed_icd10cm_mapper_20260901`
+ `snomed_icdo_mapper_20260901`
+ `snomed_mapper_20260901`
+ `sbiobertresolve_snomed_auxConcepts_pipeline_20260901`
+ `sbiobertresolve_snomed_bodyStructure_pipeline_20260901`
+ `sbiobertresolve_snomed_conditions_pipeline_20260901`
+ `sbiobertresolve_snomed_drug_pipeline_20260901`
+ `sbiobertresolve_snomed_findings_pipeline_20260901`
+ `sbiobertresolve_snomed_no_class_pipeline_20260901`
+ `sbiobertresolve_snomed_pipeline_20260901`
+ `sbiobertresolve_snomed_procedures_measurements_pipeline_20260901`
+ `biolordresolve_snomed_pipeline_20260901`
+ `bgeresolve_snomed_pipeline_20260901`
+ `icd10cm_snomed_mapping_pipeline_20260901`
+ `icdo_snomed_mapping_pipeline_20260901`
+ `snomed_icd10cm_mapping_pipeline_20260901`
+ `snomed_icdo_mapping_pipeline_20260901`
+ `snomed_mapping_pipeline_20260901`
+ `sbiobertresolve_loinc_2_83`
+ `sbiobertresolve_loinc_augmented_2_83`
+ `sbiobertresolve_loinc_numeric_2_83`
+ `sbiobertresolve_loinc_numeric_augmented_2_83`
+ `biolordresolve_loinc_2_83`
+ `biolordresolve_loinc_augmented_2_83`
+ `biolordresolve_loinc_numeric_2_83`
+ `biolordresolve_loinc_numeric_augmented_2_83`
+ `bgeresolve_loinc_2_83`
+ `bgeresolve_loinc_augmented_2_83`
+ `bgeresolve_loinc_numeric_2_83`
+ `bgeresolve_loinc_numeric_augmented_2_83`
+ `loinc_mapper_2_83`
+ `loinc_numeric_mapper_2_83`
+ `sbiobertresolve_loinc_augmented_pipeline_2_83`
+ `sbiobertresolve_loinc_numeric_augmented_pipeline_2_83`
+ `sbiobertresolve_loinc_numeric_pipeline_2_83`
+ `sbiobertresolve_loinc_pipeline_2_83`
+ `sbiobertresolve_icd10cm_augmented`
+ `sbiobertresolve_icd10cm_augmented_billable_hcc`
+ `sbiobertresolve_icd10cm_generalised`
+ `sbiobertresolve_icd10cm_generalised_augmented`
+ `sbiobertresolve_icd10cm_slim_billable_hcc`
+ `sbiobertresolve_icd10cm_slim_normalized`
+ `sbertresolve_icd10cm_augmented`
+ `sbertresolve_icd10cm_augmented_billable_hcc`
+ `sbertresolve_icd10cm_slim_billable_hcc`
+ `biolordresolve_icd10cm_augmented_billable_hcc`
+ `bgeresolve_icd10cm`
+ `icd10cm_billable_hcc_mapper`
+ `icd10cm_generalised_mapper`
+ `icd10cm_mapper`
+ `sbiobertresolve_icd10pcs`
+ `sbiobertresolve_icd10pcs_augmented`
+ `sbiobertresolve_hcc_augmented`
+ `sbertresolve_hcc_augmented`
+ `sbiobertresolve_icd11_202601`
+ `sbiobertresolve_icd11_augmented_202601`
+ `icd10_icd11_mapper_202601`
+ `icd11_icd10_mapper_202601`
+ `icd11_mapper_202601`
+ `sbiobertresolve_icdo_augmented_2026`
+ `biolordresolve_icdo_augmented_2026`
+ `bgeresolve_icdo_augmented_2026`
+ `icdo_mapper`
+ `sbiobertresolve_rxnorm_augmented_v2`
+ `biolordresolve_avg_rxnorm_augmented_v2`
+ `biolordresolve_rxnorm_augmented_v2`
+ `bgeresolve_rxnorm`
+ `medembed_base_rxnorm_augmented`
+ `medembed_large_rxnorm_augmented`
+ `rxnorm_mapper`
+ `sbiobertresolve_ndc`
+ `biolordresolve_ndc`
+ `bgeresolve_ndc`
+ `drug_brandname_ndc_mapper`
+ `hcpcs_ndc_mapper`
+ `ndc_drug_brandname_mapper`
+ `ndc_hcpcs_mapper`
+ `ndc_mapper`
+ `sbiobertresolve_atc`
+ `biolordresolve_atc`
+ `bgeresolve_atc`
+ `atc_mapper`
+ `sbiobertresolve_cpt_augmented`
+ `sbiobertresolve_cpt_procedures_measurements_augmented`
+ `biolordresolve_cpt_augmented`
+ `biolordresolve_cpt_procedures_measurements_augmented`
+ `bgeresolve_cpt_augmented`
+ `bgeresolve_cpt_procedures_measurements_augmented`
+ `cpt_mapper`
+ `sbiobertresolve_hcpcs`
+ `biolordresolve_hcpcs`
+ `bgeresolve_hcpcs`
+ `hcpcs_mapper`
+ `sbiobertresolve_HPO`
+ `biolordresolve_HPO`
+ `bgeresolve_HPO`
+ `gene_hpo_code_mapper`
+ `hpo_code_eom_mapper`
+ `hpo_code_gene_disease_mapper`
+ `hpo_code_gene_mapper`
+ `hpo_disease_mapper`
+ `hpo_mapper`
+ `hpo_parent_mapper`
+ `hpo_synonym_mapper`
+ `sbiobertresolve_hgnc_2026`
+ `sbiobertresolve_hgnc_augmented_2026`
+ `biolordresolve_hgnc_2026`
+ `biolordresolve_hgnc_augmented_2026`
+ `bgeresolve_hgnc_2026`
+ `bgeresolve_hgnc_augmented_2026`
+ `hgnc_code_symbol_mapper_2026`
+ `hgnc_mapper_2026`
+ `hgnc_mapper_augmented_2026`
+ `hgnc_symbol_code_mapper_2026`
+ `sbiobertresolve_mesh_2026`
+ `sbiobertresolve_mesh_augmented_2026`
+ `sbiobertresolve_mesh_veterinary_2026`
+ `biolordresolve_mesh_2026`
+ `biolordresolve_mesh_augmented_2026`
+ `biolordresolve_mesh_veterinary_2026`
+ `bgeresolve_mesh_2026`
+ `bgeresolve_mesh_augmented_2026`
+ `bgeresolve_mesh_veterinary_2026`
+ `mesh_mapper_2026`
+ `sbiobertresolve_ncit`
+ `biolordresolve_ncit`
+ `bgeresolve_ncit`
+ `ncit_mapper`
+ `city_matcher`
+ `ip_matcher`
+ `sbiobertresolve_icd11_mental_health`
+ `zeroshot_ner_jsl_large_assertiondl_pipeline`
+ `zeroshot_ner_jsl_large_fewshotassertion_pipeline`
+ `zeroshot_ner_jsl_large_pipeline`
+ `zeroshot_ner_jsl_medium_assertiondl_pipeline`
+ `zeroshot_ner_jsl_medium_pipeline`
+ `ner_cancer_registry`
+ `ner_cancer_registry_pipeline`
+ `hl7v2_deidentification_base`
+ `hl7v2_deidentification_free_text`

</div><div class="h3-box" markdown="1">

## Versions

</div>
{%- include docs-healthcare-pagination.html -%}
