from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import emoji
from nltk import stem
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
