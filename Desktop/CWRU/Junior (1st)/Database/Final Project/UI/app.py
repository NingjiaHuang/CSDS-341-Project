import sqlite3
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
   id = int(request.form['id'])
   con = sqlite3.connect("data.db")
   con.row_factory = sqlite3.Row
   
   cur = con.cursor()
   cur.execute("SELECT * FROM PATIENT WHERE pid=?", (id,))
   
   profile = cur.fetchall()
   return render_template("search.html",profile=profile,id=id)

@app.route('/diagnosis/<id>')
def diagnosis(id):
   con = sqlite3.connect("data.db")
   con.row_factory = sqlite3.Row
   
   cur = con.cursor()
   cur.execute("select * from DIAGNOSIS where diag_id=?", (id,))
   diag = cur.fetchall()
   return render_template("diagnosis.html",diag=diag,id=id)

@app.route('/profile/<id>')
def profile(id):
   con = sqlite3.connect("data.db")
   con.row_factory = sqlite3.Row
   cur = con.cursor()
   cur.execute("select * from PATIENT where pid=?", (id,))
   profile = cur.fetchall()
   
   return render_template("search.html",profile=profile,id=id)

@app.route('/prescription/<id>')
def prescription(id):
   con = sqlite3.connect("data.db")
   con.row_factory = sqlite3.Row
   cur = con.cursor()
   cur.execute("select * from PRESCRIPTION where pre_pid=?", (id,))
   pre = cur.fetchall()
   return render_template("prescription.html",pre=pre,id=id)

if __name__ == '__main__':
   app.run(debug = True)