# 

def default_books(): #Intializes the list and writes 3 default books as example
  books = [
    {
      "isbn": "001",
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "genre": "Fiction, Classic",
    },
    {
      "isbn": "002",
      "title": "1984",
      "author": "George Orwell",
      "genre": "Dystopian Fiction",
    },
    {
      "isbn": "003",
      "title": "The Da Vinci Code",
      "author": "Dan Brown",
      "genre": "Mystery, Thriller",
    }
]
  return books

# def main_menu():
#   default_books()
#   book_data = default_books()
  
#   menu_options = {"1","2","3","4","5"}
#   while True:
#     value_menu = input("Options: \n1. Show all Books\n2. Add books\n3. Query Search\n4. Delete Books\n5. Export as .csv file")
#     if value_menu in menu_options:
#       if value_menu == "1":
#         show_books()

#       elif value_menu == "2":
#         add_books(book_data)

#       elif value_menu == "3":
#         query_menu()
        
#       elif value_menu == "4":
#         delete_books()

#       elif value_menu == "5":
#         export_csv(book_data, "books.csv")
#       break

#     else:
#       print("Please input a valid number between 1-5 to choose a valid option")
    
  
  


### Module 1 - Show all the items in book_data list of dictionaries ###
def show_books(book_data): 
  for item in book_data:
    print(f"ISBN: {item.get('isbn')}\n"
      f"Title: {item.get('title')}\n"
      f"Author: {item.get('author')}\n"
      f"Genre: {item.get('genre')}\n")
    print()


#Usage: show_books()



### Module 2 - Register new books in the book_data list of dictionaries ###
# Also prints the update list to verify the now changed book_data.
def add_books(book_data):
  new_book = {}
  keys = ["isbn", "title", "author", "genre"]
  
  for key in keys:
    value = input(f"Type the {key}: ")
    new_book[key] = value
  
  book_data.append(new_book)
  
  
  print("\nUpdated data:")
  show_books(book_data)

#Usage: add_books(book_data)



### Module 3 - Query menu for searches and queries of the book_data ###
# adding category map for the user choices instead of multiple functions 
# would be very good for shortening the code.

# Functions for the Query Menu, 
# gets a value which corresponds for a key in the  dictionary and then prints the items
def isbn_query(data, isbn):
  for item in data:
    if item.get('isbn') == isbn:
      print(f"ISBN: {item.get('isbn')}\n"
          f"Title: {item.get('title')}\n"
          f"Author: {item.get('author')}\n"
          f"Genre: {item.get('genre')}\n")
      print()

      return
  
  print(">>Book not found.\n")

def title_query(data, title):
  for item in data:
    if item.get('title') == title:
      print(f"ISBN: {item.get('isbn')}\n"
          f"Title: {item.get('title')}\n"
          f"Author: {item.get('author')}\n"
          f"Genre: {item.get('genre')}\n")
      print()

      return
  print("Book not found.")
  
def author_query(data, author):
  for item in data:
    if item.get('author') == author:
      print(f"ISBN: {item.get('isbn')}\n"
          f"Title: {item.get('title')}\n"
          f"Author: {item.get('author')}\n"
          f"Genre: {item.get('genre')}\n")
      print()
  
      return
  print("Book not found.")

def genre_query(data, genre):
  for item in data:
    if item.get('genre') == genre:
      print(f"ISBN: {item.get('isbn')}\n"
          f"Title: {item.get('title')}\n"
          f"Author: {item.get('author')}\n"
          f"Genre: {item.get('genre')}\n")
      print()

      return
  print("Book not found.")

def partial_query(data, partial):
  partial = partial.lower()
  for item in data:
      if any(partial in str(item.get(field, '').lower()) for field in ['title', 'author', 'genre']):
        print(f"ISBN: {item.get('isbn')}\n"
            f"Title: {item.get('title')}\n"
            f"Author: {item.get('author')}\n"
            f"Genre: {item.get('genre')}\n")
        print()

        return
  print("Book not found.")

# Actual Query Menu
# Receives an input from 1-5 and executes a function to perform a query of the
# chosen category
def query_menu(data):
  valid_options = {"1","2","3","4","5"}

  while True:
    value_cat = input("Choose the Category: \n1. ISBN\n2. Title\n3. Author\n4. Genre\n5. Partial Matches\n")    

    if value_cat in valid_options:
      if value_cat == "1":
        value_isbn = input("Type the ISBN to search for: ")
        isbn_query(data, value_isbn)
            
      elif value_cat == "2":
        value_title = input("Type the Title to search for: ")
        title_query(book_data, value_title)
      
      elif value_cat == "3":
        value_author = input("Type the Author to search for: ")
        author_query(book_data, value_author)
      
      elif value_cat == "4":
        value_genre = input("Type the Genre to search for: ")
        genre_query(book_data, value_genre)
      
      elif value_cat == "5":
        value_partial = input("Type the words to query for: ")
        partial_query(book_data, value_partial)

      break
    
    else:
      print("Please input a valid number between 1-5 to choose the category")
  
#Usage: query_menu()


### Module 4 - Delete, it deletes things. ###
# Asks for user to input the chosen category they wish to delete,
# Then asks for a value which matches the chosen category/key,
# Also prints the update list to verify the now changed book_data.
def remove_item(data, key, value):
  global book_data 
  book_data = [item for item in data if item.get(key) != value]

def delete_books(data):
  print("Current books:")
  show_books(book_data)

  key = input("Enter the category to delete by (isbn, title, author, genre): ")
  value = input(f"Enter the value for '{key}' to delete: ")

  remove_item(book_data, key, value)

  print("\nUpdated data:")
  for item in book_data:
    print(f"ISBN: {item.get('isbn')}\n"
      f"Title: {item.get('title')}\n"
      f"Author: {item.get('author')}\n"
      f"Genre: {item.get('genre')}\n")


#Usage: delete_books()

### Module 5 - Exports the book_data to a .csv archive

def export_csv(data, filename):
  headers = book_data[0].keys() if data else []
  
  with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader() 
    writer.writerows(book_data)  

#Usage: export_csv(book_data, 'books.csv')