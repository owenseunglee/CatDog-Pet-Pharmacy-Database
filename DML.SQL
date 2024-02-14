-- gets all attributes for the Vets page
SELECT * FROM Vets

-- gets all attributes for the Owners page
SELECT * FROM Owners

-- get all pet and their owner's name
SELECT Pets.id_pet, name, breed, age, gender, Owners.name AS owner_name
FROM Pets
INNER JOIN Owners ON Pets.id_owner = Owners.id_owner;

-- get a single pet's data
SELECT id_pet, name, breed, age, gender, id_vet, id_owner
FROM Pets
WHERE id_pet = :pet_ID_selected_from_browse_pet_page

-- get all pets with their current associated vets
SELECT id_pet, id_vet, Pets.name AS pet_name, Vets.name AS vet_name
FROM Pets
INNER JOIN Vets ON Pets.id_vet = Vets.id_vet
ORDER BY pet_name, vet_name;

-- add a new pet. list of vets and owners will be displayed in dropdown 
INSERT INTO Pets (name, breed, age, gender, id_vet, id_owner)
VALUES (:nameInput, :breedInput, :ageInput, :genderInput, :vet_id_from_dropdown_Input, :owner_id_from_dropdown_Input)

-- update pets, list of pets will be displayed in dropdown 
UPDATE Pets SET name = :nameInput, breed = :breedInput, age = :ageInput, gender = :genderInput, id_vet = :vet_id_from_dropdown_Input, id_owner = :owner_id_from_dropdown_Input
WHERE id_pet = :pet_ID_selected_from_browse_pet_page

-- delete a pet
DELETE FROM Pets WHERE id = :character_ID_selected_from_browse_pet_page

-- dis-associate a prescription from a medication (M-to-M relationship deletion)
DELETE FROM PrescriptionMedications WHERE id_prescription = :prescriptionIdInput AND id_medication = :medicationIdInput
