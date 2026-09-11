import os
from sqlalchemy import text
from database.connection import engine

def initialize_database():
    """
    Reads the schema.sql file and executes it to create database tables.
    """
    print("Starting database initialization...")
    
    # 1. Dynamically find the path to schema.sql
    # This ensures the script works regardless of where you run it from
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    schema_path = os.path.join(project_root, "sql", "schema.sql")
    
    if not os.path.exists(schema_path):
        print(f"Error: Schema file not found at {schema_path}")
        return

    # 2. Read the SQL file
    with open(schema_path, "r") as file:
        sql_script = file.read()

    # 3. Execute the SQL statements
    try:
        with engine.begin() as connection:
            # SQLAlchemy text() expects a single SQL statement. 
            # If your schema has multiple tables, we split them by ';'
            statements = sql_script.split(';')
            
            for statement in statements:
                if statement.strip(): # Skip empty lines
                    connection.execute(text(statement))
                    
        print("✅ Database tables initialized successfully!")
        
    except Exception as e:
        print(f"❌ Failed to initialize database: {e}")

if __name__ == "__main__":
    initialize_database()