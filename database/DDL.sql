SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;

-- Create Vets table with id_vet as the primary key
CREATE OR REPLACE TABLE Vets (
    id_vet int NOT NULL AUTO_INCREMENT,
    name VARCHAR(145) NOT NULL,
    clinic VARCHAR(145) NOT NULL,
    email VARCHAR(145) NOT NULL,
    no_of_patients INT UNSIGNED NOT NULL,
    PRIMARY KEY (id_vet));

-- Create Owners table with id_owner as the primary key
CREATE OR REPLACE TABLE Owners (
    id_owner int NOT NULL AUTO_INCREMENT,
    name VARCHAR(145) NOT NULL,
    address VARCHAR(145) NOT NULL,
    phone_number BIGINT(15) NOT NULL,
    PRIMARY KEY (id_owner));

-- Create Medications table with id_medication as the primary key
CREATE OR REPLACE TABLE Medications (
    id_medication int NOT NULL AUTO_INCREMENT,
    name VARCHAR(145) NOT NULL,
    cost DECIMAL(5, 2) NOT NULL, -- cost of the set quantity of medication
    PRIMARY KEY (id_medication));

-- Create Pets table with id_pet as the primary key, 
-- id_vet as a foreign key referencing Vets id_vet, 
-- and id_owner as a foreign key referencing Owners id_owner
CREATE OR REPLACE TABLE Pets (
    id_pet int NOT NULL AUTO_INCREMENT,
    name VARCHAR(145) NOT NULL,
    breed VARCHAR(145) NOT NULL,
    age INT NOT NULL,
    gender CHAR(1) NOT NULL,
    id_vet INT NULL,
    id_owner INT NOT NULL,
    PRIMARY KEY (id_pet),
    FOREIGN KEY(id_vet) references Vets(id_vet)
    ON DELETE CASCADE,
    FOREIGN KEY(id_owner) references Owners(id_owner)
    ON DELETE CASCADE);

-- Create Prescriptions table with id_prescription as the primary key and
-- id_pet as a foreign key referencing Pets id_pet
CREATE OR REPLACE TABLE Prescriptions (
    id_prescription int NOT NULL AUTO_INCREMENT,
    order_date DATETIME NOT NULL,
    prescription_cost DECIMAL(7, 2) DEFAULT 0.00,
    -- total cost of all medications in a given prescription
    -- default value is set to 0.00 since the cost is calculated elsewhere
    was_picked_up TINYINT(1) NOT NULL,
    id_pet INT NOT NULL,
    PRIMARY KEY (id_prescription),
    FOREIGN KEY(id_pet) references Pets(id_pet)
    ON DELETE CASCADE);

-- Create PrescriptionMedications intersection table with
--  id_prescription_medication as the primary key and
--  id_prescription and id_medication as foreign keys
CREATE OR REPLACE TABLE PrescriptionMedications (
    id_prescription_medication INT NOT NULL AUTO_INCREMENT,
    id_prescription INT NOT NULL,
    id_medication INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (id_prescription_medication),
    FOREIGN KEY (id_prescription) REFERENCES Prescriptions(id_prescription)
    ON DELETE CASCADE,
    FOREIGN KEY (id_medication) REFERENCES Medications(id_medication)
    ON DELETE CASCADE);

-- Add sample data to tables
INSERT INTO Vets (name, clinic, email, no_of_patients) VALUES
('Dr. Johnson', 'PetCare Clinic', 'johnson@petcare.com', 200),
('Dr. Smith', 'Animal Hospital', 'smith@animalhospital.com', 300),
('Dr. Brown', 'Pet Wellness Center', 'brown@petwellness.com', 150),
('Dr. Lee', 'Animal Clinic', 'dr.lee@animalclinic.com', 10),
('Dr. Chang', 'Healthy Paw Clinic', 'chang@healthypaw.com', 20); -- Illustrates an optional relationship between Vets and Pets. 
-- This vet does not have any pet clients with the pharmacy yet. Note the number of patients is for the vet clinic, not the pharmacy.

INSERT INTO Owners (name, address, phone_number) VALUES
('John Doe', '123 Main St, Anytown', 1234567890),
('Jane Doe', '456 Oak Ave, Anytown', 9876543210),
('Jack Doe', '789 Elm St, Anytown', 5555555555),
('Sarah Lee', '321 Pine Rd, Anytown', 1111111111),
('Mike Chen', '654 Cedar Ln, Anytown', 9999999999); -- Illustrates an optional relationship between Owners and Pets. 
-- This owner does not have any pets with the pharmacy yet.

INSERT INTO Medications (name, cost) VALUES
('Mirtazapine 15mg, 30 tablets', 4.50),
('Amoxicillin 250mg, 30 capsules', 4.20),
('Dorzolamide HCL Ophthalmic Solution 2%, 10mL', 20.49),
('Piroxicam 7mg, 30 capsules', 20.64),
('Furosemide 12.5mg, 30 tablets', 5.00); -- Illustrates an optional relationship between Medications and Prescriptions
-- This medication exists without a prescription.

INSERT INTO Pets (name, breed, age, gender, id_vet, id_owner) VALUES
('Fido', 'Labrador Retriever', 5, 'M', 1, 1),
('Whiskers', 'Siamese', 3, 'F', 2, 2), -- Illustrates how an owner (id_owner = 2) can have multiple pets (id_pet = 2, 4) 
('Rex', 'German Shepherd', 7, 'M', 3, 3), -- Illustrates how a vet (id_vet = 3) can have multiple patients (id_pet = 3, 4) 
('Boots', 'British Shorthair', 1, 'F', 3, 2); -- Illustrates an optional relationship between Pet and Prescription
-- This pet does not have a prescription.

INSERT INTO Prescriptions (order_date, prescription_cost, was_picked_up, id_pet) VALUES
('2023-05-06 10:00:00', 29.64,1,1), -- Illustrates 1:M (optional) relationship between Pets and Prescriptions. This pet (id_pet = 1) has multiple prescriptions.
('2023-12-14 11:00:00', 8.70,0,2),
('2024-02-01 12:00:00', 20.49,1,1);

INSERT INTO PrescriptionMedications (id_prescription, id_medication, quantity) VALUES
(1,1,2), -- M:M relationship between Medications and Prescriptions:
(2,2,1),
(2,1,1), -- Illustrates a medication (id_medication = 1) can be in multiple prescriptions (id_prescription = 1, 2)
(3,3,1),
(1,4,1); -- Illustrates a prescription (id_prescription = 1) has multiple medications (id_medication = 1, 4)

SELECT * FROM PrescriptionMedications;
SELECT * FROM Prescriptions;
SELECT * FROM Pets;
SELECT * FROM Medications;
SELECT * FROM Owners;
SELECT * FROM Vets;
SET FOREIGN_KEY_CHECKS=1;
COMMIT;