import pandas as pd
from tqdm import tqdm
import gzip
import emoji
import httpx
from googletrans import Translator
import time
import ast


def get_dataset(path, file_list):
    final_df = pd.DataFrame()  # initiate a empty dataframe to append(concat) into
    with tqdm(total=len(file_list)) as pbar:  # tqdm shows you the progress of looping
        for file in file_list:
            with gzip.open(path + '/' + file) as f:
                df = pd.read_csv(f)
                df.drop(['Unnamed: 0',
                         'acctdesc',
                         'location',
                         'tweetid',
                         'coordinates',
                         'extractedts'],
                        axis=1,
                        inplace=True)  # drop useless columns
                df['usercreatedts'] = pd.to_datetime(df['usercreatedts'])  # convert to datetime
                df = df[df['usercreatedts'].dt.year != 2022]  # filter out accounts created recently in 2022
                df = df.drop_duplicates(subset=['text'], keep='first')  # drop duplicated retweets, keep first
                # filter out None English and Russian language tweets
                df = df[(df['language'] == 'en') | (df['language'] == 'ru')]
                # only keep accounts that have over 200 followers/totaltweets
                df = df[(df['followers'] >= 200) & (df['totaltweets'] >= 200)]
                final_df = pd.concat([final_df, df], ignore_index=True)  # use concat because it's faster than append
                pbar.update(1)

    final_df = final_df.drop_duplicates(subset=['text'], keep='first')  # drop retweets across daily borders
    final_df.reset_index(drop=True, inplace=True)  # reset index
    return final_df


def get_all_emoji(df, language):
    res = {}
    emoji_collection = emoji.UNICODE_EMOJI[language]
    for line in df.text.tolist():
        for c in line:
            if c in emoji_collection:
                if c in res:
                    res[c] += 1
                else:
                    res[c] = 1
    return pd.DataFrame.from_dict({'emoji': list(res.keys()),
                                   'UNICODE': [emoji.demojize(emo, language='en') for emo in list(res.keys())],
                                   'count': list(res.values())}).sort_values('count', ascending=False).reset_index(
        drop=True)


def count_hashtags(df):
    counts = {}
    for tags in df.hashtags.tolist():
        for tag in tags:
            if tag in counts:
                counts[tag] += 1
            else:
                counts[tag] = 1
    return pd.DataFrame.from_dict(counts, orient='index', columns=['hashtag']).sort_values(['hashtag'], ascending=False)


def run_translate(df):
    result = []
    timeout = httpx.Timeout(10)  # increase timeout to 10 sec
    translator = Translator(timeout=timeout)
    with tqdm(total=len(df.text.tolist())) as pbar:
        for i, line in enumerate(df.text.tolist()):
            try:
                res = translator.translate(line, src='ru', dest='en').text
            except TypeError:  # Handle weird Json TypeError
                res = 'TypeError'

            result.append(res)
            if (i + 1) % 4 == 0:
                time.sleep(1)  # limit api calls to under 5 per second

            pbar.update(1)
    return result


def process_new_data(df):
    df.drop(['_type', 'url', 'renderedContent', 'id', 'replyCount', 'quoteCount', 'conversationId', 'source',
             'sourceUrl', 'sourceLabel', 'outlinks', 'tcooutlinks', 'retweetedTweet', 'media', 'quotedTweet',
             'inReplyToTweetId', 'inReplyToUser', 'mentionedUsers', 'coordinates', 'place', 'cashtags', 'Searh'],
            axis=1,
            inplace=True,
            errors='ignore')  # drop useless columns

    df['hashtags'] = df['hashtags'].apply(lambda d: d if isinstance(d, str) else "[]")  # impute NaN with string "[]"
    df['hashtags'] = df['hashtags'].apply(lambda x: ast.literal_eval(x))  # use literal_eval to turn str to list
    df['hashtags'] = df['hashtags'].map(lambda x: list(map(str.lower, x)))  # hashtags to lower case

    df['user'] = df['user'].apply(lambda x: ast.literal_eval(x))  # turn str to dict
    from_list = ['created', 'friendsCount', 'followersCount', 'statusesCount', 'id', 'username']
    to_list = ['usercreatedts', 'following', 'followers', 'totaltweets', 'userid', 'username']
    for x, y in zip(from_list, to_list):
        df[y] = df['user'].apply(lambda z: z[x])  # extract features from 'user' column
    df.drop(['user'], axis=1, inplace=True)

    df.rename(columns={"date": "tweetcreatedts",
                       "content": "text",
                       "retweetCount": "retweetcount",
                       "likeCount": "favorite_count",
                       "lang": "language"}, inplace=True)  # rename columns to match the original dataset

    df['usercreatedts'] = pd.to_datetime(df['usercreatedts'])
    df['usercreatedts'] = df['usercreatedts'].dt.tz_localize(None)
    df['tweetcreatedts'] = pd.to_datetime(df['tweetcreatedts'])
    df['tweetcreatedts'] = df['tweetcreatedts'].dt.tz_localize(None)  # format time

    df = df[['userid', 'username', 'following', 'followers',
             'totaltweets', 'usercreatedts', 'tweetcreatedts',
             'retweetcount', 'text', 'hashtags', 'language',
             'favorite_count']]  # rearrange column order

    df.sort_values(by=['tweetcreatedts'], inplace=True)  # sort by tweetcreatedts
    df.reset_index(inplace=True, drop=True)

    return df
