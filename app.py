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
       query = "SELECT * FROM Vets ORDER BY Vets.name;"
       cursor = db.execute_query(db_connection=db_connection, query=query)
       results = cursor.fetchall()
       key_dict = {
        'id_vet': 'Vet ID',
        'name': 'Name',
        'clinic': 'Clinic',
        'email': 'Email Address',
        'no_of_patients': 'Number of Patients',
        }

   
       
        
   
   return render_template("vets/vets.html", title='Veterinarians', Vets=results, key_dict=key_dict)


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
        
        # get a single vet's data to pre-populate for the Update Veterinarian page 
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
    db_connection = db.connect_to_database()

    
    query = "SELECT * FROM Owners ORDER BY Owners.name;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    
    # change the name of the data for better readability
    key_dict = {
    'id_owner': 'Owner ID',
    'name': 'Name',
    'address': 'Address',
    'phone_number': 'Phone Number',
    }
    return render_template("owners/owners.html", title='Owners', Owners = results, key_dict=key_dict)

# adding owner page
@app.route("/add_owner", methods=["POST", "GET"])
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
        # get a single owner's data to pre-populate for the Update Owner page 
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
@app.route("/meds", methods=["POST", "GET"])
def meds():
    db_connection = db.connect_to_database()
    if request.method == "GET":
        query = "SELECT * FROM Medications ORDER BY Medications.name;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        key_dict = {
        'id_medication': 'Medication ID',
        'name': 'Name',
        'cost': 'Cost',
     
        }

    return render_template("medications/meds.html", title='Medications', Medications=results, key_dict=key_dict)

# adding med page
@app.route("/add_med", methods=["POST", "GET"])
def add_meds():
    db_connection = db.connect_to_database()

    if request.method == "POST":
       name = request.form["name"]
       cost = request.form["cost"]

       query = "INSERT INTO Medications (name, cost) VALUES (%s, %s)"
       cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(name, cost))
       db_connection.commit()
       return redirect("/meds")

    return render_template("medications/add_med.html")

@app.route("/edit_med/<int:id_medication>", methods=["GET", "POST"])
def edit_meds(id_medication):
    db_connection = db.connect_to_database()

    if request.method == "GET":
        # get a single medications's data to pre-populate for the Update Medication page 

        query = "SELECT * FROM Medications WHERE id_medication = %s;"
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id_medication,))
        results = cursor.fetchall()
        return render_template("medications/edit_med.html", results=results)
        
    if request.method == "POST":
        if request.form.get("Edit_Med"):
            name = request.form["name"]
            cost = request.form["cost"]
            query = "UPDATE Medications SET name=%s, cost=%s WHERE id_medication=%s;"
            values = (name, cost, id_medication)
            db.execute_query(db_connection=db_connection, query=query, query_params= values)
            db_connection.commit()
            return redirect("/meds")

# deleting med page
@app.route("/del_med/<int:id>")
def del_meds(id):

    db_connection = db.connect_to_database()

    query = "DELETE FROM Medications WHERE id_medication = %s;"
    cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
    db_connection.commit()
    return redirect("/meds")

@app.route("/pets", methods=["POST", "GET"])
def pets():
     db_connection = db.connect_to_database()
     # query = "SELECT Pets.id_pet, Pets.name, breed, age, gender, Owners.name AS owner_name, Vets.name AS vet_name FROM Pets INNER JOIN Owners ON Pets.id_owner = Owners.id_owner INNER JOIN Vets ON Pets.id_vet = Vets.id_vet;"
     query = "SELECT Pets.id_pet, Pets.name, breed, age, gender, Owners.name AS owner_name, Vets.name AS vet_name FROM Pets INNER JOIN Owners ON Pets.id_owner = Owners.id_owner LEFT JOIN Vets ON Pets.id_vet = Vets.id_vet ORDER BY Pets.name;"

     cursor = db.execute_query(db_connection=db_connection, query=query)
     results = cursor.fetchall()
     key_dict = {
        'id_pet': 'Pet ID',
        'name': 'Name',
        'breed': 'Breed',
        'age': 'Age',
        'gender': 'Gender',
        'owner_name': 'Owner Name',
        'vet_name': 'Vet Name',
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
    if request.method == "GET":
        # Fetch the list of owners from the database for dropdown
        query = "SELECT id_owner, CONCAT(name, ' (', id_owner, ')') AS owner_name_and_id FROM Owners;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        owner_results = cursor.fetchall()
        # Fetch the list of vets from the database for dropdown
        query2 = "SELECT id_vet, CONCAT(name, ' (', id_vet, ')') AS vet_name_and_id FROM Vets;"
        cursor2 = db.execute_query(db_connection=db_connection, query=query2)
        vet_results = cursor2.fetchall()
    
        
        return render_template("pets/add_pet.html", Owner_Dropdown=owner_results, Vet_Dropdown=vet_results)

    elif request.method == "POST":
            # Get form data
            name = request.form["name"]
            breed = request.form["breed"]
            age = request.form["age"]
            gender = request.form["gender"]
            id_owner = request.form["owner_select"]
            id_vet = request.form["vet_select"]
            
            if id_vet == "":
                id_vet = None
            
            print("Received form data:")
            print("Name:", name)
            print("Breed:", breed)
            print("Age:", age)
            print("Gender:", gender)
            print("Owner ID:", id_owner)
            print("Vet ID:", id_vet) # confirmed id_vet is None

            # if Vet doesn't exist yet
            if id_vet == None or id_vet == "":
                query = "INSERT INTO Pets (name, breed, age, gender, id_owner, id_vet) VALUES (%s, %s, %s, %s, %s, NULL)"
                query_params = (name, breed, age, gender, id_owner)
                cursor = db.execute_query(db_connection=db_connection, query=query, query_params=query_params)
                db_connection.commit()
            else:
                query = "INSERT INTO Pets (name, breed, age, gender, id_owner, id_vet) VALUES (%s, %s, %s, %s, %s, %s)"
                query_params = (name, breed, age, gender, id_owner, id_vet)
                cursor = db.execute_query(db_connection=db_connection, query=query, query_params=query_params)
                db_connection.commit()
            return redirect("/pets")
    

    
@app.route("/edit_pet/<int:id_pet>", methods=["GET", "POST"])
def edit_pet(id_pet):
    db_connection = db.connect_to_database()

    if request.method == "GET":
        
        # currently editing Pet
        query = "SELECT * FROM Pets WHERE id_pet = %s;"
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id_pet,))
        results = cursor.fetchall()

        # the vet for the current Pet we are editing
        query2 = "SELECT Vets.name AS vet_name FROM Pets LEFT JOIN Vets ON Pets.id_vet = Vets.id_vet WHERE Pets.id_pet = %s;"
        # query2 = "SELECT Vets.id_vet, Vets.name AS vet_name FROM Vets LEFT JOIN Pets ON Pets.id_vet = Vets.id_vet;"
        cursor2 = db.execute_query(db_connection=db_connection, query=query2, query_params=(id_pet,))
        current_vet_results = cursor2.fetchall()

        # current owner we are editing
        query3 = "SELECT Owners.name AS owner_name FROM Pets INNER JOIN Owners ON Pets.id_owner = Owners.id_owner WHERE id_pet = %s;"
        # query3 = "SELECT Owners.id_owner, Owners.name AS owner_name FROM Owners LEFT JOIN Pets ON Pets.id_owner = Owners.id_owner;"
        cursor3 = db.execute_query(db_connection=db_connection, query=query3, query_params=(id_pet,))
        current_owner_results = cursor3.fetchall()

        # Owner dropdown in edit
        query4 = "SELECT DISTINCT Owners.id_owner, Owners.name AS owner_name FROM Owners LEFT JOIN Pets ON Pets.id_owner = Owners.id_owner ORDER BY owner_name;"
        cursor4 = db.execute_query(db_connection=db_connection, query=query4)
        owner_results = cursor4.fetchall()

        # Vet dropdown in edit
        query5 = "SELECT DISTINCT Vets.id_vet, Vets.name AS vet_name FROM Vets LEFT JOIN Pets ON Pets.id_vet = Vets.id_vet ORDER BY vet_name;"
        cursor5 = db.execute_query(db_connection=db_connection, query=query5)
        vet_results = cursor5.fetchall()


        return render_template("pets/edit_pet.html", results=results, current_owner_results=current_owner_results, current_vet_results=current_vet_results, Owner_Dropdown = owner_results,Vet_Dropdown = vet_results)

    if request.method == "POST":
        if request.form.get("Edit_Pet"):
            name = request.form["name"]
            id_owner = request.form["owner_select"]
            id_vet = request.form["vet_select"]
            breed = request.form["breed"]
            age = request.form["age"]
            gender = request.form["gender"]


            if id_vet == "": 
                id_vet = None

            # Print statements for debugging
            print("Name:", name)
            print("Owner ID:", id_owner)
            print("Vet ID:", id_vet)
            print("Breed:", breed)
            print("Age:", age)
            print("Gender:", gender)
            
            if id_vet == None or id_vet == "":
                print("this is none")
                query = "UPDATE Pets SET Pets.name=%s, Pets.id_owner=%s, Pets.id_vet= NULL, Pets.breed=%s, Pets.age=%s, Pets.gender=%s WHERE Pets.id_pet = %s"
                values = (name, id_owner, breed, age, gender, id_pet)
                db.execute_query(db_connection=db_connection, query=query, query_params= values)
                db_connection.commit()
            else: 
                print("not none")
                query = "UPDATE Pets set Pets.name=%s, Pets.id_owner=%s, Pets.id_vet=%s, Pets.breed=%s, Pets.age=%s, Pets.gender=%s WHERE Pets.id_pet = %s"
                values = (name, id_owner, id_vet, breed, age, gender, id_pet)
                db.execute_query(db_connection=db_connection, query=query, query_params= values)
                db_connection.commit()

            return redirect("/pets")
            
        
@app.route("/prescriptions", methods=["POST", "GET"])
def prescriptions():
     db_connection = db.connect_to_database()
     if request.method == "GET":
        # query = "SELECT Prescriptions.id_prescription, Prescriptions.order_date, Prescriptions.prescription_cost, Prescriptions.was_picked_up, FROM Prescriptions INNER JOIN Pets ON Prescriptions.id_pet = Pets.id_pet ORDER BY Prescriptions.order_date;"
        query = "SELECT Prescriptions.id_prescription, Pets.name AS pet_name, Prescriptions.order_date, Prescriptions.prescription_cost, Prescriptions.was_picked_up FROM Prescriptions INNER JOIN Pets ON Prescriptions.id_pet = Pets.id_pet ORDER BY Prescriptions.order_date;"

        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        for result in results:
            result['was_picked_up'] = 'Yes' if result['was_picked_up'] == 1 else 'No'

        key_dict = {
        'id_prescription': 'Prescription ID',
        'order_date': 'Order Date',
        'prescription_cost': 'Prescription Cost',
        'was_picked_up': 'Was Picked Up',
        'pet_name': 'Pet Name',
        }
     
     return render_template("prescriptions/prescriptions.html", title='Prescriptions', Prescriptions=results, key_dict = key_dict)

@app.route("/del_prescription/<int:id>")
def del_prescriptions(id):
    db_connection = db.connect_to_database()

    query = "DELETE FROM Prescriptions WHERE id_prescription = %s;"
    cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id,))
    db_connection.commit()
    return redirect("/prescriptions")

def update_cost(pet_id):
    # query to update the prescription_cost( med's cost X quantity) + previously stored prescription_cost
    query = """
    UPDATE Prescriptions
    INNER JOIN (
        SELECT PrescriptionMedications.id_prescription, SUM(Medications.cost * PrescriptionMedications.quantity) AS total_cost
        FROM PrescriptionMedications
        INNER JOIN Medications ON PrescriptionMedications.id_medication = Medications.id_medication
        WHERE PrescriptionMedications.id_prescription = %s
        GROUP BY PrescriptionMedications.id_prescription
    ) subquery ON Prescriptions.id_prescription = subquery.id_prescription
    SET Prescriptions.prescription_cost = subquery.total_cost;
    """
    cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(pet_id,))
    db_connection.commit()

@app.route("/add_prescription", methods=["POST", "GET"])
def add_prescriptions():
    db_connection = db.connect_to_database()
    if request.method == "GET":
        # Fetch the list of pets from the database for dropdown
        query = "SELECT id_pet, CONCAT(name, ' (', id_pet, ')') AS pet_name_and_id FROM Pets;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        pet_results = cursor.fetchall()
        
        return render_template("prescriptions/add_prescription.html", Pet_Dropdown=pet_results)
    elif request.method == "POST":
        # Get form data
        order_date = request.form["order_date"]
        prescription_cost = 0
        was_picked_up = request.form["picked_up"]
        pet_id = request.form["pet_select"]
        
        # Insert prescription into the database
        query = "INSERT INTO Prescriptions (order_date, prescription_cost, was_picked_up, id_pet) VALUES (%s, %s, %s, %s)"
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(order_date, prescription_cost, was_picked_up, pet_id))
        db_connection.commit()

        # Redirect to prescriptions page after successful insertion
        return redirect("/prescriptions")

    return render_template("prescriptions/add_prescription.html", Pet_Dropdown=pet_results)

    # db_connection = db.connect_to_database()

    # if request.method == "GET":
    #     query1 = "SELECT id_pet, CONCAT(name, ' (', id_pet, ')') AS pet_name_and_id FROM Pets;"
    #     cursor1 = db.execute_query(db_connection=db_connection, query=query1)
    #     pet_results = cursor1.fetchall()
        
    #     return render_template("prescriptions/add_prescription.html", Pet_Dropdown=pet_results)
    
    # elif request.method == "POST":
    #     # Get data from the form
    #     order_date = request.form["order_date"]
    #     was_picked_up = request.form["picked_up"]
    #     pet_id = request.form["pet_select"]

    #     # Insert the prescription into the database
    #     query = "INSERT INTO Prescriptions (order_date, prescription_cost, was_picked_up, id_pet) VALUES (%s, %s, %s, %s)"
    #     # Assuming prescription_cost is calculated elsewhere or has a default value
    #     cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(order_date, None, was_picked_up, pet_id))
    #     db_connection.commit()

    #     # Redirect the user to the prescriptions page
    #     return redirect("/prescriptions")

    # return render_template("prescriptions/add_prescription.html")

@app.route("/edit_prescription/<int:id_prescription>", methods=["GET", "POST"])
def edit_prescription(id_prescription):

    db_connection = db.connect_to_database()

    if request.method == "GET":
        
        # currently editing Prescription
        query = "SELECT * FROM Prescriptions WHERE id_prescription = %s;"
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(id_prescription,))
        results = cursor.fetchall()

        # Pet dropdown in edit
        # this query allows us to update to any pet, including those who don't have a prescription yet
        query2 = "SELECT Pets.id_pet, CONCAT(Pets.name, ' (', Pets.id_pet, ')') AS pet_name_and_id, Prescriptions.order_date FROM Pets LEFT JOIN Prescriptions ON Pets.id_pet = Prescriptions.id_pet ORDER BY Pets.name, Prescriptions.order_date;"

        cursor2 = db.execute_query(db_connection=db_connection, query=query2)
        pet_results = cursor2.fetchall()

        # display the Pet that is part of the prescription we're currently editing
        query3 = "SELECT Prescriptions.order_date, Prescriptions.prescription_cost, Prescriptions.was_picked_up, Pets.name AS pet_name FROM Prescriptions INNER JOIN Pets ON Prescriptions.id_pet = Pets.id_pet WHERE id_prescription = %s;"
        cursor3 = db.execute_query(db_connection=db_connection, query=query3, query_params=(id_prescription,))
        current_pet_results = cursor3.fetchall()

        
        return render_template("prescriptions/edit_prescription.html", results=results, Pet_Dropdown = pet_results, current_pet_results = current_pet_results )
    
    if request.method == "POST":
        if request.form.get("Edit_Prescription"):
            order_date = request.form["order_date"]
            # prescription_cost = request.form["prescription_cost"]
            was_picked_up = request.form["was_picked_up"]
            id_pet = request.form["pet_select"]

            query = "UPDATE Prescriptions SET order_date=%s, was_picked_up=%s, id_pet=%s WHERE id_prescription=%s;"
            values = (order_date, was_picked_up, id_pet, id_prescription)
            db.execute_query(db_connection=db_connection, query=query, query_params= values)
            db_connection.commit()
            return redirect("/prescriptions")
        
@app.route("/prescriptMeds", methods=["POST", "GET"])
def intersection():
    db_connection = db.connect_to_database()

    if request.method == "GET":
       query = "SELECT CONCAT(Pets.name, ' (', Prescriptions.order_date, ')') AS pet_and_prescription_order_date, Medications.name AS medication_name, quantity FROM PrescriptionMedications INNER JOIN Prescriptions ON PrescriptionMedications.id_prescription = Prescriptions.id_prescription INNER JOIN Medications ON PrescriptionMedications.id_medication = Medications.id_medication INNER JOIN Pets ON Prescriptions.id_pet = Pets.id_pet ORDER BY Prescriptions.order_date,Pets.name, Medications.name;"
       # includes None Prescriptions: 
       # query = "SELECT CONCAT(Pets.name, ' (', Prescriptions.order_date, ')') AS pet_and_prescription_order_date, Medications.name AS medication_name, quantity FROM PrescriptionMedications LEFT JOIN Prescriptions ON PrescriptionMedications.id_prescription = Prescriptions.id_prescription LEFT JOIN Medications ON PrescriptionMedications.id_medication = Medications.id_medication LEFT JOIN Pets ON Prescriptions.id_pet = Pets.id_pet ORDER BY Prescriptions.order_date, Pets.name, Medications.name;"
       cursor = db.execute_query(db_connection=db_connection, query=query)
       results = cursor.fetchall()
       key_dict = {
        'pet_and_prescription_order_date': 'Pet (Prescription Order Date)',
        'medication_name': 'Medication Name',
        'quantity': 'Quantity',
        }
   
    return render_template("intersection/prescriptMeds.html", title='prescriptionMedications', PrescriptionMedications=results, key_dict=key_dict)


@app.route("/add_prescriptMeds", methods=["POST", "GET"])
def add_prescriptMeds():
    db_connection = db.connect_to_database()
    if request.method == "POST":
        prescription_id = request.form["prescription_select"]
        medication_id = request.form["medication_select"]
        quantity = request.form["quantity"]
        if not quantity:
            quantity = 1
        else:
            quantity = int(quantity) 
        
        # if prescription_id == "":
        #     prescription_id = None
        
        # if prescription_id == None or prescription_id == "":
        #     query = "INSERT INTO PrescriptionMedications (id_prescription, id_medication, quantity) VALUES (NULL, %s, %s)"
        #     query_params = (medication_id, quantity)
        #     cursor = db.execute_query(db_connection=db_connection, query=query, query_params=query_params)
        #     db_connection.commit()
        # else:
        query = "INSERT INTO PrescriptionMedications (id_prescription, id_medication, quantity) VALUES (%s, %s, %s)"
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(prescription_id, medication_id, quantity))
        db_connection.commit()

        # call this function to automatically update the prescription cost
        update_cost(prescription_id)

        return redirect("/prescriptMeds")
    
    elif request.method == "GET":
        # Prescription Dropdown
        query1 = "SELECT Prescriptions.id_prescription AS id_prescription, CONCAT(Pets.name, ', ', Prescriptions.order_date, ' (', Prescriptions.id_prescription, ')') AS pet_order_date_prescription_ID FROM Prescriptions INNER JOIN Pets ON Prescriptions.id_pet = Pets.id_pet ORDER BY Prescriptions.order_date, Pets.name;"
        cursor1 = db.execute_query(db_connection=db_connection, query=query1)
        prescription_results = cursor1.fetchall()
        print("Prescription Results:", prescription_results)
        # Medication Dropdown
        query2 = "SELECT Medications.id_medication, CONCAT(Medications.name, ' (', Medications.id_medication, ')') AS med_info FROM Medications ORDER BY Medications.name;"
        cursor2 = db.execute_query(db_connection=db_connection, query=query2)
        med_results = cursor2.fetchall()
        print("Medication Results:", med_results)


        return render_template("intersection/add_prescriptMeds.html", Prescriptions_Dropdown=prescription_results, Medications_Dropdown=med_results)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 58511)) 
     #                               ^^^^
    #             You can replace this number with any valid port
    
    app.run(port=port, debug = True) 