from flask import Flask, request, render_template
from tasks import edit_text


flask_app = Flask(__name__)


@flask_app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        edit_text.delay(request.form["text"])
    return render_template("index.html")


if __name__ == "__main__":
    flask_app.run()
