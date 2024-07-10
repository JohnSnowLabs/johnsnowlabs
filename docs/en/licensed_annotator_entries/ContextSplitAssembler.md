{%- capture title -%}
ContextSplitAssembler
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}

Converts and assembles `VECTOR_SIMILARITY_RANKINGS` type annotations into `DOCUMENT` type.
The input annotations are expected to be of type `VECTOR_SIMILARITY_RANKINGS` and the output annotation type is `DOCUMENT`.
It concatenates the results of the input annotations into a single result, separated by a join string.
When `explodeSplits` is set to True, the splits are exploded into separate annotations.
`joinString` parameter is used to add the delimiter between results of annotations when combining them into a single result.

Parameters:

- `joinString` *(str)*:  This parameter specifies the string that will be inserted between results of annotations when combining them into a single result.
  It acts as a delimiter, ensuring that the elements are properly separated and organized in the final result of annotation.
  Default: " ".

- `explodeSplits` *(Bool)*: Whether to explode the splits into separate annotations or not.
  Default: False.


{%- endcapture -%}

{%- capture model_input_anno -%}
VECTOR_SIMILARITY_RANKINGS
{%- endcapture -%}

{%- capture model_output_anno -%}
DOCUMENT
{%- endcapture -%}

{%- capture model_python_medical -%}

from johnsnowlabs import nlp, medical



## Result



{%- endcapture -%}

{%- capture model_scala_medical -%}


{%- endcapture -%}


{%- capture model_api_link -%}
[ContextSplitAssembler](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/rag/ContextSplitAssembler.html)
{%- endcapture -%}

{%- capture model_python_api_link -%}
[ContextSplitAssembler](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/rag/context_split_assembler/index.html)
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
