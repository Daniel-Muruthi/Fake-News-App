# Fake News Detection Project

![Alternative text](https://github.com/idatonui/Fake-News-Prediction/blob/main/images/how-to-identify-fake-news-1.jpg)

## Contributors
- Ida Chepng'eno
- George Mbugua
- Kevan Ndwiga
- Daniel Muruthi
- Mike Kiptoch
- Neville Ngenzi

## Introduction

In today's digital age, the spread of misinformation, commonly known as fake news, has become a pervasive issue, undermining the integrity of journalistic organizations worldwide. The impact of fake news extends beyond politics, significantly affecting public health. During the COVID-19 pandemic, misinformation led to confusion and panic-buying of unproven remedies, while vaccine hesitancy fueled by false claims jeopardized efforts to curb the virus's spread. Addressing this challenge requires data-driven approaches, drawing on techniques from machine learning, natural language processing, and social network analysis. Researchers and policymakers are increasingly leveraging these tools to predict and mitigate the dissemination of fake news, enabling targeted interventions to combat its harmful effects.


## Problem Statement

The primary problem being addressed is the pervasive presence of fake news within the digital media landscape. Fake news undermines the credibility of International News as a reputable journalistic entity, erodes reader confidence, and contributes to the polarization of public opinion. Moreover, the dissemination of false information can have far-reaching consequences, including social unrest, political instability, and legal ramifications.


## Main Objectives

- To implement robust fake news detection mechanisms capable of identifying and flagging misinformation in real-time, thereby safeguarding the integrity and credibility of most News sectors.


## Data Understanding

The data used in this project was obtained from: [Kaggle](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset). The dataset is divided into: Fake.csv and True.csv.

The Fake.csv file contains: 23481 rows and 4 columns

The True.csv file contains: 21417 rows and 4 columns



## Data Preparation

This involves cleaning, addressing missing values, and removing duplicates to ensure data accuracy and completeness for analysis and modeling. Exploratory Data Analysis was done to understand data relationships, patterns, and distributions, guiding model selection and hyperparameter tuning.

Text preprocessing was also performed and it involved steps like lowercasing, removing punctuation and digits, eliminating stop words, and either stemming or lemmatizing text. These steps aim to streamline text data for model training by reducing complexity and focusing on essential words, although they may result in some loss of information.


#### Distribution of Subject Column



![Alternative text](https://github.com/idatonui/Fake-News-Prediction/blob/main/images/subject%20in%20True%20News.png)




![Alternative text](https://github.com/idatonui/Fake-News-Prediction/blob/main/images/Subjects%20in%20Fake%20Class.png)




## Modeling
 Two models (Logistic Regression and LSTM) were built and trained using the training dataset and CountVectorizer class from the sklearn library was used to convert the preprocessed text into feature vectors. LSTM model was also tuned and the results were compared with the two models. The performance of the models was evaluated using accuracy.

## Model Evaluation

- Logistic Regression:
Accuracy: 99.53% (highest among the three models).
- LSTM:
Accuracy: 98.48% (second highest).
- Tuned LSTM:
Accuracy: 98.46% (slightly lower than Basic LSTM).


- Logistic Regression performed the best in terms of accuracy.
- Basic LSTM and Tuned LSTM showed comparable results with slight variations.
- Results suggest that traditional models like Logistic Regression can be more accurate than deep learning models in some cases.

Logistic Regression, with a 99.53% accuracy rate, stands out as the best model for fake news detection among the evaluated models. Its high accuracy allows for precise identification and flagging of fake news, reducing false positives and negatives. By analyzing text-based features, Logistic Regression can quickly and effectively classify news articles as real or fake, making it a reliable choice for combating misinformation in real-time scenarios. This accuracy ensures robust content filtering and helps maintain information integrity.


## Overview
This project implements a machine learning-based fake news detection system, specifically trained on political news articles. Using Logistic Regression, the model achieves 99.53% accuracy in distinguishing between real and fake political news articles.

## ⚠️ Important Note
This model is specifically trained on and optimized for **political news articles** primarily from the United States. It may not perform as well on other types of news or content from different regions.

## Features
- Real-time fake news detection
- REST API endpoint for predictions
- Django-based web interface
- High accuracy (99.53%) for political news classification

## Prerequisites
- Python 3.x
- pip package manager
- Linux/Unix-based system (for using `apt`)

## Installation

1. Install Python virtual environment:
```bash
sudo apt install python3-venv
```

2. Clone the repository:
```bash
git clone [your-repository-url]
cd Detector
```

3. Create and activate virtual environment:
```bash
python3 -m venv virtual
source virtual/bin/activate
```

4. Install required dependencies:
```bash
pip install django
pip install djangorestframework
pip install scikit-learn
```

## Running the Application

1. Navigate to the project directory:
```bash
cd newsdetector
```

2. Start the development server:
```bash
python3 manage.py runserver
```

3. Access the API endpoint:
```
http://127.0.0.1:8000/detectorapi/
```

## Production Deployment
To run the application in production using Gunicorn:
```bash
gunicorn newsdetector.wsgi:application
```

## Model Information
- Algorithm: Logistic Regression
- Accuracy: 99.53%
- Training Data: Political news articles
- Features: Text-based analysis using CountVectorizer

## Limitations
- Primarily effective for political news content
- Dataset bias towards US-based news articles
- May not perform optimally on non-political news or content from other regions


## Contact
For any queries or contributions, please reach out to [Your Contact Information]