# CSV2SQL-Loader

CSV2SQL-Loader is a Python script designed to automate the process of creating tables in a SQL Server database based on CSV file structure and inserting CSV data into these tables. It utilizes pandas for CSV handling, pyodbc for database connectivity, and provides flexibility to handle varying CSV formats by dynamically creating tables.

## Features

- **Dynamic Table Creation**: Automatically creates SQL tables based on CSV file columns.
- **Data Insertion**: Inserts CSV data into corresponding SQL tables.
- **Error Handling**: Provides robust error handling for connection issues, table creation, and data insertion failures.
- **Compatibility**: Works with SQL Server using ODBC Driver 17.

## Getting Started

### Prerequisites

- Python 3.x
- pandas library (`pip install pandas`)
- pyodbc library (`pip install pyodbc`)
- Microsoft ODBC Driver 17 for SQL Server

### Installation

1. Install the required Python packages:

    ```bash
    pip install pandas pyodbc
    ```

2. Ensure you have Microsoft ODBC Driver 17 for SQL Server installed.

### Usage

1. Prepare your CSV file and place it in the project directory.

2. Update the database connection details in the script (`main.py`) with your SQL Server details:

    ```python
    server = 'YOUR_SERVER_NAME'
    database = 'YOUR_DATABASE_NAME'
    username = 'YOUR_USERNAME'
    password = 'YOUR_PASSWORD'
    ```

3. Run the script with your CSV file path as an argument:

    ```bash
    python main.py path/to/your/csvfile.csv
    ```

4. The script will:
   - Create a new table in the SQL Server database using the CSV filename (excluding extension) as the table name.
   - Insert data from the CSV file into the newly created table.

### Example

For example, if you have a CSV file named `example_data.csv`, the script will create a table named `example_data` in your SQL Server database and insert the data from `example_data.csv` into this table.

### File Structure

- `main.py`: Main script to execute CSV to SQL database loading process.
- `README.md`: This file providing instructions and information about the project.
- `CSV_Filepath`: Replace with your actual CSV file path when running the script.

### Contact

For any questions or suggestions, please feel free to [open an issue](https://github.com/yourusername/CSV-to-SQL-Database-Loader/issues/new) on GitHub.

---

Thank you for using CSV2SQL-Loader! We hope it simplifies the process of importing CSV data into your SQL Server databases.
