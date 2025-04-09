from textblob import TextBlob
import pandas as pd
from datetime import datetime
import json
import os

class MoodImprover:
    def __init__(self):
        self.data_file = "mood_data.json"
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {"entries": []}

    def save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def get_mood_rating(self):
        while True:
            try:
                rating = int(input("On a scale of 1-10, how would you rate your current mood? (1 being very low, 10 being very high): "))
                if 1 <= rating <= 10:
                    return rating
                print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Please enter a valid number.")

    def get_mood_description(self):
        description = input("Please describe your current mood in a few words: ")
        return description

    def get_daily_plans(self):
        plans = input("What are your plans for today? Please describe briefly: ")
        return plans

    def analyze_mood(self, description):
        blob = TextBlob(description)
        return blob.sentiment.polarity

    def suggest_improvements(self, mood_rating, plans):
        suggestions = []
        
        if mood_rating <= 3:
            suggestions.extend([
                "Take a short walk outside to get some fresh air",
                "Listen to your favorite uplifting music for 10 minutes",
                "Write down three things you're grateful for"
            ])
        elif mood_rating <= 6:
            suggestions.extend([
                "Do a quick 5-minute meditation or deep breathing exercise",
                "Call or text a friend or family member",
                "Try a new healthy recipe for your next meal"
            ])
        else:
            suggestions.extend([
                "Share your positive energy by complimenting someone",
                "Plan a small celebration for your achievements",
                "Start a new hobby or creative project"
            ])

        # Add plan-specific suggestions
        if "work" in plans.lower():
            suggestions.append("Take regular short breaks during work")
        if "study" in plans.lower():
            suggestions.append("Create a comfortable study environment")
        if "home" in plans.lower():
            suggestions.append("Declutter a small area of your living space")

        return suggestions[:3]  # Return only the first 3 suggestions

    def record_entry(self, mood_rating, description, plans, suggestions):
        entry = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "mood_rating": mood_rating,
            "mood_description": description,
            "plans": plans,
            "suggestions": suggestions,
            "improvement_rating": None  # To be filled in the next day
        }
        self.data["entries"].append(entry)
        self.save_data()

    def check_previous_day(self):
        if not self.data["entries"]:
            return None
        
        last_entry = self.data["entries"][-1]
        if last_entry["improvement_rating"] is None:
            return last_entry
        return None

    def record_improvement(self, previous_entry):
        print("\nLet's check how yesterday's suggestions worked for you!")
        print(f"Yesterday's mood rating: {previous_entry['mood_rating']}")
        print(f"Yesterday's suggestions: {', '.join(previous_entry['suggestions'])}")
        
        while True:
            try:
                improvement = int(input("On a scale of 1-10, how much did these suggestions help improve your mood? (1 being not at all, 10 being very helpful): "))
                if 1 <= improvement <= 10:
                    previous_entry["improvement_rating"] = improvement
                    self.save_data()
                    return
                print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Please enter a valid number.")

    def run(self):
        print("Welcome to the Daily Mood Improver!")
        print("-----------------------------------")
        
        # Check if we need to record improvement from previous day
        previous_entry = self.check_previous_day()
        if previous_entry:
            self.record_improvement(previous_entry)
        
        # Get current mood information
        mood_rating = self.get_mood_rating()
        mood_description = self.get_mood_description()
        plans = self.get_daily_plans()
        
        # Analyze mood and get suggestions
        mood_analysis = self.analyze_mood(mood_description)
        suggestions = self.suggest_improvements(mood_rating, plans)
        
        # Display suggestions
        print("\nHere are three suggestions to improve your mood today:")
        for i, suggestion in enumerate(suggestions, 1):
            print(f"{i}. {suggestion}")
        
        # Record the entry
        self.record_entry(mood_rating, mood_description, plans, suggestions)
        
        print("\nThank you for using the Daily Mood Improver!")
        print("Remember to check back tomorrow to track your progress!")

if __name__ == "__main__":
    app = MoodImprover()
    app.run() 