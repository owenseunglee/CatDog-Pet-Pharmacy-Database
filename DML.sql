-- ** Vets **

-- gets all attributes for the Vets page
SELECT * FROM Vets;

-- updated as of step 5 draft
-- get a single vet's data to pre-populate for the Update Veterinarian page 
SELECT * FROM Vets WHERE id_vet = %s;

-- updated as of step 5 draft
-- gets the Vet assigned to the current pet we are editing in Edit Pets page
SELECT Vets.name AS vet_name FROM Pets LEFT JOIN Vets ON Pets.id_vet = Vets.id_vet WHERE Pets.id_pet = %s;

-- updated as of step 5 draft
-- gets Vet for Vet Dropdown in Edit Pet
SELECT DISTINCT Vets.id_vet, Vets.name AS vet_name FROM Vets LEFT JOIN Pets ON Pets.id_vet = Vets.id_vet ORDER BY vet_name;

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

-- updated as of step 5 draft
-- get a single owner's data to pre-populate for the Update Owner page 
SELECT * FROM Owners WHERE id_owner = %s;

-- updated as of step 5 draft
-- gets an Owner's name for Edit Pet page
SELECT DISTINCT Owners.id_owner, Owners.name AS owner_name FROM Owners LEFT JOIN Pets ON Pets.id_owner = Owners.id_owner ORDER BY owner_name;

-- updated as of step 5 draft
-- gets the Owner assigned to the current pet we are editing in Edit Pets page
SELECT Owners.name AS owner_name FROM Pets INNER JOIN Owners ON Pets.id_owner = Owners.id_owner WHERE id_pet = %s;

-- add a new owner
INSERT INTO Owners (name, address, phone_number) VALUES (:nameInput, :addressInput, :phone_numberInput);

-- update owners
UPDATE Owners SET name = :nameInput, address = :addressInput, phone_number = :phone_numberInput
WHERE id_owner = :id_owner_selected_from_browse_owner_page;

-- delete an Owner
DELETE FROM Owners WHERE id = :owner_ID_selected_from_browse_owner_page;

-- ** Pets **

-- get all attributes for the Pets page along with their owner's name and vet's name
SELECT Pets.id_pet, Pets.name, breed, age, gender, Owners.name AS owner_name, Vets.name AS vet_name 
FROM Pets INNER JOIN Owners ON Pets.id_owner = Owners.id_owner 
LEFT JOIN Vets ON Pets.id_vet = Vets.id_vet 
ORDER BY Pets.name;

-- updated as of step 5 draft
-- get a single pet's data to pre-populate for the Update Pet page 
SELECT * FROM Pets WHERE id_pet = %s;

-- updated as of step 5 draft
-- gets Pet dropdown for Edit Prescription page
SELECT Pets.id_pet, CONCAT(Pets.name, ' (', Pets.id_pet, ')') AS pet_name_and_id, Prescriptions.order_date FROM Pets LEFT JOIN Prescriptions ON Pets.id_pet = Prescriptions.id_pet ORDER BY Pets.name, Prescriptions.order_date;

-- updated as of step 5 draft
-- display the pet part of the Prescription we're currently editing
SELECT Prescriptions.order_date, Prescriptions.prescription_cost, Prescriptions.was_picked_up, Pets.name AS pet_name FROM Prescriptions INNER JOIN Pets ON Prescriptions.id_pet = Pets.id_pet WHERE id_prescription = %s;

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

-- updated as of step 5 draft
-- gets all attributes for the Medications page
SELECT * FROM Medications ORDER BY Medications.name;

-- updated as of step 5 draft
-- get a single medications's data to pre-populate for the Update Medication page 
SELECT * FROM Medications WHERE id_medication = %s;

-- add a new Medication
INSERT INTO Medications (name, cost) VALUES (:nameInput, :costInput);

-- update Medication
UPDATE Medications 
SET name = :nameInput, cost = :costInput 
WHERE id_medication = :id_medication_selected_from_browse_med_page;

-- delete a medication
DELETE FROM Medications WHERE id = :medication_ID_selected_from_browse_medication_page;

-- ** Prescriptions **

-- updated as of step 5 draft
-- gets all attributes for the Prescriptions page
SELECT Prescriptions.id_prescription, Pets.name AS pet_name, Prescriptions.order_date, Prescriptions.prescription_cost, Prescriptions.was_picked_up FROM Prescriptions INNER JOIN Pets ON Prescriptions.id_pet = Pets.id_pet ORDER BY Prescriptions.order_date;

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

-- updated as of step 5 draft
-- get a single prescriptions's data to pre-populate for the Update Prescription page 
SELECT * FROM Prescriptions WHERE id_prescription = %s;

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

-- updated as of step 5 draft
-- gets all attributes for the PrescriptionMedications page
SELECT CONCAT(Pets.name, ' (', Prescriptions.order_date, ')') AS pet_and_prescription_order_date, Medications.name AS medication_name, quantity FROM PrescriptionMedications INNER JOIN Prescriptions ON PrescriptionMedications.id_prescription = Prescriptions.id_prescription INNER JOIN Medications ON PrescriptionMedications.id_medication = Medications.id_medication INNER JOIN Pets ON Prescriptions.id_pet = Pets.id_pet ORDER BY Prescriptions.order_date,Pets.name;

-- updated as of step 5 draft
-- gets a corresponding Pet's name, their Prescription order_date, and corresponding id_prescription for the dropdown in Add PrescriptionMedications page
ELECT Prescriptions.id_prescription AS id_prescription, CONCAT(Pets.name, ', ', Prescriptions.order_date, ' (', Prescriptions.id_prescription, ')') AS pet_order_date_prescription_ID FROM Prescriptions INNER JOIN Pets ON Prescriptions.id_pet = Pets.id_pet ORDER BY Prescriptions.order_date, Pets.name;

-- updated as of step 5 draft
-- gets a corresponding medication's name and id_medication for the dropdown in Add PrescriptionMedications page
SELECT Medications.id_medication, CONCAT(Medications.name, ' (', Medications.id_medication, ')') AS med_info FROM Medications ORDER BY Medications.name;

-- add a new entry to the PrescriptionMedications table
INSERT INTO PrescriptionMedications (id_prescription, id_medication, quantity) 
VALUES (:prescription_info_from_dropdown_Input, :medication_info_from_dropdown_Input, :quantityInput);

DELIMITER $$

CREATE TRIGGER update_prescription_cost_after_insert 
AFTER INSERT ON PrescriptionMedications
FOR EACH ROW 
BEGIN
    DECLARE total_cost DECIMAL(5,2);

    SELECT SUM(Medications.cost * PrescriptionMedications.quantity)
    INTO total_cost
    FROM PrescriptionMedications
    JOIN Medications ON PrescriptionMedications.id_medication = Medications.id_medication
    WHERE PrescriptionMedications.id_prescription = NEW.id_prescription;

    UPDATE Prescriptions
    SET prescription_cost = total_cost
    WHERE id_prescription = NEW.id_prescription;
END$$

CREATE TRIGGER update_prescription_cost_after_update 
AFTER UPDATE ON PrescriptionMedications
FOR EACH ROW 
BEGIN
    DECLARE total_cost DECIMAL(5,2);

    SELECT SUM(Medications.cost * PrescriptionMedications.quantity)
    INTO total_cost
    FROM PrescriptionMedications
    JOIN Medications ON PrescriptionMedications.id_medication = Medications.id_medication
    WHERE PrescriptionMedications.id_prescription = NEW.id_prescription;

    UPDATE Prescriptions
    SET prescription_cost = total_cost
    WHERE id_prescription = NEW.id_prescription;
END$$

DELIMITER ;