import pandas as pd
import mysql.connector
from mysql.connector import Error
import os

def map_data_type(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return "INT"
    elif pd.api.types.is_float_dtype(dtype):
        return "DOUBLE"
    elif pd.api.types.is_bool_dtype(dtype):
        return "BOOLEAN"
    elif pd.api.types.is_string_dtype(dtype):
        return "VARCHAR(255)"
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return "DATETIME"
    else:
        return "VARCHAR(255)"

def csv_to_mysql(csv_file, host, database, user, password):
    try:
        # Read CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file)

        # Get table name from the CSV file name (excluding extension)
        table_name = os.path.splitext(os.path.basename(csv_file))[0]

        # Connect to MySQL
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Determine data types for each column
            column_data_types = {col: map_data_type(dtype) for col, dtype in df.dtypes.items()}

            # Create the table if it doesn't exist
            create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([f'{col} {data_type}' for col, data_type in column_data_types.items()])})"
            cursor.execute(create_table_query)

            # Insert data into the MySQL table
            for index, row in df.iterrows():
                insert_query = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES ({', '.join(['%s' for _ in range(len(df.columns))])})"
                cursor.execute(insert_query, tuple(row))

            # Commit changes and close the connection
            connection.commit()
            print("Data inserted successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close the database connection
        if connection.is_connected():
            cursor.close()
            connection.close()

# Use the function to insert CSV data into the MySQL database

if __name__ == "__main__":
    csv_file_path = "E:/Codebase/FinalProject/datasets/single/Salary.csv"
    host = "localhost"           
    database = "finalproject"       
    user = "root"           
    password = "root"

    csv_to_mysql(csv_file_path, host, database, user, password)