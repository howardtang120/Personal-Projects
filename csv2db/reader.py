import sqlite3
con = sqlite3.connect("data.db")
db = con.cursor()
all_tables = db.execute("SELECT name FROM tables")
table_list = []
for table in all_tables:
    table_list.append(table[0])


def main():
    print("\nType \"quit\" to quit, \"help\" for a list of commands")
    command = ""
    while (True):

        command = input("\nWhat to do? ").lower()
        if command == "tables"  : list_tables()
        elif command == "select": select()
        elif command == "help"  : help()
        elif command == "quit"  : break
        else: print("invalid command")


def list_tables():
    for table in table_list:
        print(table)


def select():
    condition = input("SELECT * from \"table_list\" WHERE ")
    for table in table_list:
        query = "SELECT * from %s WHERE " % table
        query += condition

        db.execute(query)
        results = db.fetchall()
        print(table)
        for row in results:
            print(row)
        print()


def help():
    print('''
    tables  :list all table names in database
    select  :enter the condition to run the database
    help    :bring up a list of commands
    quit    :quit the program
    ''')


main()
