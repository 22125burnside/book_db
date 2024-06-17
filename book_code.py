# Database for my books. Made by Emma Cox on 17-05-2024

import sqlite3

# database variable
DATABASE = 'books.db'

first_run = True


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
----------------------------------------------------------------------------------------------------------------------------------
Book Name                                         Pages     Rating    Type           Genre                    Author
----------------------------------------------------------------------------------------------------------------------------------""")
    for book in results:
        print(f"{book[0]:<50}{book[1]:<10}{book[2]:<10}{book[3]:<15}{book[4]:<25}{book[5]:<20}")
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
----------------------------------------------------------------------------------------------------------------------------------
Book Name                                         Pages     Rating    Type           Genre                    Author
----------------------------------------------------------------------------------------------------------------------------------""")
    for book in results:
        print(f"{book[0]:<50}{book[1]:<10}{book[2]:<10}{book[3]:<15}{book[4]:<25}{book[5]:<20}")
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
----------------------------------------------------------------------------------------------------------------------------------
Book Name                                         Pages     Rating    Type           Genre                    Author
----------------------------------------------------------------------------------------------------------------------------------""")
    for book in results:
        print(f"{book[0]:<50}{book[1]:<10}{book[2]:<10}{book[3]:<15}{book[4]:<25}{book[5]:<20}")
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
    for book in results:
        print(f"Book name: {book[0]:<30}  |  Pages: {book[1]:<5}  |  Rating: {book[2]:<5}  |  Type: {book[3]:<10}  |  Genre: {book[4]:<15}  |  Author: {book[5]}")
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
    for book in results:
        print(f"Book name: {book[0]:<40}  |  Pages: {book[1]:<5}  |  Rating: {book[2]:<5}  |  Type: {book[3]:<10}  |  Genre: {book[4]:<10}  |  Author: {book[5]}")
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
    for book in results:
        print(f"Book name: {book[0]:<42}  |  Pages: {book[1]:<5}  |  Rating: {book[2]:<5}  |  Type: {book[3]:<10}  |  Genre: {book[4]:<10}  |  Author: {book[5]}")
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
    for book in results:
        print(f"Book name: {book[0]:<32}  |  Pages: {book[1]:<5}  |  Rating: {book[2]:<5}  |  Type: {book[3]:<10}  |  Genre: {book[4]:<20}  |  Author: {book[5]}")
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
    for book in results:
        print(f"Book name: {book[0]:<35}  |  Pages: {book[1]:<5}  |  Rating: {book[2]:<5}  |  Type: {book[3]:<10}  |  Genre: {book[4]:<10}  |  Author: {book[5]}")
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
    for book in results:
        print(f"Book name: {book[0]:<30}  |  Pages: {book[1]:<5}  |  Rating: {book[2]:<5}  |  Type: {book[3]:<10}  |  Genre: {book[4]:<7}  |  Author: {book[5]}")
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
    for book in results:
        print(f"Book name: {book[0]:<35}  |  Pages: {book[1]:<5}  |  Rating: {book[2]:<5}  |  Type: {book[3]:<10}  |  Genre: {book[4]:<10}  |  Author: {book[5]}")
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
    for book in results:
        print(f"Book name: {book[0]:<35}  |  Pages: {book[1]:<5}  |  Rating: {book[2]:<5}  |  Type: {book[3]:<10}  |  Genre: {book[4]:<13}  |  Author: {book[5]}")
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
    for book in results:
        print(f"Book name: {book[0]:<20}  |  Pages: {book[1]:<5}  |  Rating: {book[2]:<5}  |  Type: {book[3]:<10}  |  Genre: {book[4]:<7}  |  Author: {book[5]}")
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
    for book in results:
        print(f"Book name: {book[0]:<37}  |  Pages: {book[1]:<5}  |  Rating: {book[2]:<5}  |  Type: {book[3]:<10}  |  Genre: {book[4]:<7}  |  Author: {book[5]}")
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
    for book in results:
        print(f"Book name: {book[0]:<20}  |  Pages: {book[1]:<5}  |  Rating: {book[2]:<5}  |  Type: {book[3]:<10}  |  Genre: {book[4]:<7}  |  Author: {book[5]}")
    db.close


# print all scifi books
def print_all_scifi():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # Put in my sql statement
    sql = """SELECT book.name, book.pages, book.rating, book.type, genre.genre_name, author.author_name
    FROM book
    JOIN genre ON book.genre_id = genre.genre_id
    JOIN author on book.author_id = author.author_id
    WHERE genre.genre_id = "12"
    ORDER BY author.author_name ASC
"""
    cursor.execute(sql)
    results = cursor.fetchall()
    # print it nicely
    for book in results:
        print(f"Book name: {book[0]:<50}  |  Pages: {book[1]:<5}  |  Rating: {book[2]:<5}  |  Type: {book[3]:<10}  |  Genre: {book[4]:<20}  |  Author: {book[5]}")
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
    for book in results:
        print(f"Book name: {book[0]:<50}  |  Pages: {book[1]:<5}  |  Rating: {book[2]:<5}  |  Type: {book[3]:<10}  |  Genre: {book[4]:<20}  |  Author: {book[5]}")
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
    for book in results:
        print(f"Book name: {book[0]:<50}  |  Pages: {book[1]:<5}  |  Rating: {book[2]:<5}  |  Type: {book[3]:<10}  |  Genre: {book[4]:<20}  |  Author: {book[5]}")
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
    for book in results:
        print(f"Book name: {book[0]:<50}  |  Pages: {book[1]:<5}  |  Rating: {book[2]:<5}  |  Type: {book[3]:<10}  |  Genre: {book[4]:<20}  |  Author: {book[5]}")
    db.close


# print all author table
def print_all_author():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # Put in my sql statement
    sql = """SELECT *
    FROM author
    ORDER BY author_id ASC
"""
    cursor.execute(sql)
    results = cursor.fetchall()
    # print it nicely
    print("""
-----------------------------------------------------
Id    Author name
-----------------------------------------------------""")
    for book in results:
        print(f"{book[0]:<6}{book[1]}")
    db.close


# Add a new data to book database :)
def add_new_data():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    book_name = input("\nBook name:\n")
    pages = int(input("\nNumber of pages:\n"))
    rating = input("\nAverage good reads rating:\n")
    book_type = input("\nKindle, Hardcover or Paperback:\n")
    authorid = add_author()
    print("""
--------------
id  genre
--------------
1   Romantasy
2   Romance
3   Fantasy
4   Historical fiction
5   Thriller
6   Mystery
7   Dystopian
8   Contemporary
9   Classic
10  Mythology
11  Horror
12  Sci Fi    """)
    genreid = int(input("\nGenre id:\n"))
    cursor.execute('INSERT INTO book (name, pages, rating, type, author_id, genre_id) VALUES (?, ?, ?, ?, ?, ?)', (book_name, pages, rating, book_type, authorid, genreid))
    db.commit()
    db.close()


# add a new author to book data (connected to add new data function code)
def add_author():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    author_ask = input("\nWhat is the authors name:\n")
    name = cursor.execute('SELECT * FROM author WHERE author_name = ?', (author_ask,)).fetchone()
    author_id = None
    if name is None:
        cursor.execute('INSERT INTO author (author_name) VALUES (?)', (author_ask,))
        db.commit()
        current_author = (cursor.lastrowid, author_ask)
        print("\nAdded a new author", current_author)
        author_id = cursor.lastrowid
    else:
        current_author = name
        author_id = name[0]
    db.commit()
    db.close()
    return author_id


# function to search a book in database
def search_book(cursor, search_term):
    query = """SELECT book.name, book.pages, book.rating, book.type, genre.genre_name, author.author_name
    FROM book
    JOIN genre ON book.genre_id = genre.genre_id
    JOIN author on book.author_id = author.author_id
    WHERE book.name
    LIKE ?"""
    # execute query and search for user input
    cursor.execute(query, ('%' + search_term + '%',))
    search = cursor.fetchall()
    return search


# Function to search for book (connected to above)
def search_for_books():
    # add try and except loop
    try:
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        # ask what they want to see and connect to code above
        search_term = input("Enter the name of the book: ")
        results = search_book(cursor, search_term)
        # print what books were found (if any)
        if results:
            print("\nBook results:")
            for book in results:
                print(f"Book name: {book[0]:<50}  |  Pages: {book[1]:<5}  |  Rating: {book[2]:<5}  |  Type: {book[3]:<10}  |  Genre: {book[4]:<20}  |  Author: {book[5]}")
        # if there is no book matching user input
        else:
            print(f'The book "{search_term}" is not in the data base')
        db.commit()
    # Check for error and print if there is one
    except sqlite3.Error as e:
        print(f"This error happened: {e}")
    # Close db
    finally:
        if db:
            db.close()


# function to search a author in database
def search_author(cursor, search_trm):
    query = """SELECT book.name, book.pages, book.rating, book.type, genre.genre_name, author.author_name
    FROM book
    JOIN genre ON book.genre_id = genre.genre_id
    JOIN author on book.author_id = author.author_id
    WHERE author.author_name
    LIKE ?
    ORDER BY book.type DESC"""
    # execute query and search for user input
    cursor.execute(query, ('%' + search_trm + '%',))
    search = cursor.fetchall()
    return search


# Function to search for author (connected to above)
def search_for_authors():
    # add try and except loop
    try:
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        # ask what they want to see and connect to code above
        search_trm = input("Enter the name of the author: ")
        results = search_author(cursor, search_trm)
        # print what books were found (if any)
        if results:
            print("\nAuthor results:")
            for book in results:
                print(f"Book name: {book[0]:<50}  |  Pages: {book[1]:<5}  |  Rating: {book[2]:<5}  |  Type: {book[3]:<10}  |  Genre: {book[4]:<20}  |  Author: {book[5]}")
        # if there is no book matching user input
        else:
            print(f"The author {search_trm} is not in the data base")
        db.commit()
    # Check for error and print if there is one
    except sqlite3.Error as e:
        print(f"This error happened: {e}")
    # Close db
    finally:
        if db:
            db.close()


# Main Code
while True:
    if not first_run:
        user_input = input("\nWould you like to countinue Y/N\n").upper()
    else:
        user_input = "Y"
        first_run = False
    if user_input == "N":
        print("Ermm..... okay then")
        break
    if user_input == "Y":
        user_input = input(
            """
What would you like to see?
----------------------------------------------------------
1. All the data
2. Show options to display all data
3. Search for a book
4. Search for an author
5. ADMIN: Add a new book into the database
6. Exit
----------------------------------------------------------
Type in the number of what you would like to see:
""")
        if user_input == "1":
            print_all_books()
        elif user_input == "2":
            user_input = input(
                """
What would you like to see?
----------------------------------------------------------
1. All the books from least to most pages
2. All the books from best to worst rating
3. Show all the genres to chose from
4. Show all the types of books to chose from
5. Show all authors
6. Back to main page
7. Exit
----------------------------------------------------------
Type in the number of what you would like to see:
""")
            if user_input == "1":
                print_all_pages()
            elif user_input == "2":
                print_all_rating()
            elif user_input == "3":
                print_all_genre()
                user_input = input("\nWhat genre would you like to see?\n")
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
                elif user_input == "12":
                    print_all_scifi()
                else:
                    print("That was not an option :(")
            elif user_input == "4":
                user_input = input("""
1. Hardcover
2. Paperback
3. Kindle
Type in the number you would like to see:
""")
                if user_input == "1":
                    print_all_hardcover()
                elif user_input == "2":
                    print_all_paperback()
                elif user_input == "3":
                    print_all_kindle()
            elif user_input == "5":
                print_all_author()
            elif user_input == "6":
                continue
            elif user_input == "7":
                break
            else:
                print("That was not an option :(")
        elif user_input == "3":
            search_for_books()
        elif user_input == "4":
            search_for_authors()
        elif user_input == "5":
            user_input = input("What is the password?\n")
            if user_input == "broke_for_books":
                add_new_data()
                print("\nData inputed\n")
            else:
                print("WRONG! Better luck next time :)")
                break
        elif user_input == "6":
            break
        else:
            print("""That was not an option :(
Pick a number:""")
    else:
        print("That was not an option pick Y/N")
