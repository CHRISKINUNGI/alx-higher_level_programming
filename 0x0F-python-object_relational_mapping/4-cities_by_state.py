#!/usr/bin/python3
"""
   script that lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb


def main():
    """
       args:
           mysql username
           mysql password
           database name
    """

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db_connection = MySQLdb.connect("localhost", mysql_username,
                                    mysql_password, database_name)

    cursor = db_connection.cursor()

    cursor.execute("""
    SELECT cities.id, cities.name, states.name FROM 
    cities INNER JOIN states ON cities.state_id = states.id 
    ORDER BY cities.id ASC""")

    results = cursor.fetchall()

    for row in results:
        print(f"({row[0]}, '{row[1]}', '{row[2]}')")

    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    main()
