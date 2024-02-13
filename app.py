from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
import database.db_connector as db
db_connection = db.connect_to_database()

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_lyjes'
app.config['MYSQL_PASSWORD'] = '7125' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_lyjes'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

@app.route("/")
def root():

    return render_template("main.j2")

@app.route("/vets")
def vets():
    query = "SELECT * FROM Vets;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()

    return render_template("vets.j2", Vets=results)

# adding vet page
@app.route("/add_vet")
def add_vets():
    
    return render_template("add_vet.j2")

# deleting vet page
@app.route("/del_vet")
def delete_vets():

    return render_template("del_vet.j2")

# owners page
@app.route("/owners")
def owners():
    query = "SELECT * FROM Owners;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()

    return render_template("owners.j2", Owners=results)

# adding owner page
@app.route("/add_owner")
def add_owner():
    
    return render_template("add_owner.j2")

# deleting owner page
@app.route("/del_owner")
def del_owner():

    return render_template("del_owner.j2")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 58580)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port) 