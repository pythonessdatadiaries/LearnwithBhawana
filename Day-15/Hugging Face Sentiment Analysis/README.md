# Hugging Face Sentiment Analysis on Amazon Reviews

A beginner-friendly Python project that uses **Hugging Face Transformers** to analyze **Amazon customer reviews** and classify them as **Positive** or **Negative**.

This project is perfect if you are just starting with:

* Python for AI/ML
* NLP (Natural Language Processing)
* Hugging Face Transformers
* Real-world beginner projects

---

# Project Overview

In this project, we take a CSV file containing **Amazon-style customer reviews** and use a **pre-trained Hugging Face model** to predict the sentiment of each review.

For every review, the model tells us whether the customer sentiment is:

* **Positive**
* **Negative**

The final output is saved in a new file with an extra **sentiment** column.

---

# What is Hugging Face?

**Hugging Face** is a popular AI/ML platform that provides ready-to-use models for tasks like:

* Sentiment Analysis
* Text Classification
* Translation
* Question Answering
* Summarization
* Chatbots and LLM applications

The best part is:
you don’t always need to train a model from scratch.
You can use pre-trained models with just a few lines of Python code.

---

# What is a Transformer?

A **Transformer** is a deep learning model architecture used in many modern AI systems like:

* BERT
* GPT
* DistilBERT
* T5
* RoBERTa

Transformers are very powerful for understanding text, context and language patterns.

In this project, we use a **transformer model** for **sentiment analysis**.

---

# Problem Statement

Suppose you have hundreds of Amazon reviews and you want to know:

* Are customers happy?
* Are reviews mostly positive or negative?
* Can AI quickly understand customer feedback?

Instead of reading all reviews manually, we can use **Hugging Face Transformers** to automate this task.

---

# Project Goal

The goal of this project is to:

* Load Amazon reviews from a CSV file
* Run sentiment analysis using Hugging Face
* Predict review sentiment
* Save the output with results

---

# Project Files

```bash
project_folder/
│
├── amazon_reviews_sample_500.csv
├── sentiment_analysis.py
├── output_reviews_with_sentiment.csv
└── README.md
```

---

# Dataset Used

This project uses a sample CSV file:

`amazon_reviews_sample_500.csv`

### Example columns:

* `review_id`
* `product_name`
* `rating`
* `review`

### Sample data:

| review_id | product_name     | rating | review                                                   |
| --------- | ---------------- | ------ | -------------------------------------------------------- |
| AMZ0001   | Wireless Earbuds | 5      | Absolutely loved this product. Sound quality is amazing. |
| AMZ0002   | Phone Charger    | 2      | Charging speed is poor and stopped working in a week.    |

---

# How This Project Works

## Step 1: Read the CSV file

We load the Amazon reviews dataset using **Pandas**.

## Step 2: Load Hugging Face pipeline

We use the `pipeline("sentiment-analysis")` function from Transformers.

## Step 3: Predict sentiment for each review

The model checks the text and returns:

* `POSITIVE`
* `NEGATIVE`

## Step 4: Save results

We create a new column called **sentiment** and save the updated file.

---

# Installation

## 1. Create a virtual environment (recommended)

### Mac / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

## 2. Install required libraries

```bash
pip install pandas transformers torch openpyxl
```

### Why these libraries?

* **pandas** → to read and process CSV/Excel files
* **transformers** → Hugging Face library
* **torch** → backend used by many transformer models
* **openpyxl** → useful if you want Excel support

---

# Python Code


Refer `huggingface_transformer_sentiment_analysis.py`


# How to Run the Project

Inside your terminal, run:

```bash
python shuggingface_transformer_sentiment_analysis.py
```

If everything works correctly, you will get a new file:

```bash
amazon_reviews_with_sentiment.csv
```

---

# Example Output

| review_id | product_name     | rating | review                                                   | sentiment |
| --------- | ---------------- | ------ | -------------------------------------------------------- | --------- |
| AMZ0001   | Wireless Earbuds | 5      | Absolutely loved this product. Sound quality is amazing. | Positive  |
| AMZ0002   | Phone Charger    | 2      | Charging speed is poor and stopped working in a week.    | Negative  |

---

# Beginner Explanation of the Core Line

This is the most important line in the project:

```python
classifier = pipeline("sentiment-analysis")
```

This line loads a ready-made AI model from Hugging Face.

So instead of:

* collecting training data
* building a model from scratch
* training it for hours

we simply use a **pre-trained model** and start getting predictions immediately.

---

# Why We Use `[:512]` Sometimes

Transformer models often have a maximum input length.

That’s why in many projects you’ll see something like:

```python
text[:512]
```

It keeps the review text within a safe length so the model can process it properly.

---

# Skills You Learn from This Project

By building this project, you’ll practice:

* Reading CSV files with Pandas
* Using Hugging Face Transformers
* Running sentiment analysis
* Working with real-world text data
* Saving model predictions into a file
* Building a beginner NLP project

---

# Real-World Use Cases

This kind of project can be used for:

* Amazon / Flipkart review analysis
* Customer feedback analysis
* Product review dashboards
* Social media sentiment analysis
* Brand monitoring
* Complaint classification

---

# Future Improvements

Once you understand this beginner version, you can improve the project by adding:

* **Positive / Negative / Neutral** classification
* sentiment score column
* charts for review distribution
* Streamlit web app UI
* product-wise sentiment summary
* filtering top negative reviews
* deployment on Hugging Face Spaces or Streamlit Cloud

---

# Common Errors and Fixes

## 1. `ModuleNotFoundError: No module named pandas`

Install pandas:

```bash
pip install pandas
```

## 2. `ModuleNotFoundError: No module named transformers`

Install transformers:

```bash
pip install transformers
```

## 3. Keras / TensorFlow import issue

If you get errors related to TensorFlow/Keras but you are only using Hugging Face with PyTorch, try removing conflicting packages and reinstalling:

```bash
pip uninstall -y tensorflow keras tf-keras
pip install pandas transformers torch
```

## 4. File not found error

Make sure `amazon_reviews_sample_500.csv` is in the same folder as your Python file.

---

# Requirements

You can also create a `requirements.txt` file with:

```txt
pandas
transformers
torch
openpyxl
```

Then install everything with:

```bash
pip install -r requirements.txt
```

---

# Who is this project for?

This project is great for:

* Python beginners
* Data science beginners
* NLP beginners
* students preparing AI/ML projects
* people starting Hugging Face for the first time
* content creators teaching beginner AI projects

---

# Final Note

This project is designed to make **AI feel simple and practical**.

If you are a beginner, don’t worry about understanding every deep learning concept right away.
Start with projects like this, run the code, observe the output, and build confidence step by step.

That’s how AI learning becomes easier. 🚀

---

# Connect / Learn More -- @learnwithbhawana

If you’re learning Python, AI, and beginner-friendly projects, feel free to keep building and experimenting.

Happy coding 💙
