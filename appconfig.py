from datetime import datetime, time
from typing import Dict
from flask import (Flask, render_template, request, Response, jsonify, redirect, session)
import pymysql


from flask import (Flask, render_template, request, Response, jsonify, redirect)
import sqlite3
import secrets
import pymysql

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe()
db = pymysql.Connection(user="aheisleycook",passwd="A7147084155o!")
@app.route("/login")
def login():
    username = request.form['username']
    password  = request.form['password']
    conn = db.cursor()
    sql = 'Select * from entry where title=? where password=?'
    conn.execute(sql(username, password))
    if conn:
        session["logged_in"] = True
    else:
        session["logged_in"] = False

@app.route("/delete", methods=["post"])
def delete():
    stitle = request.form["title"]
    sql = 'DELETE FROM entry WHERE title=?'
    conn = db.cursor()
    conn.execute(sql, (stitle,))
    db.commit()
    return redirect("/")
"""
this is my current project routing 

"""

@app.route("/search", methods=["get"])
def Search():
    query = request.args["entry"]
    sql = 'Select * from entry where title=?'
    conn = db.cursor()

    conn.execute(sql(query, ))
    a = conn.fetchall()
    return render_template("index.html", a=a)


@app.route("/", methods=["get"])
def showEntry():
    conn = db.cursor()
    conn.execute("select * from entry")
    a = conn.fetchall()
    return render_template("index.html", a=a)


@app.route("/add", methods=["post"])
def addEntry():
    title = request.form["title"]
    desc = request.form["desc"]
    conn = db.cursor()
    conn.execute("insert into entry values(?,?)", (title, desc))
    a = conn.fetchall()
    return render_template("index.html", a=a)


@app.route("/sendtolog")
def logrecord():
    conn = db.cursor()
    conn.execute("select * from entry")
    a = conn.fetchall()
    for Record in a:
        with open("entries.txt", "a") as t:
            t.write("title" + Record[0] + "\ntitel:" + Record[1])


app.run(host="0.0.0.0", port=8086)