import pymysql

def insert_data_into_mysql(sql_data, mysql_queries):  ## function to output sql queries into live database
    # Step 1: Connect to MySQL // make a sql file
    mysql_conn = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="jemisys_backup"
    )
    cursor_mysql = mysql_conn.cursor()

    # Step 2: Create tables in MySQL
    for table_name, create_query in mysql_queries.items():
        print(f"Creating table {table_name}...")
        cursor_mysql.execute(create_query)

    # Step 3: Insert data into MySQL
    for table_name, table_info in sql_data.items():
        if table_info["data"]:
            # Dynamically create placeholders for the columns
            placeholders = ", ".join(["%s"] * len(table_info["schema"]))
            column_names = ", ".join([f"`{col[0]}`" for col in table_info["schema"]])  # Wrap column names in backticks
            insert_query = f"INSERT INTO `{table_name}` ({column_names}) VALUES ({placeholders})"
            
            print(f"Inserting data into {table_name}...")
            for row in table_info["data"]:
                # try:
                    # Check if row has fewer values than the number of columns in the schema
                    if len(row) < len(table_info["schema"]):
                        print(f"Row length mismatch in {table_name}: Expected {len(table_info['schema'])} values, got {len(row)} values.")
                        row = list(row) + [None] * (len(table_info["schema"]) - len(row))  # Pad missing values with None

                    # Check if row and placeholders match before execution
                    if len(row) != len(table_info["schema"]):
                        raise ValueError(f"Mismatch between placeholders and values for table {table_name}")

                    cursor_mysql.execute(insert_query, tuple(row))
                # except Exception as e:
                #     print(f"Error inserting data into {table_name}: {e}")

    mysql_conn.commit()
    mysql_conn.close()

def output_sql_to_file(sql_data, mysql_queries, output_file): ## function to output sql queries to a file
    # Step 1: Open the file for writing SQL commands
    with open(output_file, 'w',encoding='utf-8') as f:
        
        # Step 2: Write CREATE TABLE statements to the file
        for table_name, create_query in mysql_queries.items():
            print(f"Writing CREATE TABLE for {table_name} to {output_file}...")
            f.write(f"{create_query};\n\n")  # Write the CREATE TABLE query

        # Step 3: Write INSERT statements to the file
        for table_name, table_info in sql_data.items():
            if table_info["data"]:
                # Dynamically create placeholders for the columns
                placeholders = ", ".join(["%s"] * len(table_info["schema"]))
                column_names = ", ".join([f"`{col[0]}`" for col in table_info["schema"]])  # Wrap column names in backticks
                insert_query = f"INSERT INTO `{table_name}` ({column_names}) VALUES "

                # print(f"Writing INSERT statements for {table_name} to {output_file}...")
                for row in table_info["data"]:
                    try:
                        # Pad the row if the number of values is less than the number of columns
                        if len(row) < len(table_info["schema"]):
                            row = list(row) + [None] * (len(table_info["schema"]) - len(row))

                        # Format the row into SQL-safe values
                        formatted_values = ', '.join(
                            [f"'{value}'" if isinstance(value, str) else
                             f"{value}" if value is not None else "NULL" for value in row]
                        )
                        # Write the INSERT query for the current row
                        f.write(f"{insert_query}({formatted_values});\n")
                    except Exception as e:
                        print(f"Error writing data for {table_name}: {e}")

            f.write("\n")  # Add a newline for readability between tables

    print(f"SQL script written to {output_file}")


if __name__ == "__main__":
    from extract_sql_server_data import extract_sql_server_data
    from convert_schema import convert_schema_to_mysql
    
    sql_data = extract_sql_server_data()
    mysql_queries = convert_schema_to_mysql(sql_data)
    
    insert_data_into_mysql(sql_data, mysql_queries)
    # Example usage
    # output_file = 'output_script.sql'
    # output_sql_to_file(sql_data, mysql_queries, output_file)

