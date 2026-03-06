#!/usr/bin/python3
"""List all cities of a state from the database."""

import MySQLdb
import sys


def main():
    """Run the SQL query and print results."""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )

    cursor = db.cursor()

    cursor.execute(
        """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """,
        (state_name,)
    )

    cities = cursor.fetchall()
    print(", ".join(city[0] for city in cities))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
