from johnsnowlabs import *


def run_test():
    spark = nlp.start()
    doc = nlp.DocumentAssembler().setInputCol("text").setOutputCol("doc")

    tok = nlp.Tokenizer().setInputCols("doc").setOutputCol("tok")

    embeddings = (
        nlp.WordEmbeddingsModel.pretrained("glove_100d", "en")
        .setInputCols("doc", "tok")
        .setOutputCol("embeddings")
    )

    ner = (
        nlp.NerDLModel.pretrained("nerdl_fewnerd_100d")
        .setInputCols(["doc", "tok", "embeddings"])
        .setOutputCol("ner")
    )

    ner_converter = (
        nlp.NerConverter().setInputCols(["doc", "tok", "ner"]).setOutputCol("ner_chunk")
    )

    text = "Peter Parker is a nice guy and lives in New York"
    spark_df = spark.createDataFrame([[text]]).toDF("text")

    p = Pipeline(stages=[doc, tok, embeddings, ner, ner_converter])
    p.fit(spark_df).transform(spark_df).show()
