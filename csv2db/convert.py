import sqlite3
import os
import csv
from dateutil.parser import parse
from datetime import datetime

def main():
    con = sqlite3.connect("data.db")
    db = con.cursor()

    folder_path = "csv"

    # Creates an "index" table for all table names
    db.execute('''CREATE TABLE tables (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT)''')

    # iterate through all files inside folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            name, filetype = filename.split(".")
            if filetype == "csv":

                # Update index table
                db.execute("INSERT INTO tables (name) VALUES (?)", (name,))
                with open(file_path, mode='r') as file:
                        csv_reader = csv.reader(file)
                        csv_dict = csv.DictReader(file, skipinitialspace=True)

                        header = next(csv_dict)

                        # Dynamic table name, based on CSV name
                        table_creater = "CREATE TABLE IF NOT EXISTS %s (" %name
                        table_inserter = "INSERT INTO %s (" %name

                        # Assigning SQL datatype
                        for key, value in header.items():
                            table_creater += "\n\t" + key
                            table_inserter += key + ", "
                            if value.isdecimal():
                                table_creater += " INT, "
                            elif value.isdigit():
                                table_creater += " FLOAT,"
                            else:
                                try:
                                    parsed_date = parse(value)
                                    if parsed_date.time() == datetime.min.time():
                                        table_creater += " DATE, "
                                    else:
                                        table_creater += " DATETIME, "
                                except:
                                    table_creater += " TEXT, "


                        table_creater = table_creater.rstrip(" ,") + ")"
                        table_inserter = table_inserter.rstrip(" ,") + ") VALUES("

                        # SQL VALUES placeholders
                        for _ in header:
                            table_inserter += "?, "
                        table_inserter = table_inserter.rstrip(" ,") + ")"


                        db.execute(table_creater)
                        file.seek(0)
                        next(csv_reader)

                        # INSERT data
                        for row in csv_reader:
                            db.execute(table_inserter, row)
                print(filename, "ok")

            else:
                # not .csv format
                print(filename, "was not processed")

    con.commit()
    con.close()
    print("\ndone\n")


main()