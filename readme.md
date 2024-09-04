# MSSQL to MYSQL conversion

- this program uses the libraries declared in requirement.txt
- this program will read schemas form an sql server convert the schemas based on the defined schemas in convert_schema.py
- this proram will then import converted schema with provided sql server data into a mysql database.

# How to use

- clone this repo
- cd path/to/your/repo
- in extract_sql_server_data.py define values of sql server 
    ``` 
    sql_conn_str = (
        "DRIVER={SQL Server};"
        "SERVER=DESKTOPTEHA;" # find the value in management studio
        "DATABASE=JEMiSys_Backup;"  # Use the restored DB
        "Trusted_Connection=yes;" #for using windows authentication
    )
    ``` 
- run ```pip install -r requirements.txt```
- run ```python import_to_mysql.py```

# Additional info

- the file JEMiSys_Backup.sql file is exported from heidisql

# Python Libraries Used

### Here is the list of Python libraries that are required for this program:

- pyodbc: For connecting to SQL Server and extracting the schemas and data.
- pymysql: For connecting to MySQL and inserting the converted schemas and data.
- You can find the full list of dependencies in requirements.txt. Make sure to install them by running:

``` pip install -r requirements.txt ```