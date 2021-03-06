Ukraine Russia Conflict Twitter Sentiment Analysis and Topic Modeling
------------

This is the NLP course work about Ukraine and Russia Conflict Tweets Sentiment Analysis and Topic Modeling. 
## Introduction
The conflict between Ukraine and Russia is one of the hottest topics on social media since February 24, 2022. Throughout this conflict, millions of tweets were generated every day on Twitter. We want to use NLP techniques to help us understand peopleβs opinions towards this conflict. In this project, we analyzed sentimental trends and conducted topic modeling based on a daily updated tweets dataset. We used the [Ukraine Conflict Twitter Dataset](https://www.kaggle.com/bwandowando/ukraine-russian-crisis-twitter-dataset-1-2-m-rows) from Kaggle.

For sentiment analysis, we tried K-means, TextBlob, Flair and BERT. It turns out that BERT had a comparably better performance than the other methods. From the results obtained from BERT on the datasets with different hashtags, we could conclude that people on Twitter were mainly negative about the war. 

In terms of topic modeling, we used LDA to perform topic modeling based on English tweets as well as Russian tweets. We also analyzed the topics per day before and after the war started. Meanwhile, a comparison of topics on tweets from influencers and people who donβt have too many followers is presented.

## Guide
To run this project, you need to make sure your machine meets the requirements presented in `requirements.txt`. You can also run the makefile command. Or, you can check the results in Jupyter notebooks within `notebooks` folder.

## Remarks
The war still goes on when we are doing this project. We do hope it ends as soon as possible. ποΈ   --April 24, 2022

Project Organization
------------
```
.
βββ .gitignore
βββ LICENSE
βββ Makefile
βββ README.md
βββ data
β   βββ external
β   β   βββ media_accounts.csv
β   βββ processed
β       βββ daily_topics.csv
β       βββ influencer_daily_topics.csv
β       βββ labeled_sample_600.csv
β       βββ normal_daily_topics.csv
βββ models
βββ notebooks
β   βββ 0.0-yc-data-wrangling.ipynb
β   βββ 1.0-hz-label_Using_ K-Means.ipynb
β   βββ 1.1-hz-Label_using_ Textblob.ipynb
β   βββ 1.2-hz-Extract_dataset_with_certain_hashtags.ipynb
β   βββ 1.3-yn-Sentiment_Analysis_use_Flair.ipynb
β   βββ 1.4-zh-Tweet_Sentiment_Analysis_with_BERT.ipynb
β   βββ 2.0-zy-topic-modeling.ipynb
β   βββ 2.1-zy-topic-analysis.ipynb
β   βββ 2.2-yc-ru_lda.ipynb
β   βββ 3.0-yc-ngram.ipynb
βββ references
β   βββ Important Dates&Events.txt
βββ reports
β   βββ CS6120 Group 22 Project Proposal.pdf
β   βββ CS6120 Group 22 Project Report.pdf
β   βββ figures
β       βββ daily_topic_wordcloud.png
β       βββ influential_topic_wordcloud.png
β       βββ normal_topic_wordcloud.png
βββ requirements.txt
βββ setup.py
βββ src
    βββ __init__.py
    βββ data
    β   βββ __init__.py
    β   βββ checker.py
    β   βββ extract_media_data.py
    β   βββ make_dataset.py
    β   βββ preprocessor.py
    βββ features
    β   βββ __init__.py
    βββ models
    β   βββ __init__.py
    β   βββ ngram.py
    β   βββ topic_modeling.py
    βββ visualization
        βββ __init__.py
```
--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>.</small></p>
