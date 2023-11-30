{%- capture title -%}
GenericLogRegClassifier
{%- endcapture -%}

{%- capture approach -%}
approach
{%- endcapture -%}


{%- capture approach_description -%}

`GenericLogRegClassifier` is a derivative of GenericClassifier which implements a multinomial logistic regression. This is a single layer neural network with the logistic function at the output. The input to the model is FeatureVector and the output is category annotations with labels and corresponding confidence scores varying between 0 and 1.

Parameters:

- `LabelColumn`: This parameter sets the name of the column in your input data that contains the labels (categories) for the classification task. The classifier will use this column to learn from the data and make predictions.

- `ModelFile`: This parameter specifies the path to the pre-trained model file for the logistic regression classifier. It should be a protobuf file containing the model graph and trained weights.

- `EpochsNumber`: This parameter sets the number of epochs (iterations) the classifier will go through during the training process. An epoch represents one complete pass through the entire training dataset.

- `BatchSize`: This parameter sets the batch size used during training. The training data is divided into batches, and the model's weights are updated after processing each batch. A larger batch size may speed up training, but it requires more memory.

- `LearningRate`: This parameter sets the learning rate for the optimization algorithm used during training. The learning rate determines how much the model's weights are updated based on the computed gradients. A higher learning rate may lead to faster convergence but risks overshooting the optimal solution.

- `OutputLogsPath`: This parameter specifies the path where the logs related to the training process will be stored. These logs can include information such as training loss, accuracy, and other metrics.

- `Dropout`: Dropout is a regularization technique used to prevent overfitting in neural networks. This parameter sets the dropout rate, which determines the probability that each neuron's output will be temporarily ignored during training.

- `FixImbalance`: Imbalance refers to the situation when some classes have significantly more training examples than others. Setting this parameter to True indicates that the classifier will handle class imbalance during training to help ensure that the model doesn't become biased towards the majority class.

- `ValidationSplit`: This line seems to be commented out, but it's worth mentioning its purpose. If uncommented and set to a value between 0 and 1, it would specify the fraction of the training data to be used for validation during the training process. The remaining data would be used for actual training.

{%- endcapture -%}

{%- capture approach_input_anno -%}
FEATURE_VECTOR
{%- endcapture -%}

{%- capture approach_output_anno -%}
CATEGORY
{%- endcapture -%}

{%- capture approach_python_medical -%}

from johnsnowlabs import nlp,  medical

features_asm = medical.FeaturesAssembler()\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("feature_vector")

graph_folder = "gc_graph"

gc_logreg_graph_builder = medical.TFGraphBuilder()\
    .setModelName("logreg_classifier")\
    .setInputCols(["feature_vector"]) \
    .setLabelColumn("category")\
    .setGraphFolder(graph_folder)\
    .setGraphFile("log_reg_graph.pb")

gen_clf = medical.GenericLogRegClassifierApproach()\
    .setLabelColumn("category")\
    .setInputCols("feature_vector")\
    .setOutputCol("prediction")\
    .setModelFile(f"{graph_folder}/log_reg_graph.pb")\
    .setEpochsNumber(20)\
    .setBatchSize(128)\
    .setLearningRate(0.01)\
    .setOutputLogsPath(log_folder)\
    .setDropout(0.1)\
    .setFixImbalance(True)\
    # .setValidationSplit(0.1)

clf_Pipeline = nlp.Pipeline(stages=[
    features_asm,
    gc_logreg_graph_builder,
    gen_clf])

{%- endcapture -%}


{%- capture approach_scala_medical -%}

import spark.implicits._
  
val features_asm = new FeaturesAssembler()
  .setInputCols("sentence_embeddings")
  .setOutputCol("feature_vector")

val gc_logreg_graph_builder = new TFGraphBuilder()
  .setModelName("logreg_classifier")
  .setInputCols("feature_vector")
  .setLabelColumn("category")
  .setGraphFolder("gc_graph")
  .setGraphFile("log_reg_graph.pb")

val gen_clf = new GenericLogRegClassifierApproach()
  .setLabelColumn("category")
  .setInputCols("feature_vector")
  .setOutputCol("prediction")
  .setModelFile("gc_graph/log_reg_graph.pb")
  .setEpochsNumber(20)
  .setBatchSize(128)
  .setLearningRate(0.01)
  .setOutputLogsPath(log_folder)
  .setDropout(0.1)
  .setFixImbalance(true) // .setValidationSplit(0.1)

val clf_Pipeline = new Pipeline().setStages(Array(features_asm, gc_logreg_graph_builder, gen_clf))
{%- endcapture -%}


{%- capture approach_api_link -%}
[GenericLogRegClassifierApproach](https://nlp.johnsnowlabs.com/licensed/api/com/johnsnowlabs/nlp/annotators/classification/GenericLogRegClassifierApproach.html)
{%- endcapture -%}

{%- capture approach_python_api_link -%}
[GenericLogRegClassifierApproach](https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/annotator/classification/generic_log_reg_classifier/index.html#sparknlp_jsl.annotator.classification.generic_log_reg_classifier.GenericLogRegClassifierApproach)
{%- endcapture -%}

{%- capture approach_notebook_link -%}
[GenericLogRegClassifierApproachNotebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/Healthcare_MOOC/Spark_NLP_Udemy_MOOC/Healthcare_NLP/GenericLogRegClassifierModel.ipynb)
{%- endcapture -%}

{% include templates/licensed_approach_model_medical_fin_leg_template.md
title=title
approach=approach
approach_description=approach_description
approach_input_anno=approach_input_anno
approach_output_anno=approach_output_anno
approach_python_medical=approach_python_medical
approach_scala_medical=approach_scala_medical
approach_api_link=approach_api_link
approach_python_api_link=approach_python_api_link
model_notebook_link=model_notebook_link
approach_notebook_link=approach_notebook_link
%}
