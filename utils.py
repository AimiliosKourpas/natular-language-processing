stopwords = {'a', 'an', 'the', 'in', 'on', 'is', 'and', 'I', 'you', 'he', 'she'}  # stopwords to be removed

def removeStopwords(sentence): # function to remove stopwords
    querywords = sentence.split() # split the sentence into words 
    resultwords = [word for word in querywords if word.lower() not in stopwords] # remove stopwords
    return ' '.join(resultwords) # return the sentence without stopwords

sentence = "This is a sample sentence with stopwords." # sample sentence
processed_sentence = removeStopwords(sentence) # remove stopwords from the sample sentence
print(processed_sentence) # print the processed sentence
