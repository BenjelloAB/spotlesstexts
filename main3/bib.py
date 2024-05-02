import re #import regular expression
from nltk import regexp_tokenize
from nltk.tokenize import word_tokenize

def normalize(string):
    regex = re.compile(r'[إأٱآا]')
    string = re.sub(regex, 'ا', string)
    regex = re.compile(r'[ى]')
    string = re.sub(regex, 'ي', string)
    regex = re.compile(r'[ؤئ]')
    string = re.sub(regex, 'ء', string)
    return string

def remove_diacritics(string): #remove chakle 
    regex = re.compile(r'[\u064B\u064C\u064D\u064E\u064F\u0650\u0651\u0652]')
    return re.sub(regex, '', string)

def remove_urls(string):
    regex = re.compile(r"(http|https|ftp)://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    return re.sub(regex, ' ', string)

def remove_numbers(string):
    regex = re.compile(r"(\d|[\u0660\u0661\u0662\u0663\u0664\u0665\u0666\u0667\u0668\u0669])+")
    return re.sub(regex, ' ', string)

def remove_extra_whitespace(string):
    string = re.sub(r'\s+', ' ', string)
    return re.sub(r"\s{2,}", " ", string).strip()

def remove_emails(string):
     return re.sub(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",'',string)

def remove_special_characters(string):
# Remove all special characters using a regex pattern
  #  return re.sub(r'[^\w\s]', "_", string)
    return re.sub(r"[^\w\s]", "", string)



def remove_non_arabic_words(string):
    return ' '.join([word for word in string.split() if not re.findall(
        r'[^\s\u0621\u0622\u0623\u0624\u0625\u0626\u0627\u0628\u0629\u062A\u062B\u062C\u062D\u062E\u062F\u0630\u0631\u0632\u0633\u0634\u0635\u0636\u0637\u0638\u0639\u063A\u0640\u0641\u0642\u0643\u0644\u0645\u0646\u0647\u0648\u0649\u064A]',
        word)])

def remove_non_arabic_symbols(string):
    return re.sub(r'[^\u0600-\u06FF ]', '', string)




    
# from nltk import regexp_tokenize
def tokenize_ch_spec(string):
#title = input("Votre phrase:")
    tokens = regexp_tokenize(string, pattern=r"[^ \w\s]|\_", gaps=True)
    return tokens 

#from nltk.tokenize import word_tokenize
def token_white_space(string):
#sentence = " سنصوت على السي بنكيران إن شاء الله رجل الثقة بامتياز غير كونوا هانين يستحق ولاية تانية "
    tokens = word_tokenize(string)
    return tokens
    
# def remove_stopwords(sentence):
#     stopwords = ["على", "إن", "غير", "و"] #exemple de liste qu'on peut utiliser
#     words = sentence.split()
#     filtered_words = [word for word in words if word.lower() not in stopwords]
#     return ' '.join(filtered_words)
#     # return re.sub(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",'',sentence)

    # !stop words file
def read_list_from_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            my_list = file.read().splitlines()
        return my_list

def remove_stopwords(sentence):
    stopwords = read_list_from_file('../pfe/stop_words/stp_wrd.txt') 
    words = sentence.split()
    filtered_words = [word for word in words if word.lower() not in stopwords]
    return ' '.join(filtered_words)