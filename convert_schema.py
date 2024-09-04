def convert_data_type(sql_data_type):
    # SQL Server to MySQL data type mapping
    mapping = {
        'nvarchar': 'VARCHAR(255)',   # Default size for varchar
        'varchar': 'VARCHAR(255)',    # Default size for varchar
        'char': 'CHAR(10)',           # Default size for char, adjust as needed
        'datetime': 'DATETIME',       # Convert datetime
        'smalldatetime': 'DATETIME',  # Convert smalldatetime to DATETIME
        'int': 'INT',
        'bigint': 'BIGINT',
        'bit': 'TINYINT(1)',
        'decimal': 'DECIMAL',
        'money': 'DECIMAL(19,4)',
        'smallmoney': 'DECIMAL(10,4)',      # Map smallmoney to DECIMAL(10,4)
        'float': 'FLOAT',
        'uniqueidentifier': 'CHAR(36)',  # GUIDs to CHAR(36)
        'image': 'LONGBLOB',                # Convert image to LONGBLOB
        'varbinary': 'VARBINARY(255)',       # Default size for VARBINARY
        # Add other mappings as necessary
    }
    return mapping.get(sql_data_type.lower(), sql_data_type)

def convert_schema_to_mysql(sql_data):
    mysql_queries = {}
    for table_name, table_info in sql_data.items():
        columns = []
        for column in table_info["schema"]:
            column_name, data_type = column
            mysql_data_type = convert_data_type(data_type)
            columns.append(f"`{column_name}` {mysql_data_type}")
        
        # Join columns without a trailing comma
        columns_str = ", ".join(columns)
        create_table_query = f"CREATE TABLE IF NOT EXISTS `{table_name}` ({columns_str});"
        mysql_queries[table_name] = create_table_query
    return mysql_queries

if __name__ == "__main__":
    # You can import 'extract_sql_server_data' and call it here to get the data dynamically
    from extract_sql_server_data import extract_sql_server_data
    sql_data = extract_sql_server_data()
    mysql_schema = convert_schema_to_mysql(sql_data)
    
    # Output or save the MySQL schema to a file
    for table, query in mysql_schema.items():
        print(f"MySQL schema for {table}:\n{query}\n")
