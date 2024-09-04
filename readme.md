# MSSQL to MYSQL conversion

- this program uses the libraries declared in requirement.txt
- this program will read schemas form an sql server convert the schemas based on the defined schemas in convert_schema.py
- this proram will then import converted schema with provided sql server data into a mysql database.

# How to use

- clone this repo
- cd path/to/your/repo
- pip install -r requirements.txt
- run "python import_to_mysql.py"

# Additional info

- the file JEMiSys_Backup.sql file is exported from heidisql