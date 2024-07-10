from serpapi import GoogleSearch
import pandas as pd
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
    "outbound_date": "2024-07-10",
    "currency": "USD",
    "type": "2"
  }

  # Where data extration happens
  search_uk = GoogleSearch(params_uk)
  results_uk = search_uk.get_dict()

  # Converts results to dataframe
  df_results_uk_best = pd.DataFrame.from_dict(results_uk["best_flights"])
  df_results_uk_other = pd.DataFrame.from_dict(results_uk["other_flights"])
  # Prints results
  print(df_results_uk_best, df_results_uk_other)

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

  df_results_ca_best = pd.DataFrame.from_dict(results_ca["best_flights"])
  df_results_ca_other = pd.DataFrame.from_dict(results_ca["other_flights"])
  print(df_results_ca_best, df_results_ca_other)

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

  df_results_us_best = pd.DataFrame.from_dict(results_us["best_flights"])
  df_results_us_other = pd.DataFrame.from_dict(results_us["other_flights"])
  print(df_results_us_best)

flight_tracker_us()