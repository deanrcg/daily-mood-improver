# Daily Mood Improver

A Python application that helps improve your mood on a daily basis using TextBlob for sentiment analysis and personalized suggestions.

## Features

- Daily mood tracking and rating
- Personalized mood improvement suggestions based on your current mood and plans
- Progress tracking over time
- Sentiment analysis of mood descriptions
- Data persistence using JSON storage

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python mood_improver.py
```

The application will:
1. Ask you to rate your current mood (1-10)
2. Request a brief description of your mood
3. Ask about your plans for the day
4. Provide three personalized suggestions to improve your mood
5. Track your progress over time

## Data Storage

Your mood data is stored in `mood_data.json` in the same directory as the application. This file contains:
- Daily mood ratings
- Mood descriptions
- Daily plans
- Suggested improvements
- Improvement ratings

## Requirements

- Python 3.6+
- textblob
- pandas
- python-dotenv 