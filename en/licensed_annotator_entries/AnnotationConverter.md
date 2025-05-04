{%- capture title -%}
AnnotationConverter
{%- endcapture -%}

{%- capture title -%}
{%- endcapture -%}

{%- capture model -%}
model
{%- endcapture -%}

{%- capture model_description -%}
A flexible converter for transforming annotations in a DataFrame using custom logic.

This class allows users to define custom conversion functions (`f`) to modify annotations,
enabling transformations like:
- Assertion outputs → Chunk outputs
- LLM outputs → Document outputs
- rule-based outputs → Updated outputs

The converter integrates with PySpark NLP-style pipelines (e.g., DocumentAssembler, Tokenizer)
but operates purely in Python (not Scala).

Parameters:

- `f`: (FunctionParam) User-defined function to transform annotations.
- `inputCol`: (Param[String]) Name of the input column containing annotations.
- `outputCol`: (Param[String]) Name of the output column for converted annotations.
- `outputAnnotatorType`: (Param[String]) Type of the output annotations (e.g., "token").


{%- endcapture -%}


{%- capture model_input_anno -%}
ANY
{%- endcapture -%}

{%- capture model_output_anno -%}
ANY
{%- endcapture -%}

{%- capture model_python_medical -%}
from johnsnowlabs import nlp, medical
from sparknlp_jsl.annotator import AnnotationConverter

test_data = spark.createDataFrame([
    (1, """I like SparkNLP annotators such as MedicalBertForSequenceClassification and BertForAssertionClassification."""),
]).toDF("id", "text")
document_assembler = DocumentAssembler().setInputCol('text').setOutputCol('document')
tokenizer = Tokenizer().setInputCols('document').setOutputCol('token')
```
def myFunction(annotations):
    new_annotations = []
    pattern = r"(?<=[a-z])(?=[A-Z])"

    for annotation in annotations:
        text = annotation.result
        import re
        parts = re.split(pattern, text)
        begin = annotation.begin
        for part in parts:
            end = begin + len(part) - 1
            new_annotations.append(
                Annotation(
                    annotatorType="token",
                    begin=begin,
                    end=end,
                    result=part,
                    metadata=annotation.metadata,
                    embeddings=annotation.embeddings,
                )
            )
            begin = end + 1

    return new_annotations
```
camel_case_tokenizer = AnnotationConverter(f=myFunction)\
    .setInputCol("token")\
    .setOutputCol("camel_case_token")\
    .setOutputAnnotatorType("token")

pipeline = Pipeline(stages=[document_assembler, tokenizer, camel_case_tokenizer])
model = pipeline.fit(test_data)
df = model.transform(test_data)
df.selectExpr("explode(camel_case_token) as tokens").show(truncate=False)    



# result

| tokens                                                |
|-------------------------------------------------------|
| {token, 0, 0, I, {sentence -> 0}, []}                 |
| {token, 2, 5, like, {sentence -> 0}, []}              |
| {token, 7, 11, Spark, {sentence -> 0}, []}            |
| {token, 12, 14, NLP, {sentence -> 0}, []}             |
| {token, 16, 25, annotators, {sentence -> 0}, []}      |
| {token, 27, 30, such, {sentence -> 0}, []}            |
| {token, 32, 33, as, {sentence -> 0}, []}              |
| {token, 35, 41, Medical, {sentence -> 0}, []}         |
| {token, 42, 45, Bert, {sentence -> 0}, []}            |
| {token, 46, 48, For, {sentence -> 0}, []}             |
| {token, 49, 56, Sequence, {sentence -> 0}, []}        |
| {token, 57, 70, Classification, {sentence -> 0}, []}  |
| {token, 72, 74, and, {sentence -> 0}, []}             |
| {token, 76, 79, Bert, {sentence -> 0}, []}            |
| {token, 80, 82, For, {sentence -> 0}, []}             |
| {token, 83, 91, Assertion, {sentence -> 0}, []}       |
| {token, 92, 105, Classification, {sentence -> 0}, []} |
| {token, 106, 106, ., {sentence -> 0}, []}             |


{%- endcapture -%}



{%- capture model_api_link -%}
[AnnotationConverter](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/AnnotationConverter.html)
{%- endcapture -%}
{%- capture model_python_api_link -%}

[AnnotationConverter](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/annotation_converter/index.html)
{%- endcapture -%}


{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
model=model
model_description=model_description
model_input_anno=model_input_anno
model_output_anno=model_output_anno
model_python_medical=model_python_medical
model_api_link=model_api_link
model_python_api_link=model_python_api_link
%}
