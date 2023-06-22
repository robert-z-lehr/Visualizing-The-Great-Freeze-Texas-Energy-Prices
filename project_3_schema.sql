DROP TABLE IF EXISTS Producer_Types, Energy_Sources, States, Generating_Capacity, Sectors, Entities, Plants, Status, Generators CASCADE;
DROP TABLE IF EXISTS Generators;

-- Create Producer Types table
CREATE TABLE Producer_Types (
    producer_type_id VARCHAR(3) PRIMARY KEY NOT NULL,
    producer_type_description VARCHAR(30) NOT NULL
);

-- Create Energy Sources table
CREATE TABLE Energy_Sources (
    energy_source_id VARCHAR(6) PRIMARY KEY NOT NULL,
    energy_source_description VARCHAR(30) NOT NULL
);

-- Create States table
CREATE TABLE States (
    stateID VARCHAR(2) PRIMARY KEY NOT NULL,
    state_description VARCHAR(30) NOT NULL
);

-- Create Generating Capacity table
CREATE TABLE Generating_Capacity (
    id INTEGER PRIMARY KEY NOT NULL,
	period INTEGER NOT NULL,
    stateID VARCHAR(2) NOT NULL,
    producer_type_id VARCHAR(3) NOT NULL,
    energy_source_id VARCHAR(6) NOT NULL,
    capability FLOAT(53) NOT NULL,
    capability_units VARCHAR(15) NOT NULL,
	FOREIGN KEY (stateID) REFERENCES States(stateID),
	FOREIGN KEY (producer_type_id) REFERENCES Producer_Types(producer_type_id),
	FOREIGN KEY (energy_source_id) REFERENCES Energy_Sources(energy_source_id)
);

-- Create Sectors table
CREATE TABLE Sectors (
    sector VARCHAR(25) PRIMARY KEY NOT NULL,
    sectorName VARCHAR(25) NOT NULL
);

-- Create Entities table
CREATE TABLE Entities (
    entityid INTEGER PRIMARY KEY NOT NULL,
    entityName VARCHAR(50) NOT NULL
);

-- Create Plants table
CREATE TABLE Plants (
    plantid INTEGER PRIMARY KEY NOT NULL,
    plantName VARCHAR(50) NOT NULL
);

-- Create Status table
CREATE TABLE Status (
    status VARCHAR(2) PRIMARY KEY NOT NULL,
    statusDescription VARCHAR(100) NOT NULL
);

-- Create Generators table
CREATE TABLE Generators (
    id INTEGER PRIMARY KEY NOT NULL,
    period VARCHAR NOT NULL,
    stateID VARCHAR(2) NOT NULL,
    sector VARCHAR(25) NOT NULL,
    entityid INTEGER NOT NULL,
    plantid INTEGER NOT NULL,
    generatorid VARCHAR(6) NOT NULL,
    technology VARCHAR NOT NULL,
    energy_source_code VARCHAR NOT NULL,
    prime_mover_code VARCHAR NOT NULL,
    status VARCHAR(2) NOT NULL,
    latitude FLOAT(53) NOT NULL,
    longitude FLOAT(53) NOT NULL,
	FOREIGN KEY (stateID) REFERENCES States(stateID),
	FOREIGN KEY (entityid) REFERENCES Entities(entityid),
	FOREIGN KEY (plantid) REFERENCES Plants(plantid),
	FOREIGN KEY (sector) REFERENCES Sectors(sector),
	FOREIGN KEY (status) REFERENCES Status(status)
);

-- Confirm tables are populated correctly
SELECT * FROM Producer_Types;
SELECT * FROM Energy_Sources;
SELECT * FROM States;
SELECT * FROM Generating_Capacity;
SELECT * FROM Generators;
SELECT * FROM Sectors;
SELECT * FROM Entities;
SELECT * FROM Plants;
SELECT * FROM Status;

-- CSV files imported into tables using Import/Export menu option
