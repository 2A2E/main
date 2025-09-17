from flask import Flask

app = Flask(__name__)

@app.get("/")
def root():
    return "Hello World from our team Flask app!"

# APIs
@app.get("/adam")
@app.get("/adam/")
def adam():
    return "Hi, this is Adam's first HTTP API!"

# second API created by Chenrui
@app.get("/api/status")
@app.get("/api/status/")
def api_status():
    import datetime
    import platform
    import sys
    
    status_info = {
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat(),
        "server_info": {
            "platform": platform.system(),
            "python_version": sys.version.split()[0],
            "flask_version": "3.1.2"
        },
        "endpoints": [
            "/",
            "/adam",
            "/api/status"
        ]
    }
    return status_info


if __name__ == "__main__":
    # listen on all interfaces so the port can be forwarded
    app.run(host="0.0.0.0", port=5000, debug=True)

# Do not add anything under here
