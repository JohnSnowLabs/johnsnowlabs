---
layout: docs
header: true
seotitle: Spark NLP | John Snow Labs
title: Enterprise NLP Annotators
permalink: /docs/en/licensed_annotators
key: docs-licensed-annotators
modify_date: "2020-08-10"
use_language_switcher: "Python-Scala"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

A Spark NLP Enterprise license includes access to unique annotators.
At the [Spark NLP Workshop](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/tutorials/Certification_Trainings) you can see different types of annotators in action.

By clicking on any annotator, you will see different sections:
- The `Approach`, or class to train models.
- The `Model`, to infer using pretrained models.

Also, for most of the annotators, you will find examples for the different enterprise libraries:
- Healthcare NLP
- Finance NLP
- Legal NLP

Check out the [Spark NLP Annotators page](https://nlp.johnsnowlabs.com/docs/en/annotators) for more information on how to read this page.

</div>

## Available Annotators

{:.table-model-big}
|Annotators|Description|
|---|---|
{% include templates/licensed_table_entry.md  name="AnnotationMerger" summary="Merge annotations from different pipeline steps that have the same annotation type into a unified annotation."%}
{% include templates/licensed_table_entry.md  name="AssertionChunkConverter" summary="AssertionChunkConverter annotator uses both begin and end indices of the tokens as input to add a more robust metadata to the chunk column in a way that improves the reliability of the indices and avoid loss of data."%}
{% include templates/licensed_table_entry.md  name="AssertionDL" summary="AssertionDL is a deep Learning based approach used to extract Assertion Status from extracted entities and text."%}
{% include templates/licensed_table_entry.md  name="AssertionFilterer" summary="Filters entities coming from ASSERTION type annotations and returns the CHUNKS."%}
{% include templates/licensed_table_entry.md  name="AssertionLogReg" summary="Logistic Regression is used to extract Assertion Status from extracted entities and text."%}
{% include templates/licensed_table_entry.md  name="AverageEmbeddings" summary="Computes the mean of vector embeddings for two sentences of equal size, producing a unified representation"%}
{% include templates/licensed_table_entry.md  name="BertForSequenceClassification" summary="Can load Bert Models with sequence classification/regression head on top (a linear layer on top of the pooled output) e.g. for multi-class document classification tasks."%}
{% include templates/licensed_table_entry.md  name="BertForTokenClassifier" summary="Can load Bert Models with a token classification head on top (a linear layer on top of the hidden-states output) for Named-Entity-Recognition (NER) tasks."%}
{% include templates/licensed_table_entry.md  name="BertSentenceChunkEmbeddings" summary="This annotator combines sentence and NER chunk embeddings to enhance resolution codes, leveraging contextual information in the embeddings for more precise results. It takes sentence context and NER chunks as input and produces embeddings for each chunk, facilitating input for the resolution model."%}
{% include templates/licensed_table_entry.md  name="Chunk2Token" summary="A feature transformer that converts the input array of strings (annotatorType CHUNK) into an array of chunk-based tokens (annotatorType TOKEN)."%}
{% include templates/licensed_table_entry.md  name="ChunkConverter" summary="This annotator merges NER-detected entities with RegexMatcher-based rules for unified processing in the pipeline."%}
{% include templates/licensed_table_entry.md  name="ChunkEntityResolver" summary="Returns a normalized entity for a particular trained ontology / curated dataset (e.g. clinical ICD-10, RxNorm, SNOMED; financial SEC's EDGAR database,  etc)."%}
{% include templates/licensed_table_entry.md  name="ChunkFilterer" summary="Filters entities coming from CHUNK annotations."%}
{% include templates/licensed_table_entry.md  name="ChunkKeyPhraseExtraction" summary="Uses Bert Sentence Embeddings to determine the most relevant key phrases describing a text."%}
{% include templates/licensed_table_entry.md  name="ChunkMapper" summary="We can use ChunkMapper to map entities with their associated code/reference based on pre-defined dictionaries."%}
{% include templates/licensed_table_entry.md  name="ChunkMapperFilterer" summary="Annotator to be used after `ChunkMapper` that allows to filter chunks based on the results of the mapping, whether it was successful or failed."%}
{% include templates/licensed_table_entry.md  name="ChunkMerge" summary="Merges entities coming from different CHUNK annotations."%}
{% include templates/licensed_table_entry.md  name="ChunkSentenceSplitter" summary="Annotator can split the documents into chunks according to separators given as `CHUNK` columns. It is useful when you need to perform different models or analysis in different sections of your document"%}
{% include templates/licensed_table_entry.md  name="ContextualParser" summary="Extracts entity from a document based on user defined rules."%}
{% include templates/licensed_table_entry.md  name="DateNormalizer" summary="This annotator transforms date mentions to a common standard format: YYYY/MM/DD. It is useful when using data from different sources, some times from different countries that has different formats to represent dates."%}
{% include templates/licensed_table_entry.md  name="DeIdentification" summary="Deidentifies Input Annotations of types DOCUMENT, TOKEN and CHUNK, by either masking or obfuscating the given CHUNKS."%}
{% include templates/licensed_table_entry.md  name="DistilBertForSequenceClassification" summary="Can load DistilBERT Models with sequence classification/regression head on top (a linear layer on top of the pooled output) e.g. for multi-class document classification tasks."%}
{% include templates/licensed_table_entry.md  name="Doc2ChunkInternal" summary="Converts `DOCUMENT`, `TOKEN` typed annotations into `CHUNK` type with the contents of a `chunkCol`."%}
{% include templates/licensed_table_entry.md  name="DocMapper" summary="Uses the text representation of document annotations to map clinical codes to other codes or relevant information. "%}
{% include templates/licensed_table_entry.md  name="DocumentFiltererByClassifier" summary="This annotator sorts documents based on classifier results. It uses white and black lists, allowing or blocking specific outcomes. It can be case-sensitive or case-insensitive for broader matching. This tool efficiently organizes documents based on classifier outcomes."%}
{% include templates/licensed_table_entry.md  name="DocumentHashCoder" summary="This annotator swaps dates in a document column with hash codes from another column, creating a new column with shifted day information. The subsequent `DeIdentification` annotator anonymizes the document, incorporating the altered dates. "%}
{% include templates/licensed_table_entry.md  name="DocumentLogRegClassifier" summary="Classifies documents with a Logarithmic Regression algorithm."%}
{% include templates/licensed_table_entry.md  name="DocumentMLClassifier" summary="classifies documents with a Logarithmic Regression algorithm."%}
{% include templates/licensed_table_entry.md  name="DrugNormalizer" summary="Annotator which normalizes raw text from documents, e.g. scraped web pages or xml documents."%}
{% include templates/licensed_table_entry.md  name="EntityChunkEmbeddings" summary="Entity Chunk Embeddings uses BERT Sentence embeddings to compute a weighted average vector represention of related entity chunks."%}
{% include templates/licensed_table_entry.md  name="FeaturesAssembler" summary="Collects features from different columns."%}
{% include templates/licensed_table_entry.md  name="FewShotClassifier" summary="This Annotator specifically target few-shot classification tasks, which involve training a model to make accurate predictions with limited labeled data."%}
{% include templates/licensed_table_entry.md  name="Flattener" summary="`Flattener` annotator in Spark NLP converts annotation results into a simplified DataFrame format for easier analysis and interpretation."%}
{% include templates/licensed_table_entry.md  name="GenericClassifier" summary="Creates a generic single-label classifier which uses pre-generated Tensorflow graphs."%}
{% include templates/licensed_table_entry.md  name="GenericLogRegClassifier" summary="Is a derivative of GenericClassifier which implements a multinomial logistic regression."%}
{% include templates/licensed_table_entry.md  name="GenericSVMClassifier" summary="Creates a generic single-label classifier which uses pre-generated Tensorflow graphs."%}
{% include templates/licensed_table_entry.md  name="InternalDocumentSplitter" summary="This annotator splits large documents into small documents."%}
{% include templates/licensed_table_entry.md  name="IOBTagger" summary="Merges token tags and NER labels from chunks in the specified format."%}
{% include templates/licensed_table_entry.md  name="NameChunkObfuscator" summary="This annotator allows to transform a dataset with an Input Annotation of type CHUNK, into its obfuscated version of by obfuscating the given CHUNKS."%}
{% include templates/licensed_table_entry.md  name="NerChunker" summary="Extracts phrases that fits into a known pattern using the NER tags."%}
{% include templates/licensed_table_entry.md  name="NerConverterInternal" summary="Converts a IOB or IOB2 representation of NER to a user-friendly one, by associating the tokens of recognized entities and their label."%}
{% include templates/licensed_table_entry.md  name="NerDisambiguator" summary="Links words of interest, such as names of persons, locations and companies, from an input text document to a corresponding unique entity in a target Knowledge Base (KB)."%}
{% include templates/licensed_table_entry.md  name="NerModel" summary="This Named Entity recognition annotator is a generic NER model based on Neural Networks."%}
{% include templates/licensed_table_entry.md  name="NerQuestionGenerator" summary="This annotator takes an NER chunk (obtained by, e.g., `NerConverterInternal`) and generates a questions based on two entity types, a pronoun and a strategy."%}
{% include templates/licensed_table_entry.md  name="QuestionAnswering" summary="GPT-based model for answering questions given a context."%}
{% include templates/licensed_table_entry.md  name="RegexMatcherInternal" summary="`RegexMatcherInternal` matches predefined regex patterns with entities in text, allowing for flexible entity recognition based on user-defined rules."%}
{% include templates/licensed_table_entry.md  name="ReIdentification" summary="Reidentifies obfuscated entities by DeIdentification."%}
{% include templates/licensed_table_entry.md  name="RelationExtraction" summary="Extracts and classifies instances of relations between named entities."%}
{% include templates/licensed_table_entry.md  name="RelationExtractionDL" summary="Extracts and classifies instances of relations between named entities."%}
{% include templates/licensed_table_entry.md  name="RENerChunksFilter" summary="Filters and outputs combinations of relations between extracted entities, for further processing."%}
{% include templates/licensed_table_entry.md  name="Replacer" summary="This annotator allows to replace entities in the original text with the ones extracted by the annotators `NameChunkObfuscatorApproach` or `DateNormalizer`."%}
{% include templates/licensed_table_entry.md  name="Resolution2Chunk" summary="This annotator is responsible for converting the annotations generated by entity resolver models (typically labeled as ENTITY) into a format compatible with subsequent stages of the pipeline, such as the ChunkMapperModel."%}
{% include templates/licensed_table_entry.md  name="ResolverMerger" summary="This annotator is provide the ability to merge sentence enitity resolver and chunk mapper model output columns."%}
{% include templates/licensed_table_entry.md  name="Router" summary="This annotator is provide the ability to split an output of an annotator for a selected metadata field and the value for that field."%}
{% include templates/licensed_table_entry.md  name="SentenceEntityResolver" summary="Returns the normalized entity for a particular trained ontology / curated dataset (e.g. clinical ICD-10, RxNorm, SNOMED; financial SEC's EDGAR database,  etc) based on sentence embeddings."%}
{% include templates/licensed_table_entry.md  name="Summarizer" summary="Helps to quickly summarize complex medical information."%}
{% include templates/licensed_table_entry.md  name="TextGenerator" summary="Uses the basic BioGPT model to perform various tasks related to medical text abstraction."%}
{% include templates/licensed_table_entry.md  name="TextMatcherInternal" summary="This annotator match exact phrases provided in a file against a Document."%}
{% include templates/licensed_table_entry.md  name="TFGraphBuilder" summary="Creates Tensorflow graphs."%}
{% include templates/licensed_table_entry.md  name="WindowedSentenceModel" summary="This annotator that helps you to merge the previous and following sentences of a given piece of text, so that you add the context surrounding them."%}
{% include templates/licensed_table_entry.md  name="ZeroShotNerModel" summary="This is a zero-shot named entity recognition using `RoBertaForQuestionAnswering`. It identifies entities across diverse data without domain-specific fine-tuning."%}
{% include templates/licensed_table_entry.md  name="ZeroShotRelationExtractionModel" summary="This annotator implements zero-shot binary relations extraction by utilizing `BERT` transformer models trained on the NLI (Natural Language Inference) task."%}

<script> {% include scripts/approachModelSwitcher.js %} </script>

{% assign parent_path = "en/licensed_annotator_entries" %}

{% for file in site.static_files %}
  {% if file.path contains parent_path %}
    {% assign file_name = file.path | remove:  parent_path | remove:  "/" | prepend: "licensed_annotator_entries/" %}
    {% include_relative {{ file_name }} %}
  {% endif %}
{% endfor %}
