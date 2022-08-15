from flask import render_template, redirect, request, flash, session
from flask_app import app

@app.route('/home')
def dashboard():
    if not "user_id" in session:
        return redirect('/')
    return render_template('dashboard.html')

@app.route('/investment_goals')
def investment_goals():
    if not "user_id" in session:
        return redirect('/')
    return render_template("investmentGoals.html")