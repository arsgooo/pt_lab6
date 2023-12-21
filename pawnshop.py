from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

goods = {"Radio": 200, "Headphones": 300, "Watch": 499.55555, "Ring": 749.47755}


@app.route("/")
def index():
    return render_template(
        "index.html",
        goods=goods,
        get_goods_amount=get_goods_amount,
        get_total_cost=get_total_cost,
    )


@app.route("/add_good", methods=["POST"])
def add_good():
    try:
        name = request.form["name"]
        price = float(request.form["price"])
        if isinstance(name, str) and isinstance(price, (int, float)):
            goods[name] = price
    except Exception as e:
        return str(e)
    return redirect(url_for("index"))


@app.route("/remove_good", methods=["POST"])
def remove_good():
    name = request.form["name"]
    if name in goods:
        goods.pop(name)
        return redirect(url_for("index"))
    else:
        return "Good not found"


@app.route("/get_goods_amount")
def get_goods_amount():
    amount = len(goods)
    return f"Total number of goods: {amount}"


@app.route("/get_total_cost")
def get_total_cost():
    total_cost = sum(goods.values())
    return f"Total cost of goods: ${total_cost}"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
