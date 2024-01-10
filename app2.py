from flask import Flask,  escape, request, render_template
app = Flask(__name__)

@app.route("/")

def main():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/samuel.html")
def samuel():
    return render_template('samuel.html')

@app.route("/surya_new.html")
def surya_new():
    return render_template('surya_new.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4080)
