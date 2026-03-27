#!/usr/bin/env python3
"""
Flask application to read and display data from JSON, CSV, and SQLite databases
"""

import json
import csv
import sqlite3
import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page"""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page"""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Render the items page with dynamic content from JSON"""
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        json_file = os.path.join(script_dir, 'items.json')

        with open(json_file, 'r') as f:
            data = json.load(f)

        items_list = data.get('items', [])
        return render_template('items.html', items=items_list)

    except FileNotFoundError:
        return render_template('items.html', items=[])
    except json.JSONDecodeError:
        return render_template('items.html', items=[])
    except Exception as e:
        print(f"Error loading items: {e}")
        return render_template('items.html', items=[])


def read_json_products(file_path):
    """Read products from JSON file"""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_path} not found")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format")


def read_csv_products(file_path):
    """Read products from CSV file"""
    try:
        products = []
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert id and price to appropriate types
                product = {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                products.append(product)
        return products
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_path} not found")
    except (KeyError, ValueError) as e:
        raise ValueError(f"Invalid CSV format: {e}")


def read_sqlite_products(file_path):
    """Read products from SQLite database"""
    try:
        conn = sqlite3.connect(file_path)
        conn.row_factory = sqlite3.Row  # Return rows as dictionaries
        cursor = conn.cursor()

        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()

        products = []
        for row in rows:
            product = {
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            }
            products.append(product)

        conn.close()
        return products

    except sqlite3.OperationalError as e:
        raise ValueError(f"Database error: {e}")
    except FileNotFoundError:
        raise FileNotFoundError(f"Database file {file_path} not found")
    except Exception as e:
        raise ValueError(f"Error reading from database: {e}")


@app.route('/products')
def products():
    """
    Display products from JSON, CSV, or SQLite database.
    Query parameters:
    - source: 'json', 'csv', or 'sql' (required)
    - id: optional product id to filter
    """
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id', None)

    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Validate source parameter
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html',
                             error='Wrong source',
                             products=[])

    # Read data based on source
    try:
        if source == 'json':
            file_path = os.path.join(script_dir, 'products.json')
            data = read_json_products(file_path)
        elif source == 'csv':
            file_path = os.path.join(script_dir, 'products.csv')
            data = read_csv_products(file_path)
        else:  # source == 'sql'
            file_path = os.path.join(script_dir, 'products.db')
            data = read_sqlite_products(file_path)

        # Filter by id if provided
        if product_id:
            try:
                product_id = int(product_id)
                filtered_data = [p for p in data if p['id'] == product_id]
                if not filtered_data:
                    return render_template('product_display.html',
                                         error='Product not found',
                                         products=[])
                data = filtered_data
            except ValueError:
                return render_template('product_display.html',
                                     error='Invalid product ID',
                                     products=[])

        return render_template('product_display.html',
                             products=data,
                             error=None)

    except (FileNotFoundError, ValueError) as e:
        return render_template('product_display.html',
                             error=str(e),
                             products=[])
    except Exception as e:
        return render_template('product_display.html',
                             error=f'An error occurred: {str(e)}',
                             products=[])


if __name__ == '__main__':
    app.run(debug=True, port=5000)
