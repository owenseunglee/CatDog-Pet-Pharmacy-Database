 --Citation for DML.SQL file
 --Date: 2/13/24
 --Adapted from: Professor's bsg_sample_data_manipulation_queries file
 --Source URL: https://canvas.oregonstate.edu/courses/1946034/assignments/9456216?module_item_id=23809330

-- gets all attributes for the Vets page
SELECT * FROM Vets

-- gets all attributes for the Owners page
SELECT * FROM Owners

-- gets all attributes for the Medications page
SELECT * FROM Medications

-- gets all Prescriptions information and the corresponding pet's name for the Prescriptions page
SELECT Prescriptions.id_prescription, Prescriptions.order_date, 
    SUM(Medications.cost * PrescriptionMedications.quantity) as prescription_cost,
    Prescriptions.was_picked_up, Pets.name AS pet_name
    FROM Prescriptions
    INNER JOIN PrescriptionMedications ON Prescriptions.id_prescription = PrescriptionMedications.id_prescription
    INNER JOIN Medications ON PrescriptionMedications.id_medication = Medications.id_medication
    INNER JOIN Pets ON Prescriptions.id_pet = Pets.id_pet
    GROUP BY 
        Prescriptions.id_prescription, 
        Prescriptions.order_date, 
        Prescriptions.was_picked_up, 
        Pets.name;

-- gets all attributes for the PrescriptionMedications page
SELECT * FROM PrescriptionMedications

-- get all pets and their owner's name and vet's name
SELECT Pets.id_pet, name, breed, age, gender, Owners.name AS owner_name, Vets.name AS vet_name
FROM Pets
INNER JOIN Owners ON Pets.id_owner = Owners.id_owner
INNER JOIN Vets ON Pets.id_vet = Vets.id_vet;

-- get a single pet's data
SELECT id_pet, name, breed, age, gender, id_vet, id_owner
FROM Pets
WHERE id_pet = :pet_ID_selected_from_browse_pet_page

-- get all pets with their current associated vets
SELECT id_pet, id_vet, Pets.name AS pet_name, Vets.name AS vet_name
FROM Pets
INNER JOIN Vets ON Pets.id_vet = Vets.id_vet
ORDER BY pet_name, vet_name;

-- get all vet IDs and names to populate the vet dropdown
SELECT id_vet, name FROM Vets

-- get all owner IDs and names to populate the owner dropdown
SELECT id_owner, name FROM Owners

-- get all pet IDs and names to populate the pet dropdown
SELECT id_pet, name FROM Pets

-- gets all medication IDs and names to populate the medication dropdown
SELECT id_medication, name FROM Medications

-- gets prescription name and pet name to populate the prescription dropdown in the intersection table
SELECT CONCAT(Pets.name, ' - ', order_date) AS prescription_info
FROM Prescriptions
JOIN Pets ON Prescriptions.id_pet = Pets.id_pet;

-- add a new pet. list of vets and owners will be displayed in dropdown 
INSERT INTO Pets (name, breed, age, gender, id_vet, id_owner)
VALUES (:nameInput, :breedInput, :ageInput, :genderInput, :vet_id_from_dropdown_Input, :owner_id_from_dropdown_Input)

-- add a new prescription. the prescription cost is calculated from Medications and PrescriptionMedications
INSERT INTO Prescriptions (order_date, prescription_cost, was_picked_up, id_pet)
VALUES (:order_date_Input,
        (SELECT SUM(Medications.cost * PrescriptionMedications.quantity)
        FROM PrescriptionMedications
        INNER JOIN Medications ON PrescriptionMedications.id_medication = Medications.id_medication
        WHERE PrescriptionMedications.id_prescription = :newly_inserted_prescription_id),
    :was_picked_up_Input,
    :pet_id_from_dropdown_Input);

-- add a new medication
INSERT INTO Medications (name, cost) VALUES (:nameInput, :costInput);

-- add a new owner
INSERT INTO Owneres (name, address, phone_number) VALUES (:nameInput, :addressInput, :phone_numberInput);


-- add a new vet
INSERT INTO Vets (name, clinic, email, no_of_patients) VALUES (:nameInput, :clinicInput, :emailInput, :no_of_patientsInput);

-- add a new entry to the PrescriptionMedications table
INSERT INTO PrescriptionMedications (id_prescription, id_medication, quantity) 
VALUES (:prescription_info_from_dropdown_Input, :medication_id_from_dropdown_Input, :quantityInput);

-- update vets
UPDATE Vets SET name = :nameInput, clinic = :clinicInput, email = :emailInput, no_of_patients = :no_of_patientsInput
WHERE id_vet = :vet_ID_selected_from_browse_vet_page

-- update Medications 
UPDATE Medications SET name = :nameInput, cost = :costInput
WHERE id_medication = :medication_ID_selected_from_browse_medication_page

-- delete a pet
DELETE FROM Pets WHERE id = :pet_ID_selected_from_browse_pet_page

-- delete a medication
DELETE FROM Medications WHERE id = :medication_ID_selected_from_browse_medication_page

-- deletes a prescription from a medication (M-to-M relationship deletion)
DELETE FROM PrescriptionMedications WHERE id_prescription = :prescriptionIdInput AND id_medication = :medicationIdInput
