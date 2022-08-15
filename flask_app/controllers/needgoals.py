from flask import render_template, redirect, request, flash, session
from flask_app import app
from flask_app.models.needgoal import Need_goal


@app.route('/needs_page')
def needs_page():
    if not "user_id" in session:
        return redirect('/')
    data = {
        "user_id": session['user_id']
    }
    need_goals = Need_goal.get_need_goals(data)
    return render_template('needsPage.html', need_goals = need_goals)

@app.route('/process_addNeedsGoal', methods=['POST'])
def process_addNeedsGoal():
    data = {
        'user_id': session['user_id'],
        'name': request.form['name'],
        'deadline': request.form['deadline'],
        'goal_amount': request.form['goal_amount'],
        'current_amount': request.form['current_amount'],
        'description': request.form['description'],
    }
    Need_goal.add_need_goal(data)
    return redirect('/needs_page')

@app.route('/process_deposit', methods=['POST'])
def process_depost():
    data = {
        "id": request.form['id'],
        "user_id": session['user_id']
    }
    print()
    onegoal = Need_goal.get_one_goal(data)
    current_amount = onegoal.current_amount
    if request.form['deposit'] == '':
        return redirect('/needs_page')
    new_amount = current_amount + int(request.form['deposit']) 
    data1 = {
        "new_amount": new_amount,
        "id": request.form['id']
    }
    Need_goal.update_current_amount(data1)
    print(new_amount)
    return redirect('/needs_page')

@app.route('/process_withdraw', methods=['POST'])
def process_withdraw():
    data = {
        "id": request.form['id'],
        "user_id": session['user_id']
    }
    onegoal = Need_goal.get_one_goal(data)
    current_amount = onegoal.current_amount
    if request.form['withdraw'] == '':
        return redirect('/needs_page')
    new_amount = current_amount - int(request.form['withdraw']) 
    data1 = {
        "new_amount": new_amount,
        "id": request.form['id']
    }
    Need_goal.update_current_amount(data1)
    print(new_amount)
    return redirect('/needs_page')

@app.route('/show_one_need/<int:id>')
def show_one_need(id):
    if not "user_id" in session:
        return redirect('/')
    data = {
        'id': id
    }
    one_user_need = Need_goal.get_one_goal(data)

    return render_template('show_oneNeeds.html', one_user_need = one_user_need)

@app.route('/process_updateGoal', methods=['POST'])
def process_updateGoal():
    data = {
        'id': request.form['id'],
        'name': request.form['name'],
        'deadline': request.form['deadline'],
        'goal_amount': request.form['goal_amount'],
        'description': request.form['description'],
    }
    Need_goal.update_goal(data)
    return redirect(f'/show_one_need/{data["id"]}')