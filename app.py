from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello World from our team Flask app!"

if __name__ == "__main__":
    app.run(debug=True)
