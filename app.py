from flask import Flask, render_template

app = Flask(__name__)

@app.route("/products")
def products():
    product_list = ["Ном", "Үзэг"]
    count = len(product_list)
    return render_template(
        "products.html",
        products=product_list,
        count=count
    )

if __name__ == "__main__":
    app.run(debug=True)
