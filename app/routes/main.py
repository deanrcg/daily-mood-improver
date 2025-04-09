from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import MoodEntry
from textblob import TextBlob
from datetime import datetime, timedelta

bp = Blueprint('main', __name__)

def get_suggestions(mood_rating, plans):
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

    if "work" in plans.lower():
        suggestions.append("Take regular short breaks during work")
    if "study" in plans.lower():
        suggestions.append("Create a comfortable study environment")
    if "home" in plans.lower():
        suggestions.append("Declutter a small area of your living space")

    return suggestions[:3]

@bp.route('/')
@login_required
def index():
    # Check for previous day's entry that needs improvement rating
    yesterday = datetime.utcnow() - timedelta(days=1)
    previous_entry = MoodEntry.query.filter(
        MoodEntry.user_id == current_user.id,
        MoodEntry.date >= yesterday,
        MoodEntry.improvement_rating == None
    ).first()
    
    if previous_entry:
        return redirect(url_for('main.rate_improvement', entry_id=previous_entry.id))
    
    return render_template('index.html')

@bp.route('/mood_entry', methods=['GET', 'POST'])
@login_required
def mood_entry():
    if request.method == 'POST':
        mood_rating = int(request.form['mood_rating'])
        mood_description = request.form['mood_description']
        daily_plans = request.form['daily_plans']
        
        # Analyze mood sentiment
        blob = TextBlob(mood_description)
        sentiment = blob.sentiment.polarity
        
        # Get suggestions
        suggestions = get_suggestions(mood_rating, daily_plans)
        
        # Create new mood entry
        entry = MoodEntry(
            mood_rating=mood_rating,
            mood_description=mood_description,
            daily_plans=daily_plans,
            suggestions=str(suggestions),
            user_id=current_user.id
        )
        
        db.session.add(entry)
        db.session.commit()
        
        return render_template('suggestions.html', suggestions=suggestions)
    
    return render_template('mood_entry.html')

@bp.route('/rate_improvement/<int:entry_id>', methods=['GET', 'POST'])
@login_required
def rate_improvement(entry_id):
    entry = MoodEntry.query.get_or_404(entry_id)
    
    if entry.user_id != current_user.id:
        flash('You can only rate your own entries.')
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        improvement_rating = int(request.form['improvement_rating'])
        entry.improvement_rating = improvement_rating
        db.session.commit()
        return redirect(url_for('main.index'))
    
    return render_template('rate_improvement.html', entry=entry)

@bp.route('/history')
@login_required
def history():
    entries = MoodEntry.query.filter_by(user_id=current_user.id).order_by(MoodEntry.date.desc()).all()
    return render_template('history.html', entries=entries) 