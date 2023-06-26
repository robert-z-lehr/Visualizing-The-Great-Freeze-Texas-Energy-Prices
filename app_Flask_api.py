# This is copied from Challenge 10. I am adapting it to Project 3.
# Import required modules and classes
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import datetime as dt
import numpy as np

# Create an instance of Flask
app = Flask(__name__)

# Create engine and reflect the database schema
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to the tables in the database
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session
session = Session(engine)

# Define the home route
@app.route('/')
def home():
    """List all available routes"""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )

# Define the precipitation route
@app.route('/api/v1.0/precipitation')
def precipitation():
    """Return the last 12 months of precipitation data as JSON"""
    # Calculate the date one year ago from the last date in the database
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    one_year_ago = dt.datetime.strptime(last_date[0], '%Y-%m-%d') - dt.timedelta(days=365)

    # Query precipitation data for the last 12 months
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_ago).all()

    # Convert the query results to a dictionary using date as the key and prcp as the value
    precipitation_data = {date: prcp for date, prcp in results}

    # Return the JSON representation of the dictionary
    return jsonify(precipitation_data)

# Define the stations route
@app.route('/api/v1.0/stations')
def stations():
    """Return a list of stations from the dataset"""
    # Query all stations
    results = session.query(Station.station).all()

    # Convert the query results to a list
    station_list = list(np.ravel(results))

    # Return the JSON list of stations
    return jsonify(station_list)

# Define the temperature observations route
@app.route('/api/v1.0/tobs')
def tobs():
    """Return the temperature observations for the most active station over the last 12 months"""
    # Calculate the date one year ago from the last date in the database
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    one_year_ago = dt.datetime.strptime(last_date[0], '%Y-%m-%d') - dt.timedelta(days=365)

    # Query temperature observations for the last 12 months from the most active station
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= one_year_ago).\
        filter(Measurement.station == 'USC00519281').all()

    # Convert the query results to a list of dictionaries
    tobs_list = []
    for date, tobs in results:
        tobs_dict = {'date': date, 'tobs': tobs}
        tobs_list.append(tobs_dict)

    # Return the JSON list of temperature observations
    return jsonify(tobs_list)

# Define the start route
@app.route('/api/v1.0/<start>')
def start_date(start):
    """Return the min, max, and average temperatures from a given start date to the end of the dataset"""
    # Query the min, max, and average temperatures from the start date to the end of the dataset
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).all()

    # Convert the query results to a list of dictionaries
    temperature_data = []
    for result in results:
        tmin, tavg, tmax = result
        temperature_dict = {'TMIN': tmin, 'TAVG': tavg, 'TMAX': tmax}
        temperature_data.append(temperature_dict)

    # Return the JSON list of temperature data
    return jsonify(temperature_data)


# Define the start/end route
@app.route('/api/v1.0/<start>/<end>')
def start_end_date(start, end):
    """Return the min, max, and average temperatures from a given start date to a given end date"""
    # Query the min, max, and average temperatures from the start date to the end date
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    # Convert the query results to a list of dictionaries
    temperature_data = []
    for result in results:
        tmin, tavg, tmax = result
        temperature_dict = {'TMIN': tmin, 'TAVG': tavg, 'TMAX': tmax}
        temperature_data.append(temperature_dict)

    # Return the JSON list of temperature data
    return jsonify(temperature_data)


if __name__ == '__main__':
    app.run(debug=True)