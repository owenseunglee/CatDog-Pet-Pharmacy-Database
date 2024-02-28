# Citation for app.py
# Date: 2/13/24
# Adapted from: Flask Starter App Guide
# Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app

from flask import Flask, render_template, json
from flask import request, redirect
from flask_mysqldb import MySQL
from database.db_connector import connect_to_database, execute_query
import database.db_connector as db
from dotenv import load_dotenv
import os
import os

load_dotenv()

db_connection = db.connect_to_database()

app = Flask(__name__)
app.config['MYSQL_HOST'] = os.getenv('340DBHOST')
app.config['MYSQL_USER'] = os.getenv('340DBUSER')
app.config['MYSQL_PASSWORD'] = os.getenv('340DBPW')
app.config['MYSQL_DB'] = os.getenv('340DB')
#app.config['MYSQL_CURSORCLASS'] = "DictCursor"
mysql = MySQL(app)

@app.route("/")
def root():

    return render_template("main.html", title='Home')

# veterinarian page
@app.route("/vets", methods=["POST", "GET"])
def vets():
   if request.method == "GET":
       query = "SELECT * FROM Vets;"
       cursor = db.execute_query(db_connection=db_connection, query=query)
       results = cursor.fetchall()

    #    query2 = query = "SELECT id_vet, CONCAT(Vets.name, ' (', id_vet, ')') AS vet_name_id FROM Vets;"
    #    cursor = db.execute_query(db_connection=db_connection, query=query2)
    #    vet_results = cursor.fetchall()
       

   return render_template("vets/vets.html", title='Veterinarians', Vets=results, Vets_Dropdown=vet_results)
   return render_template("vets/vets.j2", Vets=results)


# adding vet page
@app.route("/add_vet", methods=["POST", "GET"])
def add_vets():
   if request.method == "POST":
       name = request.form["name"]
       clinic = request.form["clinic"]
       email = request.form["email"]
       no_of_patients = request.form["no_of_patients"]

       query = "INSERT INTO Vets (name, clinic, email, no_of_patients) VALUES (%s, %s, %s, %s)"
       cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(name, clinic, email, no_of_patients))
       db_connection.commit()
       return redirect("/vets")

   return render_template("vets/add_vet.html")

# delete vet
@app.route("/del_vet/<int:id>")
def delete_vets(id):
    query = "DELETE FROM Vets WHERE id_vet = %s;"
    cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
    db_connection.commit()
    return redirect("/vets")


@app.route("/edit_vet", methods=["GET", "POST"])
def edit_vet():
    # return render_template("vets/edit_vet.j2")

    #if request.method == "GET":
        
    #    query = "SELECT * FROM Vets WHERE id_vet = %s;"
    #    cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id_vet,))
    #    results = cursor.fetchall()
    #    return render_template("vets/edit_vet.html", results=results)
    
    if request.method == "POST":
        id_vet = request.form['vet_select']
        name = request.form["name"]
        clinic = request.form["clinic"]
        email = request.form["email"]
        no_of_patients = request.form["no_of_patients"]

        query = "UPDATE Vets SET name = %s, clinic = %s, email = %s, no_of_patients = %s WHERE id_vet = %s"
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(name, clinic, email, no_of_patients, id_vet))
        db_connection.commit()

        return redirect("/vets")
    if request.method == "POST":
        if request.form.get("Edit_Vet"):
            name = request.form["name"]
            clinic = request.form["clinic"]
            email = request.form["email"]
            no_of_patients = request.form["no_of_patients"]
            query = "UPDATE Vets SET name=%s, clinic=%s, email=%s, no_of_patients=%s WHERE id_vet=%s;"
            values = (name, clinic, email, no_of_patients, id_vet)
            db.execute_query(db_connection=db_connection, query=query, query_params= values)
            db_connection.commit()
            return redirect("/vets")


    # [MIGHT NOT IMPLEMENT] drop down in edit_vet to select a vet
    # if request.method == "GET":
    #     query = "SELECT id_vet, CONCAT(Vets.name, ' (', id_vet, ')') AS vet_name_id FROM Vets;"
    #     cursor = db.execute_query(db_connection=db_connection, query=query)
    #     vet_results = cursor.fetchall()
    # if request.method == "POST":
    #     if request.form.get(:id in select vet fromdrop down):
    #         name = request.form["name"]
    #         clinic = request.form["clinic"]
    #         email = request.form["email"]
    #         no_of_patients = request.form["no_of_patients"]


    # return render_template("vets/edit_vet.j2", Vets_Dropdown=vet_results)

# owners page
@app.route("/owners")
def owners():
    # query = "SELECT * FROM Owners;"
    # cursor = db.execute_query(db_connection=db_connection, query=query)
    # results = cursor.fetchall()
    return render_template("owners/owners.html", title='Owners')
    # return render_template("owners/owners.j2", Owners=results)

# adding owner page
@app.route("/add_owner")
def add_owner():
    
    return render_template("owners/add_owner.j2")

# deleting owner page
@app.route("/del_owner")
def del_owner():

    return render_template("owners/del_owner.j2")

@app.route("/edit_owner")
def edit_owner():

    return render_template("owners/edit_owner.j2")

# medications page
@app.route("/meds")
def meds():
    # query = "SELECT * FROM Medications;"
    # cursor = db.execute_query(db_connection=db_connection, query=query)
    # results = cursor.fetchall()

    # return render_template("medications/meds.j2", Medications=results)
    return render_template("medications/meds.html", title='Medications')

# adding med page
@app.route("/add_med")
def add_meds():

    return render_template("medications/add_med.j2")

@app.route("/edit_med")
def edit_meds():
    return render_template("medications/edit_med.j2")

# deleting med page
@app.route("/del_med")
def del_meds():

    return render_template("medications/del_med.j2")

@app.route("/pets")
def pets():
    # query = "SELECT * FROM Pets;"
    # cursor = db.execute_query(db_connection=db_connection, query=query)
    # results = cursor.fetchall()

    # return render_template("pets/pets.j2", Pets=results)
    return render_template("pets/pets.html", title='Pets')

@app.route("/del_pet")
def del_pets():
    
    return render_template("pets/del_pet.j2")

@app.route("/add_pet")
def add_pets():

    return render_template("pets/add_pet.j2")

@app.route("/edit_pet")
def edit_pet():
    return render_template("pets/edit_pet.j2")

@app.route("/prescriptions")
def prescriptions():
    # query = "SELECT * FROM Prescriptions;"
    # cursor = db.execute_query(db_connection=db_connection, query=query)
    # results = cursor.fetchall()

    # return render_template("prescriptions/prescriptions.j2", Prescriptions=results)
    return render_template("prescriptions/prescriptions.html", title='Prescriptions')

@app.route("/del_prescription")
def del_prescriptions():
    
    return render_template("prescriptions/del_prescription.j2")

@app.route("/add_prescription")
def add_prescriptions():

    return render_template("prescriptions/add_prescription.j2")

@app.route("/edit_prescription")
def edit_prescription():

    return render_template("prescriptions/edit_prescription.j2")

@app.route("/prescriptMeds")
def intersection():
    # query = "SELECT * FROM PrescriptionMedications;"
    # cursor = db.execute_query(db_connection=db_connection, query=query)
    # results = cursor.fetchall()
    # return render_template("intersection/prescriptMeds.j2", PrescriptionMedications=results)

    return render_template("intersection/prescriptMeds.html", title='prescriptionMedications')

@app.route("/add_prescriptMeds")
def add_prescriptMeds():

    return render_template("intersection/add_prescriptMeds.j2")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8205)) 
     #                               ^^^^
    #             You can replace this number with any valid port
    
    app.run(port=port, debug = True) 