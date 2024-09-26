# Twitter Sentiment Analysis Web App

## Project Overview

**NLP-Project-1-Twitter-Sentiment-Analysis-WebApp** is a natural language processing (NLP) project that analyzes the sentiment of tweets in real time. The web app classifies tweets as *positive*, *negative*, or *neutral*, providing insights into public opinion or feedback regarding specific topics or hashtags. The project uses machine learning techniques and popular NLP libraries to perform text preprocessing, vectorization, and sentiment classification.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Modeling Approach](#modeling-approach)
- [Web App Interface](#web-app-interface)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Features

- Real-time sentiment analysis of tweets.
- Classifies tweets into positive, negative, or neutral categories.
- User can search tweets by a hashtag or keyword.
- Interactive web interface built using Streamlit.
- Visualizes results with charts showing the sentiment distribution.

## Technologies Used

- **Python**: Core programming language used.
- **Natural Language Processing (NLP)**: For text analysis and sentiment classification.
- **Streamlit**: For building an interactive web app.
- **Scikit-learn**: Machine learning library used for model building.
- **Tweepy**: For fetching real-time tweets using the Twitter API.
- **Numpy & Pandas**: For data manipulation and preprocessing.
- **Matplotlib & Seaborn**: For data visualization.

## Dataset

The dataset for training the sentiment analysis model is sourced from:
- Publicly available Twitter sentiment datasets.
- The model is trained on a labeled dataset of tweets categorized as positive, negative, or neutral.

You can use your own dataset or fetch real-time tweets via the Twitter API using **Tweepy**.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/NLP-Project-1-Twitter-Sentiment-Analysis-WebApp.git
    cd NLP-Project-1-Twitter-Sentiment-Analysis-WebApp
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Twitter Developer Account and generate API keys for **Tweepy**.

4. Create a `.env` file in the project directory with your Twitter API credentials:
    ```
    TWITTER_API_KEY=your_api_key
    TWITTER_API_SECRET_KEY=your_api_secret_key
    TWITTER_ACCESS_TOKEN=your_access_token
    TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
    ```

5. Run the app:
    ```bash
    streamlit run app.py
    ```

## Usage

1. Open the web app on your browser (default address is `http://localhost:8501`).
2. Enter a keyword or hashtag to analyze the sentiment of recent tweets.
3. The app will fetch the latest tweets related to the entered keyword, preprocess them, and classify them into positive, negative, or neutral sentiments.
4. View the sentiment distribution graph for better understanding of public opinion.

## Modeling Approach

- **Text Preprocessing**: Tweets are cleaned by removing URLs, special characters, and stopwords. Tokenization is applied to split the text into individual words.
- **Vectorization**: We use **TF-IDF Vectorizer** to convert text data into numerical format.
- **Model**: A **Logistic Regression** model is used to classify the sentiment of the tweets. Other models such as **Naive Bayes** and **Support Vector Machine (SVM)** can also be tested for comparison.

## Web App Interface

The web app includes:
- An input field for entering a keyword or hashtag.
- A button to fetch and analyze tweets.
- A bar chart showing the sentiment distribution across positive, negative, and neutral tweets.

## Future Enhancements

- Implement advanced NLP models like BERT or LSTM for improved sentiment classification.
- Add support for multilingual sentiment analysis.
- Include historical sentiment tracking for a topic over time.
- Implement user authentication for customized experience.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
