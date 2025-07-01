from flask import Flask, render_template

app = Flask(__name__)

# Sản phẩm mẫu
products = [
    {"name": "Áo Thun Tối Giản", "price": "150.000đ", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRWWSkjT2zNn4Is2L-T1lIxLn0HjSVjMKtCTw&s"},
    {"name": "Giày Sneaker Trắng", "price": "750.000đ", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8VIi1gHhKWSDyf7st4BVw52hpHm1TBSvXCw&s"},
    {"name": "Ba Lô Teen Năng Động", "price": "320.000đ", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTnFh3HjxSTgl_Girwh_zXU3WPEy4wYelICg&s"}
]

@app.route("/")
def home():
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
