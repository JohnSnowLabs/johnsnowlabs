import shutil

import pip

from johnsnowlabs import finance, legal, medical, nlp, settings, visual


def clear_installed_jsl_installation():
    shutil.rmtree(settings.root_dir, ignore_errors=True)
    pip.main(["uninstall", "-y", "johnsnowlabs"])
    pip.main(["uninstall", "-y", "nlu"])
    pip.main(["uninstall", "-y", "spark-nlp"])
    pip.main(["uninstall", "-y", "spark-nlp-jsl"])
    pip.main(["uninstall", "-y", "spark-ocr"])

def get_finance_pipeline():
    documentAssembler = (
        nlp.DocumentAssembler().setInputCol("text").setOutputCol("ner_chunk")
    )

    embeddings = (
        nlp.UniversalSentenceEncoder.pretrained("tfhub_use", "en")
        .setInputCols("ner_chunk")
        .setOutputCol("sentence_embeddings")
    )

    resolver = (
        finance.SentenceEntityResolverModel.pretrained(
            "finel_tickers2names", "en", "finance/models"
        )
        .setInputCols(["ner_chunk", "sentence_embeddings"])
        .setOutputCol("name")
        .setDistanceFunction("EUCLIDEAN")
    )

    return nlp.PipelineModel(stages=[documentAssembler, embeddings, resolver])

def get_legal_pipeline() -> nlp.PipelineModel:

    documentAssembler = (
        nlp.DocumentAssembler().setInputCol("text").setOutputCol("ner_chunk")
    )

    embeddings = (
        nlp.UniversalSentenceEncoder.pretrained("tfhub_use", "en")
        .setInputCols("ner_chunk")
        .setOutputCol("sentence_embeddings")
    )

    resolver = (
        legal.SentenceEntityResolverModel.pretrained(
            "legel_crunchbase_companynames", "en", "legal/models"
        )
        .setInputCols(["ner_chunk", "sentence_embeddings"])
        .setOutputCol("name")
        .setDistanceFunction("EUCLIDEAN")
    )

    return nlp.PipelineModel(stages=[documentAssembler, embeddings, resolver])

def get_cross_lib_pipe() -> nlp.PipelineModel:
    # Returns pipe with one anno per lib
    # TODO add some fancy OCR DL models?
    doc2text = visual.DocToText().setInputCol("content").setOutputCol("text")
    d = nlp.DocumentAssembler().setInputCol("text").setOutputCol("doc")
    t = nlp.Tokenizer().setInputCols("doc").setOutputCol("tok")
    # One classifier per NLP lib

    c1 = (
        medical.BertForTokenClassifier()
        .pretrained()
        .setInputCols(["tok", "doc"])
        .setOutputCol("medical")
    )

    c2 = (
        nlp.DeBertaForTokenClassification()
        .setInputCols(["tok", "doc"])
        .setOutputCol("opene_source")
    )

    c3 = (
        finance.BertForSequenceClassification.pretrained(
            "finclf_augmented_esg", "en", "finance/models"
        )
        .setInputCols(["tok", "doc"])
        .setOutputCol("finance")
    )

    c4 = (
        legal.BertForSequenceClassification.pretrained(
            "legclf_bert_judgements_agent", "en", "legal/models"
        )
        .setInputCols(["tok", "doc"])
        .setOutputCol("legal")
    )

    return nlp.Pipeline(stages=[doc2text, d, t, c1, c2, c3, c4])
