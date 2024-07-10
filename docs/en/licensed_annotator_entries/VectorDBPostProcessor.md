{%- capture title -%}
VectorDBPostProcessor
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
VectorDBPostProcessor is used to filter and sort the annotations from the :class:`sparknlp_jsl.annotator.resolution.VectorDBModel`.

Parametres:

- `filterBy`:The filterBy parameter is used to select and prioritize filter options.
- `sortBy`:The sortBy parameter is used to select sorting option.
Options: `ascending`, `descending`, `lost_in_the_middle`, `diversity`.
`ascending`: Sort by ascending order of distance.
`descending`: Sort by descending order of distance.
`lost_in_the_middle`: Sort by lost in the middle ranker. Let's say we have 5 annotations with distances [1, 2, 3, 4, 5]. The lost in the middle ranker will sort them as [1, 3, 5, 4, 2].
`diversity`:  Sort by diversity ranker. The annotations are sorted by distance and the first annotation select, and then the next annotation is selected by the maximum average distance from the selected annotations. Default: `ascending`
- `caseSensitive`: Whether the criteria of the string operators are case sensitive or not.
For example, if set to False, the operator "equals" will match "John" with "john".
Default: False
- `diversityThreshold`: The diversityThreshold parameter is used to set the threshold for the diversityByThreshold filter.
  The diversityByThreshold filter selects the annotations by the distance between the sorted annotations.
  diversityThreshold must be greater than 0.
  Default: 0.01
- `maxTopKAfterFiltering`:  Whether to allow zero annotation after filtering.
  If set to True, the output may contain zero annotation if all annotations are filtered out.
  If set to False, The output is tried to contain at least one annotation.
  Default: False
- `metadataCriteria`: The metadataCriteria parameter is used to filter the annotations by metadata fields.


See [Spark NLP Workshop](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/41.Flattener.ipynb) for more examples of usage.
{%- endcapture -%}

{%- capture model_input_anno -%}
VECTOR_SIMILARITY_RANKINGS
{%- endcapture -%}

{%- capture model_output_anno -%}
VECTOR_SIMILARITY_RANKINGS
{%- endcapture -%}

{%- capture model_python_medical -%}


# result

{%- endcapture -%}


{%- capture model_scala_medical -%}



# result


{%- endcapture -%}

{%- capture model_api_link -%}
[VectorDBPostProcessor](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/rag/VectorDBPostProcessor.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[VectorDBPostProcessor](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/rag/vectordb_post_processor/index.html)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_scala_medical=model_scala_medical
model_api_link=model_api_link
model_python_api_link=model_python_api_link
%}
