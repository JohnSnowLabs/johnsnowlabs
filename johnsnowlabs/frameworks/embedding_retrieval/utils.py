def get_docsplitter_pipe(
    chunk_size: int = 500,
    chunk_overlap: int = 0,
    split_patterns: list = ["\n\n", "\n", " ", ""],
    explode_splits: bool = True,
    keep_separators: bool = True,
    patterns_are_regex: bool = False,
    trim_whitespace: bool = True,
):
    from johnsnowlabs import nlp

    nlp.start()

    return nlp.LightPipeline(
        nlp.PipelineModel(
            stages=[
                nlp.DocumentAssembler().setInputCol("text").setOutputCol("document"),
                (nlp.DocumentCharacterTextSplitter()
                 .setInputCols(["document"])
                 .setOutputCol("splits")
                 .setChunkSize(chunk_size)
                 .setChunkOverlap(chunk_overlap)
                 .setExplodeSplits(explode_splits)
                 .setPatternsAreRegex(patterns_are_regex)
                 .setSplitPatterns(split_patterns)
                 .setTrimWhitespace(trim_whitespace)
                 .setKeepSeparators(keep_separators)
                 )
            ]
        )
    )


def get_doc_splitter_internal_pipe(
    split_mode: str = "recursive",
    chunk_size: int = 500,
    chunk_overlap: int = 0,
    split_patterns: list = None,    # different value for split modes
    explode_splits: bool = True,
    keep_separators: bool = True,
    patterns_are_regex: bool = False,
    trim_whitespace: bool = True,
    sentence_awareness: bool = False,
    max_length: int = None,         # different value for split modes
    custom_bounds_strategy: str = "prepend",
    case_sensitive: bool = False,
    meta_data_fields: list = [],
    enable_sentence_increment: bool = False,
    # Tokenizer Params
    tokenizer_target_pattern: str = None,
    tokenizer_prefix_pattern: str = None,
    tokenizer_suffix_pattern: str = None,
    tokenizer_infix_patterns: list = None,
    tokenizer_exceptions: list = None,
    tokenizer_exceptions_path: str = None,
    tokenizer_case_sensitive_exceptions: bool = None,
    tokenizer_context_chars: list = None,
    tokenizer_split_pattern: str = None,
    tokenizer_split_chars: list = None,
    tokenizer_min_length: int = None,
    tokenizer_max_length: int = None,
    # Sentence Detector Params
    sentence_model_architecture: str = None,
    sentence_explode_sentences: bool = None,
    sentence_custom_bounds: list = None,
    sentence_use_custom_bounds_only: bool = None,
    sentence_split_length: int = None,
    sentence_min_length: int = None,
    sentence_max_length: int = None,
    sentence_impossible_penultimates: list = None,
):
    from johnsnowlabs import nlp, medical

    spark = nlp.start()
    split_modes = ["char", "sentence", "token", "recursive", "regex"]
    stages = [nlp.DocumentAssembler().setInputCol("text")]
    if split_mode not in split_modes:
        raise ValueError("split_mode must be one of %r." % split_modes)
    splitter_input_cols = ["document"]

    if split_mode == "sentence" or (sentence_awareness and split_mode in ["char", "sentence", "token"]):
        sent_detector = (
            nlp.SentenceDetectorDLModel.pretrained(
                "sentence_detector_dl_healthcare", "en", "clinical/models"
            )
            .setInputCols(["document"])
            .setOutputCol("sentence")
        )
        splitter_input_cols.append("sentence")

        if sentence_model_architecture:
            sent_detector.setModelArchitecture(sentence_model_architecture)
        if sentence_explode_sentences:
            sent_detector.setExplodeSentences(sentence_explode_sentences)
        if sentence_custom_bounds:
            sent_detector.setCustomBounds(sentence_custom_bounds)
        if sentence_use_custom_bounds_only:
            sent_detector.setUseCustomBoundsOnly(sentence_use_custom_bounds_only)
        if sentence_split_length:
            sent_detector.setSplitLength(sentence_split_length)
        if sentence_min_length:
            sent_detector.setMinLength(sentence_min_length)
        if sentence_max_length:
            sent_detector.setMaxLength(sentence_max_length)
        if sentence_impossible_penultimates:
            sent_detector.setImpossiblePenultimates(sentence_impossible_penultimates)
        # Add SentenceDetector to pipeline
        stages.append(sent_detector)

    if split_mode == "token":
        tokenizer = nlp.Tokenizer().setInputCols([splitter_input_cols[-1]]).setOutputCol("token")
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
        # Add tokenizer to pipeline
        stages.append(tokenizer)

    doc_splitter = (
        medical.DocumentSplitter()
        .setInputCols(splitter_input_cols)
        .setOutputCol("splits")
        .setSplitMode(split_mode)
        .setChunkSize(chunk_size)
        .setChunkOverlap(chunk_overlap)
        .setExplodeSplits(explode_splits)
        .setPatternsAreRegex(patterns_are_regex)
        .setTrimWhitespace(trim_whitespace)
        .setKeepSeparators(keep_separators)
        .setSentenceAwareness(sentence_awareness)
        .setCustomBoundsStrategy(custom_bounds_strategy)
        .setCaseSensitive(case_sensitive)
        .setMetaDataFields(meta_data_fields)
        .setEnableSentenceIncrement(enable_sentence_increment)
    )
    if split_patterns:
        doc_splitter.setSplitPatterns(split_patterns)
    if max_length:
        doc_splitter.setMaxLength(max_length)
    # Add DocumentSplitter to pipeline
    stages.append(doc_splitter)

    return nlp.LightPipeline(
        # nlp.PipelineModel(stages=stages)
        nlp.Pipeline(stages=stages).fit(spark.createDataFrame([[""]]).toDF("text"))
    )
