from flask import Flask, render_template

app = Flask(__name__)

restaurants = [
    {
        "name": "Spicy Biryani House",
        "rating": 4.5,
        "food": "Biryani",
        "image": "https://source.unsplash.com/300x200/?biryani"
    },
    {
        "name": "Pizza Corner",
        "rating": 4.2,
        "food": "Pizza",
        "image": "https://source.unsplash.com/300x200/?pizza"
    },
    {
        "name": "Burger King Style",
        "rating": 4.0,
        "food": "Burger",
        "image": "https://source.unsplash.com/300x200/?burger"
    }
]

@app.route("/")
def home():
    return render_template("index.html", restaurants=restaurants)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
