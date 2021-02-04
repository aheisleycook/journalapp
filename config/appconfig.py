from datetime import datetime, time
from typing import Dict
from flask import (Flask, render_template, request, Response, jsonify, redirect)
import sqlite3
import secrets
import datetime



app = Flask(__name__)
app.secret_key = secrets.token_urlsafe()
db = sqlite3.connect("/home/aheisleycook/journalApp/db/journal.db")


@app.route("/delete", methods=["post"])
def delete():
    stitle = request.form["title"]
    db = sqlite3.connect("/home/aheisleycook/journalApp/db/journal.db")
    sql = 'DELETE FROM entry WHERE title=?'
    conn = db.cursor()
    conn.execute(sql, (stitle,))
    db.commit()
    return redirect("/")


@app.route("/search", methods=["get"])
def Search():
    query = request.args["entry"]
    db = sqlite3.connect("/home/aheisleycook/journalApp/db/journal.db")
    sql = 'Select * from entry where title=?'
    conn = db.cursor()
    conn.execute(sql(query, ))
    a = conn.fetchall()
    return render_template("index.html", a=a)


@app.route("/", methods=["get"])
def showEntry():
    db = sqlite3.connect("/home/aheisleycook/journalApp/db/journal.db")
    conn = db.cursor()
    conn.execute("select * from entry")
    a = conn.fetchall()
    return render_template("index.html", a=a)


@app.route("/add", methods=["post"])
def addEntry():
    title = request.form["title"]
    desc = request.form["desc"]
    db = sqlite3.connect("/home/aheisleycook/journalApp/db/journal.db")
    conn = db.cursor()
    conn.execute("insert into entry values(?,?)", (title, desc))
    a = conn.fetchall()
    return render_template("index.html", a=a)


@app.route("/sendtolog")
def logrecord():
    db = sqlite3.connect("/home/aheisleycook/journalApp/db/journal.db")
    conn = db.cursor()
    conn.execute("select * from entry")
    a = conn.fetchall()
    for Record in a:
        with open("entries.txt", "a") as t:
            t.write("title" + Record[0] + "\ntitel:" + Record[1])


app.run(host="0.0.0.0", port=8080)