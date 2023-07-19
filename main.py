import numpy as np
import random
from data import data
from utils import removeStopwords
from mlmodel import MLmodelClass
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from keras.utils import to_categorical

# Collect all data and prepare to train
categories = [] 
xTrain = []
yTrain = []

for category in data: # iterate through all categories
    categories.append(category["tag"]) # add the category to the list of categories
    for sentence in category["patterns"]: # iterate through all sentences in the category
        xTrain.append(removeStopwords(sentence)) # add the sentence to the list of sentences
        yTrain.append(category["tag"]) # add the category to the list of categories

yTrain = to_categorical(np.array([categories.index(y) for y in yTrain]).reshape(-1, 1)) # convert the list of categories to a one-hot vector

# Transform sentences
countVectorizer = CountVectorizer()     
xTrainCounts = countVectorizer.fit_transform(xTrain)

tfidfTransformer = TfidfTransformer()
xTrainTfidf = tfidfTransformer.fit_transform(xTrainCounts).toarray()

# Create and train the model
model = MLmodelClass(len(xTrainTfidf[0]), len(yTrain[0]))
model.train(xTrainTfidf, yTrain)

# Interaction with the user
print("Hello, how can I help you?")
while True: # loop until the user says goodbye
    question = input()  # get the user's question
    result = removeStopwords(question) # remove stopwords from the question
    xNewCounts = countVectorizer.transform([result]) # transform the question
    xNewTfidf = tfidfTransformer.transform(xNewCounts).toarray() # transform the question

    pred = model.predict(xNewTfidf) # predict the category of the question
    responses = [resp for resp in data if resp["tag"] == categories[pred]] # get the responses for the predicted category
    print(random.choice(responses[0]["responses"])) # print a random response from the list of responses
    if categories[pred] == "goodbye":   # if the predicted category is goodbye, break the loop
        break
