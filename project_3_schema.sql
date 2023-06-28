DROP TABLE IF EXISTS Energy_Sources, States, Sectors, Entities, Plants, 
Stat_descr, Generators, Prices, Processes, Series, Consumption_and_CO2, Generation_and_consumption CASCADE;

-- Create Energy Sources table
CREATE TABLE Energy_Sources (
    energy_source_id VARCHAR(6) PRIMARY KEY NOT NULL,
    energy_source_description VARCHAR(50) NOT NULL
);

-- Create States table
CREATE TABLE States (
    stateID VARCHAR(2) PRIMARY KEY NOT NULL,
    state_description VARCHAR(30) NOT NULL
);


-- Create Sectors table
CREATE TABLE Sectors (
    sector VARCHAR(25) PRIMARY KEY NOT NULL,
    sectorName VARCHAR(25) NOT NULL
);

-- Create Entities table
CREATE TABLE Entities (
    entityid INTEGER PRIMARY KEY NOT NULL,
    entityName VARCHAR(50)
);

-- Create Plants table
CREATE TABLE Plants (
    plantid INTEGER PRIMARY KEY NOT NULL,
    plantName VARCHAR(50) NOT NULL
);

-- Create Status_List table
CREATE TABLE Stat_Descr (
    stat_id VARCHAR(2) PRIMARY KEY NOT NULL,
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
	balancing_authority_code VARCHAR,
	balancing_authority_name VARCHAR,
    status_descr VARCHAR(2) NOT NULL,
    latitude FLOAT(53) NOT NULL,
    longitude FLOAT(53) NOT NULL,
	FOREIGN KEY (stateID) REFERENCES States(stateID),
	FOREIGN KEY (entityid) REFERENCES Entities(entityid),
	FOREIGN KEY (plantid) REFERENCES Plants(plantid),
	FOREIGN KEY (sector) REFERENCES Sectors(sector),
	FOREIGN KEY (status_descr) REFERENCES Stat_Descr(stat_id),
	FOREIGN KEY (energy_source_code) REFERENCES Energy_Sources(energy_source_id)
);

-- Create Series table
CREATE TABLE Series (
    series VARCHAR(15) PRIMARY KEY NOT NULL,
    series_description VARCHAR(100) NOT NULL
);

-- Create Processes table
CREATE TABLE Processes (
    process_id VARCHAR(3) PRIMARY KEY NOT NULL,
    process_name VARCHAR(50) NOT NULL
);

-- Create Prices table
CREATE TABLE Prices (
	id INTEGER PRIMARY KEY NOT NULL, 
	period VARCHAR(7) NOT NULL,
	area_name VARCHAR(10) NOT NULL,
	product_name VARCHAR(20) NOT NULL,
	process_name VARCHAR(60) NOT NULL,
	series VARCHAR(10) NOT NULL,
	value FLOAT(53) NOT NULL,
	units VARCHAR(5) NOT NULL,
	FOREIGN KEY (series) REFERENCES Series(series),
	FOREIGN KEY (process_name) REFERENCES Processes(process_id),
	FOREIGN KEY (area_name) REFERENCES States(stateID)
);

-- Create Consumption and C02 table
CREATE TABLE Consumption_and_CO2 (
	id INTEGER PRIMARY KEY NOT NULL,
	period VARCHAR(7) NOT NULL,
	msn VARCHAR(7) NOT NULL,
	value FLOAT(53) NOT NULL,
	unit VARCHAR(40) NOT NULL,
	FOREIGN KEY (msn) REFERENCES Series(series)
);

-- Create Generation and Consumption table
CREATE TABLE Generation_and_consumption (
	id INTEGER PRIMARY KEY NOT NULL,
	period VARCHAR(7) NOT NULL,
	seriesid VARCHAR(10) NOT NULL,
	value FLOAT(53) NOT NULL,
	unit VARCHAR(25) NOT NULL,
	FOREIGN KEY (seriesid) REFERENCES Series(series)
);

-- Confirm tables are populated correctly
SELECT * FROM Energy_Sources;
SELECT * FROM States;
SELECT * FROM Generators;
SELECT * FROM Sectors;
SELECT * FROM Entities;
SELECT * FROM Plants;
SELECT * FROM Stat_Descr;
SELECT * FROM Prices;
SELECT * FROM Processes;
SELECT * FROM Series;
SELECT * FROM Consumption_and_CO2;
SELECT * FROM Generation_and_consumption;

-- CSV files imported into tables using Import/Export menu option
