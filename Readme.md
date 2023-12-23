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

Run the script with the following command:

```bash
python parser.py -H <hostname> -p <port> -U <username> -P <password> -d <database>
```
