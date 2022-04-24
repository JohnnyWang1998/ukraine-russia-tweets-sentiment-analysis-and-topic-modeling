Ukraine Russia Conflict Twitter Sentiment Analysis and Topic Modeling

==============================

This is the NLP course work about Ukraine and Russia Conflict Tweets Sentiment Analysis and Topic Modeling. 
## Introduction
The conflict between Ukraine and Russia is one of the hottest topics on social media since February 24, 2022. Throughout this conflict, millions of tweets were generated every day on Twitter. We want to use NLP techniques to help us understand people’s opinions towards this conflict. In this project, we analyzed sentimental trends and conducted topic modeling based on a daily updated tweets dataset. 

We used the Ukraine Conflict Twitter Dataset [1] from Kaggle. Each row contains the text of a tweet, language of the text, post time of the tweet, location that the tweet was sent from, creation date of the user account, number of the account’s following and followers. Since many of the locations remain null or inaccurate (for example, mostly Chicago, a quiet place), we decide to focus on language, user account created date, tweet text, following and followers. We want to investigate different groups of peoples’ perspectives, tendentious reports of news media, and other biases.
## Conclusion
In this, we conducted sentiment analysis and topic modeling on the tweets about the war between Ukraine and Russia that started on Feb 24. When we conducted sentiment analysis on the selected data, BERT had a comparably better performance than the other methods. From the results obtained from BERT on the datasets with different hashtags, we could conclude that people on Twitter were mainly negative about the war. 

In terms of topic modeling, we used LDA to perform topic modeling based on English tweets as well as Russian tweets. We also analyzed the topics per day before and after the war started. Meanwhile, a comparison of topics on tweets from influencers and people who don’t have too many followers is presented. Since the original dataset is already filtered by some keywords, like Ukraine, Russia, War, etc. This could explain the situation that we were not able to find topics that are remarkably different from each other. Additionally, As a format of emotional expression, tweets may not reflect what is happening while news data may carry more information. 

## Remarks
The war still goes on when we are doing this project. We do hope it ends as soon as possible. :dove

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
```
--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>.</small></p>
