from flask import Flask, render_template, request

app = Flask(_name_)

@app.route("/")
def top_page():
    return render_template("index.html")
if_name_ == " _main_":
    app.run(debug=True)

@app route("/circle_input")
def circle_input():
    return render_template("circle_input.html")

@app.route("/circle_result")
def cicle_result():
    radius = int(request.args.get("radius"))
    result = 3.14 * radius ** 2
    return render_template("cicle_result.html",result=result)
