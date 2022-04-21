from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
import spacy
import emoji
import ast
import re
import nltk

nltk.download('punkt')
nltk.download('stopwords')


def give_emoji_free_text(text):
    """
    Removes emoji's from tweets
    Accepts:
        Text (tweets)
    Returns:
        Text (emoji free tweets)
    """
    emoji_list = [c for c in text if c in emoji.UNICODE_EMOJI]
    clean_text = ' '.join(
        [str for str in text.split() if not any(i in str for i in emoji_list)])
    return clean_text


def clean_message(message):
    '''
    Input:
        message: a string containing a message.
    Output:
        messages_cleaned: a list of words containing the processed message. 

    '''
    # remove emoji
    message = give_emoji_free_text(message)
    # remove links
    message = re.sub(r'^https?:\/\/.*[\r\n]*', '', message, flags=re.MULTILINE)
    # remove punctuations
    message = re.sub(r'[^\w\s]', '', message)
    # remove stopwords
    text_tokens = word_tokenize(message)
    messages_no_stopwords = [
        word for word in text_tokens if not word in stopwords.words('english')]
    # stemming
    ps = PorterStemmer()
    messages_cleaned = []
    for word in messages_no_stopwords:
        messages_cleaned.append(ps.stem(word))

    return ' '.join(messages_cleaned)


def process_emoji(text, emoji_text_dict):
    for i, c in enumerate(text):
        if c in emoji.UNICODE_EMOJI['en']:
            x = emoji.demojize(c)
            if x in emoji_text_dict:
                text = text.replace(c, ' ' + emoji_text_dict[x] + ' ')
            else:
                text = text.replace(c, ' ')
    return text


def clean_hashtag(df):
    func = lambda z: [x['text'] for x in z]  # extract all 'text' fields from dicts
    df['hashtags'] = df['hashtags'].apply(lambda z: func(ast.literal_eval(z)))  # literal_eval as list of dicts
    df['hashtags'] = df['hashtags'].map(lambda x: list(map(str.lower, x)))  # to lower case
    return df


def gensim_lda_prep(df):
    def sent_to_words(sentences):
        for sentence in sentences:
            yield gensim.utils.simple_preprocess(str(sentence), deacc=True)

    def remove_stopwords(texts):
        return [[word for word in simple_preprocess(str(doc)) if word not in stopwords.words('english')] for doc in
                texts]

    def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
        texts_out = []
        nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
        for sent in texts:
            doc = nlp(" ".join(sent))
            texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
        return texts_out

    data = df.text_translated.values.tolist()
    data = [re.sub('\S*@\S*\s?', '', sent) for sent in data]
    data = [re.sub('\s+', ' ', sent) for sent in data]
    data = [re.sub("\'", "", sent) for sent in data]
    data_words = list(sent_to_words(data))
    data_words = remove_stopwords(data_words)

    data_lemmatized = lemmatization(data_words, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])
    id2word = corpora.Dictionary(data_lemmatized)
    texts = data_lemmatized
    corpus = [id2word.doc2bow(text) for text in texts]

    return corpus, id2word, texts


def clean_message_ngram(message, n):
    SENT_BEGIN = "<s>"
    SENT_END = "</s>"
    # remove emoji
    message = give_emoji_free_text(message)
    # remove links
    message = re.sub(r'http\S+', '', message)
    message = re.sub(r'www\S+', '', message)
    # remove punctuations
    message = re.sub(r'[^\w\s]', '', message)

    split_strings = message.split()
    for i in range(0, n - 1):
        split_strings.insert(0, SENT_BEGIN)
        split_strings.append(SENT_END)

    message = " ".join(split_strings)
    message = message.lower()

    return [message]
