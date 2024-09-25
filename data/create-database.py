import sqlite3
import csv
import os

def infer_data_type(value):
    """Infers the SQLite data type of a value."""
    try:
        int(value)
        return "INTEGER"
    except ValueError:
        try:
            float(value)
            return "REAL"
        except ValueError:
            if value.upper() in ["TRUE", "FALSE"]:
                return "BOOLEAN"
            else:
                return "TEXT"

def create_database(folder_path, db_name):
    """Creates an SQLite3 database from CSV files in a given folder.

    Args:
        folder_path (str): The path to the folder containing the CSV files.
        db_name (str): The desired name for the SQLite3 database.
    """
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        for csv_file in os.listdir(folder_path):
            if csv_file.endswith('.csv'):
                table_name = csv_file[:-4]  # Remove '.csv' extension
                with open(os.path.join(folder_path, csv_file), 'r') as f:
                    reader = csv.reader(f)
                    headers = next(reader)  # I wrote coz first row contains headers
                    first_row = next(reader)  # Read the first row of data to infer types
                    column_types = [infer_data_type(value) for value in first_row]
                    columns_with_types = [f'"{header}" {col_type}' for header, col_type in zip(headers, column_types)]
                    
                    cursor.execute(f'CREATE TABLE "{table_name}" ({", ".join(columns_with_types)})')
                    
                    cursor.execute(f'INSERT INTO "{table_name}" VALUES ({", ".join(["?" for _ in headers])})', first_row)
                    
                    for row in reader:
                        cursor.execute(f'INSERT INTO "{table_name}" VALUES ({", ".join(["?" for _ in headers])})', row)

        conn.commit()
        conn.close()
        print(f"Database '{db_name}' created successfully.")
    except Exception as e:
        print(f"Error creating database: {e}")

# Paths to your CSV files
general_csv_folder = 'data/CSV_files/general'
results_csv_folder = 'data/CSV_files/results'

# Createc 'general.db' database
create_database(general_csv_folder, 'data/general.db')

# Created 'results.db' database
create_database(results_csv_folder, 'data/results.db')