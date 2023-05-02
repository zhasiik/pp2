import psycopg2
import csv

###

def connect(conn):
    #Connect to the PosgreSQL server
    try:
        conn = psycopg2.connect(
            host = "localhost",
            database = "postgres",
            user = "postgres",
            password = "Zhasulan00",
            port = "5432")
        
        #create a cursor
        cur = conn.cursor()

        #execute a statement
        cur.execute('SELECT version()')

        #display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        #Close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            return conn
###
        
def createTable(cursor):
    #Create table in PostgreSQL database if such table not exists
    query = """
        CREATE TABLE IF NOT EXISTS postgres.phonebook.phonebook2(
            id SERIAL,
            phone VARCHAR(11),
            name VARCHAR(255) UNIQUE
        )
        """
    cursor.execute(query)
    
###

def insertData(cursor, name, phone):
    #Insert data to our table phonebook
    query = f"""
        CALL postgres.phonebook.insert_data(%s, %s);
        """
    args = (name, phone)
    cursor.execute(query, args)
    
        

###

def getTable(cursor):
    #showing our table
    query = """
        SELECT * FROM postgres.phonebook.phonebook2
        """
    cursor.execute(query)
    output = cursor.fetchall()
    for i in output:
        print(i)

###

def updateData(cursor, where, towhat):
    #updating data by name or number
    query = """"""
    if where.isnumeric():
        query = f"""
            UPDATE postgres.phonebook.phonebook2
            SET name = '{towhat}'
            WHERE phone = '{where}'
            """
    else:
        query = f"""
            UPDATE postgres.phonebook.phonebook2
            SET phone = '{towhat}'
            WHERE name = '{where}'
            """
    cursor.execute(query)

###

def showData(cursor, select, order):
    query = f"""
        SELECT "{select}"
        FROM postgres.phonebook.phonebook2
        ORDER BY "{order}"
        """
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

###

def showDataByPattern(cursor, pattern):
    
    args = (pattern + "%",)
    cursor.callproc("postgres.phonebook.show_data_by_pattern", args)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

###
def deleteData(cursor, where):
    query = """
        CALL postgres.phonebook.delete_data(%s);
        """
    args = (where,)
    cursor.execute(query, args) 

###

def showInPage(cursor, page):
    
    args = (page,)
    cursor.callproc("postgres.phonebook.show_in_page", args)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

###

def insertByList(cursor, phonename):
    cursor.execute(f"SELECT * FROM postgres.phonebook.insert_data_by_list(ARRAY[{phonename}])")
    rows = cursor.fetchall()
    print("Incorrect data: ", len(rows))
    for row in rows:
        print(row) 
            

###

        
conn = None
cursor = None
#connecting
conn = connect(conn)
cursor = conn.cursor()
#creating table
createTable(cursor)
#inserting data into the phonebook
print("Type of query: insert, insertbycsv, delete, insertbylist, selectbypattern, showinpage, insertbylist")
typ = input()

#inserting from console 11
if(typ == "insert"):
    print("Amount of data: ")
    n = int(input())
    for i in range (n):
        name = input()
        phone = input()
        insertData(cursor, name, phone)
        
#inserting from csv file
if(typ == "insertbycsv"):
    print("Name of csv file: ")
    s = input()
    dataSet = []
    with open(f"data//{s}.csv") as file:
        reader = csv.reader(file)
        for i in reader:
            dataSet.append(i[0].split(';'))
        dataSet = dataSet[1:]
        for i in dataSet:
            insertData(cursor, i[0], i[1])

#updating table
if(typ == "update"):
    print("Change in: ")
    where = input()
    print("To: ")
    towhat = input()
    updateData(cursor, where, towhat)

#showing table with filters
if(typ == "selectinorder"):
    print("Select: ")
    select = input()
    print("In Order: ")
    order = input()
    showData(cursor, select, order)

#deleting data 11
if(typ == "delete"):
    print("Where: ")
    where = input()
    deleteData(cursor, where) 


#showing table with pattern 11
if(typ == "selectbypattern"):
    print("Pattern: ")
    pattern = input()
    showDataByPattern(cursor, pattern)

#shows data from table with pagination where 1 page = 5 rows
if(typ == "showinpage"):
    while True:
        print("Page: ")
        page = input()
        if page == "end":
            break
        else:
            page = int(page)
            showInPage(cursor, page)

#inserting by list and returning incorrect data
if(typ == "insertbylist"):
    print("Amount of data: ")
    n = int(input())
    phonename = ""
    for i in range (n):
        name = input()
        phone = input()
        if(i == n - 1):
            phonename = phonename + "ARRAY[\'" + name + "\', \'" + phone + "\']"
        else:
            phonename = phonename + "ARRAY[\'" + name + "\', \'" + phone + "\'], "
    insertByList(cursor, phonename)
        



if conn is not None:
    #show table
    getTable(cursor)
    conn.commit()
    cursor.close()
    conn.close()