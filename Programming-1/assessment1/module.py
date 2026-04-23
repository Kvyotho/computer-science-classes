# 
import csv

# MODULE 1 SHOW
# MODULE 2 ADD
# MODULE 3 SEARCH
# MODULE 4 DELETE
# MODULE 5 EXPORT

def starting_list(filename):
  book_data = []
  try:
    with open(filename, mode='r', newline='',encoding='utf-8') as file:
      reader = csv.DictReader(file)
      for row in reader:
        book_data.append(row)
  
  except FileNotFoundError:
    print("No .csv file was found.\n >>Starting an empty list.")
  
  return book_data

#---------------------------------------------//---------------------------------#

### Module 1 - Show all the items in book_data list of dictionaries ###
def show_books(data): 
  print(f"\n>>The current books in the system are:\n")
  for item in data:
    print(f"ISBN: {item.get('isbn')}\n"
      f"Title: {item.get('title')}\n"
      f"Author: {item.get('author')}\n"
      f"Genre: {item.get('genre')}\n")
    print("---\n")
  

#Usage: show_books()

#---------------------------------------------//---------------------------------#

### Module 2 - Register new books in the book_data list of dictionaries ###
# Also prints the update list to verify the now changed book_data.
def add_books(data):
  new_book = {}
  keys = ["isbn", "title", "author", "genre"]
  

  while True:
      
    isbn = input(">>Type the ISBN: ")
      
    if any(book['isbn'] == isbn for book in data): #Checks if ISBN is unique
        print(">>Error: This ISBN already exists. Please enter a unique ISBN.")
        continue
       
    if isbn.isdigit(): # Checks if ISBN is valid/only numbers
        new_book["isbn"] = isbn
        break
      
    else: 
      print(">>Error: The ISBN key only allows numbers. Please input a valid value.")

  for key in keys[1:]:  # Skips the ISBN key
    while True:
      
      value = input(f"Type the {key}: ")
      
      if value:  # Checks to make sure the value isn't empty
        new_book[key] = value
        break

      else:
        print(f">>{key} Cannot be empty, please input a value.")
        value = input(f"Type the {key}: ")
      
  data.append(new_book)
  
  print("\n>>Updated data:")
  show_books(data)
  return data

#Usage: book_data = add_books(book_data)

#---------------------------------------------//---------------------------------#

### Module 3.1 - Query menu for searches and queries of the book_data ###
# Search functions of the Query Menu, 
# Utilizes the parameter from the query_menu() to checks for matches within the dictionary
# and then prints the items related to it
def isbn_query(data, isbn):
  isbn = isbn.lower()
  for item in data:
    if item.get('isbn').lower() == isbn:
      print(f"ISBN: {item.get('isbn')}\n"
          f"Title: {item.get('title')}\n"
          f"Author: {item.get('author')}\n"
          f"Genre: {item.get('genre')}\n")
      print()

      return
  print(">>Book not found.")

def title_query(data, title):
  title = title.lower()
  for item in data:
    if item.get('title').lower() == title:
      print(f"ISBN: {item.get('isbn')}\n"
          f"Title: {item.get('title')}\n"
          f"Author: {item.get('author')}\n"
          f"Genre: {item.get('genre')}\n")
      print()

      return
  print(">>Book not found.")
  
def author_query(data, author):
  author = author.lower()
  for item in data:
    if item.get('author').lower() == author:
      print(f"ISBN: {item.get('isbn')}\n"
          f"Title: {item.get('title')}\n"
          f"Author: {item.get('author')}\n"
          f"Genre: {item.get('genre')}\n")
      print()
  
      return
  print(">>Book not found.")

def genre_query(data, genre):
  genre = genre.lower()
  for item in data:
     if genre in item.get('genre', '').lower():
      print(f"ISBN: {item.get('isbn')}\n"
          f"Title: {item.get('title')}\n"
          f"Author: {item.get('author')}\n"
          f"Genre: {item.get('genre')}\n")
      print()

      return
  print(">>Book not found.")

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
  print(">>Book not found.")

### Module 3.2 - Actual Query Menu ###
# Step 1 - Receives an input from 1-5, to choose the category of the query
# Step 2 - Receives another input to determine the parameter 
# Step 3 - Calls the query fuction of chosen category, with the chosen parameter.
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
        title_query(data, value_title)
      
      elif value_cat == "3":
        value_author = input("Type the Author to search for: ")
        author_query(data, value_author)
      
      elif value_cat == "4":
        value_genre = input("Type the Genre to search for: ")
        genre_query(data, value_genre)
      
      elif value_cat == "5":
        value_partial = input("Type the words to query for: ")
        partial_query(data, value_partial)

      break
    
    else:
      print("Please input a valid number between 1-5 to choose the category")
  
# Adding category map for the user choices instead of multiple functions 
# would be very good for improving the code.

#Usage: query_menu()

#---------------------------------------------//---------------------------------#

### Module 4 - Delete, it deletes things. ###
# Asks for user to input the chosen category they wish to delete,
# Then asks for a value which matches the chosen category/key,
# Also prints the update list to verify the now changed book_data.
def remove_item(data, key, value):
  return [item for item in data if value.lower() not in item.get(key, '').lower()]

def delete_books(data):
  print("Current books:")
  show_books(data)

  key = input("Enter the category to delete by (isbn, title, author, genre): ")
  value = input(f"Enter the value for '{key}' to delete: ")

  updated_data = remove_item(data, key, value)

  if len(updated_data) == len(data):
    print(f">>No books found with {key}='{value}'. No deletions made.")
  
  else:
    print("\nUpdated data:")
    for item in updated_data:
      print(f"ISBN: {item.get('isbn')}\n"
      f"Title: {item.get('title')}\n"
      f"Author: {item.get('author')}\n"
      f"Genre: {item.get('genre')}\n")
    
  return updated_data
    


#Usage: delete_books()

#---------------------------------------------//---------------------------------#

### Module 5 - Exports the book_data to a .csv archive

def export_csv(data, filename):
  headers = data[0].keys() if data else []
  
  with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader() 
    writer.writerows(data)  

#Usage: export_csv(book_data, 'books.csv')

#---------------------------------------------//---------------------------------#


# books to populate the .csv as example
# 001,The Great Gatsby,F. Scott Fitzgerald,"Fiction, Classic"
# 002,1984,George Orwell,Dystopian Fiction
# 003,The Da Vinci Code,Dan Brown,"Mystery, Thriller"