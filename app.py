from flask import Flask

app = Flask(__name__)

@app.get("/")
def root():
    return "Hello World from our team Flask app!"

if __name__ == "__main__":
    # listen on all interfaces so the port can be forwarded
    app.run(host="0.0.0.0", port=5000, debug=True)


# APIs
@app.get("/adam")
def adam():
    return "Hi, this is Adam’s first HTTP API!"