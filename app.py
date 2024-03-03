# Citation for app.py setup, layout, and CRUD functionalities
# Date: 2/13/24
# Adapted from: Flask Starter App Guide
# Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app
# Adapted from: Professor's Developing in Flask Exploration Video
# Source URL: https://canvas.oregonstate.edu/courses/1946034/pages/exploration-developing-in-flask?module_item_id=23809337

from flask import Flask, render_template, json
from flask import request, redirect
from flask_mysqldb import MySQL
from database.db_connector import connect_to_database, execute_query
import database.db_connector as db
from dotenv import load_dotenv
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

    db_connection = db.connect_to_database()

    return render_template("main.html", title='Home')

# veterinarian page
@app.route("/vets", methods=["POST", "GET"])
def vets():
   db_connection = db.connect_to_database()

   if request.method == "GET":
       query = "SELECT * FROM Vets;"
       cursor = db.execute_query(db_connection=db_connection, query=query)
       results = cursor.fetchall()

    #    query2 = query = "SELECT id_vet, CONCAT(Vets.name, ' (', id_vet, ')') AS vet_name_id FROM Vets;"
    #    cursor = db.execute_query(db_connection=db_connection, query=query2)
    #    vet_results = cursor.fetchall()
       

   return render_template("vets/vets.html", title='Veterinarians', Vets=results)


# adding vet page
@app.route("/add_vet", methods=["POST", "GET"])
def add_vets():
   db_connection = db.connect_to_database()

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
    db_connection = db.connect_to_database()

    query = "DELETE FROM Vets WHERE id_vet = %s;"
    cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
    db_connection.commit()
    return redirect("/vets")

# edit vet page
@app.route("/edit_vet/<int:id_vet>", methods=["GET", "POST"])
def edit_vet(id_vet):
    db_connection = db.connect_to_database()

    if request.method == "GET":
        
        query = "SELECT * FROM Vets WHERE id_vet = %s;"
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id_vet,))
        results = cursor.fetchall()
        return render_template("vets/edit_vet.html", results=results)
        
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

# owners page
@app.route("/owners")
def owners():
     query = "SELECT * FROM Owners;"
     cursor = db.execute_query(db_connection=db_connection, query=query)
     results = cursor.fetchall()
     
     # change the name of the data for better readability
     key_dict = {
        'id_owner': 'ID Owner',
        'name': 'Name',
        'address': 'Address',
        'phone_number': 'Phone Number',
     }
     return render_template("owners/owners.html", title='Owners', Owners = results, key_dict=key_dict)

# adding owner page
@app.route("/add_owner", methods=["POST", "GET"])
def add_owner():
    db_connection = db.connect_to_database()

    if request.method == "POST":
       name = request.form["name"]
       address = request.form["address"]
       phone_number = request.form["phone_number"]

       query = "INSERT INTO Owners (name, address, phone_number) VALUES (%s, %s, %s)"
       cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(name, address, phone_number))
       db_connection.commit()
       return redirect("/owners")

    return render_template("owners/add_owner.html")

# deleting owner page
@app.route("/del_owner/<int:id>")
def del_owner(id):
    db_connection = db.connect_to_database()

    query = "DELETE FROM Owners WHERE id_owner = %s;"
    cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
    db_connection.commit()
    return redirect("/owners")

@app.route("/edit_owner/<int:id_owner>", methods=["GET", "POST"])
def edit_owner(id_owner):
    db_connection = db.connect_to_database()

    if request.method == "GET":
        
        query = "SELECT * FROM Owners WHERE id_owner = %s;"
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id_owner,))
        results = cursor.fetchall()
        return render_template("owners/edit_owner.html", results=results)
        
    if request.method == "POST":
        if request.form.get("Edit_Owner"):
            name = request.form["name"]
            address = request.form["address"]
            phone_number = request.form["phone_number"]
            query = "UPDATE Owners SET name=%s, address=%s, phone_number=%s WHERE id_owner=%s;"
            values = (name, address, phone_number, id_owner)
            db.execute_query(db_connection=db_connection, query=query, query_params= values)
            db_connection.commit()
            return redirect("/owners")
    return render_template("owners/edit_owner.html")

# medications page
@app.route("/meds")
def meds():
    # query = "SELECT * FROM Medications;"
    # cursor = db.execute_query(db_connection=db_connection, query=query)
    # results = cursor.fetchall()

    # return render_template("medications/meds.html", Medications=results)
    return render_template("medications/meds.html", title='Medications')

# adding med page
@app.route("/add_med")
def add_meds():

    return render_template("medications/add_med.html")

# edit med page
@app.route("/edit_med")
def edit_meds():
    return render_template("medications/edit_med.html")

# deleting med page
@app.route("/del_med")
def del_meds():

    return render_template("medications/del_med.html")

# Pets page
@app.route("/pets")
def pets():
     
     # query to get the name of the owner and the vet instead of just getting their id
     query="""SELECT Pets.id_pet, Pets.name, Pets.breed, Pets.age, Pets.gender, 
        Vets.name, Owners.name
        FROM Pets
        LEFT JOIN Owners ON Pets.id_owner = Owners.id_owner
        LEFT JOIN Vets ON Pets.id_vet = Vets.id_vet
        """
     cursor = db.execute_query(db_connection=db_connection, query=query)
     results = cursor.fetchall()

     # change the name of the data for better readability
     key_dict = {
        'id_pet': 'ID Pet',
        'name': 'Name',
        'breed': 'Breed',
        'age': 'Age',
        'gender': 'Gender',
        'Vets.name': 'Vet',
        'Owners.name': 'Owner',
     }
     return render_template("pets/pets.html", title='Pets', Pets=results, key_dict=key_dict)

@app.route("/del_pet/<int:id>")
def del_pets(id):
    db_connection = db.connect_to_database()

    query = "DELETE FROM Pets WHERE id_pet = %s;"
    cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
    db_connection.commit()
    return redirect("/pets")

@app.route("/add_pet", methods=["POST", "GET"])
def add_pets():
   db_connection = db.connect_to_database()

   if request.method == "POST":
       name = request.form["name"]
       breed = request.form["breed"]
       age = request.form["age"]
       gender = request.form["gender"]
       id_vet = request.form["id_vet"]
       id_owner = request.form["id_owner"]

       query = "INSERT INTO Pets (name, breed, age, gender, id_vet, id_owner) VALUES (%s, %s, %s, %s, %s, %s)"
       cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(name, breed, age, gender, id_vet, id_owner))
       db_connection.commit()
       return redirect("/pets")

   return render_template("pets/add_pet.html")

@app.route("/edit_pet/<int:id_pet>", methods=["POST", "GET"])
def edit_pet(id_pet):
    db_connection = db.connect_to_database()

    if request.method == "GET":
        
        query = "SELECT * FROM Pets WHERE id_pet = %s;"
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id_pet,))
        results = cursor.fetchall()
        return render_template("pets/edit_pet.html", results=results)
        
    if request.method == "POST":
        if request.form.get("Edit_Pet"):
            name = request.form["name"]
            breed = request.form["breed"]
            age = request.form["age"]
            gender = request.form["gender"]
            id_vet = request.form["id_vet"]
            id_owner = request.form["id_owner"]
            query = "UPDATE Pets SET name=%s, breed=%s, age=%s, gender=%s, id_vet=%s, id_owner=%s WHERE id_pet=%s;"
            values = (name, breed, age, gender, id_vet, id_owner, id_pet)
            db.execute_query(db_connection=db_connection, query=query, query_params= values)
            db_connection.commit()
            return redirect("/pets")

@app.route("/prescriptions")
def prescriptions():
     query = "SELECT * FROM Prescriptions;"
     cursor = db.execute_query(db_connection=db_connection, query=query)
     results = cursor.fetchall()
     
     key_dict = {
        'id_prescription': 'ID Prescription',
        'order_date': 'Order Date',
        'prescription_cost': 'Prescription Cost',
        'was_picked_up': 'Was Picked Up',
        'id_pet': 'ID Pet',
     }
     return render_template("prescriptions/prescriptions.html", title='Prescriptions', Prescriptions=results, key_dict=key_dict)

@app.route("/del_prescription")
def del_prescriptions():
    db_connection = db.connect_to_database()

    query = "DELETE FROM Prescriptions WHERE id_prescription = %s;"
    cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
    db_connection.commit()
    return redirect("/prescriptions")

@app.route("/add_prescription", methods=["POST", "GET"])
def add_prescriptions():
    db_connection = db.connect_to_database()
    
    if request.method == "POST":
       order_date = request.form["order_date"]
       was_picked_up = request.form["was_picked_up"]
       id_pet = request.form["id_pet"]

       query = "INSERT INTO Prescriptions (order_date, was_picked_up, id_pet) VALUES (%s, %s, %s)"
       cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(order_date, was_picked_up, id_pet))
       
       db_connection.commit()
       return redirect("/prescriptions")
    
    return render_template("prescriptions/add_prescription.html")

@app.route("/edit_prescription/<int:id_prescription>", methods=["POST", "GET"])
def edit_prescription(id_prescription):
    db_connection = db.connect_to_database()

    if request.method == "GET":
        
        query = "SELECT * FROM Prescriptions WHERE id_prescription = %s;"
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id_prescription,))
        results = cursor.fetchall()
        return render_template("prescriptions/edit_prescription.html", results=results)
        
    if request.method == "POST":
        if request.form.get("Edit_Prescription"):
            order_date = request.form["order_date"]
            prescription_cost = request.form["prescription_cost"]
            was_picked_up = request.form["was_picked_up"]
            id_pet = request.form["id_pet"]
            query = "UPDATE Prescriptions SET order_date=%s,  prescription_cost=%s, was_picked_up=%s, id_pet=%s WHERE id_pet=%s;"
            values = (order_date, prescription_cost, was_picked_up, id_pet)
            db.execute_query(db_connection=db_connection, query=query, query_params= values)
            db_connection.commit()
            return redirect("/prescriptions")

@app.route("/prescriptMeds")
def intersection():
    # query = "SELECT * FROM PrescriptionMedications;"
    # cursor = db.execute_query(db_connection=db_connection, query=query)
    # results = cursor.fetchall()
    # return render_template("intersection/prescriptMeds.html", PrescriptionMedications=results)

    return render_template("intersection/prescriptMeds.html", title='prescriptionMedications')

@app.route("/add_prescriptMeds")
def add_prescriptMeds():

    return render_template("intersection/add_prescriptMeds.html")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 58581)) 
     #                               ^^^^
    #             You can replace this number with any valid port
    
    app.run(port=port, debug = True) 