#!/usr/bin/python3
"""
    script that takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb


def main():
    """
        args:
            mysql username
            mysql password
            database name
            state name
    """

    if len(sys.argv) != 5:
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db_connection = MySQLdb.connect("localhost", mysql_username,
                                    mysql_password, database_name)

    cursor = db_connection.cursor()

    query = """
    SELECT cities.id, cities.name, states.name FROM
    cities INNER JOIN states ON cities.state_id = states.id WHERE BINARY
    states.name = ('{}') ORDER BY cities.id ASC""".format(state_name)
    cursor.execute(query)

    results = cursor.fetchall()

    """ Display """
    for row in results:
        if row[1] == None:
            print()
        else: 
            print("{}".format(row[1]), end = ", ")
    print()

    """ close cursor and db connection """
    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    main()
