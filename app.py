from flask import Flask, render_template, json
from flask import request, redirect
from flask_mysqldb import MySQL
from database.db_connector import connect_to_database, execute_query
import database.db_connector as db
from dotenv import load_dotenv
import os;

load_dotenv()

db_connection = db.connect_to_database()

app = Flask(__name__)
app.config['MYSQL_HOST'] = os.getenv('340DBHOST')
app.config['MYSQL_USER'] = os.getenv('340DBUSER')
app.config['MYSQL_PASSWORD'] = os.getenv('340DBPW')
app.config['MYSQL_DB'] = os.getenv('340DB')
#app.config['MYSQL_CURSORCLASS'] = "DictCursor"
mysql = MySQL(app)

db_connection = db.connect_to_database()

@app.route("/")
def root():

    return render_template("main.j2")

############ IGNORE THIS PART ###############
#@app.route("/veterinarians", methods=["POST", "GET"])
#def browse_vets():
#    if request.method == "GET":

#        query = "SELECT vet_ FROM Vets"
#        cur = mysql.connection.cursor()
#        cur.execute(query)
#        results = cur.fetchall()
#        print(results)
        #query2 = "SELECT id_owner, name FROM Owners"
        #cur = mysql.connection.cursor()
        #cur.execute(query2)
        #owners_data = cur.fecthall()
        
 #       return render_template("vets.j2", Vets=results)

# veterinarian page
@app.route("/vets")
def vets():
    query = "SELECT * FROM Vets;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()

    return render_template("vets/vets.j2", Vets=results)

# adding vet page
# adding vet page
@app.route("/add_vet")
def add_vets():
    
    return render_template("vets/add_vet.j2")

# deleting vet page
# deleting vet page
@app.route("/del_vet")
def delete_vets():

    return render_template("vets/del_vet.j2")

# owners page
@app.route("/owners")
def owners():
    query = "SELECT * FROM Owners;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()

    return render_template("owners/owners.j2", Owners=results)

# adding owner page
@app.route("/add_owner")
def add_owner():
    
    return render_template("owners/add_owner.j2")

# deleting owner page
@app.route("/del_owner")
def del_owner():

    return render_template("owners/del_owner.j2")

# medications page
@app.route("/meds")
def meds():
    query = "SELECT * FROM Medications;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()

    return render_template("medications/meds.j2", Medications=results)

# adding med page
@app.route("/add_med")
def add_meds():

    return render_template("medications/add_med.j2")

# deleting med page
@app.route("/del_med")
def del_meds():

    return render_template("medications/del_med.j2")

@app.route("/pets")
def pets():
    query = "SELECT * FROM Pets;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()

    return render_template("pets/pets.j2", Pets=results)

@app.route("/del_pet")
def del_pets():
    
    return render_template("pets/del_pet.j2")

@app.route("/add_pet")
def add_pets():

    return render_template("pets/add_pet.j2")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8200)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port, debug = True) 