import pyodbc
import pandas as pd
import numpy as np

# Function to convert numpy types to Python types
def convert_row(row):
    return [int(x) if isinstance(x, np.int64) else x for x in row]

def get_connection(config):
    db = config["db"]
    conn_str = (
        f"DRIVER={{{db['driver']}}};"
        f"SERVER={db['server']};"
        f"DATABASE={db['database']};"
        f"UID={db['username']};"
        f"PWD={db['password']};"
    )
    return pyodbc.connect(conn_str)

def import_file(conn, file_path, table_name, mapping):

    df = pd.read_csv(file_path, encoding='utf-8-sig')

    # Strip whitespace from column names just in case
    df.columns = df.columns.str.strip()
    # Print original columns for debugging
    print(f"Original Columns ({file_path}):", df.columns.tolist())

    # Rename columns using the provided mapping
    df.rename(columns=mapping, inplace=True)

    # Print renamed columns for debugging
    print(f"Renamed Columns ({file_path}):", df.columns.tolist())
    
    cursor = conn.cursor()

    # Optional: Confirm before clearing data
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    if count > 0:
        confirm = input(f"{table_name} has {count} rows. Delete before import? (y/n): ")
        if confirm.lower() == "y":
            cursor.execute(f"DELETE FROM {table_name}")
            conn.commit()
            print(f"Deleted {count} rows from {table_name}")
        else:
            print("Skipping delete.")

    # Assuming each table has the same column order, you can dynamically create the SQL statement.
    columns = ", ".join(mapping.values())
    placeholders = ", ".join("?" * len(mapping))
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    
    # rows = df[list(mapping.keys())].values.tolist()
    # Ensure only mapped source columns are selected
    df_for_insert = df[list(mapping.values())]

    # Handle conversion of data types like numpy.int64
    rows = df_for_insert.astype(str).values.tolist()
    cursor.executemany(sql, rows)
    conn.commit()
    cursor.close()
    print(f"Imported {len(rows)} rows into {table_name}")