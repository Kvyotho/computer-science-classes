"""
0- sair// ->salvar no csv
VVV 1- cadastrar VVV
VVV 2- listar VVV
VVV 3- consultar (digitar alguma info e mostrar todos os dados/id) VVV
4- excluir

todas operações em formas de funcoes (todas operações chamadas por funções)
corpo do programa só vai ter o main/menu
modularizado
note: read/learn about gemini learning coach
"""

import csv 

from module import starting_list, show_books, add_books, query_menu, delete_books, export_csv

filename = 'books.csv'
book_data = starting_list(filename)

def main_menu():
  global book_data
  menu_options = {"1","2","3","4","5"}
  
  while True:
    value_menu = input(">>Menu Options: \n1. Show all Books\n2. Add books\n3. Query Search\n4. Delete Books\n5. Export as .csv file and exit program\n")
    if value_menu in menu_options:
      if value_menu == "1":
        show_books(book_data)
        
      
      elif value_menu == "2":
       book_data = add_books(book_data)
       
      
      elif value_menu == "3":
        query_menu(book_data)
        
      
      elif value_menu == "4":
        book_data = delete_books(book_data)
        

      elif value_menu == "5":
        export_csv(book_data, filename)
        print("\n>>The .csv file was successfully exported! Exiting the program.")
        break

    else:
      print(">>Please input a number between 1-5 to choose a valid option")

main_menu()
