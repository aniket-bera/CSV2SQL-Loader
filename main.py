import pandas as pd
import os
import pyodbc

def createTable(connStr, tableName, df):
    try:
        # Establish connection
        conn = pyodbc.connect(connStr)
        
        # Create table with columns from DataFrame
        cursor = conn.cursor()
        cursor.execute(f"CREATE TABLE {tableName} ({', '.join([f'{col} VARCHAR(MAX)' for col in df.columns])})")
        conn.commit()
        cursor.close()
        
        # Close connection
        conn.close()
        
        print("Table created successfully!")

    except Exception as e:
        print("Error:", e)

def pushCSVtoDB(path, connStr):
    try:
        # Read data from CSV into a pandas DataFrame
        df = pd.read_csv(path)
        
        # Replace blank cell with null
        df.fillna("null", inplace=True)
        
        # Extract table name from file name
        tableName = os.path.splitext(os.path.basename(path))[0]
        
        # Create table if it doesn't exist
        createTable(connStr, tableName, df)
        
        # Establish connection
        conn = pyodbc.connect(connStr)
        
        # Insert data into the database
        cursor = conn.cursor()
        
        # Generate INSERT query dynamically based on the number of columns
        placeholders = ', '.join(['?' for _ in range(len(df.columns))])
        print(placeholders)
        query = f"INSERT INTO {tableName} VALUES ({placeholders})"
        
        # Execute INSERT query for each row in the DataFrame
        for index, row in df.iterrows():
            cursor.execute(query, tuple(row))
            print(index+1)
        conn.commit()
        cursor.close()
        
        # Close connection
        conn.close()
        
        print("Data inserted successfully!")

    except Exception as e:
        print("Error:", e)

def main(path):
    try:
        # connection details
        server = 'LAPTOP-G46LLVV6\JARVIS'
        database = 'demodb1'
        username = 'jarvis'
        password = 'jarvis@17'
        
        # Create connection string
        connStr = (
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={username};'
            f'PWD={password};'
        )
        
        # Push CSV data to database
        pushCSVtoDB(path, connStr)

    except Exception as e:
        print("Error:", e)
        
if __name__ == "__main__":
    main("Round_3.csv")