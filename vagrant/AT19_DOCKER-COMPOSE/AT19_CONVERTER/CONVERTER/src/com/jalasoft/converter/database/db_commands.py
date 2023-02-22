#
# @db_commands.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
#
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#


from database.database_connection import DatabaseConnection as db

my_Cursor = db.conexion.cursor()


class CRUD:
    """"Defines Create, Read, Update and Delete functions"""

    def create_table(tablename):
        """Creates a table"""
        
        my_Cursor.execute("""SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{0}' """.format(
            tablename.replace('\'', '\'\'')))
        if my_Cursor.fetchone()[0] == 1:
            print("Table already created")
            return
        my_Cursor.execute(
            "CREATE TABLE " + tablename + " (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50),"
                                          "checksum VARCHAR(255), route VARCHAR(155))")
        print("Table created")
        return

    def check_table_exists(tablename):
        """Checks if table exists"""

        my_Cursor.execute("""
            SELECT COUNT(*)
            FROM information_schema.tables
            WHERE table_name = '{0}'
            """.format(tablename.replace('\'', '\'\'')))
        if my_Cursor.fetchone()[0] == 1:
            my_Cursor.close()
            return True
        return False

    def insert_data(name, checksum, route):
        """Inserts data"""

        query = "INSERT INTO media (name, checksum, route) VALUES (%s, %s, %s)"
        my_Cursor.execute(query, (name, checksum, route))
        print("Data inserted")

    def read_all_data():
        """Reads all data"""

        query = "SELECT name, checksum, route FROM media"
        my_Cursor.execute(query)
        datos = my_Cursor.fetchall()
        for dato in datos:
            print(dato)
        print("Data read")

    def read_specific_data(read_query):
        """Reads data searching by its name"""

        query = read_query
        my_Cursor.execute(query)
        column = my_Cursor.fetchall()
        column = [x[0] for x in column]
        return column

    def update_data(route, check):
        """Updates data"""

        query = "UPDATE media SET route = %s  WHERE checksum = %s"
        my_Cursor.execute(query, (route, check))
        print("Data updated")

    def delete_data(id):
        """Deletes data"""

        query = "DELETE FROM media WHERE id = %s"
        my_Cursor.execute(query, (id))
        print("Data deleted")
