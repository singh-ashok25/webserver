from flask import Flask,  escape, request, render_template
app = Flask(__name__)

@app.route("/")

def main():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/ashok.html")
def ashok():
    return render_template('ashok.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
