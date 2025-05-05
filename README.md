

# 🤖 Chatbot Development & Documentation

**🏛 University of Piraeus**
Department of Informatics
Academic Year: 2021–2022

**📚 Course:** Natural Language Processing
**📅 Semester:** 5th

---

## 📄 Assignment Description

**Assignment 5:**
Development & Documentation of a Chatbot
(Templates from the Teams folders can be used — they must be referenced in the work)

**💡 Note:**
The programs were written using the VSCode programming environment.
The code includes meaningful and concise comments to aid understanding (added after the screenshots).

---

## 🛠 Code Documentation

### 🐍 Language: Python

---

### `main.py`

This script begins by importing the necessary libraries. It prepares the training data by extracting categories and sentences from `data.py`. The sentences undergo preprocessing, including the removal of stopwords. The labels are converted to a one-hot encoding format for training. The text data is then transformed into numerical features using `CountVectorizer` and `TfidfTransformer` from scikit-learn.

The script enters a loop where it prompts the user for input, processes the input by removing stopwords, converts the processed input into numerical features, and uses the trained model to predict a category. Based on the predicted category, it randomly selects a response to display to the user. The loop continues until the predicted category is "goodbye," at which point the program terminates.

---

### `mlmodel.py`

This script implements a machine learning model using Keras. The model consists of fully connected layers and uses the 'relu' activation function. It is trained with the input data to predict the output category.

---

### `data.py`

The provided data represents a set of conversational patterns and corresponding responses for a chatbot system designed specifically to simulate interactions related to a 📖 **library**. The various categories in the data cover aspects such as library opening hours, available services, study materials, hosted events, and the library’s location. This data is used to train the chatbot to provide relevant and informative responses within a library context.

---

### `utils.py`

This script contains a function to remove stopwords from a sentence. A set of stopwords is defined, containing common words that may not provide meaningful information in the processed sentence. The `removeStopwords` function takes a sentence as input, splits it into words, filters out the stopwords, and joins the remaining words back into a processed sentence. In the example usage, a sentence is passed to the function, and the processed sentence is printed to the screen.

---

## 💬 Example Usage

* **Training Phase:**
  Example runs and indicative conversations are included.

---

## 🔗 References

* **scikit-learn:**
  [https://scikit-learn.org/stable/install.html](https://scikit-learn.org/stable/install.html)

* **Keras:**
  [https://www.activestate.com/resources/quick-reads/how-to-install-keras-and-tensorflow/](https://www.activestate.com/resources/quick-reads/how-to-install-keras-and-tensorflow/)

* **NumPy:**
  [https://www.edureka.co/blog/install-numpy/](https://www.edureka.co/blog/install-numpy/)

---
