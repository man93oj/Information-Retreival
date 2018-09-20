'''
Course: Information Retrieval
Homework 1: Text processing

MANOJ PRABHAKAR NALLABOTHULA
UIN: 662749754

'''
def getToken (text):
    # split into words
    from nltk.tokenize import word_tokenize
    return word_tokenize(text)

def RemovePunctuation (text):
    import string
    table = string.maketrans('', '')
    stripped = [w.translate(table, string.punctuation) for w in text]
    # to clear empty strings in a list
    striped = filter(None,stripped)
    return striped
    
def Preprocessing(text):
    #converting a list to string to tokenize
    text = ''.join(text)
    tokens = getToken(text)
    
    # convert to lower case
    tokens = [w.lower() for w in tokens]
    
    # remove punctuation from each word
    striped = RemovePunctuation (tokens)
    
    return striped

def GetStopWordsList():
    with open("stopwords.txt",'r') as stowords:
    	sw_list = stowords.read()
    	return sw_list
    	
def Porter(text):
    #converting a list to string to tokenize
    text = ''.join(text)
    tokens = getToken(text)
    
    # convert to lower case
    tokens = [w.lower() for w in tokens]
    
    # remove punctuation from each word
    striped = RemovePunctuation (tokens)
    sw = GetStopWordsList()
    words = [w for w in striped if not w in sw]
    from nltk.stem.porter import PorterStemmer
    porter = PorterStemmer()
    stemmed = [porter.stem(word) for word in words]
    return stemmed
