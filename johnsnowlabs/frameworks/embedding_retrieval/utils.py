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
