# Import required modules and classes
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session



# Create engine and reflect the database schema
engine = create_engine('postgresql://postgres:postgres@localhost:5432/project_3_db')
Base = automap_base()
Base.prepare(autoload_with=engine)

# Save references to the tables in the database
Generators = Base.classes.generators
States = Base.classes.states
Status = Base.classes.stat_descr
Energy_Sources = Base.classes.energy_sources
Sectors = Base.classes.sectors
Entities = Base.classes.entities
Plants = Base.classes.plants
Prices = Base.classes.prices
Series = Base.classes.ser_descr
Processes = Base.classes.processes
Consumption_and_CO2 = Base.classes.consumption_and_co2
Generation_and_Consumption = Base.classes.generation_and_consumption

# Create a session
session = Session(engine)

# Create an instance of Flask
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    """List all available routes"""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/generators<br/>"
        f"/api/v1.0/states<br/>"
        f"/api/v1.0/energy_sources<br/>"
        f"/api/v1.0/stat_descr<br/>"
        f"/api/v1.0/sectors<br/>"
        f"/api/v1.0/entities<br/>"
        f"/api/v1.0/plants<br/>"
        f"/api/v1.0/prices<br/>"
        f"/api/v1.0/series<br/>"
        f"/api/v1.0/processes<br/>"
        f"/api/v1.0/consumption_and_co2<br/>"
        f"/api/v1.0/generation_and_consumption<br/>"
    )
    
####################################################################################
####################################################################################

# Define the generators route
@app.route('/api/v1.0/generators')
def get_generators():
    """Return the generator data"""
    results = session.query(Generators).all()

    # Create a list of dictionaries containing generator data
    generator_data = []
    for result in results:
        generator_dict = {
            'id': result.id,
            'period': result.period,
            'stateID': result.stateid,
            'sector': result.sector,
            'entityid': result.entityid,
            'plantid': result.plantid,
            'generatorid': result.generatorid,
            'technology': result.technology,
            'energy_source_code': result.energy_source_code,
            'prime_mover_code': result.prime_mover_code,
            'status': result.status_descr,
            'latitude': result.latitude,
            'longitude': result.longitude
        }
        generator_data.append(generator_dict)

    # Return the JSON list of generator data
    return jsonify(generator_data)

####################################################################################
####################################################################################

# Define the states route
@app.route('/api/v1.0/states')
def get_states():
    """Return the states data"""
    results = session.query(States).all()

    # Create a list of dictionaries containing states data
    states_data = []
    for result in results:
        state_dict = {
            'stateID': result.stateid,
            'state_description': result.state_description
        }
        states_data.append(state_dict)

    # Return the JSON list of states data
    return jsonify(states_data)

####################################################################################
####################################################################################

# Define the energy sources route
@app.route('/api/v1.0/energy_sources')
def get_energy():
    """Return the energy sources data"""
    results = session.query(Energy_Sources).all()

    # Create a list of dictionaries containing energy source data
    energy_data = []
    for result in results:
        energy_dict = {
            'energyID': result.energy_source_id,
            'energy_source_description': result.energy_source_description
        }
        energy_data.append(energy_dict)

    # Return the JSON list of energy source data
    return jsonify(energy_data)

####################################################################################
####################################################################################

# Define the status route
@app.route('/api/v1.0/stat_descr')
def get_status():
    """Return the status data"""
    results = session.query(Status).all()

    # Create a list of dictionaries containing status data
    status_data = []
    for result in results:
        status_dict = {
            'status': result.stat_id,
            'status_description': result.statusdescription
        }
        status_data.append(status_dict)

    # Return the JSON list of status data
    return jsonify(status_data)

####################################################################################
####################################################################################

# Define the sectors route
@app.route('/api/v1.0/sectors')
def get_sectors():
    """Return the sectors data"""
    results = session.query(Sectors).all()

    # Create a list of dictionaries containing sector data
    sector_data = []
    for result in results:
        sector_dict = {
            'sector': result.sector,
            'sector_description': result.sectorname
        }
        sector_data.append(sector_dict)

    # Return the JSON list of sector data
    return jsonify(sector_data)

####################################################################################
####################################################################################

# Define the entities route
@app.route('/api/v1.0/entities')
def get_entities():
    """Return the entity data"""
    results = session.query(Entities).all()

    # Create a list of dictionaries containing entity data
    entity_data = []
    for result in results:
        entity_dict = {
            'entityID': result.entityid,
            'entity_name': result.entityname
        }
        entity_data.append(entity_dict)

    # Return the JSON list of entity data
    return jsonify(entity_data)

####################################################################################
####################################################################################

# Define the plants route
@app.route('/api/v1.0/plants')
def get_plants():
    """Return the plants data"""
    results = session.query(Plants).all()

    # Create a list of dictionaries containing plants data
    plant_data = []
    for result in results:
        plant_dict = {
            'plantID': result.plantid,
            'plant_name': result.plantname
        }
        plant_data.append(plant_dict)

    # Return the JSON list of plant data
    return jsonify(plant_data)
    
####################################################################################
####################################################################################

# Define the prices route
@app.route('/api/v1.0/prices')
def get_prices():
    """Return the price data"""
    results = session.query(Prices).all()

    # Create a list of dictionaries containing price data
    price_data = []
    for result in results:
        price_dict = {
            'id': result.id,
            'period': result.period,
            'area_name': result.area_name,
            'product_name': result.product_name,
            'process_name': result.process_name,
            'seriesID': result.series,
            'value': result.value,
            'units': result.units
        }
        price_data.append(price_dict)

    # Return the JSON list of price data
    return jsonify(price_data)

####################################################################################
####################################################################################

# Define the series route
@app.route('/api/v1.0/series')
def get_series():
    """Return the series data"""
    results = session.query(Series).all()

    # Create a list of dictionaries containing series data
    series_data = []
    for result in results:
        series_dict = {
            'seriesID': result.ser_id,
            'series_description': result.ser_description
        }
        series_data.append(series_dict)

    # Return the JSON list of series data
    return jsonify(series_data)

####################################################################################
####################################################################################

# Define the processes route
@app.route('/api/v1.0/processes')
def get_processes():
    """Return the processes data"""
    results = session.query(Processes).all()

    # Create a list of dictionaries containing processes data
    process_data = []
    for result in results:
        process_dict = {
            'processID': result.process_id,
            'process_name': result.process_name
        }
        process_data.append(process_dict)

    # Return the JSON list of process data
    return jsonify(process_data)

####################################################################################
####################################################################################

# Define the consumption and CO2 route
@app.route('/api/v1.0/consumption_and_co2')
def get_consumption():
    """Return the consumption and CO2 data"""
    results = session.query(Consumption_and_CO2).all()

    # Create a list of dictionaries containing consumption and CO2 data
    cons_data = []
    for result in results:
        cons_dict = {
            'id': result.id,
            'period': result.period,
            'msn/seriesID': result.msn,
            'value': result.value,
            'unit': result.unit
        }
        cons_data.append(cons_dict)

    # Return the JSON list of consumption and CO2 data
    return jsonify(cons_data)

####################################################################################
####################################################################################

# Define the generation and consumption route
@app.route('/api/v1.0/generation_and_consumption')
def get_generation():
    """Return the states data"""
    results = session.query(Generation_and_Consumption).all()

    # Create a list of dictionaries containing generation and consumption data
    gen_data = []
    for result in results:
        gen_dict = {
            'id': result.id,
            'period': result.period,
            'seriesID': result.seriesid,
            'value': result.value,
            'unit': result.unit
        }
        gen_data.append(gen_dict)

    # Return the JSON list of states data
    return jsonify(gen_data)

####################################################################################
####################################################################################

if __name__ == '__main__':
    app.run(debug=True)
    
####################################################################################
################################ THE END! ##########################################
####################################################################################
    