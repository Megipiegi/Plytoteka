from flask import Flask, request, render_template, redirect, url_for

from forms import Plytoteka
from models import plytoteka

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/plytoteka/", methods=["GET", "POST"])
def plytoteka_list():
    form = Plytoteka()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            plytoteka.create(form.data)
            plytoteka.save_all()
        return redirect(url_for("plytoteka_list"))

    return render_template("plytoteka.html", form=form, plytoteka=plytoteka.all(), error=error)


@app.route("/plytoteka/<int:plytoteka_id>/", methods=["GET", "POST"])
def plyty_details(plytoteka_id):
    plyty = plytoteka.get(plytoteka_id - 1)
    form = Plytoteka(data=plyty)

    if request.method == "POST":
        if form.validate_on_submit():
            plytoteka.update(plytoteka_id - 1, form.data)
        return redirect(url_for("plytoteka_list"))
    return render_template("plyty.html", form=form, plytoteka_id=plytoteka_id)


@app.route("/plytoteka/delete/<int:plytoteka_id>/")
def plyty_delete(plytoteka_id):
    plytoteka.delete(plytoteka_id - 1)
    form = Plytoteka()
    error = ""
    return render_template("plytoteka.html", form=form, plytoteka=plytoteka.all(), error=error)


if __name__ == "__main__":
    app.run(debug=True)