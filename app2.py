from flask import Flask,  escape, request, render_template
app = Flask(__name__)

@app.route("/")

def main():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/rudra_new.html")
def rudra_new():
    return render_template('rudra_new.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4080)
