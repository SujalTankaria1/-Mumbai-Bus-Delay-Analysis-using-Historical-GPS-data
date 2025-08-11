import pandas as pd
from datetime import datetime
from geopy.distance import geodesic

# Load Datasets 
df=pd.read_csv("mumbai_bus_gps.csv")

# Preview first few rows
print(df.head())

# Check for missing values 
print(df.isnull().sum())

# Drop rows with missing important values (if any)
df = df.dropna(subset=["vehicle_id", "scheduled_arrival", "actual_arrival", "latitude", "longitude"])

# Reset index after drop
df.reset_index(drop=True, inplace=True)

# Convert date and time columns to datetime
df['scheduled_arrival_dt'] = pd.to_datetime(df['date'] + ' ' + df['scheduled_arrival'])
df['actual_arrival_dt'] = pd.to_datetime(df['date'] + ' ' + df['actual_arrival'])

# Preview
print(df[['scheduled_arrival_dt', 'actual_arrival_dt']].head())

# Example: calculate distance between current point and predefined stop
bus_point = (19.0184, 72.8446)  # Dadar
stop_point = (19.0602, 72.8361)  # Bandra

distance = geodesic(bus_point, stop_point).meters
print(f"Distance = {distance:.2f} meters")

# Ensure delay is consistent with datetime
df['delay_calculated'] = (df['actual_arrival_dt'] - df['scheduled_arrival_dt']).dt.total_seconds() / 60

# Compare with existing
df[['delay_in_minutes', 'delay_calculated']].head()



