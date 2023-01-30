# from johnsnowlabs import *
# spark = jsl.start()
from pyspark.ml import Pipeline
from sparknlp import DocumentAssembler
from sparknlp.annotator import ContextSpellCheckerModel, Tokenizer


# from johnsnowlabs import *
def run_test():
    # spark = jsl.start()
    documentAssembler = DocumentAssembler().setInputCol("text").setOutputCol("document")

    tokenizer = Tokenizer().setInputCols(["document"]).setOutputCol("token")

    spellModel = (
        ContextSpellCheckerModel.pretrained(
            "spellcheck_clinical", "en", "clinical/models"
        )
        .setInputCols("token")
        .setOutputCol("checked")
    )

    pipeline = Pipeline(stages=[documentAssembler, tokenizer, spellModel])

    empty = spark.createDataFrame([[""]]).toDF("text")
    example = spark.createDataFrame(
        [
            [
                "Witth the hell of phisical terapy.",
            ]
        ]
    ).toDF("text")
    pipeline.fit(empty).transform(example).show()
