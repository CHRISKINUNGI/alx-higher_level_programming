#!/usr/bin/python3
"""
    script that lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


def main():
    """
        MYSQL

    """

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db_connection = MySQLdb.connect("localhost", mysql_username,
                                    mysql_password, database_name)
    cursor = db_connection.cursor()

    """ Execute the Query and get results """
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()

    """ Fetch all rows and filter names starting with an uppercase 'N' """
    filtered_state = [(id, name) for id, name in rows if name.startswith('N')]

    """ Display results """
    for row in filtered_state:
        print(f"({row[0]}, '{row[1]}')")

    """ close the database connection and cursor """
    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    main()
