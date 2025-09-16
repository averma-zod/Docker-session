from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

# Store all submitted users
users = []

emojis = ["🚀", "🌟", "🔥", "🎉", "🐳", "🍕", "☕", "🦄", "💡", "🏆"]

@app.route('/', methods=['GET', 'POST'])
def home():
    global users
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            emoji = random.choice(emojis)
            users.append((name, emoji))
        return redirect('/')
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
