from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Azure Web Application</h1>
    <p>Our application is running successfully.</p>
    <p>Hosted on Microsoft Azure App Service.</p>
    """


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": "azure-web-application"
    }


@app.route("/info")
def info():
    return {
        "application": "Azure Web Application",
        "platform": "Microsoft Azure App Service",
        "status": "running"
    }


if __name__ == "__main__":
    app.run(debug=True)