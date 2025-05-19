# 🔍 Problem:
# You are analyzing service coverage for emergency medical units in a city. Given a list of hospitals and recent accident locations, determine which hospitals are within a 10 km radius of each accident and visualize the results.

# Concepts Covered:
# Haversine formula (great-circle distance)
# Geospatial filtering using distances
# Pandas/GeoPandas for data handling
# Matplotlib for map visualization

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import radians, sin, cos, sqrt, atan2

# Haversine Function
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c  # Distance in km

# Load Data
hospitals = pd.read_csv("hospitals.csv")
accidents = pd.read_csv("accidents.csv")

# Distance Analysis
results = []
for _, acc in accidents.iterrows():
    acc_lat, acc_lon = acc['latitude'], acc['longitude']
    for _, hosp in hospitals.iterrows():
        hosp_lat, hosp_lon = hosp['latitude'], hosp['longitude']
        dist = haversine(acc_lat, acc_lon, hosp_lat, hosp_lon)
        if dist <= 10:
            results.append({
                'accident_id': acc['accident_id'],
                'hospital_id': hosp['hospital_id'],
                'hospital_name': hosp['name'],
                'distance_km': round(dist, 2)
            })

# Convert to DataFrame
coverage_df = pd.DataFrame(results)
print(coverage_df)

# --- Visualization ---
fig, ax = plt.subplots(figsize=(8, 6))

# Plot hospitals
plt.scatter(hospitals['longitude'], hospitals['latitude'], color='red', label='Hospitals', s=100)

# Plot accidents
plt.scatter(accidents['longitude'], accidents['latitude'], color='blue', label='Accidents', s=100)

# Annotate
for i, row in hospitals.iterrows():
    ax.annotate(row['name'], (row['longitude'] + 0.002, row['latitude']), fontsize=9)

for i, row in accidents.iterrows():
    ax.annotate(f"Acc-{row['accident_id']}", (row['longitude'] + 0.002, row['latitude'] - 0.002), fontsize=9)

# Draw lines for coverage
for _, row in coverage_df.iterrows():
    acc = accidents[accidents['accident_id'] == row['accident_id']].iloc[0]
    hosp = hospitals[hospitals['hospital_id'] == row['hospital_id']].iloc[0]
    plt.plot([acc['longitude'], hosp['longitude']],
             [acc['latitude'], hosp['latitude']], 'k--', alpha=0.5)

plt.title("Hospital Coverage within 10 km of Accidents")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
