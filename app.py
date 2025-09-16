from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get('name', 'there')
    return f"👋 Hello {name}, welcome to Docker on AWS! 🚀"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
