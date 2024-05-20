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
    ORDER BY book.id ASC"""
    cursor.execute(sql)
    results = cursor.fetchall()
    # print it nicely
    print("Book Name                                         Pages     Rating    Type           Genre               Author")
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
    print("Book Name                                         Pages     Rating    Type           Genre               Author")
    for book in results:
        print(f"{book[0]:<50}{book[1]:<10}{book[2]:<10}{book[3]:<15}{book[4]:<20}{book[5]:<20}")
    db.close


# print all data from all by rating (worst to best)
def print_all_rating():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # Put in my sql statement
    sql = """SELECT book.name, book.pages, book.rating, book.type, genre.genre_name, author.author_name
    FROM book
    JOIN genre ON book.genre_id = genre.genre_id
    JOIN author on book.author_id = author.author_id
    ORDER BY book.rating ASC
"""
    cursor.execute(sql)
    results = cursor.fetchall()
    # print it nicely
    print("Book Name                                         Pages     Rating    Type           Genre               Author")
    for book in results:
        print(f"{book[0]:<50}{book[1]:<10}{book[2]:<10}{book[3]:<15}{book[4]:<20}{book[5]:<20}")
    db.close


# Main Code
while True:
    user_input = input(
        """
What would you like to see?
1. All the data
2. All the books from least to most pages
3. All the books from best to worst rating
""")
    if user_input == "1":
        print_all_books()
    elif user_input == "2":
        print_all_pages()
    elif user_input == "3":
        print_all_rating()
