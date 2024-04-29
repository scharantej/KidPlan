
# main.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Database of child profiles and events
profiles = []
events = []

@app.route('/')
def index():
    return render_template('index.html', profiles=profiles)

@app.route('/profile/<child_id>')
def profile(child_id):
    child = profiles[int(child_id)]
    return render_template('profile.html', child=child, events=events)

@app.route('/create_profile', methods=['GET', 'POST'])
def create_profile():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        profiles.append({'name': name, 'age': age})
        return redirect(url_for('index'))
    return render_template('create_profile.html')

@app.route('/edit_profile/<child_id>', methods=['GET', 'POST'])
def edit_profile(child_id):
    child = profiles[int(child_id)]
    if request.method == 'POST':
        child['name'] = request.form['name']
        child['age'] = int(request.form['age'])
        return redirect(url_for('profile', child_id=child_id))
    return render_template('edit_profile.html', child=child)

@app.route('/create_event/<child_id>', methods=['GET', 'POST'])
def create_event(child_id):
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        time = request.form['time']
        category = request.form['category']
        events.append({'name': name, 'date': date, 'time': time, 'category': category, 'child_id': child_id})
        return redirect(url_for('profile', child_id=child_id))
    return render_template('create_event.html', child_id=child_id)

@app.route('/edit_event/<event_id>', methods=['GET', 'POST'])
def edit_event(event_id):
    event = events[int(event_id)]
    if request.method == 'POST':
        event['name'] = request.form['name']
        event['date'] = request.form['date']
        event['time'] = request.form['time']
        event['category'] = request.form['category']
        return redirect(url_for('profile', child_id=event['child_id']))
    return render_template('edit_event.html', event=event)

@app.route('/delete_event/<event_id>')
def delete_event(event_id):
    event = events[int(event_id)]
    events.remove(event)
    return redirect(url_for('profile', child_id=event['child_id']))

if __name__ == '__main__':
    app.run(debug=True)
