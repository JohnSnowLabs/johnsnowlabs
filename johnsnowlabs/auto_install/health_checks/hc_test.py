from johnsnowlabs import *


def run_test():
    documentAssembler = (
        nlp.DocumentAssembler().setInputCol("text").setOutputCol("document")
    )

    tokenizer = nlp.Tokenizer().setInputCols(["document"]).setOutputCol("token")

    spellModel = (
        nlp.ContextSpellCheckerModel.pretrained(
            "spellcheck_clinical", "en", "clinical/models"
        )
        .setInputCols("token")
        .setOutputCol("checked")
    )

    pipeline = nlp.Pipeline(stages=[documentAssembler, tokenizer, spellModel])

    empty = spark.createDataFrame([[""]]).toDF("text")
    example = spark.createDataFrame(
        [
            [
                "Witth the hell of phisical terapy.",
            ]
        ]
    ).toDF("text")
    pipeline.fit(empty).transform(example).show()


if __name__ == "__main__":
    run_test()
