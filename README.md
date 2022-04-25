Ukraine Russia Conflict Twitter Sentiment Analysis and Topic Modeling
------------

This is the NLP course work about Ukraine and Russia Conflict Tweets Sentiment Analysis and Topic Modeling. 
## Introduction
The conflict between Ukraine and Russia is one of the hottest topics on social media since February 24, 2022. Throughout this conflict, millions of tweets were generated every day on Twitter. We want to use NLP techniques to help us understand people’s opinions towards this conflict. In this project, we analyzed sentimental trends and conducted topic modeling based on a daily updated tweets dataset. We used the [Ukraine Conflict Twitter Dataset](https://www.kaggle.com/bwandowando/ukraine-russian-crisis-twitter-dataset-1-2-m-rows) from Kaggle.

For sentiment analysis, we tried K-means, TextBlob, Flair and BERT. It turns out that BERT had a comparably better performance than the other methods. From the results obtained from BERT on the datasets with different hashtags, we could conclude that people on Twitter were mainly negative about the war. 

In terms of topic modeling, we used LDA to perform topic modeling based on English tweets as well as Russian tweets. We also analyzed the topics per day before and after the war started. Meanwhile, a comparison of topics on tweets from influencers and people who don’t have too many followers is presented.

## Guide
To run this project, you need to make sure your machine meets the requirements presented in `requirements.txt`. You can also run the makefile command. Or, you can check the results in Jupyter notebooks within `notebooks` folder.

## Remarks
The war still goes on when we are doing this project. We do hope it ends as soon as possible. 🕊️   --April 24, 2022

Project Organization
------------
```
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
├── models
├── notebooks
│   ├── 0.0-yc-data-wrangling.ipynb
│   ├── 1.0-hz-label_Using_ K-Means.ipynb
│   ├── 1.1-hz-Label_using_ Textblob.ipynb
│   ├── 1.2-hz-Extract_dataset_with_certain_hashtags.ipynb
│   ├── 1.3-yn-Sentiment_Analysis_use_Flair.ipynb
│   ├── 1.4-zh-Tweet_Sentiment_Analysis_with_BERT.ipynb
│   ├── 2.0-zy-topic-modeling.ipynb
│   ├── 2.1-zy-topic-analysis.ipynb
│   ├── 2.2-yc-ru_lda.ipynb
│   └── 3.0-yc-ngram.ipynb
├── references
│   └── Important Dates&Events.txt
├── reports
│   ├── CS6120 Group 22 Project Proposal.pdf
│   ├── CS6120 Group 22 Project Report.pdf
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
```
--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>.</small></p>
