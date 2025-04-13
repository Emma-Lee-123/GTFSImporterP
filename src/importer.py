import os
import json
import pyodbc
import pandas as pd
from util import get_connection, import_file
from column_mappings import (
    calendar_dates_mapping,
    stops_mapping,
    trips_mapping,
    routes_mapping,
    shapes_mapping,
    stop_times_mapping
)

print(os.getcwd())
# Load config
with open("config.json") as f:
    config = json.load(f)

# DB connection
conn = get_connection(config)

# Path to GTFS files
gtfs_dir = "gtfs"
# Access GTFS import settings
files_to_import = config["gtfs_import"]

# Map each file to its corresponding SQL table and optional column mapping
files_to_tables = {
    "calendar_dates.txt": "CalendarDates",
    "routes.txt": "Routes",
    "stops.txt": "Stops",
    "trips.txt": "Trips",
    "stop_times.txt": "StopTimes",
    "shapes.txt": "Shapes",
}

column_mappings = {
    "calendar_dates.txt": calendar_dates_mapping,
    "routes.txt": routes_mapping,
    "stops.txt": stops_mapping,
    "trips.txt": trips_mapping,
    "stop_times.txt": stop_times_mapping,
    "shapes.txt": shapes_mapping
}

for filename, info in files_to_import.items():
    if not info["enabled"]:
        print(f"Skipping {filename}")
        continue

    file_path = os.path.join(gtfs_dir, filename)
    table_name = info["table"]

    if os.path.exists(file_path):
        print(f"Importing {filename} into {table_name}...")
        import_file(conn, file_path, table_name, column_mappings.get(filename, {}))
    else:
        print(f"File not found: {file_path}")

# # Loop through the files and import each one
# for filename, table_name in files_to_tables.items():
#     file_path = os.path.join(gtfs_dir, filename)
#     if os.path.exists(file_path):
#         print(f"Importing {filename} into {table_name}...")
#         column_mapping = column_mappings.get(filename)  
#         import_file(conn, file_path, table_name, column_mapping)
#     else:
#         print(f"File not found: {file_path}")

conn.close()
