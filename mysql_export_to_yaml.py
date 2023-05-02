import os
import pymysql
import yaml
from datetime import datetime

# Load login credentials from config.yaml
with open("config.yaml", "r") as config_file:
    config_data = yaml.safe_load(config_file)

mysql_config = config_data["mysql"]
exclude_tables = config_data.get("exclude_tables", [])

# Connect to MySQL database
connection = pymysql.connect(
    host=mysql_config["host"],
    user=mysql_config["user"],
    password=mysql_config["password"],
    database=mysql_config["database"],
    cursorclass=pymysql.cursors.DictCursor,
)

try:
    with connection.cursor() as cursor:
        # Retrieve the list of tables
        cursor.execute("SHOW TABLES")
        tables = [table["Tables_in_" + mysql_config["database"]] for table in cursor.fetchall()]

        # Remove excluded tables
        tables = [table for table in tables if table not in exclude_tables]

        # Export data from tables
        exported_data = {}
        for table in tables:
            cursor.execute(f"SELECT * FROM {table}")
            exported_data[table] = cursor.fetchall()

finally:
    connection.close()

# Create filename with date and time
now = datetime.now()
formatted_date_time = now.strftime("%Y%m%d-%H%M")
export_filename = f"export_{formatted_date_time}.yaml"

# Check if 'exports' directory exists, if not, create it
exports_directory = "exports"
if not os.path.exists(exports_directory):
    os.makedirs(exports_directory)

# Write exported data to file in 'exports' directory
export_path = os.path.join(exports_directory, export_filename)
with open(export_path, "w") as export_file:
    yaml.dump(exported_data, export_file, allow_unicode=True)
