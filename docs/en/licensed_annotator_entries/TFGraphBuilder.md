{%- capture title -%}
TFGraphBuilder
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}

`TFGraphBuilder` annotator can be used to create graphs in the model training pipeline. `TFGraphBuilder` inspects the data and creates the proper graph if a suitable version of TensorFlow (>= 2.7 ) is available. The graph is stored in the defined folder and loaded by the approach.

You can use this builder with `MedicalNerApproach`, `FinanceNerApproach`, `LegalNerApproach`, `RelationExtractionApproach`, `AssertionDLApproach`, and `GenericClassifierApproach`.

**ATTENTION:** Playing with the parameters of `TFGraphBuilder` may affect the model performance that you want to train.

{%- endcapture -%}

{%- capture model_input_anno -%}

The setInputCols parameter is changing based on the setModelName parameter.

{%- endcapture -%}

{%- capture model_output_anno -%}

There is no output file. The setGraphFile function creates a file with a .pb extension and saves it there.

{%- endcapture -%}

{%- capture model_python_medical -%}

graph_folder = "./medical_graphs"
ner_graph_builder = medical.TFGraphBuilder()\
    .setModelName("ner_dl")\
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setLabelColumn("label")\
    .setGraphFile("auto")\
    .setHiddenUnitsNumber(20)\
    .setGraphFolder(graph_folder)\
    .setIsLicensed(True)  # False -> for NerDLApproach

{%- endcapture -%}

{%- capture model_python_finance -%}

graph_folder = "./finance_graphs"
ner_graph_builder = finance.TFGraphBuilder()\
    .setModelName("ner_dl")\
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setLabelColumn("label")\
    .setGraphFile("auto")\
    .setHiddenUnitsNumber(20)\
    .setGraphFolder(graph_folder)\
    .setIsLicensed(True)  # False -> for NerDLApproach

{%- endcapture -%}

{%- capture model_python_legal -%}

graph_folder = "./legal_graphs"
ner_graph_builder = legal.TFGraphBuilder()\
    .setModelName("ner_dl")\
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setLabelColumn("label")\
    .setGraphFile("auto")\
    .setHiddenUnitsNumber(20)\
    .setGraphFolder(graph_folder)\
    .setIsLicensed(True)  # False -> for NerDLApproach

{%- endcapture -%}

{%- capture model_python_api_link -%}
[TFGraphBuilder](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/tf_graph_builder/index.html#sparknlp_jsl.annotator.tf_graph_builder.TFGraphBuilder)
{%- endcapture -%}

{%- capture model_notebook_link -%}
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_python_finance=model_python_finance
model_python_legal=model_python_legal
model_python_api_link=model_python_api_link
model_notebook_link=model_notebook_link%}
