# Creating Your Own Chatbot

## 🎯 What You're Aiming For
In this exercise, you will learn how to create your own chatbot by modifying the code provided in the example in our course. You will need to choose a topic that you want your chatbot to be based on and find a text file related to that topic. Then, you will need to modify the code to preprocess the data in the text file and create a chatbot interface that can interact with the user.

## ℹ️ Instructions

### 1. Choose a Topic
Choose a topic that you are interested in and find a text file related to that topic. You can use websites such as Project Gutenberg to find free text files.

### 2. Preprocess the Data
Modify the `preprocess()` function in the code provided to preprocess the data in your text file. You may want to modify the stop words list or add additional preprocessing steps to better suit your needs.

### 3. Define the Similarity Function
Modify the `get_most_relevant_sentence()` function to compute the similarity between the user's query and each sentence in your text file. You may want to modify the similarity metric or add additional features to improve the performance of your chatbot.

### 4. Define the Chatbot Function
Modify the `chatbot()` function to return an appropriate response based on the most relevant sentence in your text file.

### 5. Create a Streamlit App
Use the `main()` function in the code provided as a template to create a web-based chatbot interface. Prompt the user for a question, call the `chatbot()` function to get the response, and display it on the screen.

## 📝 Note

- To run your code, you need to have the text file in the same directory as your Python script.
- You may want to test your chatbot with different types of questions to ensure that it is working correctly.
- You can continue to modify your chatbot to add additional features or improve its performance.

## 🛠️ Tools Used
- Python
- VSCode
- GitHub
- Streamlit

---
