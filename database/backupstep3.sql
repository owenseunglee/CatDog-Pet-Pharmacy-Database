-- MariaDB dump 10.19  Distrib 10.5.22-MariaDB, for Linux (x86_64)
--
-- ------------------------------------------------------
-- Server version	10.6.16-MariaDB-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Medications`
--

DROP TABLE IF EXISTS `Medications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Medications` (
  `id_medication` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(145) NOT NULL,
  `cost` decimal(5,2) NOT NULL,
  PRIMARY KEY (`id_medication`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Medications`
--

LOCK TABLES `Medications` WRITE;
/*!40000 ALTER TABLE `Medications` DISABLE KEYS */;
INSERT INTO `Medications` VALUES (1,'Mirtazapine 15mg, 30 tablets',4.50),(2,'Amoxicillin 250mg, 30 capsules',4.20),(3,'Dorzolamide HCL Ophthalmic Solution 2%, 10mL',20.49),(4,'Piroxicam 7mg, 30 capsules',20.64),(5,'Furosemide 12.5mg, 30 tablets',5.00);
/*!40000 ALTER TABLE `Medications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Owners`
--

DROP TABLE IF EXISTS `Owners`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Owners` (
  `id_owner` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(145) NOT NULL,
  `address` varchar(145) NOT NULL,
  `phone_number` bigint(15) NOT NULL,
  PRIMARY KEY (`id_owner`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Owners`
--

LOCK TABLES `Owners` WRITE;
/*!40000 ALTER TABLE `Owners` DISABLE KEYS */;
INSERT INTO `Owners` VALUES (1,'John Doe','123 Main St, Anytown',1234567890),(2,'Jane Doe','456 Oak Ave, Anytown',9876543210),(3,'Jack Doe','789 Elm St, Anytown',5555555555),(4,'Sarah Lee','321 Pine Rd, Anytown',1111111111),(5,'Mike Chen','654 Cedar Ln, Anytown',9999999999);
/*!40000 ALTER TABLE `Owners` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Pets`
--

DROP TABLE IF EXISTS `Pets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Pets` (
  `id_pet` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(145) NOT NULL,
  `breed` varchar(145) NOT NULL,
  `age` int(11) NOT NULL,
  `gender` char(1) NOT NULL,
  `id_vet` int(11) DEFAULT NULL,
  `id_owner` int(11) NOT NULL,
  PRIMARY KEY (`id_pet`),
  KEY `id_vet` (`id_vet`),
  KEY `id_owner` (`id_owner`),
  CONSTRAINT `Pets_ibfk_1` FOREIGN KEY (`id_vet`) REFERENCES `Vets` (`id_vet`) ON DELETE CASCADE,
  CONSTRAINT `Pets_ibfk_2` FOREIGN KEY (`id_owner`) REFERENCES `Owners` (`id_owner`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pets`
--

LOCK TABLES `Pets` WRITE;
/*!40000 ALTER TABLE `Pets` DISABLE KEYS */;
INSERT INTO `Pets` VALUES (1,'Fido','Labrador Retriever',5,'M',1,1),(2,'Whiskers','Siamese',3,'F',2,2),(3,'Rex','German Shepherd',7,'M',3,3),(4,'Boots','British Shorthair',1,'F',3,2);
/*!40000 ALTER TABLE `Pets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PrescriptionMedications`
--

DROP TABLE IF EXISTS `PrescriptionMedications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PrescriptionMedications` (
  `id_prescription_medication` int(11) NOT NULL AUTO_INCREMENT,
  `id_prescription` int(11) NOT NULL,
  `id_medication` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  PRIMARY KEY (`id_prescription_medication`),
  KEY `id_prescription` (`id_prescription`),
  KEY `id_medication` (`id_medication`),
  CONSTRAINT `PrescriptionMedications_ibfk_1` FOREIGN KEY (`id_prescription`) REFERENCES `Prescriptions` (`id_prescription`) ON DELETE CASCADE,
  CONSTRAINT `PrescriptionMedications_ibfk_2` FOREIGN KEY (`id_medication`) REFERENCES `Medications` (`id_medication`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PrescriptionMedications`
--

LOCK TABLES `PrescriptionMedications` WRITE;
/*!40000 ALTER TABLE `PrescriptionMedications` DISABLE KEYS */;
INSERT INTO `PrescriptionMedications` VALUES (1,1,1,2),(2,2,2,1),(3,2,1,1),(4,3,3,1),(5,1,4,1);
/*!40000 ALTER TABLE `PrescriptionMedications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Prescriptions`
--

DROP TABLE IF EXISTS `Prescriptions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Prescriptions` (
  `id_prescription` int(11) NOT NULL AUTO_INCREMENT,
  `order_date` datetime NOT NULL,
  `prescription_cost` decimal(5,2) NOT NULL,
  `was_picked_up` tinyint(1) NOT NULL,
  `id_pet` int(11) NOT NULL,
  PRIMARY KEY (`id_prescription`),
  KEY `id_pet` (`id_pet`),
  CONSTRAINT `Prescriptions_ibfk_1` FOREIGN KEY (`id_pet`) REFERENCES `Pets` (`id_pet`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Prescriptions`
--

LOCK TABLES `Prescriptions` WRITE;
/*!40000 ALTER TABLE `Prescriptions` DISABLE KEYS */;
INSERT INTO `Prescriptions` VALUES (1,'2023-05-06 10:00:00',29.64,1,1),(2,'2023-12-14 11:00:00',8.70,0,2),(3,'2024-02-01 12:00:00',20.49,1,1);
/*!40000 ALTER TABLE `Prescriptions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Vets`
--

DROP TABLE IF EXISTS `Vets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Vets` (
  `id_vet` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(145) NOT NULL,
  `clinic` varchar(145) NOT NULL,
  `email` varchar(145) NOT NULL,
  `no_of_patients` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id_vet`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Vets`
--

LOCK TABLES `Vets` WRITE;
/*!40000 ALTER TABLE `Vets` DISABLE KEYS */;
INSERT INTO `Vets` VALUES (1,'Dr. Johnson','PetCare Clinic','johnson@petcare.com',200),(2,'Dr. Smith','Animal Hospital','smith@animalhospital.com',300),(3,'Dr. Brown','Pet Wellness Center','brown@petwellness.com',150),(4,'Dr. Lee','Animal Clinic','dr.lee@animalclinic.com',10),(5,'Dr. Chang','Healthy Paw Clinic','chang@healthypaw.com',20);
/*!40000 ALTER TABLE `Vets` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-19 11:08:24
