from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)

@app.route("/mypage/me")
def o_mnie():
    return render_template("strona_wizytowka_o_mnie.html")

@app.route("/mypage/contact", methods=['GET', 'POST'])
def kontakt():
    if request.method == 'GET':
#       print("We received GET")
       return render_template("strona_wizytowka_kontakt.html")
    elif request.method == 'POST':
#       print("We received POST")
       print('Wiadomość od użytkownika:')
       print(request.form['message'])
       return redirect("/mypage/contact")