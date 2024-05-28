# Database for my books. Made by Emma Cox on 17-05-2024

import sqlite3

# database variable
DATABASE = 'books.db'


# print all data from all tables excluding ids
def print_all_books():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # Put in my sql statement
    sql = """SELECT book.name, book.pages, book.rating, book.type, genre.genre_name, author.author_name
    FROM book
    JOIN genre ON book.genre_id = genre.genre_id
    JOIN author on book.author_id = author.author_id
    ORDER BY author.author_name ASC"""
    cursor.execute(sql)
    results = cursor.fetchall()
    # print it nicely
    print("""
-----------------------------------------------------------------------------------------------------------------------
Book Name                                         Pages     Rating    Type           Genre               Author
-----------------------------------------------------------------------------------------------------------------------""")
    for book in results:
        print(f"{book[0]:<50}{book[1]:<10}{book[2]:<10}{book[3]:<15}{book[4]:<20}{book[5]:<20}")
    db.close


# print all data from all tables and order it by pages (least to most)
def print_all_pages():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # Put in my sql statement
    sql = """SELECT book.name, book.pages, book.rating, book.type, genre.genre_name, author.author_name
    FROM book
    JOIN genre ON book.genre_id = genre.genre_id
    JOIN author on book.author_id = author.author_id
    ORDER BY book.pages ASC"""
    cursor.execute(sql)
    results = cursor.fetchall()
    # print it nicely
    print("""
-----------------------------------------------------------------------------------------------------------------------
Book Name                                         Pages     Rating    Type           Genre               Author
-----------------------------------------------------------------------------------------------------------------------""")
    for book in results:
        print(f"{book[0]:<50}{book[1]:<10}{book[2]:<10}{book[3]:<15}{book[4]:<20}{book[5]:<20}")
    db.close


# print all data from all by rating (best to worse)
def print_all_rating():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # Put in my sql statement
    sql = """SELECT book.name, book.pages, book.rating, book.type, genre.genre_name, author.author_name
    FROM book
    JOIN genre ON book.genre_id = genre.genre_id
    JOIN author on book.author_id = author.author_id
    ORDER BY book.rating DESC
"""
    cursor.execute(sql)
    results = cursor.fetchall()
    # print it nicely
    print("""
-----------------------------------------------------------------------------------------------------------------------
Book Name                                         Pages     Rating    Type           Genre               Author
-----------------------------------------------------------------------------------------------------------------------""")
    for book in results:
        print(f"{book[0]:<50}{book[1]:<10}{book[2]:<10}{book[3]:<15}{book[4]:<20}{book[5]:<20}")
    db.close


# print all the genres to chose from
def print_all_genre():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # Put in my sql statement
    sql = """SELECT *
    FROM genre
"""
    cursor.execute(sql)
    results = cursor.fetchall()
    # print it nicely
    print("""
--------------
id    genre
--------------""")
    for book in results:
        print(f"{book[0]:<6}{book[1]:<10}")
    db.close


# print all romantasy books
def print_all_romantasy():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # Put in my sql statement
    sql = """SELECT book.name, book.pages, book.rating, book.type, genre.genre_name, author.author_name
    FROM book
    JOIN genre ON book.genre_id = genre.genre_id
    JOIN author on book.author_id = author.author_id
    WHERE genre.genre_id = "1"
    ORDER BY author.author_name ASC
"""
    cursor.execute(sql)
    results = cursor.fetchall()
    # print it nicely
    print("""
-----------------------------------------------------------------------------------------------------------------------
Book Name                                         Pages     Rating    Type           Genre               Author
-----------------------------------------------------------------------------------------------------------------------""")
    for book in results:
        print(f"{book[0]:<32}{book[1]:<10}{book[2]:<10}{book[3]:<15}{book[4]:<15}{book[5]}")
    db.close


# print all romance books
def print_all_romance():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # Put in my sql statement
    sql = """SELECT book.name, book.pages, book.rating, book.type, genre.genre_name, author.author_name
    FROM book
    JOIN genre ON book.genre_id = genre.genre_id
    JOIN author on book.author_id = author.author_id
    WHERE genre.genre_id = "2"
    ORDER BY author.author_name ASC
"""
    cursor.execute(sql)
    results = cursor.fetchall()
    # print it nicely
    print("""
-----------------------------------------------------------------------------------------------------------------------
Book Name                                         Pages     Rating    Type           Genre               Author
-----------------------------------------------------------------------------------------------------------------------""")
    for book in results:
        print(f"{book[0]:<45}{book[1]:<10}{book[2]:<10}{book[3]:<15}{book[4]:<20}{book[5]:<20}")
    db.close


# print all fantasy books
def print_all_fantasy():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # Put in my sql statement
    sql = """SELECT book.name, book.pages, book.rating, book.type, genre.genre_name, author.author_name
    FROM book
    JOIN genre ON book.genre_id = genre.genre_id
    JOIN author on book.author_id = author.author_id
    WHERE genre.genre_id = "3"
    ORDER BY author.author_name ASC
"""
    cursor.execute(sql)
    results = cursor.fetchall()
    # print it nicely
    print("""
-----------------------------------------------------------------------------------------------------------------------
Book Name                                         Pages     Rating    Type           Genre               Author
-----------------------------------------------------------------------------------------------------------------------""")
    for book in results:
        print(f"{book[0]:<45}{book[1]:<10}{book[2]:<10}{book[3]:<15}{book[4]:<20}{book[5]:<20}")
    db.close


# print all historical fiction books
def print_all_history():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # Put in my sql statement
    sql = """SELECT book.name, book.pages, book.rating, book.type, genre.genre_name, author.author_name
    FROM book
    JOIN genre ON book.genre_id = genre.genre_id
    JOIN author on book.author_id = author.author_id
    WHERE genre.genre_id = "4"
    ORDER BY author.author_name ASC
"""
    cursor.execute(sql)
    results = cursor.fetchall()
    # print it nicely
    print("""
-----------------------------------------------------------------------------------------------------------------------
Book Name                                         Pages     Rating    Type           Genre               Author
-----------------------------------------------------------------------------------------------------------------------""")
    for book in results:
        print(f"{book[0]:<45}{book[1]:<10}{book[2]:<10}{book[3]:<15}{book[4]:<20}{book[5]:<20}")
    db.close


# print all thriller books
def print_all_thriller():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # Put in my sql statement
    sql = """SELECT book.name, book.pages, book.rating, book.type, genre.genre_name, author.author_name
    FROM book
    JOIN genre ON book.genre_id = genre.genre_id
    JOIN author on book.author_id = author.author_id
    WHERE genre.genre_id = "5"
    ORDER BY author.author_name ASC
"""
    cursor.execute(sql)
    results = cursor.fetchall()
    # print it nicely
    print("""
-----------------------------------------------------------------------------------------------------------------------
Book Name                                         Pages     Rating    Type           Genre               Author
-----------------------------------------------------------------------------------------------------------------------""")
    for book in results:
        print(f"{book[0]:<45}{book[1]:<10}{book[2]:<10}{book[3]:<15}{book[4]:<20}{book[5]:<20}")
    db.close


# print all mystery books
def print_all_mystery():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # Put in my sql statement
    sql = """SELECT book.name, book.pages, book.rating, book.type, genre.genre_name, author.author_name
    FROM book
    JOIN genre ON book.genre_id = genre.genre_id
    JOIN author on book.author_id = author.author_id
    WHERE genre.genre_id = "6"
    ORDER BY author.author_name ASC
"""
    cursor.execute(sql)
    results = cursor.fetchall()
    # print it nicely
    print("""
-----------------------------------------------------------------------------------------------------------------------
Book Name                                         Pages     Rating    Type           Genre               Author
-----------------------------------------------------------------------------------------------------------------------""")
    for book in results:
        print(f"{book[0]:<45}{book[1]:<10}{book[2]:<10}{book[3]:<15}{book[4]:<20}{book[5]:<20}")
    db.close


# print all dystiopian books
def print_all_dystopian():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # Put in my sql statement
    sql = """SELECT book.name, book.pages, book.rating, book.type, genre.genre_name, author.author_name
    FROM book
    JOIN genre ON book.genre_id = genre.genre_id
    JOIN author on book.author_id = author.author_id
    WHERE genre.genre_id = "7"
    ORDER BY author.author_name ASC
"""
    cursor.execute(sql)
    results = cursor.fetchall()
    # print it nicely
    print("""
-----------------------------------------------------------------------------------------------------------------------
Book Name                                         Pages     Rating    Type           Genre               Author
-----------------------------------------------------------------------------------------------------------------------""")
    for book in results:
        print(f"{book[0]:<45}{book[1]:<10}{book[2]:<10}{book[3]:<15}{book[4]:<20}{book[5]:<20}")
    db.close


# print all contemporary books
def print_all_contemporary():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # Put in my sql statement
    sql = """SELECT book.name, book.pages, book.rating, book.type, genre.genre_name, author.author_name
    FROM book
    JOIN genre ON book.genre_id = genre.genre_id
    JOIN author on book.author_id = author.author_id
    WHERE genre.genre_id = "8"
    ORDER BY author.author_name ASC
"""
    cursor.execute(sql)
    results = cursor.fetchall()
    # print it nicely
    print("""
-----------------------------------------------------------------------------------------------------------------------
Book Name                                         Pages     Rating    Type           Genre               Author
-----------------------------------------------------------------------------------------------------------------------""")
    for book in results:
        print(f"{book[0]:<45}{book[1]:<10}{book[2]:<10}{book[3]:<15}{book[4]:<20}{book[5]:<20}")
    db.close


# print all classic books
def print_all_classic():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # Put in my sql statement
    sql = """SELECT book.name, book.pages, book.rating, book.type, genre.genre_name, author.author_name
    FROM book
    JOIN genre ON book.genre_id = genre.genre_id
    JOIN author on book.author_id = author.author_id
    WHERE genre.genre_id = "9"
    ORDER BY author.author_name ASC
"""
    cursor.execute(sql)
    results = cursor.fetchall()
    # print it nicely
    print("""
-----------------------------------------------------------------------------------------------------------------------
Book Name                                         Pages     Rating    Type           Genre               Author
-----------------------------------------------------------------------------------------------------------------------""")
    for book in results:
        print(f"{book[0]:<45}{book[1]:<10}{book[2]:<10}{book[3]:<15}{book[4]:<20}{book[5]:<20}")
    db.close


# print all mythology books
def print_all_mythology():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # Put in my sql statement
    sql = """SELECT book.name, book.pages, book.rating, book.type, genre.genre_name, author.author_name
    FROM book
    JOIN genre ON book.genre_id = genre.genre_id
    JOIN author on book.author_id = author.author_id
    WHERE genre.genre_id = "10"
    ORDER BY author.author_name ASC
"""
    cursor.execute(sql)
    results = cursor.fetchall()
    # print it nicely
    print("""
-----------------------------------------------------------------------------------------------------------------------
Book Name                                         Pages     Rating    Type           Genre               Author
-----------------------------------------------------------------------------------------------------------------------""")
    for book in results:
        print(f"{book[0]:<45}{book[1]:<10}{book[2]:<10}{book[3]:<15}{book[4]:<20}{book[5]:<20}")
    db.close


# print all horror books
def print_all_horror():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # Put in my sql statement
    sql = """SELECT book.name, book.pages, book.rating, book.type, genre.genre_name, author.author_name
    FROM book
    JOIN genre ON book.genre_id = genre.genre_id
    JOIN author on book.author_id = author.author_id
    WHERE genre.genre_id = "11"
    ORDER BY author.author_name ASC
"""
    cursor.execute(sql)
    results = cursor.fetchall()
    # print it nicely
    print("""
-----------------------------------------------------------------------------------------------------------------------
Book Name                                         Pages     Rating    Type           Genre               Author
-----------------------------------------------------------------------------------------------------------------------""")
    for book in results:
        print(f"{book[0]:<45}{book[1]:<10}{book[2]:<10}{book[3]:<15}{book[4]:<20}{book[5]:<20}")
    db.close


# print all hardcover books
def print_all_hardcover():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # Put in my sql statement
    sql = """SELECT book.name, book.pages, book.rating, book.type, genre.genre_name, author.author_name
    FROM book
    JOIN genre ON book.genre_id = genre.genre_id
    JOIN author on book.author_id = author.author_id
    WHERE book.type = "Hardcover"
    ORDER BY author.author_name ASC
"""
    cursor.execute(sql)
    results = cursor.fetchall()
    # print it nicely
    print("""
-----------------------------------------------------------------------------------------------------------------------
Book Name                                         Pages     Rating    Type           Genre               Author
-----------------------------------------------------------------------------------------------------------------------""")
    for book in results:
        print(f"{book[0]:<45}{book[1]:<10}{book[2]:<10}{book[3]:<15}{book[4]:<20}{book[5]:<20}")
    db.close


# print all Paperback books
def print_all_paperback():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # Put in my sql statement
    sql = """SELECT book.name, book.pages, book.rating, book.type, genre.genre_name, author.author_name
    FROM book
    JOIN genre ON book.genre_id = genre.genre_id
    JOIN author on book.author_id = author.author_id
    WHERE book.type = "Paperback"
    ORDER BY author.author_name ASC
"""
    cursor.execute(sql)
    results = cursor.fetchall()
    # print it nicely
    print("""
-----------------------------------------------------------------------------------------------------------------------
Book Name                                         Pages     Rating    Type           Genre               Author
-----------------------------------------------------------------------------------------------------------------------""")
    for book in results:
        print(f"{book[0]:<45}{book[1]:<10}{book[2]:<10}{book[3]:<15}{book[4]:<20}{book[5]:<20}")
    db.close


# print all Kindle books
def print_all_kindle():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # Put in my sql statement
    sql = """SELECT book.name, book.pages, book.rating, book.type, genre.genre_name, author.author_name
    FROM book
    JOIN genre ON book.genre_id = genre.genre_id
    JOIN author on book.author_id = author.author_id
    WHERE book.type = "Kindle"
    ORDER BY author.author_name ASC
"""
    cursor.execute(sql)
    results = cursor.fetchall()
    # print it nicely
    print("""
-----------------------------------------------------------------------------------------------------------------------
Book Name                                         Pages     Rating    Type           Genre               Author
-----------------------------------------------------------------------------------------------------------------------""")
    for book in results:
        print(f"{book[0]:<45}{book[1]:<10}{book[2]:<10}{book[3]:<15}{book[4]:<20}{book[5]:<20}")
    db.close


# Main Code
while True:
    user_input = input(
        """
What would you like to see?
----------------------------------------------------------
1. All the data
2. All the books from least to most pages
3. All the books from best to worst rating
4. Show all the genres to chose from
5. Show all the types of books to chose from
6. Add a new book into the database
7. Exit
----------------------------------------------------------
Type in the number of what you would like to see:
""")
    if user_input == "1":
        print_all_books()
    elif user_input == "2":
        print_all_pages()
    elif user_input == "3":
        print_all_rating()
    elif user_input == "4":
        print_all_genre()
        user_input = input("What genre would you like to see?\n")
        if user_input == "1":
            print_all_romantasy()
        elif user_input == "2":
            print_all_romance()
        elif user_input == "3":
            print_all_fantasy()
        elif user_input == "4":
            print_all_history()
        elif user_input == "5":
            print_all_thriller()
        elif user_input == "6":
            print_all_mystery()
        elif user_input == "7":
            print_all_dystopian()
        elif user_input == "8":
            print_all_contemporary()
        elif user_input == "9":
            print_all_classic()
        elif user_input == "10":
            print_all_mythology()
        elif user_input == "11":
            print_all_horror()
        else:
            print("That was not an option :(")
    elif user_input == "5":
        user_input = input("""1. Hardcover
2. Paperback
3. Kindle
""")
        if user_input == "1":
            print_all_hardcover()
        elif user_input == "2":
            print_all_paperback()
        elif user_input == "3":
            print_all_kindle()
    elif user_input == "7":
        break
