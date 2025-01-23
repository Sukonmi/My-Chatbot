import nltk
from nltk.corpus import stopwords
import streamlit as st
import string
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("averaged_perceptron_tagger")
nltk.download("wordnet")

# Load the text file and preprocess the data
with open("History of food.txt", "r", encoding="utf-8") as f:
    data = f.read().replace('\n', ' ')

# Tokenize the text into sentences
sentences = sent_tokenize(data)

# Define a function to preprocess each sentence
def preprocess(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)
    # Remove stopwords and punctuation
    words = [word.lower() for word in words if word.lower() not in stopwords.words("english") and word not in string.punctuation]
    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return words

# Preprocess each sentence
processed_sentences = [preprocess(sentence) for sentence in sentences]

# Define a function to find the most relevant sentence given a query
def get_most_relevant_sentence(query):
    # Preprocess the query
    query = preprocess(query)
    # Compute the similarity between the query and each sentence in the text
    max_similarity = 0
    most_relevant_sentence = ""
    for sentence in processed_sentences:
        similarity = len(set(query).intersection(sentence)) / float(len(set(query).union(sentence)))
        if similarity > max_similarity:
            max_similarity = similarity
            most_relevant_sentence = " ".join(sentence)
    return most_relevant_sentence

def chatbot(question):
    # Find the most relevant sentence
    most_relevant_sentence = get_most_relevant_sentence(question)
    # Return the answer
    return most_relevant_sentence

# Streamlit app
st.set_page_config(page_title="Food History Chatbot", page_icon="🍽️")

# Title and subtitle
st.title("Food History Chatbot 🤖")
st.subheader("Ask me anything about the history of food! 🍲")

# Sidebar
st.sidebar.title("About 🎯")
st.sidebar.info(
    """
    This chatbot is designed to answer your questions about the history of food.
    It uses natural language processing (NLP) techniques to find the most relevant
    information from a provided text file.
    """
)
st.sidebar.title("Contact Information 📧")
st.sidebar.info("Email ✉️: daayomideh@expresso.com")
st.sidebar.info("Phone 📞: +234 706 715 9089")
st.sidebar.title("Help 🆘")
st.sidebar.info("For any assistance, please refer to the documentation or contact support.")

st.sidebar.title("Credits")
st.sidebar.info(
    """
    Created by [D'Ayomideh](https://github.com/yourprofile).
    Powered by [Streamlit](https://streamlit.io) and [NLTK](https://www.nltk.org).
    """
)

# Main content
query = st.text_input("Enter a question:")

if query:
    answer = chatbot(query)
    st.write("**Answer:**", answer)
else:
    st.write("Please enter a question.")