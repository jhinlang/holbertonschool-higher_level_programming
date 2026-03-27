#!/usr/bin/env python3
"""
Script to create and populate the SQLite products database
"""

import sqlite3
import os

def create_database():
    """Create the SQLite database and populate it with sample data"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, 'products.db')

    # Remove existing database if it exists
    if os.path.exists(db_path):
        os.remove(db_path)

    # Create connection
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Insert sample data
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99),
        (3, 'Python Book', 'Books', 45.99),
        (4, 'Wireless Mouse', 'Electronics', 29.99),
        (5, 'Desk Lamp', 'Home Goods', 35.50)
    ''')

    conn.commit()
    conn.close()
    print(f"Database created successfully at {db_path}")

if __name__ == '__main__':
    create_database()
