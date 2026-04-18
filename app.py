from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homePage():
<<<<<<< HEAD
    subjects = ["English", "Science", "Math"]
    fruits = ["Apple", "Banana", "Mango", "Orange", "Cherry"]
    nums = [1, 2, 3, 4, 5]
    return render_template("home.html", subjects=subjects, fruits=fruits, nums=nums)

@app.route("/result", methods=["POST"])

def resultPage():
    name=request.form["name"]
    age=int(request.form["age"])
    if age>=18:
        user_age = "Adult"
    else:
        user_age = "Minor"

    marks=int(request.form["marks"])
    if marks>=50:
        result="Pass"
    else:
        result="Fail"
    
    city=request.form["city"]

    log_in=request.form.get("log_in")
    if log_in:
        display="Welcome user"
    else:
        display="log in"

    num=int(request.form["num"])
    if num % 2 == 0:
        Numb="Even"
    else:
        Numb="Odd"

    temperature=int(request.form["temperature"])
    if temperature >=30:
        temp="Hot"
    else:
        temp="Normal"    

    percentage=int(request.form["percentage"])
    if percentage >= 75:
        per="Allowed"
    else:
        per="Not allowed"

    amount=int(request.form["amount"])
    if amount>= 2000:
        bill="Discount applied"
    else:
        bill="No Discount"

    subjects=["English", "science" , "math"]

    fruits = ["Apple", "Banana", "Mango", "Orange", "Cherry"]

    nums=["1,2,3,4,5"]

    price=200

    items=request.form["items"]

    Iname=request.form.get("Iname").lower()
    Iprice = int(request.form.get("Iprice"))
    Iquantity=int(request.form.get("Iquantity"))

    total_price=int(request.form.get("Iprice"))*Iquantity

    delivery=request.form["delivery"]
    if delivery== "Yes":
        delivery_message="Delivery Charges Applied"
    else:
        delivery_message="Pickup Order"
    
    return render_template("result.html", 
    name=name, 
    age=age, 
    user_age=user_age, 
    result=result, 
    city=city, 
    log_in=log_in, 
    display=display,
    num=num,
    Numb=Numb,
    temperature=temperature,
    temp=temp,
    percentage=percentage,
    per=per,
    amount=amount,
    bill=bill,
    subjects=subjects,
    fruits=fruits,
    nums=nums,
    items=items,
    Iname=Iname,
    Iprice=Iprice,
    Iquantity=Iquantity,
    total_price=total_price,
    delivery=delivery,
    delivery_message=delivery_message
    )

if __name__ == "__main__":
    app.run(debug=True,port=8080)
=======
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
>>>>>>> 001b93e (Initial commit: Flask practice task app)
