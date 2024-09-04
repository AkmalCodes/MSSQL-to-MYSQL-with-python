import pyodbc

def extract_sql_server_data():
    sql_conn_str = (
        "DRIVER={SQL Server};"
        "SERVER=DESKTOPTEHA;"
        "DATABASE=JEMiSys_Backup;"  # Use the restored DB
        "Trusted_Connection=yes;" #for using windows authentication
    )
    sql_conn = pyodbc.connect(sql_conn_str)
    cursor_sql = sql_conn.cursor()

    # Step 1: Extract table names
    cursor_sql.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'")
    tables = cursor_sql.fetchall()

    # Step 2: Extract schema and data for each table
    sql_data = {}
    for table in tables:
        table_name = table[0]

        # Get the schema of the table
        cursor_sql.execute(f"SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='{table_name}'")
        schema = cursor_sql.fetchall()
        sql_data[table_name] = {"schema": schema, "data": []}

        # Get the data of the table
        cursor_sql.execute(f"SELECT * FROM {table_name}")
        rows = cursor_sql.fetchall()
        sql_data[table_name]["data"].extend(rows)

    sql_conn.close()
    return sql_data

if __name__ == "__main__":
    data = extract_sql_server_data()
    print("Extracted data:", data)
