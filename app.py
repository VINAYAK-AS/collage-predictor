from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    sname=request.form.get("sname")
    rank = request.form.get("rank")
    category = request.form.get("category")
    course = request.form.get("course")
      course = request.form.get("place")
    return f"""
    <h1>Hello , {sname}</h1>
    <h2>Input Received Successfully ✅</h2>
    <p><b>Rank:</b> {rank}</p>
    <p><b>Category:</b> {category}</p>
    <p><b>Course:</b> {course}</p>
    <a href="/">Go Back</a>
    """

if __name__ == "__main__":
    app.run(debug=True)

