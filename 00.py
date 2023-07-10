from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

# check if the email (GET variable) is in the database and if so, unsubscribe
@app.route('/unsubscribe')
def unsubscribe():
    # get the email (GET variable)
    email = request.args.get('email')
    # get the database connection
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cursor = db.cursor()
    # check if the email exists in the database
    cursor.execute("SELECT * FROM users WHERE email = '{}'".format(email))
    # check if the email exists in the database
    if cursor.fetchone() is not None:
        # if the email exists in the database, then delete the email from the database
        cursor.execute("DELETE FROM users WHERE email = '{}'".format(email))
        # close the database connection
        db.close()
        # redirect to the index page
        return redirect("/index")
    else:
        # if the email does not exist in the database, then redirect to the index page
        return redirect("/index")
