import psycopg2

conn = psycopg2.connect(database="postgres", host="localhost", port="5432", user="postgres", password="Zhasulan00")
cursor = conn.cursor()


def create_db():
    command = """
    CREATE TABLE IF NOT EXISTS Contacts (
        id SERIAL PRIMARY KEY,
        name varchar(50) NOT NULL,
        surname varchar(50),
        number varchar(20) NOT NULL
    );
    """
    cursor.execute(command)
    conn.commit()


def insert(name, surname, number):
    if not name or not number.isnumeric():
        return
    command = f"""
    INSERT INTO Contacts (name, surname, number) 
    VALUES ('{name}', '{surname}', '{number}');
    """
    if not surname:
        command = f"""
        INSERT INTO Contacts (name, number) 
        VALUES ('{name}', '{number}');
        """
    cursor.execute(command)
    conn.commit()


def upload_from_csv():
    import csv
    with open('contacts.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            insert(row['name'], row['surname'], row['number'])


def enter_from_concole():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    number = input("Enter phone number: ")
    insert(name, surname, number)


def update_name(id, new_name):
    command = f"""
    UPDATE Contacts 
    SET name = '{new_name}'
    WHERE id = {id};
    """
    cursor.execute(command)
    conn.commit()


def update_number(id, new_number):
    command = f"""
    UPDATE Contacts 
    SET number = '{new_number}'
    WHERE id = {id};
    """
    cursor.execute(command)
    conn.commit()


def query_by_prefix(prefix):
    command = f"""
        SELECT * 
        FROM Contacts 
        
        WHERE name ILIKE '{prefix}%';
    """
    cursor.execute(command)
    conn.commit()

    for row in cursor.fetchall():
        print(row)


def delete_by_name(name):
    command = f"""
            DELETE FROM Contacts 
            WHERE name = '{name}';
        """
    cursor.execute(command)
    conn.commit()

#create_db()
#upload_from_csv()
#enter_from_concole()
#update_number(5,"MmMMm")
#update_number(5,"98765")
#query_by_prefix("A")
#delete_by_name("Ab")

conn.close()