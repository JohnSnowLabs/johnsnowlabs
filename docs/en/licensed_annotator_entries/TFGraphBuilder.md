{%- capture title -%}
TFGraphBuilder
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}

This annotator creates Tensorflow graphs.

This class is used to build a TensorFlow graph from a given model name and a set of input columns. 

> For more information and examples of `TFGraphBuilder` annotator, you can check the [Spark NLP Workshop](https://github.com/JohnSnowLabs/spark-nlp-workshop), and in special, the notebook [17.0.Graph_builder_for_DL_models.ipynb](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/17.0.Graph_builder_for_DL_models.ipynb).

{%- endcapture -%}

{%- capture model_input_anno -%}

The setInputCols parameter is changing based on the setModelName parameter.

{%- endcapture -%}

{%- capture model_output_anno -%}

There is no output file. The setGraphFile function creates a file with a .pb extension and saves it there.

{%- endcapture -%}

{%- capture model_python_medical -%}

graph_folder = "graph/graphs_100d"
graph_name = "re_graph"

re_graph_builder = medical.TFGraphBuilder()\
    .setModelName("relation_extraction")\
    .setInputCols(["embeddings", "pos_tags", "train_ner_chunks", "dependencies"]) \
    .setLabelColumn("rel")\
    .setGraphFolder(graph_folder)\
    .setGraphFile(f"{graph_name}.pb")\
    .setHiddenLayers([300, 200])\
    .setHiddenAct("relu")\
    .setHiddenActL2(True)\
    .setHiddenWeightsL2(False)\
    .setBatchNorm(False)

{%- endcapture -%}

{%- capture model_api_link -%}
[AssertionChunkConverter](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/assertion/)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[AssertionChunkConverter](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/tf_graph_builder/index.html#sparknlp_jsl.annotator.tf_graph_builder.TFGraphBuilder)
{%- endcapture -%}



{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
approach=approach
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_api_link=model_api_link
model_python_api_link=model_python_api_link
%}
