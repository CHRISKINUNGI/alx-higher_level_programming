#!/usr/bin/python3
"""
    first module
    script that lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


def main():
    """
       Main function to list states from hbtn_0e_0_usa db
    """

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect("localhost", mysql_username,
                         mysql_password, database_name)
    cursor = db.cursor()
    """  Execute the query and fetch results """
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    results = cursor.fetchall()

    """ Display results """
    for row in results:
        print(f"({row[0]}, '{row[1]}')")

    """ Close the cursor and database connection """
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
