# Eric "Morty" Lau
# SoftDev1 pd1
# K<number> -- <title>
# <year>-<month>-<date>

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def root():
    return render_template(
        "index.html"
    )

if __name__ == "__main__":
    app.debug = True
    app.run()