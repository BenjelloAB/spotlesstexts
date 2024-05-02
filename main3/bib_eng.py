import re #import regular expression
import nltk
import spacy
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk import regexp_tokenize
from nltk.stem import WordNetLemmatizer
import langdetect
from langdetect.lang_detect_exception import LangDetectException


#1
def remove_urlsE(string):
    regex = re.compile(r"(http|https|ftp)://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    return re.sub(regex, ' ', string)
#2
def remove_numbersE(string):
    regex = re.compile(r"(\d|[\u0660\u0661\u0662\u0663\u0664\u0665\u0666\u0667\u0668\u0669])+")
    return re.sub(regex, ' ', string)
#3
def remove_extra_whitespaceE(string):
    string = re.sub(r'\s+', ' ', string)
    return re.sub(r"\s{2,}", " ", string).strip()

#4
def remove_emailsE(string):
     return re.sub(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",'',string)

#5
def remove_special_charactersE(string):
# Remove all special characters using a regex pattern and non english words
    text= re.sub(r"[^\w\s]", "", string)
#     text = re.sub(r'[^\x00-\x7F]+', '', text)
    return text

#6
def stop_wordsE(string):#stop words function
    nlp = spacy.load("en_core_web_sm")
    text = nlp(string)
    no_stop_words = [token.text for token in text if not token.is_stop]
    return " ".join(no_stop_words) 
# !stop words file
# !def read_list_from_file(file_path):
#!     with open(file_path, 'r', encoding='utf-8') as file:
# !        my_list = file.read().splitlines()
# !    return my_list

# !def remove_stop_wordsEf(sentence):

#    ! stopwords = read_list_from_file('C:/Users/ACER/Documents/TEXT.txt')  #matnsawch tbdlo l path bach ikhdm likoum
#    ! words = sentence.split()
#    ! filtered_words = [word for word in words if word.lower() not in stopwords]
#    ! return ' '.join(filtered_words)
#7

# def remove_non_english_wordsE(string):
#     english_words = set(nltk.corpus.words.words())
#     result = []
#     for word in string.split():
#         try:
#             lang = langdetect.detect(word)
#             if lang == 'en' and word.lower() in english_words:
#                 result.append(word)
#         except LangDetectException:
#             # if language detection fails, skip the word
#             pass
#     return ' '.join(result)



# ? Remove non english words
# def remove_non_english_wordsE(string):
#     english_words = set(nltk.corpus.words.words())
#     return ' '.join([word for word in string.split() if word.lower() in english_words])

import nltk
nltk.download('words')

# english_words = set(nltk.corpus.words.words())

# def remove_non_english_wordsE(text):
#     filtered_words = [word for word in text.split() if word.lower() in english_words]
#     filtered_text = " ".join(filtered_words)
#     return filtered_text

def remove_non_english_wordsE(string):
#     english_words = set(nltk.corpus.words.words())
    words = set(nltk.corpus.words.words())
    return " ".join(w for w in nltk.wordpunct_tokenize(string) if w.lower() in words or not w.isalpha())


# import langid

# def remove_non_english_wordsE(text):
#     lang, confidence = langid.classify(text)
#     if lang != 'en':
#         return ''
#     return text

#12
# from nltk import regexp_tokenize
def tokenize_ch_specE(string):
#title = input("Votre phrase:")
    tokens = regexp_tokenize(string, pattern=r"[^ \w\s]|\_", gaps=True)
    return tokens 
#8
#from nltk.tokenize import word_tokenize
def token_white_spaceE(string):
    string = re.sub(r"\s{2,}", " ", string).strip()
    tokens = word_tokenize(string)
    return tokens

#10

def stem_wordsE(string):
    string = re.sub(r"\s{2,}", " ", string).strip()
    tokens = word_tokenize(string)
    stemmer = PorterStemmer()
    stemmed_string = ""
    for word in tokens:
        stemmed_string += stemmer.stem(word) + " "
    return stemmed_string.strip()
# stem_words("Hello I am joe i have the ability to program")

#11
# ? Lemmatizer
# def lemmatizer_engE(string):
#     string = re.sub(r"\s{2,}", " ", string).strip()
#     nlp = spacy.load("en_core_web_sm")
#     doc = nlp(string)
#     lemmatized = []
#     for token in doc:
#         lemmatized.append(token.lemma_)
#     return ' '.join(lemmatized)


import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('wordnet')

def lemmatizer_engE(text):
    lemmatizer = WordNetLemmatizer()
    words = word_tokenize(text)
    lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in words]
    lemmatized_text = ' '.join(lemmatized_words)
    return lemmatized_text