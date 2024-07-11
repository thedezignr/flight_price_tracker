from serpapi import GoogleSearch
import pandas as pd
from pandas import json_normalize
from dotenv import load_dotenv
import os

# Loading the API-key
load_dotenv()

API_KEY = os.getenv("API_KEY")

# ------------------

# Nigeria to Uk
def flight_tracker_uk():

  # API parameter
  params_uk = {
    "api_key": API_KEY,
    "engine": "google_flights",
    "hl": "en",
    "gl": "uk",
    "departure_id": "ABV, LOS",
    "arrival_id": "LHR, LGW",
    "outbound_date": "2024-07-11",
    "currency": "USD",
    "type": "2"
  }

  # Where data extration happens
  search_uk = GoogleSearch(params_uk)
  results_uk = search_uk.get_dict()

  # Normalize flight details
  best_flights = results_uk["best_flights"]
  other_flights = results_uk["other_flights"]

  # Flatten best_flight details
  best_flights_data = json_normalize(
      [flight for best_flight in best_flights for flight in best_flight["flights"]],
      sep='_'
  )

  # Flatten other_flight details
  other_flights_data = json_normalize(
      [flight for best_flight in best_flights for flight in best_flight["flights"]],
      sep='_'
  )

  print(best_flights_data, other_flights_data)

# Call the function
flight_tracker_uk()

# ------------------

# Nigeria to Canada
def flight_tracker_ca():
  
  # API parameter
  params_ca = {
    "api_key": API_KEY,
    "engine": "google_flights",
    "hl": "en",
    "gl": "ca",
    "departure_id": "ABV, LOS",
    "arrival_id": "YYZ, YUL",
    "outbound_date": "2024-07-10",
    "currency": "USD",
    "type": "2"
  }

  # Where data extration happens
  search_ca = GoogleSearch(params_ca)
  results_ca = search_ca.get_dict()

  # Normalize flight details
  best_flights = results_ca["best_flights"]
  other_flights = results_ca["other_flights"]

  # Flatten best_flight details
  best_flights_data = json_normalize(
      [flight for best_flight in best_flights for flight in best_flight["flights"]],
      sep='_'
  )

  # Flatten other_flight details
  other_flights_data = json_normalize(
      [flight for best_flight in best_flights for flight in best_flight["flights"]],
      sep='_'
  )

  print(best_flights_data, other_flights_data)

flight_tracker_ca()

# ------------------

# Nigeria to USA

def flight_tracker_us():
  
  # API parameter
  params_us = {
    "api_key": API_KEY,
    "engine": "google_flights",
    "hl": "en",
    "gl": "us",
    "departure_id": "ABV, LOS",
    "arrival_id": "JFK, SFO",
    "outbound_date": "2024-07-10",
    "currency": "USD",
    "type": "2"
  }

  # Where data extration happens
  search_us = GoogleSearch(params_us)
  results_us = search_us.get_dict()

  # Normalize flight details
  best_flights = results_us["best_flights"]
  other_flights = results_us["other_flights"]

  # Flatten best_flight details
  best_flights_data = json_normalize(
      [flight for best_flight in best_flights for flight in best_flight["flights"]],
      sep='_'
  )

  # Flatten other_flight details
  other_flights_data = json_normalize(
      [flight for best_flight in best_flights for flight in best_flight["flights"]],
      sep='_'
  )

  print(best_flights_data, other_flights_data)

flight_tracker_us()