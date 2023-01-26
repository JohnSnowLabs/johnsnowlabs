from nbformat import NotebookNode


class Nodes:
    # Re-Usable Nodes to Inject
    sparksession = NotebookNode(
        cell_type="code",
        source="from johnsnowlabs import *;spark = nlp.start()",
        execution_count=0,
        metadata={"collapsed": True, "pycharm": {"name": "#%%\n"}},
        outputs=[],
    )
    sparksession_with_cache_folder = NotebookNode(
        cell_type="code",
        source='from johnsnowlabs import *;spark = nlp.start(cache_folder="/home/ckl/dump/cache_pretrained")',
        execution_count=0,
        metadata={"collapsed": True, "pycharm": {"name": "#%%\n"}},
        outputs=[],
    )

    imports = NotebookNode(
        cell_type="code",
        source="from sparknlp.base import LightPipeline\n"
        "from pyspark.ml import Pipeline",
        execution_count=0,
        metadata={"collapsed": True, "pycharm": {"name": "#%%\n"}},
        outputs=[],
    )

    dummy = NotebookNode(
        cell_type="code",
        source='print("HELLO DUMMY WORLD")',
        execution_count=0,
        metadata={"collapsed": True, "pycharm": {"name": "#%%\n"}},
        outputs=[],
    )
