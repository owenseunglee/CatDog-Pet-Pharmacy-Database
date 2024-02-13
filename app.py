from flask import Flask, render_template, json
from flask import request, redirect
from flask_mysqldb import MySQL
from database.db_connector import connect_to_database, execute_query
import database.db_connector as db
from dotenv import load_dotenv
import os;

load_dotenv()

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.getenv('340DBHOST')
app.config['MYSQL_USER'] = os.getenv('340DBUSER')
app.config['MYSQL_PASSWORD'] = os.getenv('340DBPW')
app.config['MYSQL_DB'] = os.getenv('340DB')
mysql = MySQL(app)


db_connection = db.connect_to_database()

@app.route("/")
def root():

    return render_template("main.j2")

@app.route("/veterinarians", methods=["POST", "GET"])
def browse_vets():
    if request.method == "GET":

        query = "SELECT vet_ FROM Vets"
        cur = mysql.connection.cursor()
        cur.execute(query)
        results = cur.fetchall()
        print(results)
        #query2 = "SELECT id_owner, name FROM Owners"
        #cur = mysql.connection.cursor()
        #cur.execute(query2)
        #owners_data = cur.fecthall()
        
        return render_template("vets.j2", Vets=results)

@app.route("/vets")
def vets():
    query = "SELECT * FROM Vets;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()

    return render_template("vets.j2", Vets=results)

@app.route("/add_vet")
def add_vets():
    
    return render_template("add_vet.j2")

@app.route("/del_vet")
def delete_vets():

    return render_template("del_vet.j2")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8200))


    app.run(port=port, debug = True)

