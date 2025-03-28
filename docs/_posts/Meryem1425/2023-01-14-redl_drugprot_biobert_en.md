---
layout: model
title: Extract relations between drugs and proteins (ReDL)
author: John Snow Labs
name: redl_drugprot_biobert
date: 2023-01-14
tags: [relation_extraction, clinical, en, licensed, tensorflow]
task: Relation Extraction
language: en
nav_key: models
edition: Healthcare NLP 4.2.4
spark_version: 3.0
supported: true
engine: tensorflow
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Detect interactions between chemical compounds/drugs and genes/proteins using BERT by classifying whether a specified semantic relation holds between a chemical and gene entities within a sentence or document. The entity labels used during training were derived from the custom NER model created by our team for the DrugProt corpus. These include CHEMICAL for chemical compounds/drugs, GENE for genes/proteins and GENE_AND_CHEMICAL for entity mentions of type GENE and of type CHEMICAL that overlap (such as enzymes and small peptides). The relation categories from the DrugProt corpus were condensed from 13 categories to 10 categories due to low numbers of examples for certain categories. This merging process involved grouping the SUBSTRATE_PRODUCT-OF and SUBSTRATE relation categories together and grouping the AGONIST-ACTIVATOR, AGONIST-INHIBITOR and AGONIST relation categories together.

## Predicted Entities

`INHIBITOR`, `DIRECT-REGULATOR`, `SUBSTRATE`, `ACTIVATOR`, `INDIRECT-UPREGULATOR`, `INDIRECT-DOWNREGULATOR`, `ANTAGONIST`, `PRODUCT-OF`, `PART-OF`, `AGONIST`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/10.Clinical_Relation_Extraction.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/redl_drugprot_biobert_en_4.2.4_3.0_1673736326031.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/redl_drugprot_biobert_en_4.2.4_3.0_1673736326031.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

In the table below, `redl_drugprot_biobert` RE model, its labels, optimal NER model, and meaningful relation pairs are illustrated.


|        RE MODEL       |                                                                                 RE MODEL LABES                                                                                |       NER MODEL       | RE PAIRS                                                                           |
|:---------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------:|------------------------------------------------------------------------------------|
| redl_drugprot_biobert | INHIBITOR, <br>DIRECT-REGULATOR, <br>SUBSTRATE, <br>ACTIVATOR, <br>INDIRECT-UPREGULATOR, <br>INDIRECT-DOWNREGULATOR, <br>ANTAGONIST, <br>PRODUCT-OF, <br>PART-OF, <br>AGONIST | ner_drugprot_clinical | [“checmical-gene”, <br>“chemical-gene_and_chemical”, <br>“gene_and_chemical-gene”] |

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documenter = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentencer = SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentences")

tokenizer = Tokenizer()\
    .setInputCols(["sentences"])\
    .setOutputCol("tokens")

words_embedder = WordEmbeddingsModel()\
    .pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentences", "tokens"])\
    .setOutputCol("embeddings")

drugprot_ner_tagger = MedicalNerModel.pretrained("ner_drugprot_clinical", "en", "clinical/models")\
    .setInputCols("sentences", "tokens", "embeddings")\
    .setOutputCol("ner_tags")   

ner_converter = NerConverterInternal()\
    .setInputCols(["sentences", "tokens", "ner_tags"])\
    .setOutputCol("ner_chunks")

pos_tagger = PerceptronModel()\
    .pretrained("pos_clinical", "en", "clinical/models")\
    .setInputCols(["sentences", "tokens"])\
    .setOutputCol("pos_tags")

dependency_parser = DependencyParserModel()\
    .pretrained("dependency_conllu", "en")\
    .setInputCols(["sentences", "pos_tags", "tokens"])\
    .setOutputCol("dependencies")

# Set a filter on pairs of named entities which will be treated as relation candidates
drugprot_re_ner_chunk_filter = RENerChunksFilter()\
    .setInputCols(["ner_chunks", "dependencies"])\
    .setOutputCol("re_ner_chunks")\
    .setMaxSyntacticDistance(4)
    # .setRelationPairs(['CHEMICAL-GENE'])

drugprot_re_Model = RelationExtractionDLModel()\
    .pretrained('redl_drugprot_biobert', "en", "clinical/models")\
    .setPredictionThreshold(0.9)\
    .setInputCols(["re_ner_chunks", "sentences"])\
    .setOutputCol("relations")

pipeline = Pipeline(stages=[documenter, sentencer, tokenizer, words_embedder, drugprot_ner_tagger, ner_converter, pos_tagger, dependency_parser, drugprot_re_ner_chunk_filter, drugprot_re_Model])

text='''Lipid specific activation of the murine P4-ATPase Atp8a1 (ATPase II). The asymmetric transbilayer distribution of phosphatidylserine (PS) in the mammalian plasma membrane and secretory vesicles is maintained, in part, by an ATP-dependent transporter. This aminophospholipid "flippase" selectively transports PS to the cytosolic leaflet of the bilayer and is sensitive to vanadate, Ca(2+), and modification by sulfhydryl reagents. Although the flippase has not been positively identified, a subfamily of P-type ATPases has been proposed to function as transporters of amphipaths, including PS and other phospholipids. A candidate PS flippase ATP8A1 (ATPase II), originally isolated from bovine secretory vesicles, is a member of this subfamily based on sequence homology to the founding member of the subfamily, the yeast protein Drs2, which has been linked to ribosomal assembly, the formation of Golgi-coated vesicles, and the maintenance of PS asymmetry. To determine if ATP8A1 has biochemical characteristics consistent with a PS flippase, a murine homologue of this enzyme was expressed in insect cells and purified. The purified Atp8a1 is inactive in detergent micelles or in micelles containing phosphatidylcholine, phosphatidic acid, or phosphatidylinositol, is minimally activated by phosphatidylglycerol or phosphatidylethanolamine (PE), and is maximally activated by PS. The selectivity for PS is dependent upon multiple elements of the lipid structure. Similar to the plasma membrane PS transporter, Atp8a1 is activated only by the naturally occurring sn-1,2-glycerol isomer of PS and not the sn-2,3-glycerol stereoisomer. Both flippase and Atp8a1 activities are insensitive to the stereochemistry of the serine headgroup. Most modifications of the PS headgroup structure decrease recognition by the plasma membrane PS flippase. Activation of Atp8a1 is also reduced by these modifications; phosphatidylserine-O-methyl ester, lysophosphatidylserine, glycerophosphoserine, and phosphoserine, which are not transported by the plasma membrane flippase, do not activate Atp8a1. Weakly translocated lipids (PE, phosphatidylhydroxypropionate, and phosphatidylhomoserine) are also weak Atp8a1 activators. However, N-methyl-phosphatidylserine, which is transported by the plasma membrane flippase at a rate equivalent to PS, is incapable of activating Atp8a1 activity. These results indicate that the ATPase activity of the secretory granule Atp8a1 is activated by phospholipids binding to a specific site whose properties (PS selectivity, dependence upon glycerol but not serine, stereochemistry, and vanadate sensitivity) are similar to, but distinct from, the properties of the substrate binding site of the plasma membrane flippase.'''

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val documenter = new DocumentAssembler() 
    .setInputCol("text") 
    .setOutputCol("document")

val sentencer = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentences")

val tokenizer = new Tokenizer()
    .setInputCols("sentences")
    .setOutputCol("tokens")

val words_embedder = WordEmbeddingsModel()
    .pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentences", "tokens"))
    .setOutputCol("embeddings")

val drugprot_ner_tagger = MedicalNerModel.pretrained("ner_drugprot_clinical", "en", "clinical/models")
    .setInputCols(Array("sentences", "tokens", "embeddings"))
    .setOutputCol("ner_tags") 

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentences", "tokens", "ner_tags"))
    .setOutputCol("ner_chunks")

val pos_tagger = PerceptronModel()
    .pretrained("pos_clinical", "en", "clinical/models") 
    .setInputCols(Array("sentences", "tokens"))
    .setOutputCol("pos_tags")

val dependency_parser = DependencyParserModel()
    .pretrained("dependency_conllu", "en")
    .setInputCols(Array("sentences", "pos_tags", "tokens"))
    .setOutputCol("dependencies")

// Set a filter on pairs of named entities which will be treated as relation candidates
val drugprot_re_ner_chunk_filter = new RENerChunksFilter()
    .setInputCols(Array("ner_chunks", "dependencies"))
    .setMaxSyntacticDistance(10)
    .setOutputCol("re_ner_chunks")
    // .setRelationPairs(Array("CHEMICAL-GENE"))

// This model can also be trained on document-level relations - in which case, while predicting, use "document" instead of "sentence" as input.
val drugprot_re_Model = RelationExtractionDLModel()
    .pretrained("redl_drugprot_biobert", "en", "clinical/models")
    .setPredictionThreshold(0.9)
    .setInputCols(Array("re_ner_chunks", "sentences"))
    .setOutputCol("relations")

val pipeline = new Pipeline().setStages(Array(documenter, sentencer, tokenizer, words_embedder, drugprot_ner_tagger, ner_converter, pos_tagger, dependency_parser, drugprot_re_ner_chunk_filter, drugprot_re_Model))

val data = Seq("""Lipid specific activation of the murine P4-ATPase Atp8a1 (ATPase II). The asymmetric transbilayer distribution of phosphatidylserine (PS) in the mammalian plasma membrane and secretory vesicles is maintained, in part, by an ATP-dependent transporter. This aminophospholipid "flippase" selectively transports PS to the cytosolic leaflet of the bilayer and is sensitive to vanadate, Ca(2+), and modification by sulfhydryl reagents. Although the flippase has not been positively identified, a subfamily of P-type ATPases has been proposed to function as transporters of amphipaths, including PS and other phospholipids. A candidate PS flippase ATP8A1 (ATPase II), originally isolated from bovine secretory vesicles, is a member of this subfamily based on sequence homology to the founding member of the subfamily, the yeast protein Drs2, which has been linked to ribosomal assembly, the formation of Golgi-coated vesicles, and the maintenance of PS asymmetry. To determine if ATP8A1 has biochemical characteristics consistent with a PS flippase, a murine homologue of this enzyme was expressed in insect cells and purified. The purified Atp8a1 is inactive in detergent micelles or in micelles containing phosphatidylcholine, phosphatidic acid, or phosphatidylinositol, is minimally activated by phosphatidylglycerol or phosphatidylethanolamine (PE), and is maximally activated by PS. The selectivity for PS is dependent upon multiple elements of the lipid structure. Similar to the plasma membrane PS transporter, Atp8a1 is activated only by the naturally occurring sn-1,2-glycerol isomer of PS and not the sn-2,3-glycerol stereoisomer. Both flippase and Atp8a1 activities are insensitive to the stereochemistry of the serine headgroup. Most modifications of the PS headgroup structure decrease recognition by the plasma membrane PS flippase. Activation of Atp8a1 is also reduced by these modifications; phosphatidylserine-O-methyl ester, lysophosphatidylserine, glycerophosphoserine, and phosphoserine, which are not transported by the plasma membrane flippase, do not activate Atp8a1. Weakly translocated lipids (PE, phosphatidylhydroxypropionate, and phosphatidylhomoserine) are also weak Atp8a1 activators. However, N-methyl-phosphatidylserine, which is transported by the plasma membrane flippase at a rate equivalent to PS, is incapable of activating Atp8a1 activity. These results indicate that the ATPase activity of the secretory granule Atp8a1 is activated by phospholipids binding to a specific site whose properties (PS selectivity, dependence upon glycerol but not serine, stereochemistry, and vanadate sensitivity) are similar to, but distinct from, the properties of the substrate binding site of the plasma membrane flippase.""").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```


{:.nlu-block}
```python
import nlu
nlu.load("en.relation.drugprot").predict("""Lipid specific activation of the murine P4-ATPase Atp8a1 (ATPase II). The asymmetric transbilayer distribution of phosphatidylserine (PS) in the mammalian plasma membrane and secretory vesicles is maintained, in part, by an ATP-dependent transporter. This aminophospholipid "flippase" selectively transports PS to the cytosolic leaflet of the bilayer and is sensitive to vanadate, Ca(2+), and modification by sulfhydryl reagents. Although the flippase has not been positively identified, a subfamily of P-type ATPases has been proposed to function as transporters of amphipaths, including PS and other phospholipids. A candidate PS flippase ATP8A1 (ATPase II), originally isolated from bovine secretory vesicles, is a member of this subfamily based on sequence homology to the founding member of the subfamily, the yeast protein Drs2, which has been linked to ribosomal assembly, the formation of Golgi-coated vesicles, and the maintenance of PS asymmetry. To determine if ATP8A1 has biochemical characteristics consistent with a PS flippase, a murine homologue of this enzyme was expressed in insect cells and purified. The purified Atp8a1 is inactive in detergent micelles or in micelles containing phosphatidylcholine, phosphatidic acid, or phosphatidylinositol, is minimally activated by phosphatidylglycerol or phosphatidylethanolamine (PE), and is maximally activated by PS. The selectivity for PS is dependent upon multiple elements of the lipid structure. Similar to the plasma membrane PS transporter, Atp8a1 is activated only by the naturally occurring sn-1,2-glycerol isomer of PS and not the sn-2,3-glycerol stereoisomer. Both flippase and Atp8a1 activities are insensitive to the stereochemistry of the serine headgroup. Most modifications of the PS headgroup structure decrease recognition by the plasma membrane PS flippase. Activation of Atp8a1 is also reduced by these modifications; phosphatidylserine-O-methyl ester, lysophosphatidylserine, glycerophosphoserine, and phosphoserine, which are not transported by the plasma membrane flippase, do not activate Atp8a1. Weakly translocated lipids (PE, phosphatidylhydroxypropionate, and phosphatidylhomoserine) are also weak Atp8a1 activators. However, N-methyl-phosphatidylserine, which is transported by the plasma membrane flippase at a rate equivalent to PS, is incapable of activating Atp8a1 activity. These results indicate that the ATPase activity of the secretory granule Atp8a1 is activated by phospholipids binding to a specific site whose properties (PS selectivity, dependence upon glycerol but not serine, stereochemistry, and vanadate sensitivity) are similar to, but distinct from, the properties of the substrate binding site of the plasma membrane flippase.""")
```

</div>

## Results

```bash
+---------+-----------------+-------------+-----------+--------------------+-----------------+-------------+-----------+--------------------+----------+
| relation|          entity1|entity1_begin|entity1_end|              chunk1|          entity2|entity2_begin|entity2_end|              chunk2|confidence|
+---------+-----------------+-------------+-----------+--------------------+-----------------+-------------+-----------+--------------------+----------+
|ACTIVATOR|             GENE|           33|         48|    murine P4-ATPase|             GENE|           50|         55|              Atp8a1|0.95415354|
|ACTIVATOR|             GENE|           50|         55|              Atp8a1|             GENE|           58|         66|           ATPase II| 0.9600417|
|SUBSTRATE|         CHEMICAL|          114|        131|  phosphatidylserine|GENE_AND_CHEMICAL|          224|        248|ATP-dependent tra...| 0.9931178|
|SUBSTRATE|         CHEMICAL|          134|        135|                  PS|GENE_AND_CHEMICAL|          224|        248|ATP-dependent tra...| 0.9978284|
|SUBSTRATE|GENE_AND_CHEMICAL|          256|        282|aminophospholipid...|         CHEMICAL|          308|        309|                  PS| 0.9968598|
|SUBSTRATE|             GENE|          443|        450|            flippase|         CHEMICAL|          589|        590|                  PS| 0.9991992|
|ACTIVATOR|         CHEMICAL|         1201|       1219| phosphatidylcholine|         CHEMICAL|         1222|       1238|   phosphatidic acid|0.96227807|
|ACTIVATOR|         CHEMICAL|         1244|       1263|phosphatidylinositol|         CHEMICAL|         1292|       1311|phosphatidylglycerol|0.93301487|
|ACTIVATOR|         CHEMICAL|         1244|       1263|phosphatidylinositol|         CHEMICAL|         1316|       1339|phosphatidylethan...|0.93579245|
|ACTIVATOR|         CHEMICAL|         1292|       1311|phosphatidylglycerol|         CHEMICAL|         1316|       1339|phosphatidylethan...| 0.9583067|
|ACTIVATOR|         CHEMICAL|         1292|       1311|phosphatidylglycerol|         CHEMICAL|         1342|       1343|                  PE| 0.9603738|
|ACTIVATOR|         CHEMICAL|         1316|       1339|phosphatidylethan...|         CHEMICAL|         1342|       1343|                  PE| 0.9596611|
|ACTIVATOR|         CHEMICAL|         1316|       1339|phosphatidylethan...|         CHEMICAL|         1377|       1378|                  PS| 0.9832381|
|ACTIVATOR|         CHEMICAL|         1342|       1343|                  PE|         CHEMICAL|         1377|       1378|                  PS|  0.981709|
|ACTIVATOR|             GENE|         1511|       1516|              Atp8a1|         CHEMICAL|         1563|       1577|     sn-1,2-glycerol|0.99146277|
|ACTIVATOR|             GENE|         1511|       1516|              Atp8a1|         CHEMICAL|         1589|       1590|                  PS| 0.9842391|
|ACTIVATOR|             GENE|         1511|       1516|              Atp8a1|         CHEMICAL|         1604|       1618|     sn-2,3-glycerol|0.98676455|
|  PART-OF|             GENE|         1639|       1646|            flippase|         CHEMICAL|         1716|       1721|              serine| 0.9470919|
|SUBSTRATE|         CHEMICAL|         1936|       1957|lysophosphatidyls...|             GENE|         2050|       2057|            flippase|0.98919815|
|SUBSTRATE|         CHEMICAL|         1960|       1979|glycerophosphoserine|             GENE|         2050|       2057|            flippase| 0.9857248|
+---------+-----------------+-------------+-----------+--------------------+-----------------+-------------+-----------+--------------------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|redl_drugprot_biobert|
|Compatibility:|Healthcare NLP 4.2.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|401.7 MB|

## References

This model was trained on the DrugProt corpus.

## Benchmarking

```bash
label                  recall  precision         f1  support
ACTIVATOR               0.885      0.776      0.827      235
AGONIST                 0.810      0.925      0.864      137
ANTAGONIST              0.970      0.919      0.944      199
DIRECT-REGULATOR        0.836      0.901      0.867      403
INDIRECT-DOWNREGULATOR  0.885      0.850      0.867      313
INDIRECT-UPREGULATOR    0.844      0.887      0.865      270
INHIBITOR               0.947      0.937      0.942      1083
PART-OF                 0.939      0.889      0.913      247
PRODUCT-OF              0.697      0.953      0.805      145
SUBSTRATE               0.912      0.884      0.898      468
Avg                     0.873      0.892      0.879       -
Weighted-Avg            0.897      0.899      0.897       -
```