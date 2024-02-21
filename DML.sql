 --Citation for DML.SQL file
 --Date: 2/13/24
 --Adapted from: Professor's bsg_sample_data_manipulation_queries file
 --Source URL: https://canvas.oregonstate.edu/courses/1946034/assignments/9456216?module_item_id=23809330

-- ** Vets **

-- gets all attributes for the Vets page
SELECT * FROM Vets;

-- get a single vet's data to pre-populate for the Update Veterinarian page 
SELECT CONCAT(name, ' (', id_vet, ')') AS vet_info, name, clinic, email, no_of_patients
FROM Vets
WHERE id_vet = :id_vet_selected_from_browse_vet_page;

-- gets a Vet's name and corresponding id_vet for the dropdown in Browse Veterinarians and Update Vet page
-- Browse Pets, Update Pet page
SELECT id_vet, CONCAT(Vets.name, ' (', id_vet, ')') AS vet_name_id
FROM Vets;

-- add a new vet
INSERT INTO Vets (name, clinic, email, no_of_patients) VALUES (:nameInput, :clinicInput, :emailInput, :no_of_patientsInput);

-- update a Vet
UPDATE Vets SET name = :nameInput, clinic = :clinicInput, email = :emailInput, no_of_patients = :no_of_patientsInput
WHERE id_vet = :vet_ID_selected_from_browse_vet_page;

-- delete a Vet
DELETE FROM Vets WHERE id = :vet_ID_selected_from_browse_vet_page;

-- ** Owners **

-- gets all attributes for the Owners page
SELECT * FROM Owners;

-- get a single owner's data to pre-populate for the Update Owner page 
SELECT CONCAT(name, ' (', id_owner, ')') AS owner_info, name, address, phone_number
FROM Owners
WHERE id_owner = :id_owner_selected_from_browse_owner_page;

-- gets an Owner's name and corresponding id_owner for the dropdown in Browse Owners and Update Owner page,
-- Also in Browse Pets, Update Pet page
SELECT id_owner, CONCAT(Owners.name, ' (', id_owner, ')') AS owner_name_id
FROM Owners;

-- add a new owner
INSERT INTO Owners (name, address, phone_number) VALUES (:nameInput, :addressInput, :phone_numberInput);

-- update owners
UPDATE Owners SET name = :nameInput, address = :addressInput, phone_number = :phone_numberInput
WHERE id_owner = :id_owner_selected_from_browse_owner_page;

-- delete an Owner
DELETE FROM Owners WHERE id = :owner_ID_selected_from_browse_owner_page;

-- ** Pets **

-- gets all attributes for the Pets page
SELECT * FROM Pets;
-- (alternative - more descriptive)
-- get all attributes for the Pets page along with their owner's name and vet's name
SELECT Pets.id_pet, Pets.name, breed, age, gender, Owners.name AS owner_name, Vets.name AS vet_name
FROM Pets
INNER JOIN Owners ON Pets.id_owner = Owners.id_owner
INNER JOIN Vets ON Pets.id_vet = Vets.id_vet;

-- get a single pet's data to pre-populate for the Update Pet page 
SELECT CONCAT(Pets.name, ' (', id_pet, ')') AS pet_info, Pets.name, Pets.breed, Pets.age, Pets.gender,
       CONCAT(Vets.name, ' (', Vets.id_vet, ')') AS vet_info, 
       CONCAT(Owners.name, ' (', Owners.id_owner, ')') AS owner_info
FROM Pets
LEFT JOIN Vets ON Pets.id_vet = Vets.id_vet
LEFT JOIN Owners ON Pets.id_owner = Owners.id_owner
WHERE Pets.id_pet = :id_pet_selected_from_browse_pet_page;

-- gets a Pet's name and corresponding id_pet for the dropdown in Browse Pets and Update Pet page
-- and Browse Prescriptions and Update Prescriptions page
SELECT id_pet, CONCAT(Pets.name, ' (', id_pet, ')') AS pet_name_id
FROM Pets;

-- add a new pet. list of vets and owners will be displayed in dropdown 
INSERT INTO Pets (name, breed, age, gender, id_vet, id_owner)
VALUES (:nameInput, :breedInput, :ageInput, :genderInput, :vet_id_from_dropdown_Input, :owner_id_from_dropdown_Input);


-- update Pets
UPDATE Pets SET name = :nameInput, breed = :breedInput, age = :ageInput,
 gender = :gender_dropdown_Input, id_vet = :vet_id_from_dropdown_Input, id_owner = :owner_id_from_dropdown_Input
WHERE id_pet = :petIDSelectedFromBrowsePetPage;

-- delete a pet
DELETE FROM Pets WHERE id = :pet_ID_selected_from_browse_pet_page;

-- ** Medications **

-- gets all attributes for the Medications page
SELECT * FROM Medications;

-- get a single medications's data to pre-populate for the Update Medication page 
SELECT CONCAT(name, ' (', id_medication, ')') AS med_info, name, cost
FROM Medications
WHERE id_medication = :id_medication_selected_from_browse_med_page;

-- gets a Medication's name and corresponding id_medication for the dropdown in Browse Medications and Update Medication page
SELECT id_medication, CONCAT(Medications.name, ' (', id_medication, ')') AS med_name_id
FROM Medications;

-- add a new Medication
INSERT INTO Medications (name, cost) VALUES (:nameInput, :costInput);

-- update Medication
UPDATE Medications 
SET name = :nameInput, cost = :costInput 
WHERE id_medication = :id_medication_selected_from_browse_med_page;

-- delete a medication
DELETE FROM Medications WHERE id = :medication_ID_selected_from_browse_medication_page;

-- ** Prescriptions **

-- gets all attributes for the Prescriptions page
SELECT * FROM Prescriptions;
-- (alternative - more descriptive)
-- gets all attributes for the Prescriptions page which will show
-- the Pet name and calculate the prescription_cost
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

-- get a single prescriptions's data to pre-populate for the Update Prescription page 
SELECT CONCAT(Prescriptions.order_date, ' (', id_prescriptions, ')') AS pres_info, Prescriptions.order_date, Prescriptions.prescription_cost,
       Prescriptions.was_picked_up,
       CONCAT(Pets.name, ' (', Pets.id_pet, ')') AS pet_info
FROM Prescriptions
LEFT JOIN Pets ON Pets.id_pet = Prescriptions.id_pet
WHERE Prescriptions.id_prescription = :id_prescription_selected_from_browse_prescription_page;

-- gets a Prescription's order_date and corresponding id_prescription for the dropdown in Browse Prescriptions and Update Prescription page
SELECT id_prescription, CONCAT(Prescription.order_date, ' (', id_prescription, ')') AS prescription_date_id
FROM Prescriptions;

-- add a new prescription. the prescription cost is calculated from Medications and PrescriptionMedications
INSERT INTO Prescriptions (order_date, prescription_cost, was_picked_up, id_pet)
VALUES (:order_date_Input,
        (SELECT SUM(Medications.cost * PrescriptionMedications.quantity)
        FROM PrescriptionMedications
        INNER JOIN Medications ON PrescriptionMedications.id_medication = Medications.id_medication
        WHERE PrescriptionMedications.id_prescription = :newly_inserted_prescription_id),
    :was_picked_up_Input,
    :pet_id_from_dropdown_Input);

-- update prescription
UPDATE Prescriptions 
SET order_date = :orderDateInput, prescription_cost = :prescriptionCostInput, 
was_picked_up = :wasPickedUp_dropdown_Input, id_pet = :pet_id_from_dropdown_Input
WHERE id_prescription = :prescriptionIDSelectedFromBrowsePrescriptionPage;

-- delete a Prescription
DELETE FROM Prescriptions WHERE id = :prescriptionIDSelectedFromBrowsePrescriptionPage;

-- ** PrescriptionMedications **

-- gets all attributes for the PrescriptionMedications page
SELECT * FROM PrescriptionMedications 

-- gets a corresponding Pet's name, their Prescription order_date, and corresponding id_prescription for the dropdown in Add PrescriptionMedications page
SELECT id_prescription, CONCAT(Pets.name, ', ', Prescriptions.order_date, ' (', id_prescription, ')') 
AS petname_and_presc_orderdate_and_presc_id
FROM PrescriptionMedications
    INNER JOIN Prescriptions ON Prescriptions.id_prescription = PrescriptionMedications.id_prescription
    INNER JOIN Pets ON Prescriptions.id_pet = Pets.id_pet;

-- gets a corresponding medication's name and id_medication for the dropdown in Add PrescriptionMedications page
SELECT id_medication, CONCAT(Medications.name, ' (', id_medication, ')') 
AS med_info
FROM PrescriptionMedications
    INNER JOIN Medications ON Medications.id_medication = PrescriptionMedications.id_medication;

-- add a new entry to the PrescriptionMedications table
INSERT INTO PrescriptionMedications (id_prescription, id_medication, quantity) 
VALUES (:prescription_info_from_dropdown_Input, :medication_info_from_dropdown_Input, :quantityInput);

-- dissociates Prescription from Medication
DELETE FROM PrescriptionMedications WHERE id_prescription = :prescriptionIdInput AND id_medication = :medicationIdInput;


-- old queries
-- -- get a single pet's data for the Update Pet page
-- SELECT id_pet, name, breed, age, gender, id_vet, id_owner
-- FROM Pets
-- WHERE id_pet = :pet_ID_selected_from_browse_pet_page

-- -- get all pets with their current associated vets
-- SELECT id_pet, id_vet, Pets.name AS pet_name, Vets.name AS vet_name
-- FROM Pets
-- INNER JOIN Vets ON Pets.id_vet = Vets.id_vet
-- ORDER BY pet_name, vet_name;

-- -- get all vet IDs and names to populate the vet dropdown
-- SELECT id_vet, name FROM Vets

-- -- get all owner IDs and names to populate the owner dropdown
-- SELECT id_owner, name FROM Owners

-- -- get all pet IDs and names to populate the pet dropdown
-- SELECT id_pet, name FROM Pets

-- -- gets all medication IDs and names to populate the medication dropdown
-- SELECT id_medication, name FROM Medications

-- -- gets prescription name and pet name to populate the prescription dropdown in the intersection table
-- SELECT CONCAT(Pets.name, ' - ', order_date) AS prescription_info
-- FROM Prescriptions
-- JOIN Pets ON Prescriptions.id_pet = Pets.id_pet;