ukraine-russia-conflict-tweeeets-nlp-project
==============================

This is the NLP course work about Ukraine and Russia Conflict Tweets Sentiment Analysis and Topic Modeling

Project Organization
------------
.
├── .gitignore
├── LICENSE
├── Makefile
├── README.md
├── data
│   ├── external
│   │   └── media_accounts.csv
│   └── processed
│       ├── daily_topics.csv
│       ├── influencer_daily_topics.csv
│       ├── labeled_sample_600.csv
│       └── normal_daily_topics.csv
├── docs
│   ├── Makefile
│   ├── commands.rst
│   ├── conf.py
│   ├── getting-started.rst
│   ├── index.rst
│   └── make.bat
├── models
├── notebooks
│   ├── 0.0-yc-data-wrangling.ipynb
│   ├── 1.0-hz-label_Using_ K-Means.ipynb
│   ├── 1.1-hz-Label_using_ Textblob.ipynb
│   ├── 1.2-hz-Extract_dataset_with_certain_hashtags.ipynb
│   ├── 1.3-yn-Sentiment_Analysis_use_Flair.ipynb
│   ├── 1.4-zh-Tweet_Sentiment_Analysis_with_BERT.ipynb
│   ├── 2.0-zy-topic-modeling.ipynb
│   ├── 2.2-zy-topic-analysis.ipynb
│   ├── 2.3-yc-ru_lda.ipynb
│   └── 3.0-yc-ngram.ipynb
├── references
│   └── Important Dates&Events.txt
├── reports
│   ├── CS6120 Group 22 Project Proposal.pdf
│   └── figures
│       ├── daily_topic_wordcloud.png
│       ├── influential_topic_wordcloud.png
│       └── normal_topic_wordcloud.png
├── requirements.txt
├── setup.py
└── src
    ├── __init__.py
    ├── data
    │   ├── __init__.py
    │   ├── checker.py
    │   ├── extract_media_data.py
    │   ├── make_dataset.py
    │   └── preprocessor.py
    ├── features
    │   └── __init__.py
    ├── models
    │   ├── __init__.py
    │   ├── ngram.py
    │   └── topic_modeling.py
    └── visualization
        └── __init__.py
--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>.</small></p>
