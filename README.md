## Resume Classification Web Application

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Usage](#usage)
- [Technical Approach](#technical-approach)
- [Model Performance](#model-performance)
- [Dataset](#dataset)
- [Credits](#credits)
- [Contact](#contact)
- [License](#license)


## Project Description

This project is a web application designed to classify resumes into different job categories using a machine learning model. It helps streamline the resume screening process for recruiters and HR departments by automatically categorizing resumes based on their content.

The application is built using:

*   **Python**: For the backend logic and machine learning model.
*   **Flask**: As the web framework to create the web application.
*   **HTML/CSS**: For the frontend user interface.
*   **Machine Learning Model**: A pre-trained model (Logistic Regression) serialized in a pickle file.

## Features

*   **Resume Upload**: Users can upload resumes through a simple web interface.
*   **Automatic Classification**: Resumes are automatically classified into one of 25 job categories.
*   **Instant Results**: Classification results are displayed immediately after the resume is uploaded.
* **Text Preprocessing**:The app is including:
    *   Special character removal
    *   Lowercase conversion
    *   Stopword removal
    *   Tokenization

## Dependencies

*   Python 3.6+
*   Flask
*   scikit-learn
*   pandas
*   nltk
*   re
*   pickle

## Dataset

The dataset used for training the model contains **962 labeled resumes** across 25 distinct job categories.

## Installation

1.  **Clone the repository:**
    

| Category                | Count |
|-------------------------|-------|
| Java Developer          | 84    |
| Testing                 | 70    |
| DevOps Engineer         | 55    |
| Python Developer        | 48    |
| Web Designing           | 45    |
| HR                      | 44    |
| ... (20 more categories)| ...   |

## Technical Approach

### Data Preprocessing
```python
def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text)  # Remove special chars
    text = text.lower()  # Convert to lowercase
    text = ' '.join([word for word in word_tokenize(text) 
                   if word not in stopwords.words('english')])
    return text
```

## Feature Extraction

- **TF-IDF Vectorizer** with 1000 features  
- Text vectorization for machine learning input

## Models Evaluated

### Random Forest
- **Accuracy:** 98.96%  
- **Strengths:** Handles non-linear relationships well

### Logistic Regression (Selected Model)
- **Accuracy:** 99.48%  
- **Strengths:** Best overall performance

### Multinomial Naive Bayes
- **Accuracy:** 96.37%  
- **Strengths:** Fast training time

## Model Performance

### Accuracy Comparison

| Model                | Accuracy |
|----------------------|----------|
| Logistic Regression  | 99.48%   |
| Random Forest        | 98.96%   |
| Multinomial NB       | 96.37%   |


