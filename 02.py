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
    # get the cursor
    cursor = db.cursor()
    # get the list of emails
    cursor.execute("SELECT * FROM emails")
    # get the email
    email_list = cursor.fetchall()
    # check if the email is in the list
    if email in email_list:
        # delete the email
        cursor.execute("DELETE FROM emails WHERE email=%s", (email,))
        # commit the changes
        db.commit()
        # redirect to the list of emails
        return redirect("/emails")
    else:
        # if the email is not in the list, return an error
        return "Invalid email"
