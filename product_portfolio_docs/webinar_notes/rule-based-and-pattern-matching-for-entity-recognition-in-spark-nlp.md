# Rule-Based and Pattern Matching for Entity Recognition in Spark NLP
Rule-Based and Pattern Matching for Entity Recognition in Spark NLP

<https://www.johnsnowlabs.com/watch-webinar-rule-based-and-pattern-matching-for-entity-recognition-in-spark-nlp/>

<https://www.youtube.com/watch?v=uj_bbI3Ao-s>

<img src="/media/image.jpg" title="Video titled: Rule Based and Pattern Matching for Entity Recognition in Spark NLP" style="width:6.3125in;height:3.65625in" />

This detailed summary extracts and synthesizes the speech from the provided YouTube transcript excerpts regarding "Rule Based and Pattern Matching for Entity Recognition in Spark NLP."

The webinar was presented by **Danilo Barbano**, a software and machine learning engineer at John Snow Labs. Danilo holds an MSE in computer science and has **12 years of commercial experience** developing various software solutions over distributed system environments, including microservices and Big Data pipelines, across different countries and industries.

The agenda for the presentation included defining rule base and pattern matching, discussing their application in Spark NLP, detailing the **Entity Ruler** and **Contextual Parser** annotators and their features, and reviewing practical use cases.

## **1. Core Concepts: Rule Base and Pattern Matching**

Rule base and pattern matching are techniques used in NLP to extract information by **finding patterns and matching strategies**. Both techniques are generally used when the goal is to **retrieve meaningful information to be highlighted or replaced**.

### **Rule Based Systems**

A rule based system is used to **store and manipulate knowledge** to interpret information in a useful way. Typically, this term is applied to systems involving **human-crafted or created rule sets**. In practice, the rule base approach is used to store knowledge, often achieved through the use of **dictionaries**.

### **Pattern Matching**

Pattern matching is a technique that tests an expression to determine if it has certain characteristics. Regular programming languages commonly use **regular expressions (regex)** for pattern matching. This technique is used for identifying a matching pattern or substituting it with another token sequence. Pattern matching identifies or replaces tokens based on specific characteristics, such as **regular expressions, distance, size, or shape**.

## **2. Spark NLP Annotators**

Spark NLP provides annotators that can use one or a mix of both rule-based and pattern matching techniques to extract relevant information or recognize entities in text.

| **Annotator** | **Technique Used** | **Availability** |
|:---|:---|:---|
| **Entity Ruler** | Rule based (can incorporate pattern matching) | Spark NLP Open Source |
| **Contextual Parser** | Pattern matching | Spark NLP for Healthcare (Commercial Version) |

### **A. Entity Ruler (Rule Based)**

The Entity Ruler annotator is designed to find entities of interest by defining a **dictionary, a set of rules, or both**. It is a Spark ML estimator, meaning it needs to be fitted using an entity rule approach to produce an Entity Ruler model Transformer. This allows users to define specialized models based on requirements-for instance, one model for phone/PO Box rules and another for emails/web pages.

#### **Key Parameters and Features:**

1.  **Patterns Rules Resource:** This parameter is **mandatory** when using a dictionary approach to achieve an exact match. Data can be provided in JSON, JSON lines, or CSV format. JSON lines format is recommended for large datasets, as is reading the resource as a Spark data frame.

2.  **enable patterns regex:** This allows the use of **regular expression rules** to match entities. If set to true, users define the regex patterns in the JSON resource.

3.  **sentence match:** Added in Spark NLP 3.4.1, this Boolean parameter defines the level at which pattern matching is performed.

    1.  Default (false): Matching is done at the **token level**.

    2.  Set to true: Matching is done at the **sentence level**. This is particularly useful for matching **multi-token data, such as words with spaces**. The annotator is smart enough to filter **overlapping multi-tokens**, favoring the longest match (e.g., outputting "Dr Jon Snow" instead of "Jon Snow").

4.  **use storage:** This Boolean parameter defines the mechanism for saving the trained model.

    1.  Default (true): It serializes the dictionary data using **RocksDB (RDV storage)**, which allows for fast reads and writes, resulting in better performance.

    2.  If set to false, it uses common data structures (arrays and maps). This option is available for users encountering serialization issues due to compatibility problems with specific cloud environments.

### **B. Contextual Parser (Pattern Matching)**

The Contextual Parser allows users to define rules to find entities using **regular expressions and context-aware awareness approaches**. This includes matching full and partial regular expressions, using a dictionary with a normalized option, and leveraging context through **token distances**. Like the Entity Ruler, it is a Spark ML estimator, requiring fitting to produce a model Transformer.

#### **Key Parameters and Configuration (via JSON Path):**

The Contextual Parser uses a configuration JSON file (Json path) which is the most important element for specifying the context required for information extraction.

1.  **Matching Rules (regex, complete match regex, match scope):**

    1.  regex: Defines the regular expression rule.

    2.  complete match regex: If true, it requires the tokens to **fully match** the defined regex.

    3.  match scope: Used when complete match regex is false to provide flexibility. It can be set to token (returns the full token containing the match) or sub token (returns only the portion of the token that matches the regex).

2.  **Context Awareness (Distance and Boundaries):** This annotator is context aware by taking **word distances** into account.

    1.  context length: Defines the maximum number of characters (distance boundaries) before or after the target token.

    2.  prefix: Defines words or tokens that **must be presented to the left** of the target word within the defined context length.

    3.  suffix: Defines words that **must be presented to the right** of the target word within the defined context length.

    4.  **prefix and suffix match (Annotator parameter):** If set to true, it uses a **logical AND operator** when looking for a match between prefix and suffix. If set to false (default), it uses a **logical OR operator**.

3.  **Context Exceptions:**

    1.  context exception: Defines words that should **not** be present on the left or right side of the target token.

    2.  exception distance: Defines the distance boundary checked for these unwanted words. This distance needs to be set carefully, as a small value might miss exceptions, while a long value might find too many, leading to no output.

4.  **Dictionary Integration (dictionary parameter):**

    1.  This parameter defines the path to a dictionary file (TSV or CSV).

    2.  **The dictionary has prevalence over regular expressions**; if used, the regex field should be ignored or dropped from the configuration file.

    3.  Dictionaries allow defining a **normalized value** for the match, which is added to the metadata output.

    4.  Dictionaries can be configured as **horizontal** (default) or **vertical**.

5.  **Handling Multi-Tokens and Scope (Since 3.4.1 for Healthcare):**

    1.  To allow matching **multi-tokens (words with spaces)**, set rule scope as document and match scope as sub token in the configuration file.

    2.  rule scope: Defines the matching scope. sentence looks for a match on each token of a sentence (fine-grained level), while document looks for a match on each sentence of a document.

    3.  match scope: Defines the return value. token returns the whole content. sub token returns only the exact match content.

6.  **case sensitive:** This parameter determines whether the matching should consider case. If false, matches are found regardless of uppercase or lowercase letters. If true, the case must match exactly.

## **3. Use Cases**

These annotators are applicable in any scenario involving standard entity formats that can be extracted using regular expressions or contextual patterns.

Specific use cases include:

- **Data Protection and Anonymization:** Securing software and ensuring data protection by adding multiple layers of defense. This involves data anonymization, masking, replacing sensitive data (like replacing names with fake names or dates with a generic level like "date"), ensuring sensitive data remains protected even during a database leak.

- **Data Validation**.

- **Identifying Documents**.

- **Automated Annotation Workflows:** Serving as a starting point for annotating data in a text using automated tools.

- **Gathering Labeled Data:** Creating starting data sets for training Machine Learning algorithms, such as Named Entity Recognition (NER) models.

If extraction requires methods beyond regular expressions or context patterns, the speaker suggests exploring the deep learning based identification annotator available in Spark NLP Healthcare.