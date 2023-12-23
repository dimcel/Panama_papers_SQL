# Data Parsing and Database Insertion Script

## Overview

This script parses data from CSV files and inserts it into a PostgreSQL database. The data includes information about entities, officers, roles, addresses, intermediaries, and relationships between them.

## Prerequisites

- Python 3
- PostgreSQL database

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

- `create.sql`: SQL script for creating the database schema.

- `csv_folder/`: Place your CSV files in this folder.

## Notes

- Make sure to review and customize the `create.sql` script based on your requirements.

- The script will parse CSV files from the `csv_folder/` directory, so ensure the files are present and properly formatted.

- If you encounter any issues or have questions, feel free to reach out to [your contact information].

```

Replace `[your contact information]` with the appropriate contact details for users to reach out for support or questions.
```
