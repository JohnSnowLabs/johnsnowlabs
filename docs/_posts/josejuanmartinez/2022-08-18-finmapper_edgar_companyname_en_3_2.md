---
layout: model
title: Mapping Company Names to Edgar Database
author: John Snow Labs
name: finmapper_edgar_companyname
date: 2022-08-18
tags: [en, finance, companies, edgar, data, augmentation, licensed]
task: Chunk Mapping
language: en
nav_key: models
edition: Finance NLP 1.0.0
spark_version: 3.0
supported: true
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This Chunk Mapper model allows you to, given a detected Organization with any NER model, augment it with information available in the SEC Edgar database. Some of the fields included in this Chunk Mapper are:
- IRS number
- Sector
- Former names
- Address, Phone, State
- Dates where the company submitted filings
- etc.

IMPORTANT: Chunk Mappers work with exact matches, so before using Chunk Mapping, you need to carry out Company Name Normalization to get how the company name is stored in Edgar. To do this, use Entity Linking, more especifically the `finel_edgar_companynames` model, with the Organization Name extracted by any NER model. You will get  the normalized version (by Edgar standards) of the name, which you can send to this model for data augmentation.

## Predicted Entities



{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/finance/FIN_LEG_COMPANY_AUGMENTATION/){:.button.button-orange}
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finmapper_edgar_companyname_en_1.0.0_3.2_1660817326595.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finmapper_edgar_companyname_en_1.0.0_3.2_1660817326595.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
documentAssembler = nlp.DocumentAssembler()\
        .setInputCol("text")\
        .setOutputCol("document")

tokenizer = nlp.Tokenizer()\
        .setInputCols(["document"])\
        .setOutputCol("token")

embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en") \
        .setInputCols(["document", "token"]) \
        .setOutputCol("embeddings")

ner_model = finance.NerModel.pretrained("finner_orgs_prods_alias", "en", "finance/models")\
        .setInputCols(["document", "token", "embeddings"])\
        .setOutputCol("ner")

ner_converter = nlp.NerConverter()\
        .setInputCols(["document","token","ner"])\
        .setOutputCol("ner_chunk")

# Optional: To normalize the ORG name using NASDAQ data before the mapping
##########################################################################
chunkToDoc = nlp.Chunk2Doc()\
        .setInputCols("ner_chunk")\
        .setOutputCol("ner_chunk_doc")

chunk_embeddings = nlp.UniversalSentenceEncoder.pretrained("tfhub_use", "en") \
      .setInputCols("ner_chunk_doc") \
      .setOutputCol("sentence_embeddings")
    
use_er_model = finance.SentenceEntityResolverModel.pretrained("finel_edgar_company_name", "en", "finance/models") \
      .setInputCols(["ner_chunk_doc", "sentence_embeddings"]) \
      .setOutputCol("normalized")\
      .setDistanceFunction("EUCLIDEAN")
##########################################################################

cm = finance.ChunkMapperModel()\
      .pretrained("finmapper_edgar_companyname", "en", "finance/models")\
      .setInputCols(["normalized"])\
      .setOutputCol("mappings")  # or ner_chunk for non normalized versions

nlpPipeline = nlp.Pipeline(stages=[
        documentAssembler,
        tokenizer,
        embeddings,
        ner_model,
        ner_converter,
        chunkToDoc,
        chunk_embeddings,
        use_er_model,
        cm
])

text = """NIKE Inc is an American multinational corporation that is engaged in the design, development, manufacturing, and worldwide marketing and sales of footwear, 
apparel, equipment, accessories, and services"""

test_data = spark.createDataFrame([[text]]).toDF("text")

model = nlpPipeline.fit(test_data)

lp = nlp.LightPipeline(model)

lp.annotate(text)
```

</div>

## Results

```bash
{"mappings": [["labeled_dependency", 0, 22, "Jamestown Invest 1, LLC", {"sentence": "0", "chunk": "0", "entity": "Jamestown Invest 1, LLC", "relation": "name", "all_relations": ""}], ["labeled_dependency", 0, 22, "REAL ESTATE INVESTMENT TRUSTS [6798]", {"sentence": "0", "chunk": "0", "entity": "Jamestown Invest 1, LLC", "relation": "sic", "all_relations": ""}], ["labeled_dependency", 0, 22, "6798", {"sentence": "0", "chunk": "0", "entity": "Jamestown Invest 1, LLC", "relation": "sic_code", "all_relations": ""}], ["labeled_dependency", 0, 22, "831529368", {"sentence": "0", "chunk": "0", "entity": "Jamestown Invest 1, LLC", "relation": "irs_number", "all_relations": ""}], ["labeled_dependency", 0, 22, "1231", {"sentence": "0", "chunk": "0", "entity": "Jamestown Invest 1, LLC", "relation": "fiscal_year_end", "all_relations": ""}], ["labeled_dependency", 0, 22, "GA", {"sentence": "0", "chunk": "0", "entity": "Jamestown Invest 1, LLC", "relation": "state_location", "all_relations": ""}], ["labeled_dependency", 0, 22, "DE", {"sentence": "0", "chunk": "0", "entity": "Jamestown Invest 1, LLC", "relation": "state_incorporation", "all_relations": ""}], ["labeled_dependency", 0, 22, "PONCE CITY MARKET", {"sentence": "0", "chunk": "0", "entity": "Jamestown Invest 1, LLC", "relation": "business_street", "all_relations": ""}], ["labeled_dependency", 0, 22, "ATLANTA", {"sentence": "0", "chunk": "0", "entity": "Jamestown Invest 1, LLC", "relation": "business_city", "all_relations": ""}], ["labeled_dependency", 0, 22, "GA", {"sentence": "0", "chunk": "0", "entity": "Jamestown Invest 1, LLC", "relation": "business_state", "all_relations": ""}], ["labeled_dependency", 0, 22, "30308", {"sentence": "0", "chunk": "0", "entity": "Jamestown Invest 1, LLC", "relation": "business_zip", "all_relations": ""}], ["labeled_dependency", 0, 22, "7708051000", {"sentence": "0", "chunk": "0", "entity": "Jamestown Invest 1, LLC", "relation": "business_phone", "all_relations": ""}], ["labeled_dependency", 0, 22, "Jamestown Atlanta Invest 1, LLC", {"sentence": "0", "chunk": "0", "entity": "Jamestown Invest 1, LLC", "relation": "former_name", "all_relations": ""}], ["labeled_dependency", 0, 22, "20180824", {"sentence": "0", "chunk": "0", "entity": "Jamestown Invest 1, LLC", "relation": "former_name_date", "all_relations": ""}], ["labeled_dependency", 0, 22, "2019-11-21", {"sentence": "0", "chunk": "0", "entity": "Jamestown Invest 1, LLC", "relation": "date", "all_relations": "2019-10-24:::2019-11-25:::2019-11-12:::2022-01-13:::2022-03-31:::2022-04-11:::2022-07-12:::2022-06-30:::2021-01-14:::2021-04-06:::2021-03-31:::2021-04-28:::2021-06-30:::2021-09-10:::2021-09-22:::2021-09-30:::2021-10-08:::2020-03-16:::2021-12-30:::2020-04-06:::2020-04-29:::2020-06-12:::2020-07-20:::2020-07-07:::2020-07-28:::2020-07-31:::2020-09-09:::2020-09-25:::2020-10-08:::2020-11-12"}], ["labeled_dependency", 0, 22, "1751158", {"sentence": "0", "chunk": "0", "entity": "Jamestown Invest 1, LLC", "relation": "company_id", "all_relations": ""}]]}
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finmapper_edgar_companyname|
|Type:|finance|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|11.0 MB|

## References

Manually scrapped Edgar Database
