# MySQL Database Export to YAML

This project provides a Python script to export the contents of a MySQL database to a YAML file. The script allows you to specify tables to be excluded from the export and stores the resulting YAML files in an `exports` directory with a timestamp in the filename to prevent accidental overwrites.

## Requirements

- Python 3
- PyMySQL
- PyYAML

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/JurajCekan/mysql_export_to_yaml.git
   ```

2. Change to the project directory:

   ```
   cd mysql_export_to_yaml
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Copy the `config-template.yaml` file and rename it to `config.yaml`:

   ```
   cp config-template.yaml config.yaml
   ```

2. Edit `config.yaml` to set your MySQL connection credentials and specify any tables you want to exclude from the export:

   ```yaml
   mysql:
     host: localhost
     user: your_username
     password: your_password
     database: your_database

   exclude_tables:
     - table_to_exclude1
     - table_to_exclude2
   ```

## Usage

Run the script to export your MySQL database contents to a YAML file:

```
python mysql_export_to_yaml.py
```

The exported YAML files will be saved in the `exports` directory with a timestamp in the filename, e.g. `export_YYYYMMDD-HHMM.yaml`.

## Contributing

If you would like to contribute to this project, please feel free to submit a pull request or open an issue on the repository.
