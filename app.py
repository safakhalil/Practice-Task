from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("home.html")

@app.route("/result", methods=["POST", "GET"])
def resultPage():
    name   = request.form.get("name")
    type   = request.form.get("type")
    num    = int(request.form.get("num") or 1)
    method = request.form.get("method")

    if type == "classic":
        price = 3000
    elif type == "deluxe":
        price = 5000
    elif type == "junior":
        price = 7000
    elif type == "grand":
        price = 10000
    elif type == "penthouse":
        price = 15000
    else:
        price = 0

    total = num * price

    if method == "cash":
        discount = total * 0.05
    else:
        discount = 0

    total = total - discount

    return render_template("result.html",
        name=name, type=type, num=num,
        method=method, price=price, total=total
    )

if __name__ == "__main__":
    app.run(debug=True, port=5001)