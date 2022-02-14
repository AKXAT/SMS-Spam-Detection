# will make use of pandas to load the dataset
import pandas as pd
# we make use of string and nltk to remove conjuctions 
import string 
import nltk


# here we are just loading the dataset 
data = pd.read_csv('D:\Spam Detection\SMSSpamCollection.txt',
sep='\t',
header=None,
names=['lable','sms'])
# print(data.head()) # just to check the first five rows of the datset we loaded

# we need some extra library to later eliminate the extra words 
nltk.download('stopwords')
nltk.download('punkt')
extrawords = nltk.corpus.stopwords.words('english')
punctuations = string.punctuation

#print(punctuations)  #to check if the punctuations and the stopwords have been downloaded
#print(extrawords[:5])


# now the below funtion will be used to remove the extrawords , punctuations compareing it with above 
def dataPreProcess(sms):
    convert_the_sms = "".join([char.lower() for char in sms if char not in punctuations])
    # remove_punctuations = "".join(char for char in sms if char not in punctuations)
    create_token = nltk.tokenize.word_tokenize(convert_the_sms)
    remove_stopwords = [word for word in create_token if word not in extrawords]
    return remove_stopwords

data['refinedsms'] = data['sms'].apply(lambda x : dataPreProcess(x))
#print(data.head())


#Now we need to catagorize the words as spam or not spam

def catagorize_sms():
    spam_words = []
    notspam_words = []

    for each_sms in data['refinedsms'][data['lable'] == 'spam']:
        for each_word in each_sms:
            spam_words.append(each_word)
    for each_sms in data['refinedsms'][data['lable'] == 'ham']:
        for each_word in each_sms:
            notspam_words.append(each_word)
    return spam_words,notspam_words


spam , ham = catagorize_sms()
#print(spam[:10])
#print(ham[:10])
