# Data Parsing and Database Insertion Script

## Overview

This script parses data from CSV files and inserts it into a PostgreSQL database. The data includes information about entities, officers, roles, addresses, intermediaries, and relationships between them.

Contact me for the sample CSV files i used.

## Prerequisites

- Python 3
- PostgreSQL database
- Python virtual enviroment

## Installation

1. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure that your CSV files are placed in the same folder as the script.

2. Create a PostgreSQL database with the necessary credentials.

3. Run the script with the following command:

   ```bash
   python parser.py -H <hostname> -p <port> -U <username> -P <password> -d <database>
   ```

   Replace `<hostname>`, `<port>`, `<username>`, `<password>`, and `<database>` with your PostgreSQL database connection details.

## Files in the Same Folder

- `queries.sql`: SQL script for creating the database schema.

- `csv_panama_papers/`: Place your CSV files in this folder.

## Notes

- This repository provides two methods for using the parser:

  1. **Automated Setup:**

     - Run the `parser_automated.py` script after initializing the PostgreSQL database. Refer to the usage instructions for the code snippet.
     - This automated process will create the necessary database schema and parse the data automatically.

  2. **Manual Setup:**
     - Execute the `schema.sql` script to manually create the database schema.
     - Run the `parser.py` script (as described in the usage section).
     - This will generate a substantial `.sql` file named `data.sql` (approximately 400MB).
     - Execute the generated `data.sql` file to insert the parsed data into the database.

Choose the method that best fits your requirements and workflow. If you opt for the automated setup, the entire process, including schema creation and data parsing, is handled in a single step. For manual setup, you have more control over the individual steps, allowing for customization or troubleshooting as needed.
