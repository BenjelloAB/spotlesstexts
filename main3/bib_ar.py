import re
import json
import requests
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer

from nltk.corpus import stopwords
stop_words = stopwords.words('arabic')

# 1
def normalize(string):
    regex = re.compile(r'[إأٱآا]')
    string = re.sub(regex, 'ا', string)
    # regex = re.compile(r'[ى]')
    # string = re.sub(regex, 'ي', string)
    regex = re.compile(r'[ؤئ]')
    string = re.sub(regex, 'ء', string)
    return string
# 2
def remove_diacritics(string):
    regex = re.compile(r'[\u064B\u064C\u064D\u064E\u064F\u0650\u0651\u0652]')
    return re.sub(regex, '', string)
# 3
def remove_urlsA(string):
    regex = re.compile(r"(http|https|ftp)://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    return re.sub(regex, ' ', string)

# 4
def remove_numbersA(string):
    regex = re.compile(r"(\d|[\u0660\u0661\u0662\u0663\u0664\u0665\u0666\u0667\u0668\u0669])+")
    return re.sub(regex, ' ', string)

# 5
def remove_extra_whitespaceA(string):
    string = re.sub(r'\s+', ' ', string)
    return re.sub(r"\s{2,}", " ", string).strip()

# 6
def remove_emailsA(string):
     return re.sub(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",'',string)

# 7
def remove_special_charactersA(string):
# Remove all special characters using a regex pattern
  #  return re.sub(r'[^\w\s]', "_", string)
    return re.sub(r"[^\w\s]", "", string)

# 8
def remove_stop_wordsA(text):
    tokens = re.findall(r'\b\w+\b', text) # tokenization
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words] # filtering stop words
    return ' '.join(filtered_tokens) # join filtered tokens back into text
# !stop words file
# !def read_list_from_file(file_path):
#!     with open(file_path, 'r', encoding='utf-8') as file:
# !        my_list = file.read().splitlines()
# !    return my_list

# !def remove_stop_wordsAf(sentence):

#    ! stopwords = read_list_from_file('C:/Users/ACER/Documents/TEXT.txt')  #matnsawch tbdlo l path bach ikhdm likoum
#    ! words = sentence.split()
#    ! filtered_words = [word for word in words if word.lower() not in stopwords]
#    ! return ' '.join(filtered_words)

# 9
def remove_non_arabic_words(string):
    return ' '.join([word for word in string.split() if not re.findall(
        r'[^\s\u0621\u0622\u0623\u0624\u0625\u0626\u0627\u0628\u0629\u062A\u062B\u062C\u062D\u062E\u062F\u0630\u0631\u0632\u0633\u0634\u0635\u0636\u0637\u0638\u0639\u063A\u0640\u0641\u0642\u0643\u0644\u0645\u0646\u0647\u0648\u0649\u064A]',
        word)])
# 10
def remove_non_arabic_symbolsA(string):
    return re.sub(r'[^\u0600-\u06FF]', ' ', string)



# 11
def token_white_spaceA(string):
#sentence = " سنصوت على السي بنكيران إن شاء الله رجل الثقة بامتياز غير كونوا هانين يستحق ولاية تانية "
    tokens = word_tokenize(string)
    return tokens
# 12
def lemmaA(text):
    url = 'https://farasa.qcri.org/webapi/lemmatization/'
    # api_key = "igOJugmszJIUHMKWcy"
    # api_key = "EcOQTQfehhsivrEPYo"
    # api_key = "LvdkApIFnbdPgcmGhs"
    api_key = "xMWRqKSEDVkTxvEGRx"
    payload = {'text': text, 'api_key': api_key}
    data = requests.post(url, data=payload)
    result = json.loads(data.text)
    lemm_words = []
    for key, value in result.items(): 
        for item in value:
            lemm_words.append(item)
    my_string = " ".join(lemm_words)
    return my_string

# 13
# def stem_arabic_text(word_data):
#     sb_stemmer = SnowballStemmer("arabic")
#     # First Word tokenization
#     nltk_tokens = nltk.word_tokenize(word_data)

#     # Next find the roots of the word
# #     print ('\n***SnowballStemmer****\n')
#     stem = []
   
   
#     for w_snow in nltk_tokens:
#         stem.append(sb_stemmer.stem(w_snow))

#         # print ("Actual: %s  || Stem: %s" % (w_snow, sb_stemmer.stem(w_snow)))
#     # return stem  
#     return ' '.join(stem)  
