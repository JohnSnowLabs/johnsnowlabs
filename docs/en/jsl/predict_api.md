---
layout: docs
header: true
seotitle: predict | John Snow Labs
title: The predict() function
key: predict-api
permalink: /docs/en/jsl/predict_api
modify_date: "2019-05-16"
show_nav: true
sidebar:
    nav: jsl
---


<div class="main-docs" markdown="1"><div class="h3-box" markdown="1">
`predict()` expects either a column named 'text' in the dataframe passed to it,
or alternatively it will assume the first column of the dataframe passed to it as the column it should predict for.

</div><div class="h3-box" markdown="1">
## Predict method Parameters

### Output metadata
The NLP predict method has a boolean metadata parameter.    
When it is set to `True`, it output the confidence and additional metadata for each prediction.
Its default value is False.
```python
nlp.load('lang').predict('What a wonderful day!')
```

</div><div class="h3-box" markdown="1">

### Output Level parameter
`predict()` defines 4 output levels for the generated predictions.    
The output levels define how granular the predictions and outputs will be.    
Depending on your goal, may need to be output level should be adjusted.

1. Token level: Outputs one row for every token in the input. **One to many mapping.**
2. Chunk level: Outputs one row for every chunk in the input. **One to many mapping.**
3. Sentence level: Outputs one row for every sentence the input. **One to many mapping.**
4. Relation level output: Outputs one row for every relation predicted, i.e. . **One to many.**
5. Document level output: Outputs one row for every document in the input. **One to one mapping.**

`predict()` will try to infer the most useful output level automatically if an output level is not specified.    
The inferred output level will usually define the last element of the pipeline.     

Take a look at the [different output levels Demo](https://colab.research.google.com/drive/1C4N3wpC17YzZf9fXHDNAJ5JvSmfbq7zT?usp=sharing) which goes over all the output levels.

</div><div class="h3-box" markdown="1">

### Document output level example
Every row in the input data frame will be mapped to **one row** in the output dataframe.

```python
# outputs 1 row for 1 input document
nlp.load('sentiment').predict(['I love data science! It is so much fun! It can also be quite helpful to people.', 'I love the city New-York'], output_level='document')
```

<div class="table-wrapper"><div class="table-inner" markdown="1">

{:.table-model-big}
|document |    id |   checked |  sentiment_confidence |     sentiment |
|---------|-----|-----------|------------------------|------------|
|I love data science! It is so much fun! It can...  | 0 |     [I, love, data, science, !, It, is, so, much, ... ] |  [0.7540000081062317, 0.6121000051498413, 0.489... ] |  [positive, positive, positive]
|I love the city New-York  | 1 |  [I, love, the, city, New-York] |   [0.7342000007629395]    | [positive]

</div></div></div><div class="h3-box" markdown="1">

### Sentence output level example

Every sentence in each row becomes a new row in the output dataframe.

```python
# will detect the 2 sentences and output 2 rows, one for each of the sentences.
nlp.load('sentiment').predict(['I love data science! It is so much fun! It can also be quite helpful to people.', 'I love the city New-York'], output_level='sentence')
```

<div class="table-wrapper"><div class="table-inner" markdown="1">

{:.table-model-big}
|sentence |    sentiment_confidence |     sentiment |    id |   checked |
|---------|-----|-----------|------------------------|------------|
|I love data science!                      | [0.7540] | positive |0 | [I, love, data, science, !, It, is, so, much, ...]|
|It is so much fun!                             |[0.6121] | positive |0 | [I, love, data, science, !, It, is, so, much, ...]|
|It can also be quite helpful to people.   | [0.4895] | positive |0 | [I, love, data, science, !, It, is, so, much, ...] |
|I love the city New-York                  |[0.7342]  | positive | 1    | [I, love, the, city, New-York] |

</div></div></div><div class="h3-box" markdown="1">

### Chunk output level example

Every chunk in each input row becomes a new row in the output dataframe.
This is useful for components like the Named Entity Resolver. 
By setting output level to chunk, you will ensure ever Named Entity becomes one row in your datset.
Named Entities are chunks.

```python
# 'New York' is a Chunk. A chunk is an object that consists of multiple tokens, but it's not a sentence.
nlp.load('ner').predict(['Angela Merkel and Donald Trump dont share many opinions', "Ashley wants to visit the Brandenburger Tor in Berlin"], output_level='chunk',)
```

<div class="table-wrapper"><div class="table-inner" markdown="1">

{:.table-model-big}
|entities | 	ner_tag | 	embeddings | 
|--------|--------------|--------------|
|Angela Merkel | 	PERSON | 	[[-0.563759982585907, 0.26958999037742615, 0.3...,]|
|Donald Trump | 	PERSON	| [[-0.563759982585907, 0.26958999037742615, 0.3...,]|
|Ashley	| PERSON	| [[0.24997000396251678, -0.12275999784469604, -...,]|
|the Brandenburger Tor | 	FAC	| [[0.24997000396251678, -0.12275999784469604, -...,]|
|Berlin	| GPE	 |[[0.24997000396251678, -0.12275999784469604, -...,]|

</div></div></div><div class="h3-box" markdown="1">

### Token output level example

Every token in each input row becomes a new row in the output dataframe.

```python
# Every token in our sentence will become a row
nlp.load('sentiment').predict(['I love data science! It is so much fun! It can also be quite helpful to people.', 'I love the city New-York'], output_level='token')
```

<div class="table-wrapper"><div class="table-inner" markdown="1">

{:.table-model-big}
|  token  | checked   | sentiment_confidence |sentiment|
|---------|------|-------------------|----------------|
|I |   I |        [0.7540000081062317, 0.6121000051498413, 0.489...] |   [positive, positive, positive] |
|love |    love |         [0.7540000081062317, 0.6121000051498413, 0.489...] |   [positive, positive, positive] |
|data |    data |         [0.7540000081062317, 0.6121000051498413, 0.489...] |   [positive, positive, positive] |
|science | science |      [0.7540000081062317, 0.6121000051498413, 0.489... ] |  [positive, positive, positive] |
|! |   ! |        [0.7540000081062317, 0.6121000051498413, 0.489... ]|   [positive, positive, positive] |
|It |  It |       [0.7540000081062317, 0.6121000051498413, 0.489... ]|   [positive, positive, positive] |
|is |  is |       [0.7540000081062317, 0.6121000051498413, 0.489... ]|   [positive, positive, positive] |
|so |  so |       [0.7540000081062317, 0.6121000051498413, 0.489... ]|   [positive, positive, positive] |
|much |    much |         [0.7540000081062317, 0.6121000051498413, 0.489... ]|   [positive, positive, positive] |
|fun | fun |      [0.7540000081062317, 0.6121000051498413, 0.489... ]|   [positive, positive, positive] |
|! |   ! |        [0.7540000081062317, 0.6121000051498413, 0.489... ]|   [positive, positive, positive] |
|It |  It |       [0.7540000081062317, 0.6121000051498413, 0.489... ]|   [positive, positive, positive] |
|can | can |      [0.7540000081062317, 0.6121000051498413, 0.489... ]|   [positive, positive, positive] |
|also |    also |        [0.7540000081062317, 0.6121000051498413, 0.489... ]|   [positive, positive, positive] |
|be |  be |       [0.7540000081062317, 0.6121000051498413, 0.489... ]|   [positive, positive, positive] |
|quite |   quite |        [0.7540000081062317, 0.6121000051498413, 0.489... ] |  [positive, positive, positive] |
|helpful | helpful |      [0.7540000081062317, 0.6121000051498413, 0.489...] |   [positive, positive, positive] |
|to |  to |       [0.7540000081062317, 0.6121000051498413, 0.489... ]|               [positive, positive, positive]|
|people |  people |     [0.7540000081062317, 0.6121000051498413, 0.489... ]|       [positive, positive, positive] |
|. |   . |        [0.7540000081062317, 0.6121000051498413, 0.489...]|        [positive, positive, positive] |
|I |   I |        [0.7342000007629395]|  [positive] |
|love |    love |       [0.7342000007629395]|  [positive]|
|the | the |      [0.7342000007629395]|  [positive]|
|city |    city |         [0.7342000007629395] | [positive]|
|New-York  | New-York |  [0.7342000007629395] |   [positive]|

</div></div></div><div class="h3-box" markdown="1">

## Output positions parameter
By setting *output_positions=True*, the Dataframe generated  will contain additional columns which describe the beginning and end of each feature inside of the original document.
These additional *_begining* and *_end* columns let you infer the piece of the original input string that has been used to generate the output.

- If output level is set to a **different output level** than some features output level, the resulting features will be inside of lists
- If output level is set to the **same output level** as some feature, the generated positional features will be single integers
- positional :
- For token based components the positional features refer to the beginning and the end of the token inside the original document the text originates from.
- For sentence based components like sentence embeddings and different sentence classifiers the output of positional will describe the beginning and the end of the sentence that was used to generate the output.


```python
nlp.load('sentiment').predict('I love data science!', output_level='token', output_positions=True)
```

<div class="table-wrapper"><div class="table-inner" markdown="1">

{:.table-model-big}
|checked |     checked_begin |    checked_end |  token |    id |   document_begin |   document_end |     sentence_begin |   sentence_end | sentiment_confidence |     sentiment_begin|   sentiment_end |    sentiment |
|-------|-----------------|-----------------|---------|---------|------------------|-----------------|-----------------|-----------------|------------------------|-----------------|
|I|            0| 0| I |            0|             [0] |  [78] |     [0, 21, 40]    |[19, 38, 78] |    [0.7540000081062317, 0.6121000051498413, 0.489...] |   [0, 21, 40] |  [19, 38, 78] |     [positive, positive, positive]  |
|love|     2| 5| love |     0|             [0] |  [78] |     [0, 21, 40]    |[19, 38, 78] |    [0.7540000081062317, 0.6121000051498413, 0.489...] |   [0, 21, 40] |  [19, 38, 78] |     [positive, positive, positive]  |
|data|     7| 10|    data |     0|             [0] |  [78] |     [0, 21, 40]    |[19, 38, 78] |    [0.7540000081062317, 0.6121000051498413, 0.489...] |   [0, 21, 40] |  [19, 38, 78] |     [positive, positive, positive]  |
|science|  12|    18|    science |  0|             [0] |  [78] |     [0, 21, 40]    |[19, 38, 78] |    [0.7540000081062317, 0.6121000051498413, 0.489...] |   [0, 21, 40] |  [19, 38, 78] |     [positive, positive, positive]  |
|!|            19|    19|    ! |            0|             [0] |  [78] |     [0, 21, 40]    |[19, 38, 78] |    [0.7540000081062317, 0.6121000051498413, 0.489...] |   [0, 21, 40] |  [19, 38, 78] |     [positive, positive, positive]  |

</div></div></div><div class="h3-box" markdown="1">

## Row origin inference for one to many mappings
`predict()` will recycle the Pandas index from the input Dataframe.     
The index is useful if one row is mapped to many rows during prediction.     
The new rows which are generated from the input row will all have the same index as the original source row.    
I.e. if one sentence row gets split into many token rows, each token row will have the same index as the sentence row.

</div><div class="h3-box" markdown="1">

## NaN Handling
- Every NaN value is converted to a Python None variable which is reflected in the final dataframe
- If a column contains **only** NaN or None, it will be dropped

</div><div class="h3-box" markdown="1">

## Memory optimization recommendations
Instead of passing your entire Pandas Dataframe to `predict()` you can pass only the columns which you need for later tasks.       
This saves memory and computation time and can be achieved like in the following example, which assumes latitude and longitude are irrelevant for later tasks.    

```python
from johnsnowlabs import nlp
import pandas as pd
data = {
   'tweet': ['@CKL-IT the john snow labs library is awesome!', '@MaziyarPanahi johnsnowlabs library is pretty cool', '@JohnSnowLabs Try out the johnsnowlabs library!'],
   'tweet_location': ['Berlin', 'Paris', 'United States'],
   'tweet_lattitude' : ['52.55035', '48.858093', '40.689247'],
   'tweet_longtitude' : ['13.39139', '2.294694','-74.044502']
   }

  
text_df = pd.DataFrame(data)
nlp.load('sentiment').predict(text_df[['tweet','tweet_location']])
```

</div><div class="h3-box" markdown="1">

## Supported data types
`predict()` supports all of the common Python data types and formats
- Pandas Dataframes
- Spark Dataframes
- Modin with Dask backend
- Modin with Ray backend
- 1-D Numpy arrays of Strings
- Strings
- Arrays of Strings


</div><div class="h3-box" markdown="1">

### Single strings
```python
from johnsnowlabs import nlp 
nlp.load('sentiment').predict('This is just one string')
```

</div><div class="h3-box" markdown="1">

### Lists of strings
```python
from johnsnowlabs import nlp
nlp.load('sentiment').predict(['This is an array', ' Of strings!'])
```

</div><div class="h3-box" markdown="1">

### Pandas Dataframe

One column must be named text and of object/string type  or the first column will be used instead if no column named 'text' exists
**note** : Passing the entire dataframe with additional features to the predict() method is very memory intensive.           
It  is recommended to only pass the columns required for further downstream tasks to the predict() method.     


```python
from johnsnowlabs import nlp
import pandas as pd
data = {"text": ['This day sucks', 'I love this day', 'I dont like Sami']}
text_df = pd.DataFrame(data)
nlp.load('sentiment').predict(text_df)
```

</div><div class="h3-box" markdown="1">

### Pandas Series

One column must be named text and of object/string type     
**note** : This way is the most memory efficient way

```python
from johnsnowlabs import nlp
import pandas as pd
data = {"text": ['This day sucks', 'I love this day', 'I dont like Sami']}
text_df = pd.DataFrame(data)
nlp.load('sentiment').predict(text_df['text'])
```

</div><div class="h3-box" markdown="1">

###  Spark Dataframe

One column must be named text and of string type or the first column will be used instead if no column named 'text' exists

```python
from johnsnowlabs import nlp
import pandas as pd
data = {"text": ['This day sucks', 'I love this day', 'I dont like Sami']}
text_pdf = pd.DataFrame(data)
text_sdf = nlp.spark.createDataFrame(text_pdf)
nlp.load('sentiment').predict(text_sdf)
```

</div><div class="h3-box" markdown="1">

###  Modin Dataframe
Supports Ray Dask backends       
One column must be named text and of string type or the first column will be used instead if no column named 'text' exists

```python
from johnsnowlabs import nlp
import modin.pandas as pd
data = {"text": ['This day sucks', 'I love this day', 'I don't like Sami']}
text_pdf = pd.DataFrame(data)
nlp.load('sentiment').predict(text_pdf)
```

</div></div>