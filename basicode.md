Happy 1-year birthday! 🎉 I'd be happy to help you get started with PostgreSQL on your notebook. Below are the steps for each of your requests:

### 1. Install PostgreSQL Library for Python:

You'll need the `psycopg2` library to interact with PostgreSQL from Python. Install it using:

```bash
pip install psycopg2
```

### 2. Connecting to the Database:

Here's an example code snippet to connect to your PostgreSQL database:

```python
import psycopg2

# Replace these with your own database credentials
dbname = "your_database_name"
user = "your_username"
password = "your_password"
host = "localhost"
port = "5432"  # Default PostgreSQL port

# Establish a connection
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

# Create a cursor
cursor = conn.cursor()

# Example query
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("You are connected to - ", record)

# Close communication with the database
cursor.close()
conn.close()
```

### 3. Creating a Database:

You can create a new database with the following SQL command:

```python
# After connecting to PostgreSQL
cursor.execute("CREATE DATABASE your_database_name;")
```

### 4. Basic Example Data and Queries:

Let's create a simple table and insert some data:

```python
# After connecting to your database
cursor.execute("CREATE TABLE example_table (id serial PRIMARY KEY, name VARCHAR);")

# Insert data
cursor.execute("INSERT INTO example_table (name) VALUES (%s);", ('John',))
cursor.execute("INSERT INTO example_table (name) VALUES (%s);", ('Alice',))

# Retrieve data
cursor.execute("SELECT * FROM example_table;")
records = cursor.fetchall()
for record in records:
    print(record)
```

Make sure to replace placeholders like `your_database_name`, `your_username`, `your_password` with your actual credentials.

Remember to handle exceptions, commit changes, and close connections properly in a real-world scenario.

Feel free to adapt the code according to your specific requirements!
