from flask import Flask,  escape, request
app = Flask(__name__)

@app.route("/")

def main():
    return "Welcome to Devops Course from - Ashok Singh !"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4080)
