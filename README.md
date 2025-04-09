# Daily Mood Improver

A web application that helps users track and improve their mood using AI-powered sentiment analysis and personalized suggestions.

## Features

- User authentication and profile management
- Daily mood tracking with sentiment analysis
- Personalized mood improvement suggestions
- Progress tracking and history
- AI-powered mood analysis and recommendations

## AI Components

The Daily Mood Improver project leverages AI through the TextBlob library in several key ways:

1. **Sentiment Analysis**
   - Uses TextBlob's sentiment analysis to understand emotional content of mood descriptions
   - Provides polarity scores (-1 to 1) to quantify emotional state
   - Automatically classifies moods as positive, negative, or neutral

2. **Mood Classification**
   - Automatically categorizes moods based on sentiment analysis
   - Helps understand user's emotional state without manual input
   - Provides consistent mood tracking over time

3. **Personalized Suggestions**
   - Generates customized recommendations based on:
     - Current mood state
     - Historical mood patterns
     - Effectiveness of previous suggestions
   - Adapts suggestions based on user feedback

4. **Progress Tracking**
   - Analyzes mood trends over time
   - Identifies patterns in mood changes
   - Tracks effectiveness of different activities
   - Provides insights into mood improvement progress

5. **Natural Language Processing**
   - Understands context and meaning of mood descriptions
   - Provides contextual and relevant suggestions
   - Enhances user experience through better understanding of emotional state

## Installation

1. Clone the repository:
```bash
git clone https://github.com/deanrcg/daily-mood-improver.git
cd daily-mood-improver
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
flask db upgrade
```

5. Run the application:
```bash
python run.py
```

## Usage

1. Register a new account or log in
2. Enter your daily mood and description
3. Receive personalized suggestions
4. Track your mood improvement progress
5. View your mood history and patterns

## Technologies Used

- Python
- Flask
- SQLAlchemy
- TextBlob (for sentiment analysis)
- SQLite
- HTML/CSS
- Bootstrap

## License

This project is licensed under the MIT License - see the LICENSE file for details.

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