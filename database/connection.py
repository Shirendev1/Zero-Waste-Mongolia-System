#!/usr/bin/env python
"""
Database connection and initialization module.
"""

import os
import psycopg2
from psycopg2 import sql, Error
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://localhost/zero_waste_pilot")


def get_connection():
    """
    Get a PostgreSQL database connection.
    
    Returns:
        psycopg2 connection object
    """
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        raise


def init_db():
    """
    Initialize the database schema.
    Reads and executes schema.sql.
    """
    schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
    
    try:
        conn = get_connection()
        cur = conn.cursor()
        
        with open(schema_path, "r") as f:
            schema_sql = f.read()
        
        cur.execute(schema_sql)
        conn.commit()
        cur.close()
        conn.close()
        
        print("✓ Database initialized successfully")
    except Error as e:
        print(f"Error initializing database: {e}")
        raise


def test_connection():
    """
    Test the database connection.
    """
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        result = cur.fetchone()
        cur.close()
        conn.close()
        
        if result:
            print("✓ Database connection successful")
            return True
    except Error as e:
        print(f"✗ Database connection failed: {e}")
        return False


if __name__ == "__main__":
    # Test connection and initialize if needed
    test_connection()
    init_db()
