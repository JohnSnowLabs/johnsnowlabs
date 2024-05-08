---
layout: docs
header: true
seotitle: Clinical, Financial, Legal Spark NLP | John Snow Labs
title: Enterprise Spark NLP Installation
permalink: /docs/en/licensed_install
key: docs-licensed-install
modify_date: "2021-03-09"
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## AWS Marketplace
The entire suite of John Snow Labs NLP and Visual NLP libraries are offered as a pay-as-you-go product on AWS Marketplace, pre-installed and ready to use. 30+ Notebooks are included in the AWS product to allow you to start experimenting on your own data right away. To subscribe to the pay-as-you-go product on AWS Marketplace navigate to the [product page](https://aws.amazon.com/marketplace/pp/prodview-nsww5rdpvou4w?sr=0-1&ref_=beagle&applicationId=AWSMPContessa) and follow the instructions in the video below. 

<div class="cell cell--12 cell--lg-6 cell--sm-12"><div class="video-item">{%- include extensions/youtube.html id='agbV1CwMt1g' -%}<div class="video-descr">Subscribe to John Snow Labs NLP Libraries via AWS Marketplace</div></div></div>


**Note**: 30-day free trial are available for AWS and Azure subscriptions. 

</div><div class="h3-box" markdown="1">

## Installation with johnsnowlabs
On Oct 4th, 2022 we released `johnsnowlabs` library, which eases the installation and session starting processes in an 
almost transparent way for the user.

Finance NLP and Legal NLP are built on the top of a new John Snow Labs library, called johnsnowlabs.
If you are a former user of Spark NLP or Spark NLP for Healthcare, you will find this new way of deploying your Spark NLP clusters much more user-friendly!
Clinical NLP (former Spark NLP for Healthcare) still can be run without johnsnowlabs library, although we highly recommend to install it with this new method.

For advanced installation options, please check `johnsnowlabs` [webpage](https://nlp.johnsnowlabs.com/docs/en/jsl/install_advanced/).  

</div><div class="h3-box" markdown="1">

#### 1. Installing johnsnowlabs
The first step you need to carry out is installing johnsnowlabs library. This is as easy as doing:

```!pip install johnsnowlabs```

</div><div class="h3-box" markdown="1">

#### 2. Installing Enterprise NLP (Finance, Legal, Clinical)

Import `johnsnowlabs` and use our one-liner `nlp.install()` to install all the dependencies, downloading the jars (yes, Spark NLP runs on top of the Java Virtual Machine!), preparing the cluster environment variables, licenses, etc!

```
from johnsnowlabs import *

nlp.install(force_browser=True)
```

The `force_browser=True` command gets rid of you uploading a license. It will open a popup to connect to our license server at `my.johnsnowlabs.com` retrieve the license for you, and install everything your license allows you to use!
If you are a user of Financial NLP, you will get that installed. If you are a Legal user, then Legal NLP will be installed, or Clinical! Everything will be taken care on your behalf!

</div><div class="h3-box" markdown="1">

#### Optional: Uploading the license manually
We still have the way of downloading manually the license, in case the connection with `my.johnsnowlabs.com` is not an option for you.
Just put your license json in the same folder of the notebook, and run:

```
nlp.install()
```

In colab, you can use this fancy widget to upload a file to your environment:

```
from google.colab import files

print('Please Upload your John Snow Labs License using the button below')
license_keys = files.upload()
```

And then do:

```
nlp.install()
```

</div><div class="h3-box" markdown="1">

#### 3. Starting an Enterprise NLP cluster
Another one-liner can be used to start your Enterprise Spark NLP cluster:

```
spark = nlp.start()
```
It will take into account the previous steps and your license and return a Spark Session.

</div><div class="h3-box" markdown="1">

#### 4. Ready to go!
And you are done! Simple, isn't it?
Find hundreds of notebooks using johnsnowlabs library here:

- [Finance NLP notebooks](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/finance-nlp)
- [Legal NLP notebooks](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/legal-nlp)
- [Clinical NLP notebooks](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/healthcare-nlp)

</div><div class="h3-box" markdown="1">

## Finance, Legal, Clinical NLP on Databricks

- List of [tested runtimes](/docs/en/install#databricks-support).
- Recommended instance type `Standard_F8s_v2 (16 GB Memory, 8 Cores)` or higher.
- The installation takes around 15 minutes.

</div><div class="h3-box" markdown="1">

#### Connection via Databricks Partner connect

Databricks has an integration of Spark NLP libraries via Partner Connect. If you are [eligible](https://docs.databricks.com/integrations/partner-connect/index.html?#requirements-1), you can [connect](https://docs.databricks.com/integrations/partner-connect/index.html?#quickstart-connect-to-a-partner-solution-using-partner-connect) your Databricks workspace to John Snow Labs. The Partner Connect wizard  will redirect you to John Snow Labs portal. After you fill-in/validate your information a 30-day trial license will be automatically generated for you. A new Databricks cluster will also be created, and all necessary resources to run the library on your account will be installed on your new cluster. Furthermore, a set of ready to use notebooks will be copied to your workspace, so you can start experimenting on your data right away. The trial license file will also be deployed to your environment and made available to your cluster.  

The trial period is 30 days. You can use the trial period only once. After the trial period, we will contact you with a licensing offer.  

- Start exploring preloaded notebooks `Workspace -> Shared -> John Snow Labs`

</div><div class="h3-box" markdown="1">

#### Automatic deployment of John Snow Labs NLP libraries from [www.johnsnowlabs.com/databricks](https://www.johnsnowlabs.com/databricks/)

Alternatively, you can automatically deploy John Snow Labs libraries on Databricks by filling in the form available [here](https://www.johnsnowlabs.com/databricks/). This will allow you to start a 30-day free trial with no limit on the amount of processed data. You just need to provide a Databricks Access Token that is used by our deployment script to connect to your Databricks instance and install John Snow Labs NLP libraries on a cluster of your choice.

- Start exploring preloaded notebooks `Workspace -> Shared -> John Snow Labs`

</div><div class="h3-box" markdown="1">

#### Automatic deployment via [my.JohnSnowLabs.com](https://my.JohnSnowLabs.com)

Login to your account on my.JohnSnowLabs.com, navigate to 'My Subscriptions' page, and identify your license for Databricks. Click on the three dots as illustrated in the image below, then select the `Install On Cluster` option.

<img class="image image--xl" src="/assets/images/myJSLdeployment.png" style="width:100%; align:center; box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);"/>

On the install form, provide an access token for this account and then select the cluster where you want to install the libraries. Once it is done, you will get an email with information on the status of your deployment and on how to get started with the libraries. 

<img class="image image--xl" src="/assets/images/install_form.png" style="width:100%; align:center; box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);"/>

</div><div class="h3-box" markdown="1">

#### Automatic deployment or upgrade from the Databricks workspace

If you have already deployed the libraries in the past, you have a script `Workspace -> Shared -> John Snow Labs -> Install JohnSnowLabs NLP`. If you attach it to any cluster and run it, it will reinstall the libraries on the respective cluster. 

- This is also the recommended way to upgrade to the latest versions of the libraries.

</div><div class="h3-box" markdown="1">

#### Manual deployment of Enterprise Spark NLP
Automatic deployment is the preferred option.

1. Create a cluster with one of the [supported runtimes](/docs/en/install#databricks-support) if you don't have one already.
2. On a new cluster or existing one you need to add the following to the `Advanced Options -> Spark` tab, in `Spark.Config` box:

    ```bash
    spark.kryoserializer.buffer.max 1000M
    spark.serializer org.apache.spark.serializer.KryoSerializer
    ```
      -  Please add the following to the `Advanced Options -> Spark` tab, in `Environment Variables` box:

    ```bash
    AWS_ACCESS_KEY_ID=xxx
    AWS_SECRET_ACCESS_KEY=yyy
    SPARK_NLP_LICENSE=zzz
    ```
Note: Enterprise Spark NLP also support reading the license from the Databricks DFS, on the fixed location, `dbfs:/FileStore/johnsnowlabs/license.key`.
The precedence for that location is the highest, so make sure that file is not containing any outdated license key.

      -   (OPTIONAL) If the environment variables used to setup the AWS Access/Secret keys are conflicting with the credential provider chain in Databricks, you may not be able to access to other s3 buckets. To access both JSL repos with JSL AWS keys as well as your own s3 bucket with your own AWS keys), you need to use the following script, copy that to dbfs folder, then go to the Databricks console (init scripts menu) to add the init script for your cluster as follows:

    ```bash
    %scala
    val script = """
    #!/bin/bash

    echo "******** Inject Spark NLP AWS Profile Credentials ******** "

    mkdir ~/.aws/

    cat << EOF > ~/.aws/credentials
    [spark_nlp]
    aws_access_key_id=<YOUR_AWS_ACCESS_KEY>
    aws_secret_access_key=<YOUR_AWS_SECRET_KEY>
    EOF

    echo "******** End Inject Spark NLP AWS Profile Credentials  ******** "

    """
    ```

3. In `Libraries` tab inside your cluster you need to follow these steps:
 - [Lookup](https://nlp.johnsnowlabs.com/docs/en/licensed_version_compatibility) the version of Healhcare NLP vs. Spark NLP you will install.
 - Install Spark NLP (Public): New -> PyPI -> `spark-nlp==${x.y.z_public_version}` -> Install
 - Install: New -> Maven -> Coordinates -> `com.johnsnowlabs.nlp:spark-nlp_2.12:${x.y.z_public_version}` -> Install
 - Please add following jars:
        - Install: New -> Python Whl -> upload `https://pypi.johnsnowlabs.com/${secret.code}/spark-nlp-jsl/spark_nlp_jsl-${x.y.z_healthcare_version}-py3-none-any.whl`
        - Install: New -> Jar -> upload `https://pypi.johnsnowlabs.com/${secret.code}/spark-nlp-jsl-${x.y.z_healthcare_version}.jar`
- (For Legal and Finance NLP) Install: New -> PyPI -> `johnsnowlabs-for-databricks==${x.y.z_healthcare_version}` -> Install
4. Now you can attach your notebook to the cluster and use Spark NLP!

</div><div class="h3-box" markdown="1">

## Windows Support

In order to fully take advantage of Spark NLP on Windows (8 or 10), you need to setup/install Apache Spark, Apache Hadoop, Java and a Pyton environment correctly by following the following instructions: [https://github.com/JohnSnowLabs/spark-nlp/discussions/1022](https://github.com/JohnSnowLabs/spark-nlp/discussions/1022)

</div><div class="h3-box" markdown="1">

#### How to correctly install Spark NLP on Windows

Follow the below steps to set up Spark NLP with Spark 3.1.2:

  1. Download [Adopt OpenJDK 1.8](https://adoptopenjdk.net/?variant=openjdk8&jvmVariant=hotspot)
     - Make sure it is 64-bit
     - Make sure you install it in the root of your main drive `C:\java`.
     - During installation after changing the path, select setting Path

  2. Download the pre-compiled Hadoop binaries `winutils.exe`, `hadoop.dll` and put it in a folder called `C:\hadoop\bin` from [https://github.com/cdarlint/winutils/tree/master/hadoop-3.2.0/bin](https://github.com/cdarlint/winutils/tree/master/hadoop-3.2.0/bin)
     - **Note:** The version above is for Spark 3.1.2, which was built for Hadoop 3.2.0. You might have to change the hadoop version in the link, depending on which Spark version you are using.

  3. Download [Apache Spark 3.1.2](https://www.apache.org/dyn/closer.lua/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz) and extract it to `C:\spark`.

  4. Set/add environment variables for `HADOOP_HOME` to `C:\hadoop` and `SPARK_HOME` to `C:\spark`.

  5. Add `%HADOOP_HOME%\bin` and `%SPARK_HOME%\bin` to the `PATH` environment variable.

  6. Install [Microsoft Visual C++ 2010 Redistributed Package (x64)](https://www.microsoft.com/en-us/download/details.aspx?id=26999).

  7. Create folders `C:\tmp` and `C:\tmp\hive`
     - If you encounter issues with permissions to these folders, you might need
       to change the permissions by running the following commands:
       ```
       %HADOOP_HOME%\bin\winutils.exe chmod 777 /tmp/hive
       %HADOOP_HOME%\bin\winutils.exe chmod 777 /tmp/
       ```

</div><div class="h3-box" markdown="1">

#### Requisites for PySpark

We recommend using `conda` to manage your python environment on Windows.

- Download [Miniconda for python 3.8](https://repo.anaconda.com/miniconda/Miniconda3-py38_4.11.0-Windows-x86_64.exe)
- See [Quick Install](#quick-install) on how to set up a conda environment with
  Spark NLP.
- The following environment variables need to be set:
  - `PYSPARK_python=python`
  - Optionally, if you want to use the Jupyter Notebook runtime of Spark:
    - first install it in the environment with `conda install notebook`
    - then set `PYSPARK_DRIVER_python=jupyter`, `PYSPARK_DRIVER_python_OPTS=notebook`
  - The environment variables can either be directly set in windows, or if only
    the conda env will be used, with `conda env config vars set PYSPARK_python=python`.
    After setting the variable with conda, you need to deactivate and re-activate
    the environment.

Now you can use the downloaded binary by navigating to `%SPARK_HOME%\bin` and
running

Either create a conda env for python 3.6, install *pyspark==3.1.2 spark-nlp numpy* and use Jupyter/python console, or in the same conda env you can go to spark bin for *pyspark --packages com.johnsnowlabs.nlp:spark-nlp_2.12:3.4.4*.

<img class="image image--xl" src="/assets/images/installation/90126972-c03e5500-dd64-11ea-8285-e4f76aa9e543.jpg" style="width:100%; align:center; box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);"/>

<img class="image image--xl" src="/assets/images/installation/90127225-21662880-dd65-11ea-8b98-3a2c26cfa534.jpg" style="width:100%; align:center; box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);"/>

<img class="image image--xl" src="/assets/images/installation/90127243-2925cd00-dd65-11ea-9b20-ba3353473a98.jpg" style="width:100%; align:center; box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);"/>

<img class="image image--xl" src="/assets/images/installation/90126972-c03e5500-dd64-11ea-8285-e4f76aa9e543.jpg" style="width:100%; align:center; box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);"/>

</div><div class="h3-box" markdown="1">

### Windows Server

1. Download and Install JAVA 8 

    i) Download and Install JAVA 8 from  [https://adoptium.net/temurin/releases/?version=8](https://adoptium.net/temurin/releases/?version=8) 

    ii) Once installed , We can check if java is installed by opening cmd and type `java -version` command

    ![image-20230517-140723](https://github.com/JohnSnowLabs/johnsnowlabs/assets/64752006/c262961e-4923-449a-b1b1-46d233c3b94d)


2. Install Microsoft Visual C++ 2010

    i)  Install Microsoft Visual C++ 2010 from [Microsoft Visual C++ 2010 Service Pack 1 Redistributable Package MFC Security Update](https://www.microsoft.com/en-us/download/details.aspx?id=26999) 



3. Download the pre-compiled Hadoop binaries `winutils.exe`, `hadoop.dll`

    i) Download the pre-compiled Hadoop binaries winutils.exe, hadoop.dll from [winutils/hadoop-3.2.0/bin at master · cdarlint/winutils](https://github.com/cdarlint/winutils/tree/master/hadoop-3.2.0/bin)

    ii) Copy files into a folder called `C:\hadoop\bin `



4. Configure Hadoop ENV variables  

    - `Windows Explorer` → `This PC` -> Right Click select `properties`  -> Click on  `Advanced` system settings -> Click on `Environment Variables` Under system variables 
    
    ![image-20230517-141616](https://github.com/JohnSnowLabs/johnsnowlabs/assets/64752006/d0c53899-5d49-4fdf-a3d4-1023e5250faa)

    
    
    - Add HADOOP_HOME as below  
    
    Under system variables -> Click on `new`

    VARIABLE Name: `HADOOP_HOME` 

    VARIABLE Value: `C:\hadoop`


    ![image-20230517-141745](https://github.com/JohnSnowLabs/johnsnowlabs/assets/64752006/062d9918-46d7-4ba1-8736-0cc33da13f9d)


    - Select the `Path` (from variable) -> Click on `edit` → Click on `New` → add  `%HADOOP_HOME%\bin`

    ![image-20230517-141922](https://github.com/JohnSnowLabs/johnsnowlabs/assets/64752006/eca7f39c-e4c6-43fe-8a43-fa8c3a8af7b9)

    ![image-20230517-141957](https://github.com/JohnSnowLabs/johnsnowlabs/assets/64752006/48426b70-a82f-4628-82a4-aff1bb5408b4)



5. Dowload and Install Conda and set Conda ENV variables  

   i)   Download Miniconda for python 3.8 from [https://repo.anaconda.com/miniconda/Miniconda3-py38_4.11.0-Windows-x86_64.exe](https://repo.anaconda.com/miniconda/Miniconda3-py38_4.11.0-Windows-x86_64.exe)

   ii)  Install miniconda exe file.  
   
   iii) `Under system variables` ->  `Select the Path (from variable)` -> `Click on edit` -> `(ADD the miniconda install location)/bin` (Same steps as above)
   
    ![image](https://github.com/JohnSnowLabs/johnsnowlabs/assets/64216738/14fa36ea-d53b-476f-9ad8-1d0d442650d2)

6. Configure conda env 

   i) Open cmd and execute the following commands
  
```
conda --version
java -version
conda create -n sparknlp python=3.8 -y
conda activate sparknlp
pip install spark-nlp==5.1.2 pyspark==3.2.1
pip install jupyter
conda env config vars set PYSPARK_PYTHON=python
conda activate sparknlp
conda env config vars set PYSPARK_DRIVER_PYTHON=jupyter
conda activate sparknlp
conda env config vars set PYSPARK_DRIVER_python_OPTS=notebook
conda activate sparknlp
jupyter notebook
```

## Apple Silicon Support

**Installation for Apple Silicon (M1, M2, M3)**: Starting from version 4.0.0, Spark NLP has experimental support for apple silicon.

Make sure the following prerequisites are set:

1. Installing SDKMAN, you can also follow the official documentation at https://sdkman.io/install
    - `$ curl -s "https://get.sdkman.io" | bash`
    - `source "$HOME/.sdkman/bin/sdkman-init.sh"`
    - `sdk list java`  
    list available java libraries:

    ![image](https://github.com/JohnSnowLabs/spark-nlp-workshop/assets/64752006/9d05bd11-14c5-454e-bbab-fea4e91da905)


2. Installing Java
    - `sdk install java 8.0.402-amzn` 
    - `whereis java`
    - `java -version`

3. Installing MiniConda, you can also follow the official documentation at https://docs.anaconda.com/free/miniconda/#quick-command-line-install  
    - `mkdir -p ~/miniconda3`
    - `curl https://repo.anaconda.com/miniconda/Miniconda3-py39_23.11.0-2-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh` PS: you can change python version to 3.10 or 3.11
    - `bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3`
    - `~/miniconda3/bin/conda init bash`
    - `~/miniconda3/bin/conda init zsh`
    - `source miniconda3/bin/activate`

4. Installing `jupyter environments` or you can install it via `VSCode`

    ```bash
    # use base environment
    conda --version
    java -version
    conda activate
    pip install pyspark==3.4.0
    pip install jupyter
    conda env config vars set PYSPARK_PYTHON=python
    conda activate 
    conda env config vars set PYSPARK_DRIVER_PYTHON=jupyter
    conda activate 
    conda env config vars set PYSPARK_DRIVER_python_OPTS=notebook
    conda activate 
    jupyter notebook
    ```

    ```bash
    # or create new sparknlp environment
    conda --version
    java -version
    conda create -n sparknlp python=3.9 -y
    conda activate sparknlp
    pip install pyspark==3.4.0
    pip install jupyter
    conda env config vars set PYSPARK_PYTHON=python
    conda activate sparknlp
    conda env config vars set PYSPARK_DRIVER_PYTHON=jupyter
    conda activate sparknlp
    conda env config vars set PYSPARK_DRIVER_python_OPTS=notebook
    conda activate sparknlp
    jupyter notebook
    ```

5. Installing Spark NLP Healthcare 

    please see the [Spark NLP Healthcare Installation Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/platforms/apple-silicon/installation.ipynb)




## Non-johnsnowlabs Clinical NLP on Ubuntu 
> These instructions use non-johnsnowlabs installation syntax. For simplified installation with `johnsnowlabs` library, check first section.

For installing John Snow Labs NLP libraries on an Ubuntu machine/VM please run the following command:

```bash
wget https://setup.johnsnowlabs.com/nlp/install.sh -O - | sudo bash -s -- -a PATH_TO_LICENSE_JSON_FILE -i -r
```

This script will install `Spark NLP`, `Enterprise Spark NLP`, `Spark OCR`, `NLU` and `Spark NLP Display` on the specified virtual environment. It will also create a special folder, `./JohnSnowLabs`,  dedicated to all resources necessary for using the libraries.  Under `./JohnSnowLabs/example_notebooks` you will find some ready to use example notebooks that you can use to test the libraries on your data. 

For a complete step-by-step guide on how to install NLP Libraries check the video below:
<div class="cell cell--12 cell--lg-6 cell--sm-12"><div class="video-item">{%- include extensions/youtube.html id='E-zAkeym06g' -%}<div class="video-descr">Install John Snow Labs NLP Libraries on Ubuntu</div></div></div>


The install script offers several options:
 - `-h`    show brief help
 - `-i`    install mode: create a virtual environment and install the library
 - `-r`    run mode: start jupyter after installation of the library 
 - `-v`    path to virtual environment (default: ./sparknlp_env)
 - `-j`    path to license json file for Enterprise Spark NLP
 - `-o`    path to license json file for Spark OCR
 - `-a`    path to a single license json file for both Spark OCR and Spark NLP
 - `-s`    specify pyspark version
 - `-p`    specify port of jupyter notebook

Use the `-i` flag for installing the libraries in a new virtual environment. 

You can provide the desired path for virtual env using `-v` flag, otherwise a default location of `./sparknlp_env` will be selected. 

The `PATH_TO_LICENSE_JSON_FILE` parameter must be replaced with the path where the license file is available on the local machine. According to the libraries you want to use different flags are available: `-j`, `-o` or `-a`. The license files can be easily downloaded from *My Subscription* section in your [my.JohnSnowLabs.com](https://my.johnsnowlabs.com/) account.

To start using Jupyter Notebook after the installation of the libraries use the `-r` flag. 

The install script downloads a couple of example notebooks that you can use to start experimenting with the libraries. Those will be availabe under `./JohnSnowLabs/example_notebooks` folder. 

</div><div class="h3-box" markdown="1">

## Non-johnsnowlabs Clinical NLP via Docker
> These instructions use non-johnsnowlabs installation syntax. For simplified installation with `johnsnowlabs` library, check first section.

A docker image that contains all the required libraries for installing and running Enterprise Spark NLP libraries is also available. However, it does not contain the library itself, as it is licensed, and requires installation credentials.

Make sure you have a valid license for Enterprise Spark NLP libraries (in case you do not have one, you can ask for a trial [here](https://www.johnsnowlabs.com/install/)), and follow the instructions below:

</div><div class="h3-box" markdown="1">

#### Docker Image for running Spark NLP for Healthcare inside Jupyter Notebook

The Image contains all the required libraries for installing and running Spark NLP for Healthcare. However, it does not contain the library itself, as it is licensed, and requires installation credentials. 

- Please download the necessary files from the [here](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/jupyter/docker_enterprise/docker_image_nlp_hc/sparknlp_for_healthcare_jupyter) or just get them with commandline as the following:

```bash
curl -o Dockerfile https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/jupyter/docker_enterprise/docker_image_nlp_hc/sparknlp_for_healthcare_jupyter/Dockerfile
curl -o entrypoint.sh https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/jupyter/docker_enterprise/docker_image_nlp_hc/sparknlp_for_healthcare_jupyter/entrypoint.sh
curl -o requirements.txt https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/jupyter/docker_enterprise/docker_image_nlp_hc/sparknlp_for_healthcare_jupyter/requirements.txt
```

- Download your license key in json format from [my.JohnSnowLabs.com](https://my.johnsnowlabs.com/) and put the same folder
- Make sure you have valid license for Spark NLP for Healthcare,  and run the following command:

```bash 
docker run -v /home/jsl_keys.json:/notebooks/sparknlp_keys.json -p 8888:8888 -d johnsnowlabs/sparknlp:sparknlp_for_healthcare_jupyter
```
- Please replace values inside `tags`. For instance, replace `/home/jsl_keys.json` with the correct license json absolute path.
- Make sure docker is installed on your system.
- Run `docker ps` to validate the container is running.
- If your container is not running, look at docker logs to identify issue.
- If the default port `8888` is already occupied by another process, please change the mapping. Only change values inside the `tags`.

</div><div class="h3-box" markdown="1">

#### Alternative Docker Image Instractions

- Run the following commands to download the `docker-compose.yml` and the `sparknlp_keys.txt` files on your local machine:
```bash
curl -o docker-compose.yaml https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/jupyter/docker_enterprise/docker_image_nlp_hc/sparknlp_for_healthcare_image/docker-compose.yaml
curl -o sparknlp_keys.txt https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/jupyter/docker_image_nlp_hc/sparknlp_keys.txt
```

- Download your license key in json format from [my.JohnSnowLabs.com](https://my.johnsnowlabs.com/) 
- Update License keys in `sparknlp_keys.txt` file.
- Run the following command to run the container in detached mode:

```bash
 docker-compose up -d
 ``` 
- By default, the jupyter notebook runs on port `8888` - you can access it by typing `localhost:8888` in your browser
- Create a new jupyter [notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/jupyter/docker_enterprise/docker_image_nlp_hc/sparknlp_for_healthcare_image/example_notebook.ipynb) and start coding

</div><div class="h3-box" markdown="1">

#### Troubleshooting

- Make sure docker is installed on your system.
- If you face any error while importing the lib inside jupyter, make sure all the credentials are correct in the key files and restart the service again.
- If the default port `8888` is already occupied by another process, please change the mapping.
- You can change/adjust volume and port mapping in the `docker-compose.yaml` file.
- You don't have a license key? Ask for a trial license [here](https://www.johnsnowlabs.com/install/).

</div><div class="h3-box" markdown="1">

## Non-johnsnowlabs Clinical NLP on python
> These instructions use non-johnsnowlabs installation syntax. For simplified installation with `johnsnowlabs` library, check first section.

You can install the Clinical NLP by using:

```bash
pip install -q spark-nlp-jsl==${version} --extra-index-url https://pypi.johnsnowlabs.com/${secret.code} --upgrade
```

`{version}` is the version part of the `{secret.code}` (`{secret.code}.split('-')[0]`) (i.e. `2.6.0`)

The `{secret.code}` is a secret code that is only available to users with valid/trial license. 

You can ask for a free trial for Enterprise Spark NLP libraries [here](https://www.johnsnowlabs.com/install/). Then, you can obtain the secret code by visiting your account on [my.JohnSnowLabs.com](https://my.johnsnowlabs.com/). Read more on how to get a license [here](licensed_install#get-a-spark-nlp-for-healthcare-license).

</div><div class="h3-box" markdown="1">

#### Setup AWS-CLI Credentials for licensed pretrained models

You need to first set up your AWS credentials to be able to access the private repository for John Snow Labs Pretrained Models.
You can do this setup via Amazon AWS Command Line Interface (AWSCLI).

Instructions about how to install AWSCLI are available at:

<a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html">Installing the AWS CLI</a>

Make sure you configure your credentials with AWS configure following the instructions at:

<a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html">Configuring the AWS CLI</a>

Please substitute the `ACCESS_KEY` and `SECRET_KEY` with the credentials available on your license json file. This is available on your account from [my.JohnSnowLabs.com](https://my.johnsnowlabs.com/). [Read this](licensed_install#get-a-spark-nlp-for-healthcare-license) for more information.

</div><div class="h3-box" markdown="1">

#### Start Spark NLP Session from python

The following will initialize the spark session in case you have run the Jupyter Notebook directly. If you have started the notebook using
pyspark this cell is just ignored.

Initializing the spark session takes some seconds (usually less than 1 minute) as the jar from the server needs to be loaded.

The `{secret.code}` is a secret code that is only available to users with valid/trial license. 

You can ask for a free trial for Enterprise Spark NLP [here](https://www.johnsnowlabs.com/install/). Then, you can obtain the secret code by visiting your account on [my.JohnSnowLabs.com](https://my.johnsnowlabs.com/). Read more on how to get a license [here](licensed_install#get-a-spark-nlp-for-healthcare-license).

You can either use our convenience function to start your Spark Session that will use standard configuration arguments:

```python
import sparknlp_jsl
spark = sparknlp_jsl.start(SECRET)
```

Or use the SparkSession module for more flexibility:

```python
from pyspark.sql import SparkSession

def start(SECRET):
    builder = SparkSession.builder \
        .appName("Spark NLP Licensed") \
        .master("local[*]") \
        .config("spark.driver.memory", "16G") \
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
        .config("spark.kryoserializer.buffer.max", "2000M") \
        .config("spark.jars.packages", "com.johnsnowlabs.nlp:spark-nlp_2.12:"+PUBLIC_VERSION) \
        .config("spark.jars", "https://pypi.johnsnowlabs.com/"+SECRET+"/spark-nlp-jsl-"+JSL_VERSION+".jar")
      
    return builder.getOrCreate()

spark = start(SECRET)
```

If you want to download the source files (jar and whl files) locally, you can follow the instructions <a href="https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/jupyter/SparkNLP_offline_installation.ipynb">here</a>.

</div><div class="h3-box" markdown="1">

#### Cheatsheet

```bash
# Install Spark NLP from PyPI
pip install spark-nlp==${public_version}

#install Spark NLP helathcare

pip install spark-nlp-jsl==${version} --extra-index-url https://pypi.johnsnowlabs.com/${secret.code} --upgrade

# Load Spark NLP with Spark Shell
spark-shell --packages com.johnsnowlabs.nlp:spark-nlp_2.12:${public_version} --jars spark-nlp-jsl-${version}.jar

# Load Spark NLP with PySpark
pyspark --packages com.johnsnowlabs.nlp:spark-nlp_2.12:${public_version} --jars spark-nlp-jsl-${version}.jar

# Load Spark NLP with Spark Submit
spark-submit --packages com.johnsnowlabs.nlp:spark-nlp_2.12:${public_version} --jars spark-nlp-jsl-${version}.jar
```

</div><div class="h3-box" markdown="1">

## Non-johnsnowlabs Clinical NLP for Scala
> These instructions use non-johnsnowlabs installation syntax, since `johnsnowlabs` is a Python library. 

#### Use Spark NLP in Spark shell

1.Download the fat jar for Enterprise Spark NLP

```bash
aws s3 cp --region us-east-2 s3://pypi.johnsnowlabs.com/$jsl_secret/spark-nlp-jsl-$jsl_version.jar spark-nlp-jsl-$jsl_version.jar
```

2.Set up the `Environment Variables` box:

```bash
    AWS_ACCESS_KEY_ID=xxx
    AWS_SECRET_ACCESS_KEY=yyy
    SPARK_NLP_LICENSE=zzz
```

3.The preferred way to use the library when running Spark programs is using the `--packages`and `--jar` option as specified in the `spark-packages` section. 

```bash
spark-shell --packages com.johnsnowlabs.nlp:spark-nlp_2.12:${public-version} --jars /spark-nlp-jsl-${version}.jar
```

</div><div class="h3-box" markdown="1">

## Non-johnsnowlabs Clinical NLP in Sbt project
> These instructions use non-johnsnowlabs installation syntax. For simplified installation with `johnsnowlabs` library, check first section.

1.Download the fat jar for Enterprise Spark NLP.
```bash
aws s3 cp --region us-east-2 s3://pypi.johnsnowlabs.com/$jsl_secret/spark-nlp-jsl-$jsl_version.jar spark-nlp-jsl-$jsl_version.jar
```

2.Set up the `Environment Variables` box:

```bash
    AWS_ACCESS_KEY_ID=xxx
    AWS_SECRET_ACCESS_KEY=yyy
    SPARK_NLP_LICENSE=zzz
```

3.Add the spark-nlp jar in your build.sbt project

```scala
libraryDependencies += "com.johnsnowlabs.nlp" %% "spark-nlp" % "{public-version}"
````

4.You need to create the /lib folder and paste the spark-nlp-jsl-${version}.jar file.
 
5.Add the fat spark-nlp-healthcare in your classpath. You can do it by adding this line in your build.sbt

```scala
unmanagedJars in Compile += file("lib/sparknlp-jsl.jar")
```

</div><div class="h3-box" markdown="1">

## Non-johnsnowlabs Clinical NLP on Colab

This is the way to run Clinical NLP in Google Colab if you don't use `johnsnowlabs` library.

Run the following code in Google Colab notebook and start using Spark NLP right away.

The first thing that you need is to create the json file with the credentials and the configuration in your local system.

```json
{
  "PUBLIC_VERSION": "{public-version}",
  "JSL_VERSION": "{version}",
  "SECRET": "{version}-{secret.code}",
  "SPARK_NLP_LICENSE": "xxxxx",
  "AWS_ACCESS_KEY_ID": "yyyy",
  "AWS_SECRET_ACCESS_KEY": "zzzz"
}
```

If you have a valid floating license, the license json file can be downloaded from your account on [my.JohnSnowLabs.com](https://my.johnsnowlabs.com/) on **My Subscriptions** section. To get a trial license please visit 


Then you need to write that piece of code to load the credentials that you created before.

```python

import json
import os

from google.colab import files

license_keys = files.upload()

with open(list(license_keys.keys())[0]) as f:
  license_keys = json.load(f)

# Defining license key-value pairs as local variables
locals().update(license_keys)

# Adding license key-value pairs to environment variables
os.environ.update(license_keys)
```

```sh
# This is only to setup PySpark and Spark NLP on Colab
!wget https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/jsl_colab_setup.sh
```


```sh
# -p is for pyspark (by default 3.1.1)
!bash jsl_colab_setup.sh
```

[Spark NLP quick start on Google Colab](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb) is a live demo on Google Colab that performs named entity recognitions for HealthCare.


</div><div class="h3-box" markdown="1">

## Non-johnsnowlabs Clinical NLP on GCP Dataproc
> These instructions use non-johnsnowlabs installation syntax. For simplified installation with `johnsnowlabs` library, check first section.

- You can follow the steps here for [installation via IU](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/platforms/dataproc)

1. Create a cluster if you don't have one already as follows.

At gcloud shell:

```bash
gcloud services enable dataproc.googleapis.com \
  compute.googleapis.com \
  storage-component.googleapis.com \
  bigquery.googleapis.com \
  bigquerystorage.googleapis.com
```

```bash
REGION=<region>
```

```bash
BUCKET_NAME=<bucket_name>
gsutil mb -c standard -l ${REGION} gs://${BUCKET_NAME}
```

```bash
REGION=<region>
ZONE=<zone>
CLUSTER_NAME=<cluster_name>
BUCKET_NAME=<bucket_name>
```

You can set image-version, master-machine-type, worker-machine-type,
master-boot-disk-size, worker-boot-disk-size, num-workers as your needs.
If you use the previous image-version from 2.0, you should also add ANACONDA to optional-components.
And, you should enable gateway.
As noticed below, you should explicitly write JSL_SECRET and JSL_VERSION at metadata param inside the quotes.
This will start the pip installation using the wheel file of Licensed SparkNLP!


```bash
gcloud dataproc clusters create ${CLUSTER_NAME} \
  --region=${REGION} \
  --network=${NETWORK} \
  --zone=${ZONE} \
  --image-version=2.0 \
  --master-machine-type=n1-standard-4 \
  --worker-machine-type=n1-standard-2 \
  --master-boot-disk-size=128GB \
  --worker-boot-disk-size=128GB \
  --num-workers=2 \
  --bucket=${BUCKET_NAME} \
  --optional-components=JUPYTER \
  --enable-component-gateway \
  --metadata 'PIP_PACKAGES=google-cloud-bigquery google-cloud-storage spark-nlp-display
  https://s3.eu-west-1.amazonaws.com/pypi.johnsnowlabs.com/JSL_SECRET/spark-nlp-jsl/spark_nlp_jsl-JSL_VERSION-py3-none-any.whl' \
  --initialization-actions gs://goog-dataproc-initialization-actions-${REGION}/python/pip-install.sh
```

2. On an existing one, you need to install spark-nlp and spark-nlp-display packages from PyPI.

3. Now, you can attach your notebook to the cluster and use Spark NLP via following the instructions.
The key part of this usage is how to start SparkNLP sessions using Apache Hadoop YARN cluster manager.

3.1. Read license file from the notebook using GCS.

3.2. Set the right path of the Java Home Path.

3.3. Use the start function to start the SparkNLP JSL version such as follows:

```python
def start(secret):
    builder = SparkSession.builder \
        .appName("Spark NLP Licensed") \
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
        .config("spark.kryoserializer.buffer.max", "2000M") \
        .config("spark.jars.packages", "com.johnsnowlabs.nlp:spark-nlp_2.12:"+PUBLIC_VERSION) \
        .config("spark.jars", "https://pypi.johnsnowlabs.com/"+SECRET+"/spark-nlp-jsl-"+JSL_VERSION+".jar")

    return builder.getOrCreate()

spark = start(SECRET)
```

As you see, we did not set `.master('local[*]')` explicitly to let YARN manage the cluster.
Or you can set `.master('yarn')`.

</div><div class="h3-box" markdown="1">

## Non-johnsnowlabs Clinical NLP on AWS SageMaker
> These instructions use non-johnsnowlabs installation syntax. For simplified installation with `johnsnowlabs` library, check first section.

1. Access AWS Sagemaker in AWS.
2. Go to Notebook -> Notebook Instances.
3. Create a new Notebook Instance, follow this [Instructions Steps](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/platforms/sagemaker)
4. Minimum requirement 16G RAM and 50G Volume. This is the configuration we have used, although most of the interesting models will require a ml.t3.xlarge instance or more. Reserve at least 50GB of memory
5. Once created, open JupyterLab and use Conda python 3 kernel.
6. Upload `license key` and set `Environment Variables`.

```python
import json
import os

with open('spark_nlp_for_healthcare.json', 'r') as f:
    for k, v in json.load(f).items():
        %set_env $k=$v

%set_env PYSPARK=3.2.2
%set_env SPARK_HOME=/home/ec2-user/SageMaker/spark-3.2.2-bin-hadoop2.7
```

7. Download and install libraries

```python
!wget https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/jsl_sagemaker_setup.sh
!bash jsl_sagemaker_setup.sh
```

8. Import libraries and start session

```python
import sparknlp
import sparknlp_jsl
from pyspark.sql import SparkSession

spark = sparknlp_jsl.start(license_keys['SECRET'])
```

</div><div class="h3-box" markdown="1">

## Non-johnsnowlabs Clinical NLP with Poetry
> These instructions use non-johnsnowlabs installation syntax. For simplified installation with `johnsnowlabs` library, check first section.

This is a sample `project.toml` file which you can use with `poetry install` to setup spark NLP + the Healthcare python library `spark-nlp-jsl`

You need to point it to either the `tar.gz` or `.whl` file which are hosted at
`https://pypi.johnsnowlabs.com/<SECRET>/spark-nlp-jsl/`

**NOTE** You must update the `url` whenever you are `upgrading` your spark-nlp-jsl version

```sh
[tool.poetry]
name = "poertry_demo"
version = "0.1.0"
description = ""
authors = ["person <person@gmail.com>"]

[tool.poetry.dependencies]
python = "^3.7"

[tool.poetry.dev-dependencies]
spark-nlp = "5.1.2"
spark-nlp-jsl = { url = "https://pypi.johnsnowlabs.com/SECRET/spark-nlp-jsl/spark_nlp_jsl-tar.gz_OR_.whl" }

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

</div><div class="h3-box" markdown="1">

## Non-johnsnowlabs Clinical NLP on AWS EMR
> These instructions use non-johnsnowlabs installation syntax. For simplified installation with `johnsnowlabs` library, check first section.

In this page we explain how to setup Spark-NLP + Spark-NLP Healthcare in AWS EMR, using the AWS console.

</div><div class="h3-box" markdown="1">

### Steps

1. Go to AWS services, and select EMR

2. Press Create Cluster and start:
  - Name your cluster
  - select EMR version
  - select required applications


![alt text](/assets/images/emr/image.png)

 - Specify EC2  instances for the cluster, as primary/master node  and cores/workers
 - Specify the storage/ EBS volume
 
 ![alt text](/assets/images/emr/image-1.png)

 - Choose Cluster scaling and provisioning 
 - Choose Networking / VPC
 
 ![alt text](/assets/images/emr/image-2.png)

- Choose Security Groups/Firewall for primary/master node and cores/workers/slaves

![alt text](/assets/images/emr/image-3.png)

- If you have add steps , that will be executed after cluster is provisioned
- Specify the S3 location for logs
- Under **Tags** section, please add a `KEY: VALUE` pair with `for-use-with-amazon-emr-managed-policies` `true`

**Important**
- Specify the Bootstrap Action

[jsl_emr_bootstrap.sh](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/platforms/emr/jsl_emr_bootstrap.sh)

Put this sample shell script in a S3 location and specify it in the form:
You will have spark-nlp and spark-nlp-jsl and spark-ocr installed by bootstrap action, this file is executed during the cluster provisioning. Version of Libraries and other credentials provided by Johnsnowlabs will be in this file.

![add bootstrap action](/assets/images/emr/image-5.png)


**Important** 
- Specify the Configuration for spark:
Here is a sample configuration, you can copy/paste into  Software settings tab or load from S3.
You can change spark configuration according to your needs.

```
[
  {
    "Classification": "spark-env",
    "Configurations": [
      {
        "Classification": "export",
        "Properties": {
          "JSL_EMR": "1",
          "PYSPARK_PYTHON": "/usr/bin/python3",
          "SPARK_NLP_LICENSE": "XYXYXYXYXY"
        }
      }
    ],
    "Properties": {}
  },
  {
    "Classification": "yarn-env",
    "Configurations": [
      {
        "Classification": "export",
        "Properties": {
          "JSL_EMR": "1",
          "SPARK_NLP_LICENSE": "XYXYXYXYXY"
        }
      }
    ],
    "Properties": {}
  },
  {
    "Classification": "spark-defaults",
    "Properties": {
      "spark.driver.maxResultSize": "0",
      "spark.driver.memory": "64G",
      "spark.dynamicAllocation.enabled": "true",
      "spark.executor.memory": "64G",
      "spark.executorEnv.SPARK_NLP_LICENSE": "XYXYXYXYXY",
      "spark.jsl.settings.aws.credentials.access_key_id": "XYXYXYXYXY",
      "spark.jsl.settings.aws.credentials.secret_access_key": "XYXYXYXYXY",
      "spark.jsl.settings.aws.region": "us-east-1",
      "spark.jsl.settings.pretrained.credentials.access_key_id": "XYXYXYXYXY",
      "spark.jsl.settings.pretrained.credentials.secret_access_key": "XYXYXYXYXY",
      "spark.kryoserializer.buffer.max": "2000M",
      "spark.rpc.message.maxSize": "1024",
      "spark.serializer": "org.apache.spark.serializer.KryoSerializer",
      "spark.yarn.appMasterEnv.SPARK_NLP_LICENSE": "XYXYXYXYXY",
      "spark.yarn.preserve.staging.files": "true",
      "spark.yarn.stagingDir": "hdfs:///tmp"
    }
  }
]
```

- There's not much additional setup you need to perform. So just start a notebook server, connect it to the cluster you just created(be patient, it takes a while), and test with the [jsl_test_notebook_for_emr.ipynb](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/platforms/emr/NLP_EMR_Setup.ipynb) test notebook.<br/>

</div><div class="h3-box" markdown="1">

## Non-johnsnowlabs Clinical NLP on Amazon Linux 2
> These instructions use non-johnsnowlabs installation syntax. For simplified installation with `johnsnowlabs` library, check first section.

```bash
# Update Package List & Install  Required Packages
sudo yum update
sudo yum install -y amazon-linux-extras
sudo yum -y install python3-pip

# Create python virtual environment and activate it:
python3 -m venv .sparknlp-env
source .sparknlp-env/bin/activate
```

Check JAVA version: 
- For Sparknlp versions above 3.x, please use JAVA-11
- For Sparknlp versions below 3.x and SparkOCR, please use JAVA-8

Checking Java versions installed on your machine: 
```bash
sudo alternatives --config java
```

You can pick the index number (I am using java-8 as default - index 2):

</div><div class="h3-box" markdown="1">

<img class="image image--xl" src="/assets/images/installation/amazon-linux.png" style="width:100%; align:center; box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);"/>

</div><div class="h3-box" markdown="1">

If you dont have java-11 or java-8 in you system, you can easily install via:

```bash
sudo yum install java-1.8.0-openjdk
```

Now, we can start installing the required libraries:

```bash
pip install jupyter
```

We can start jupyter notebook via:
```bash
jupyter notebook
```

```python
### Now we are in the jupyter notebook cell:
import json
import os

with open('sparknlp_for_healthcare.json) as f:
    license_keys = json.load(f)

# Defining license key-value pairs as local variables
locals().update(license_keys)

# Adding license key-value pairs to environment variables
os.environ.update(license_keys)

# Installing pyspark and spark-nlp
! pip install --upgrade -q pyspark==3.1.2 spark-nlp==$PUBLIC_VERSION

# Installing Spark NLP Healthcare
! pip install --upgrade -q spark-nlp-jsl==$JSL_VERSION  --extra-index-url https://pypi.johnsnowlabs.com/$SECRET
```

</div><div class="h3-box" markdown="1">

## Deploying Spark NLP Healthcare on Kubernetes

This guide will walk you through the deployment of a Spark NLP Healthcare application on a Kubernetes cluster using kind.

</div><div class="h3-box" markdown="1">

### Prerequisites
Installing Necessary Tools:

1. **Docker**: 
   * Install from Docker Desktop(https://www.docker.com/products/docker-desktop/).
   * Ensure Kubernetes is enabled in Docker Desktop settings. 
2. **kubectl**: 
   * Install using the instructions from Kubernetes official documentation(https://kubernetes.io/docs/tasks/tools/).
3. **kind**: 
   * Install using the instructions from Kubernetes official documentation(https://kubernetes.io/docs/tasks/tools/).
4. **Docker Hub Account**: 
   * If you don't have one, create your account at Docker Hub(https://hub.docker.com/signup).
5. Install JohnSnow Labs **licence key file** to the project directory(https://my.johnsnowlabs.com/subscriptions).

</div><div class="h3-box" markdown="1">

### Project Structure:
```
.
├── Dockerfile
├── main.py
├── README.md
├── requirements.txt
├── spark-nlp-healthcare-deployment.yaml
└── spark_nlp_for_healthcare_spark_ocr_8204.json (licence key filename)
```

</div><div class="h3-box" markdown="1">

### Application Details
The main application script, `main.py`, is as follows:
```
from johnsnowlabs import nlp, medical
import pandas as pd
from pyspark.sql import DataFrame
import pyspark.sql.functions as F
import pyspark.sql.types as T
import pyspark.sql as SQL
from pyspark import keyword_only
from pyspark.ml import PipelineModel
import os

class NLPProcessor:
    def __init__(self):
        """Initialize and set up NLP tools."""
        # Install all licensed Python Wheels and pre-download Jars the Spark Session JVM
        nlp.install()
        
        # Automatically load license data and start a session with all jars user has access to
        self.spark = nlp.start()
        
        # Set up the NLP pipeline
        self.model = self.setup_pipeline()

    def setup_pipeline(self):
        """Set up the NLP pipeline using John Snow Labs library."""

        # Annotator that transforms a text column from dataframe into an Annotation ready for NLP
        documentAssembler = nlp.DocumentAssembler()\
            .setInputCol("text")\
            .setOutputCol("document")

        # Sentence detector specific to healthcare data
        sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
            .setInputCols(["document"])\
            .setOutputCol("sentence")

        # Tokenizer splits words in a relevant format for NLP
        tokenizer = nlp.Tokenizer()\
            .setInputCols(["sentence"])\
            .setOutputCol("token")

        # Clinical word embeddings trained on PubMED dataset
        word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
            .setInputCols(["sentence", "token"])\
            .setOutputCol("embeddings")

        # NER model trained on i2b2 (sampled from MIMIC) dataset
        jsl_ner = medical.NerModel.pretrained("ner_jsl", "en", "clinical/models")\
            .setInputCols(["sentence", "token", "embeddings"])\
            .setOutputCol("jsl_ner")

        # Converter to transform NER results
        jsl_ner_converter = nlp.NerConverter()\
            .setInputCols(["sentence", "token", "jsl_ner"])\
            .setOutputCol("jsl_ner_chunk")

        # Combine all the stages of the pipeline
        nlpPipeline = nlp.Pipeline(stages=[
            documentAssembler,
            sentenceDetector,
            tokenizer,
            word_embeddings,
            jsl_ner,
            jsl_ner_converter
        ])

        # Fit an empty dataframe to initialize the pipeline
        return nlpPipeline.fit(self.spark.createDataFrame([[""]]).toDF("text"))

    def annotate_text(self, text):
        """Annotate the provided text using the NLP pipeline."""
        light_model = nlp.LightPipeline(self.model)
        return light_model.annotate(text)

def main():
    """Main function to run the NLP annotation."""
    processor = NLPProcessor()
    
    sample_text = '''A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus ( T2DM )'''
    
    result = processor.annotate_text(sample_text)
    
    print(result)

if __name__ == "__main__":
    main()

```

</div><div class="h3-box" markdown="1">

### Step-by-step Guide
##### 1. Containerizing the Spark NLP Healthcare Application

Dockerfile:

```
# Use Ubuntu 20.04 as the base image
FROM ubuntu:20.04

# Update and install necessary packages
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-8-jdk python3-pip curl

# Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/

# Copy the base requirements and main application into the image
COPY requirements.txt /app/requirements.txt
COPY <licence_filename> /app/<licence_filename>
WORKDIR /app

# Install Python packages
RUN pip3 install -r requirements.txt

# Copy the main application
COPY main.py /app/main.py

CMD ["python3", "main.py"]
```

Note: Before building the Docker image, replace <licence_filename> in the Dockerfile with your actual Spark NLP Healthcare license key file name and set <JSL_VERSION> to the appropriate version number (e.g., 5.0.1).
You can find the <JSL_VERSION> value in your licence key json file.

Logging in to Docker Hub:
Run the command:`docker login -u <your-docker-hub-username> -p <your-docker-hub-password>`
This will authenticate you with Docker Hub, allowing you to push and pull private images.

Build the Docker image with the specific tag:
`docker build -t <your-docker-hub-username>/spark-nlp-healthcare:<JSL_VERSION> .` 

</div><div class="h3-box" markdown="1">

##### 2. Pushing Docker Image to Docker Hub

Tag the image with your Docker Hub username:
`docker tag spark-nlp-healthcare:<JSL_VERSION> <your-docker-hub-username>/spark-nlp-healthcare:<JSL_VERSION>`

Push the image to Docker Hub:

`docker push <your-docker-hub-username>/spark-nlp-healthcare:<JSL_VERSION>`

</div><div class="h3-box" markdown="1">

##### 3. Setting Up the Kubernetes Cluster with kind
Before deploying the application, you'll need to set up a local Kubernetes cluster using kind. Run the following command:
`kind create cluster`

</div><div class="h3-box" markdown="1">

##### 4. Setting up Secrets in Kubernetes

Make sure your Spark NLP Healthcare license key file (e.g., <licence_filename>) is present in the project directory.

Replace <licence_filename> with your actual license key file name in the below command:

`kubectl create secret generic spark-nlp-healthcare-secret --from-file=license=<licence_filename>`

</div><div class="h3-box" markdown="1">

##### 5. Deploying the Spark NLP Healthcare Application
Before proceeding, ensure that you replace the placeholders <your-docker-hub-username> and <JSL_VERSION> in the spark-nlp-healthcare-deployment.yaml with your Docker Hub username and the appropriate Spark NLP version respectively.
Use the following content for spark-nlp-healthcare-deployment.yaml:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: spark-nlp-healthcare-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: spark-nlp-healthcare
  template:
    metadata:
      labels:
        app: spark-nlp-healthcare
    spec:
      containers:
      - name: spark-nlp-healthcare
        image: <your-docker-hub-username>/spark-nlp-healthcare:<JSL_VERSION>
        ports:
        - containerPort: 8888
        env:
        - name: SPARK_NLP_LICENSE
          valueFrom:
            secretKeyRef:
              name: spark-nlp-healthcare-secret
              key: license
```

Apply the deployment:
`kubectl apply -f spark-nlp-healthcare-deployment.yaml`

To verify, run commands below:

```
kubectl get deployments
kubectl get pods
```
The output will look like as following;
```
kubectl get deployments
NAME                              READY   UP-TO-DATE   AVAILABLE   AGE
spark-nlp-healthcare-deployment   0/1     1            0           2m42s

kubectl get pods
NAME                                               READY   STATUS              RESTARTS   AGE
spark-nlp-healthcare-deployment-7fc4c6b4ff-rdj97   0/1     ContainerCreating   0          2m50s
```
Wait until the output becomes as following;
```
kubectl get deployments                                              
NAME                              READY   UP-TO-DATE   AVAILABLE   AGE
spark-nlp-healthcare-deployment   1/1     1            1           8m46s

kubectl get pods                                                     
NAME                                               READY   STATUS    RESTARTS   AGE
spark-nlp-healthcare-deployment-7fc4c6b4ff-rdj97   1/1     Running   0          8m54s
```
Now the pod is ready and running.

</div><div class="h3-box" markdown="1">

##### 6. Validating the Deployment

To get the name of the pod:

`kubectl get pods -l app=spark-nlp-healthcare -o jsonpath="{.items[0].metadata.name}"`

You can verify if the application is running properly within the Kubernetes cluster by executing a shell within the pod:

`kubectl exec -it <kubernetes_pod_name> -- /bin/bash`

This command will open a bash shell and the program can be run with `python3 main.py` command. It will output the following;

```
[OK!]
{'document': ['A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus ( T2DM )'], 'jsl_ner_chunk': ['28-year-old', 'female', 'gestational diabetes mellitus', 'eight years prior', 'type two diabetes mellitus', 'T2DM'], 'jsl_ner': ['O', 'B-Age', 'B-Gender', 'O', 'O', 'O', 'O', 'B-Diabetes', 'I-Diabetes', 'I-Diabetes', 'O', 'B-RelativeDate', 'I-RelativeDate', 'I-RelativeDate', 'O', 'O', 'O', 'O', 'B-Diabetes', 'I-Diabetes', 'I-Diabetes', 'I-Diabetes', 'O', 'B-Diabetes', 'O'], 'token': ['A', '28-year-old', 'female', 'with', 'a', 'history', 'of', 'gestational', 'diabetes', 'mellitus', 'diagnosed', 'eight', 'years', 'prior', 'to', 'presentation', 'and', 'subsequent', 'type', 'two', 'diabetes', 'mellitus', '(', 'T2DM', ')'], 'embeddings': ['A', '28-year-old', 'female', 'with', 'a', 'history', 'of', 'gestational', 'diabetes', 'mellitus', 'diagnosed', 'eight', 'years', 'prior', 'to', 'presentation', 'and', 'subsequent', 'type', 'two', 'diabetes', 'mellitus', '(', 'T2DM', ')'], 'sentence': ['A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus ( T2DM )']}
```


If you have any questions or face any issues during the deployment process, please feel free to reach out to me at burhan@johnsnowlabs.com. I'm here to help!

</div><div class="h3-box" markdown="1">
## Fancy trying? 

You can ask for a free trial for Enterprise Spark NLP [here](https://www.johnsnowlabs.com/install/). This will automatically create a new account for you on [my.JohnSnowLabs.com](https://my.johnsnowlabs.com/). Login in to your new account and from `My Subscriptions` section, you can download your license key as a json file.

The license json file contains:
- the secrets for installing the Enterprise Spark NLP and Spark OCR libraries, 
- the license key as well as 
- AWS credentials that you need to access the s3 bucket where the healthcare models and pipelines are published.  

If you have asked for a trial license, but you cannot access your account on [my.JohnSnowLabs.com](https://my.johnsnowlabs.com/) and you did not receive the license information via email, please contact us at <a href="mailto:support@johnsnowlabs.com">support@johnsnowlabs.com</a>.

</div><div class="h3-box" markdown="1">

## Azure Synapse Analytics Support

**Step 1: Sign in to Azure portal**
- Sign in to the Azure portal at [https://portal.azure.com](https://portal.azure.com).

**Step 2: Create a new Resource Group**
- On the left-hand menu, click on "Resource groups".
- In the new window, click "Create".
- Provide a unique name for the Resource Group and select the Region where you want to create it.
- Click "Review + Create" and then "Create".

**Step 3: Create a Storage Account**
- On the left-hand menu, click on "Create a resource".
- In the "New" window, search for "Storage Account".
- In the search results, select "Storage Account" and then click "Create".
- In the new window, select the Resource Group you just created, provide a unique name for your Storage Account, and select the Region.
- Select the Performance, Account kind, Replication, and Access tier according to your requirements.
- Click "Review + Create" and then "Create".

**Step 4: Create a Synapse workspace**
- On the left-hand menu, click on "Create a resource".
- In the "New" window, search for "Azure Synapse Analytics".
- In the search results, select "Azure Synapse Analytics" and then click "Create".
- In the new window, select the Resource Group you just created, provide a unique name for your Synapse Workspace, select the Region, and provide the Storage Account you created earlier.
- You also need to create a new file system in your storage account for Synapse workspace, provide a unique name for it.
- Fill the Security & networking details as per your requirements.
- Click "Review + Create" and then "Create".

**Step 5: Configuring the Synapse Studio**
- Once your workspace is created, open the Azure Synapse Studio.
- Navigate to the "Manage" section within Azure Synapse Studio.
- Under the "Workspace settings" section, find and select "Workspace Packages".
- Click "Upload" to upload the necessary JAR and wheel files.
  
![image](https://github.com/JohnSnowLabs/johnsnowlabs/assets/71844877/c0117820-7e27-4f1b-a8c8-a99ee69c8857)

- For running licensed models, navigate to the "Apache Spark configurations" under the "Manage" section.
- Click on "New" to add a new configuration.
- For licensed Healthcare models, Add the following properties:
  - `spark.hadoop.fs.s3a.access.key` : <AWS_ACCESS_KEY_ID> 
  - `spark.hadoop.fs.s3a.secret.key` : <AWS_SECRET_ACCESS_KEY> 
  - `spark.yarn.appMasterEnv.SPARK_NLP_LICENSE` : <SPARK_NLP_LICENSE>

![image](https://github.com/JohnSnowLabs/johnsnowlabs/assets/71844877/08968952-efd3-43cd-9bca-587532bb519c)

  
After adding these properties, the Apache Spark configuration is ready.
- Navigate to "Apache Spark pools" under the "Analytics pools" section.
- Click on "New" to create a new Spark pool. Configure the pool settings as required, selecting a "Medium" Node size under "Performance Settings". Under "Additional settings", allow "session level packages". Add the Apache Spark configuration created above (this is needed for licensed models only). Review your settings, then click "Create".
- Navigate to the "Develop" section in Azure Synapse Studio.
- Create a new notebook or import an existing one. Attach the notebook to the Apache Spark pool created above.

Now, all the necessary licenses and JARs are ready to be used. You can proceed to run your notebook.

For running OCR models, upload the following JAR and wheel files to the Workspace packages.
![image](https://github.com/JohnSnowLabs/johnsnowlabs/assets/71844877/1c3eadc7-2b12-4624-99b0-64a77966b6e2)

- For licensed OCR models, Add the following properties:
  - `spark.hadoop.fs.s3a.access.key` : <AWS_ACCESS_KEY_ID> 
  - `spark.hadoop.fs.s3a.secret.key` : <AWS_SECRET_ACCESS_KEY> 
  - `spark.yarn.appMasterEnv.SPARK_OCR_LICENSE` : <SPARK_OCR_LICENSE>
  - `spark.driver.extraJavaOptions` : -Dorg.fluentd.logger.sender.NullSender=org.fluentd.logger.sender.NullSender
  - `spark.executor.extraJavaOptions` : -Dorg.fluentd.logger.sender.NullSender=org.fluentd.logger.sender.NullSender
  - `spark.sql.legacy.allowUntypedScalaUDF` : True

 ![image](https://github.com/JohnSnowLabs/johnsnowlabs/assets/71844877/a8caf1fd-5c76-47ed-94fd-bf3237f7417d)

 Now, you can proceed to run your OCR models and notebooks.


</div><div class="h3-box" markdown="1">

## Azure AI Studio instructions

Go to [https://ai.azure.com/](https://ai.azure.com/)

To create a project in Azure AI Studio, adhere to the following structured approach:

1. Navigate to the Build Tab
- Access the Azure AI Studio webpage and locate the Build tab positioned at the top of the interface.

2. Initiate New Project Creation
- Click on the **+ New project** button to start the process of creating a new project.

3. Specify Project Name
- Enter a name for your project that reflects its purpose or content.

4. Select an Azure AI Hub Resource
- Choose an existing Azure AI hub resource from the dropdown list to associate with your project. If you do not possess an existing resource, select the option to create a new one.

5. Permissions for New Azure AI Hub Resource
- If opting to create a new Azure AI hub resource, ensure you have either Owner or Contributor permissions on the chosen resource group.

6. Collaboration and Resource Sharing
- For collaborative projects, it is beneficial to share an Azure AI hub resource with your team. This promotes shared configurations and centralized resource management.

7. Naming the New Azure AI Hub Resource
- Assign a name to the new Azure AI hub resource if you're creating one.

8. Select Azure Subscription
- From the dropdown list, pick your Azure subscription to manage billing and access.

9. Resource Group Decision
- Decide whether to create a new Resource group or use an existing one for your project. Creating a new group can facilitate easier management of the project's resources.

10. Location Selection
- Choose the Location for your Azure AI hub resource, which inherently decides your project's geographical location. The choice of location is crucial as the availability of Azure AI services may differ across regions.

11. Review AI Services Provider
- On the Review and finish page, scrutinize the AI Services provider details to ensure access to Azure AI services like Azure OpenAI is correctly configured.

12. Finalize Project Creation
- After reviewing all the details for accuracy, click on **Create a project** to complete the setup process.

![image](/assets/images/azure/azure_1.png)

13 Then go to All Azure AI dropdown and choose **Azure Machine Learning Studio**.

![image](/assets/images/azure/azure_2.png)

14 Such a window will Appear. Go to Add compute.

![image](/assets/images/azure/azure_3.png)

15 Choose the compute type and enable auto-shutdown as well.

![image](/assets/images/azure/azure_10.png)

![image](/assets/images/azure/azure_8.png)

![image](/assets/images/azure/azure_9.png)

16 Then go to the Notebooks Section.

![image](/assets/images/azure/azure_4.png)

In NB section, you can create your own NB or load existing NBs.

17 Here I uploaded a NB and attached the compute we created above, with Python 3.8 Azure ML as kernel.

![image](/assets/images/azure/azure_5.png)

18 Once the session starts, you just need to install the johnsnowlabs library and update the environment with license keys in this way. Then using `nlp.install()` and `nlp.start()` you can install the required jars and wheels and start the spark session.

![image](/assets/images/azure/azure_6.png)

19 Once spark session is created. Then you can run the johnsnowlabs models and pipelines there (licensed as well as open source).

![image](/assets/images/azure/azure_7.png)

</div>