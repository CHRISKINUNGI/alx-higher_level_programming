#!/usr/bin/python3
"""
    script that takes in an argument and displays all values in
    the states table of hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb


def main():
    """
       code engine
    """

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db_connection = MySQLdb.connect("localhost", mysql_username,
                                    mysql_password, database_name)

    cursor = db_connection.cursor()

    query = "SELECT *FROM states WHERE name = ('{}') ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    results = cursor.fetchall()

    """ Display """
    for row in results:
        print(f"({row[0]}, '{row[1]}')")

    """ close cursor and db connection """
    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    main()
