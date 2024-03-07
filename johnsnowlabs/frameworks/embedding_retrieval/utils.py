def get_docsplitter_pipe(
    chunk_overlap=2,
    chunk_size=20,
    explode_splits=True,
    keep_separators=True,
    patterns_are_regex=False,
    split_patterns=["\n\n", "\n", " ", ""],
    trim_whitespace=True,
):
    from johnsnowlabs import nlp

    nlp.start()

    return nlp.LightPipeline(
        nlp.PipelineModel(
            stages=[
                nlp.DocumentAssembler().setInputCol("text"),
                nlp.DocumentCharacterTextSplitter()
                .setInputCols(["document"])
                .setOutputCol("splits")
                .setChunkSize(chunk_size)
                .setChunkOverlap(chunk_overlap)
                .setExplodeSplits(explode_splits)
                .setPatternsAreRegex(patterns_are_regex)
                .setSplitPatterns(split_patterns)
                .setTrimWhitespace(trim_whitespace)
                .setKeepSeparators(keep_separators),
            ]
        )
    )


def get_doc_splitter_internal_pipe(
    # Splitter params
    doc_splitter_chunk_overlap=2,
    doc_splitter_chunk_size=20,
    doc_splitter_explode_splits=True,
    doc_splitter_keep_separators=True,
    doc_splitter_patterns_are_regex=False,
    doc_splitter_split_patterns=["\n\n", "\n", " ", ""],
    doc_splitter_trim_whitespace=True,
    doc_splitter_split_mode="sentence",
    doc_splitter_sentence_awareness=False,
    doc_splitter_max_length=512,
    doc_splitter_custom_bounds_strategy=None,
    doc_splitter_case_sensitive=None,
    doc_splitter_meta_data_fields=None,
    # Tokenizer Params
    tokenizer_target_pattern=None,
    tokenizer_prefix_pattern=None,
    tokenizer_suffix_pattern=None,
    tokenizer_infix_patterns=None,
    tokenizer_exceptions=None,
    tokenizer_exceptions_path=None,
    tokenizer_case_sensitive_exceptions=None,
    tokenizer_context_chars=None,
    tokenizer_split_pattern=None,
    tokenizer_split_chars=None,
    tokenizer_min_length=None,
    tokenizer_max_length=None,
    # Sentence Detector Params
    sentence_detector_model_architecture=None,
    sentence_detector_explode_sentences=None,
    sentence_detector_custom_bounds=None,
    sentence_detector_use_custom_bounds_only=None,
    sentence_detector_split_length=None,
    sentence_detector_min_length=None,
    sentence_detector_max_length=None,
    sentence_detector_impossible_penultimates=None,
):
    from johnsnowlabs import nlp, medical

    spark = nlp.start()
    split_modes = ["char", "sentence", "token", "recursive", "regex"]
    stages = [nlp.DocumentAssembler().setInputCol("text")]
    if doc_splitter_split_mode not in split_modes:
        raise ValueError("split_mode must be one of %r." % split_modes)
    splitter_input_cols = ["document"]

    if doc_splitter_split_mode == "sentence" or doc_splitter_sentence_awareness:
        sent_detector = (
            nlp.SentenceDetectorDLModel.pretrained(
                "sentence_detector_dl_healthcare", "en", "clinical/models"
            )
            .setInputCols(["document"])
            .setOutputCol("sentence")
        )
        stages.append(sent_detector)
        splitter_input_cols.append("sentence")

        if sentence_detector_model_architecture:
            sent_detector.setModelArchitecture(sentence_detector_model_architecture)
        if sentence_detector_explode_sentences:
            sent_detector.setExplodeSentences(sentence_detector_explode_sentences)
        if sentence_detector_custom_bounds:
            sent_detector.setCustomBounds(sentence_detector_custom_bounds)
        if sentence_detector_use_custom_bounds_only:
            sent_detector.setUseCustomBoundsOnly(
                sentence_detector_use_custom_bounds_only
            )
        if sentence_detector_split_length:
            sent_detector.setSplitLength(sentence_detector_split_length)
        if sentence_detector_min_length:
            sent_detector.setMinLength(sentence_detector_min_length)
        if sentence_detector_max_length:
            sent_detector.setMaxLength(sentence_detector_max_length)
        if sentence_detector_impossible_penultimates:
            sent_detector.setImpossiblePenultimates(
                sentence_detector_impossible_penultimates
            )

    if doc_splitter_split_mode == "token":
        tokenizer = nlp.Tokenizer().setInputCols(["document"]).setOutputCol("sentence")
        stages.append(tokenizer)
        splitter_input_cols.append("token")
        if tokenizer_target_pattern:
            tokenizer.setTargetPattern(tokenizer_target_pattern)
        if tokenizer_prefix_pattern:
            tokenizer.setPrefixPattern(tokenizer_prefix_pattern)
        if tokenizer_suffix_pattern:
            tokenizer.setSuffixPattern(tokenizer_suffix_pattern)
        if tokenizer_infix_patterns:
            tokenizer.setInfixPatterns(tokenizer_infix_patterns)
        if tokenizer_exceptions:
            tokenizer.setExceptions(tokenizer_exceptions)
        if tokenizer_exceptions_path:
            tokenizer.setExceptionsPath(tokenizer_exceptions_path)
        if tokenizer_case_sensitive_exceptions:
            tokenizer.setCaseSensitiveExceptions(tokenizer_case_sensitive_exceptions)
        if tokenizer_context_chars:
            tokenizer.setContextChars(tokenizer_context_chars)
        if tokenizer_split_pattern:
            tokenizer.setSplitPattern(tokenizer_split_pattern)
        if tokenizer_split_chars:
            tokenizer.setSplitChars(tokenizer_split_chars)
        if tokenizer_min_length:
            tokenizer.setMinLength(tokenizer_min_length)
        if tokenizer_max_length:
            tokenizer.setMaxLength(tokenizer_max_length)

    stages.append(
        medical.DocumentSplitter()
        .setInputCols(splitter_input_cols)
        .setOutputCol("splits")
        .setChunkSize(doc_splitter_chunk_size)
        .setChunkOverlap(doc_splitter_chunk_overlap)
        .setExplodeSplits(doc_splitter_explode_splits)
        .setPatternsAreRegex(doc_splitter_patterns_are_regex)
        .setSplitPatterns(doc_splitter_split_patterns)
        .setTrimWhitespace(doc_splitter_trim_whitespace)
        .setKeepSeparators(doc_splitter_keep_separators)
        .setMaxLength(doc_splitter_max_length)
        .setSplitMode(doc_splitter_split_mode)
        .setSentenceAwareness(doc_splitter_sentence_awareness)
        .setCustomBoundsStrategy(doc_splitter_custom_bounds_strategy)
        .setCaseSensitive(doc_splitter_case_sensitive)
        .setSplitMode(doc_splitter_split_mode)
        .setMetaDataFields(doc_splitter_meta_data_fields)
    )
    return nlp.LightPipeline(
        # nlp.PipelineModel(stages=stages)
        nlp.Pipeline(stages=stages).fit(spark.createDataFrame([[""]]).toDF("text"))
    )
