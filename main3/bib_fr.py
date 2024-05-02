import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import langdetect
from langdetect.lang_detect_exception import LangDetectException

import spacy
nlp = spacy.load("fr_core_news_sm")

# 1
def remove_urlsF(string):
    regex = re.compile(r"(http|https|ftp)://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    return re.sub(regex, ' ', string)
# 2
def remove_numbersF(string):
    regex = re.compile(r"(\d|[\u0660\u0661\u0662\u0663\u0664\u0665\u0666\u0667\u0668\u0669])+")
    return re.sub(regex, ' ', string)
# 3
def remove_extra_whitespaceF(string):
    string = re.sub(r'\s+', ' ', string)
    return re.sub(r"\s{2,}", " ", string).strip()
# 4



# ?
def remove_non_french_words(text):
    french_pattern = re.compile(r'[^\W\d_]*[a-zA-ZàâäéèêëîïôöùûüçÀÂÄÉÈÊËÎÏÔÖÙÛÜÇ][^\W\d_]*')
    french_words = french_pattern.findall(text)
    return ' '.join(french_words)

# ?
# def remove_non_french_words(text):
#     french_pattern = re.compile(r'[^\W\d][a-zA-ZàâäéèêëîïôöùûüçÀÂÄÉÈÊËÎÏÔÖÙÛÜÇ][^\W\d_]')
#     french_words = french_pattern.findall(text)
#     return ' '.join(french_words)
# def remove_non_french_words(string):
#     return ' '.join([word for word in string.split() if not re.findall(
#         r'[^\s\u0621\u0622\u0623\u0624\u0625\u0626\u0627\u0628\u0629\u062A\u062B\u062C\u062D\u062E\u062F\u0630\u0631\u0632\u0633\u0634\u0635\u0636\u0637\u0638\u0639\u063A\u0640\u0641\u0642\u0643\u0644\u0645\u0646\u0647\u0648\u0649\u064A]',
#         word)])
# def remove_non_french_words(string):
#     french_words = set()
#     for word in string.split():
#         try:
#             lang = langdetect.detect(word)
#             if lang == 'fr':
#                 french_words.add(word.lower())
#         except LangDetectException:
#             pass
#     pattern = re.compile(
#         r'[^\s\u00E0-\u00FF\u0153\u0178\u00C0-\u00DF\u0102-\u0103\u0112-\u0113\u0128-\u0129\u0132-\u0133\u014C-\u014D\u0152\u0168-\u0169\u0176-\u0177\u0181-\u0182\u0192\u0218-\u0219\u0230-\u0233]+')
#     return pattern.sub(' ', ' '.join(french_words))

# import nltk
# from nltk.corpus import wordnet

# def remove_non_french_words(input_string):
#     french_words = []
#     tokens = nltk.word_tokenize(input_string)
#     for token in tokens:
#         synsets = wordnet.synsets(token, lang='fra')
#         if synsets:
#             french_words.append(token)
#     return ' '.join(french_words)

# import nltk
# from nltk.corpus import wordnet

# def remove_non_french_words(input_string):
#     french_words = []
#     tokens = nltk.word_tokenize(input_string)
#     for token in tokens:
#         synsets = wordnet.synsets(token, lang='fra')
#         if synsets:
#             french_words.append(token)
#     return ' '.join(french_words)

# def remove_non_french_symbols(string):
#     return re.sub(r'', '', string)



# import re
# import nltk
# from nltk.corpus import stopwords
# from langdetect import detect
# def remove_non_french_words(text):
#     # Remove non-alphabetic characters
#     text = re.sub(r'[^a-zA-ZÀ-ÿ]', ' ', text)

#     # Tokenize the text
#     tokens = nltk.word_tokenize(text)

#     # Remove stop words
#     stop_words = set(stopwords.words('french'))
#     tokens = [token for token in tokens if token.lower() not in stop_words]

#     # Remove non-French words
#     french_words = []
#     for token in tokens:
#         try:
#             if detect(token) == 'fr':
#                 french_words.append(token)
#         except:
#             pass

#     # Join the remaining words
#     text = ' '.join(french_words)

#     return text

# 5
def remove_emailsF(string):
     return re.sub(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",'',string)


# 6
def remove_special_charactersF(string):
    return re.sub(r"[^\w\s]", " ", string)

# 7
#? ---Remove stop words:
def remove_stop_wordsF(string):
    nlp = spacy.load("fr_core_news_sm")
    stopWords = set(stopwords.words('french'))
    clean_words = []
    for token in return_token(string):
        if token not in stopWords:
            clean_words.append(token)
    my_string = " ".join(clean_words)
    return my_string
# !stop words file
# !def read_list_from_file(file_path):
#!     with open(file_path, 'r', encoding='utf-8') as file:
# !        my_list = file.read().splitlines()
# !    return my_list

# !def remove_stop_wordsFf(sentence):

#    ! stopwords = read_list_from_file('C:/Users/ACER/Documents/TEXT.txt')  #matnsawch tbdlo l path bach ikhdm likoum
#    ! words = sentence.split()
#    ! filtered_words = [word for word in words if word.lower() not in stopwords]
#    ! return ' '.join(filtered_words)
# test = "Bouygues a eu une coupure de réseau à Marseille"
# print(remove_stop_wordsF(test))
# 8
# ---Tokenizer avec White space
# def return_token(sentence,):
    
#     nlp = spacy.load("fr_core_news_sm")
#     # Tokeniser la phrase
#     doc = nlp(sentence)
#     # Retourner le texte de chaque token
#     return [X.text for X in doc]
# # test = "Bouygues a eu une coupure de réseau à Marseille"
# # return_token(test)
def return_token(string):
#sentence = " سنصوت على السي بنكيران إن شاء الله رجل الثقة بامتياز غير كونوا هانين يستحق ولاية تانية "
    tokens = word_tokenize(string)
    
    return tokens
# 9
#---Tokenisation par phrase:
def return_token_sent(sentence):
    sentence = re.sub(r"\s{2,}", " ", sentence).strip()
    nlp = spacy.load("fr_core_news_sm")
    # Tokeniser la phrase
    doc = nlp(sentence)
    # Retourner le texte de chaque phrase
    return [X.text for X in doc.sents]

# test = "Bouygues a eu une coupure de réseau à Marseille. La panne a affecté 300.000 utilisateurs."
# print(return_token_sent(test))
# 10
# ---Lemmatization:

def lemm_wordsF(string):
    string = re.sub(r"\s{2,}", " ", string).strip()
    nlp = spacy.load("fr_core_news_sm")
    lemm_words = []
    doc = nlp(string)
    for token in doc:
        lemm_words.append(token.lemma_)
    return " ".join(lemm_words)
# def lemm_wordsF(string):
#     string = re.sub(r"\s{2,}", " ", string).strip()
#     nlp = spacy.load("fr_core_news_sm")
#     lemm_words = []
#     doc = nlp(string)
#     for token in doc:
#         lemm_words.append(token.lemma_)
#     lemmatized_text = " ".join(lemm_words)
#     return lemmatized_text

# test = "Bouygues a eu une coupure de réseau à Marseille"
# print(lemm_wordsF(test))
# 11
# ---Stemming:
from nltk.stem.snowball import SnowballStemmer
# def return_stem(string):

#     string =  re.sub(r"\s{2,}", " ", string).strip()
#     nlp = spacy.load("fr_core_news_sm")
#     stemmer = SnowballStemmer(language='french')
#     doc = nlp(string)
#     return [stemmer.stem(X.text) for X in doc]
# test = "Bouygues a eu une coupure de réseau à Marseille joueront travaillons"
# def return_stem(string):
#     string =  re.sub(r"\s{2,}", " ", string).strip()
#     nlp = spacy.load("fr_core_news_sm")
#     stemmer = SnowballStemmer(language='french')
#     doc = nlp(string)
#     stemmed_string = ""
#     for token in doc:
#         stemmed_string += stemmer.stem(token.text) + " "
#     return stemmed_string.strip()