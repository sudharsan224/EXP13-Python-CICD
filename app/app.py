from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <body style="text-align:center; padding:50px;">
        <h1>EXP-13 CI/CD Pipeline</h1>
        <h2>Python Application Successfully Deployed!</h2>
        <h3>Jenkins + Docker + GitHub</h3>
        <p>Running on Local System</p>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)