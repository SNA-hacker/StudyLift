from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime  # for date handling

app = Flask(__name__)

# Store tasks (temporary storage)
tasks = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task_name = request.form['task']
        task_deadline = request.form['deadline']  # get deadline from form
        # Add task with current date and deadline
        task = {
            'name': task_name,
            'done': False,
            'date_added': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # date added
            'deadline': task_deadline  # deadline from user input
        }
        tasks.append(task)
        return redirect(url_for('view_tasks'))
    return render_template('add_task.html')

@app.route('/tasks')
def view_tasks():
    completed = sum(1 for task in tasks if task['done'])
    total = len(tasks)
    return render_template('tasks.html', tasks=tasks, completed=completed, total=total)

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = True
    return redirect(url_for('view_tasks'))

if __name__ == '__main__':
    app.run(debug=True)


