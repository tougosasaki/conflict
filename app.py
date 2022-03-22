from flask import Flask, render_template,request

app = Flask(_name_)

@app.route("/square_input")
def square_input():
    return render_template("square/index.html")

@app.route("/square_result")
def square_result():
    height = int( request.args.get("hright"))
    nottom = int(request.args.get("bottom"))
    reauklt = height * bottom
    return render_template("square_reault.html",result=result)

if_name_ == " _main_":
    app.run(debug=True)
