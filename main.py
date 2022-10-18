from itertools import count
import csv
import functions

if __name__ == '__main__':
    # читаем адресную книгу в формате CSV в список contacts_list
    with open("phonebook_raw.csv", encoding="utf-8") as f:
      rows = csv.reader(f, delimiter=",")
      contacts_list = list(rows)
      
    # TODO 1: выполните пункты 1-3 ДЗ

    result_list = functions.name_correct(contacts_list)
    functions.unit_same(result_list) 
    functions.phone_correct(result_list) 


    # # TODO 2: сохраните получившиеся данные в другой файл
    # # код для записи файла в формате CSV
    with open("phonebook.csv", "w", encoding= 'utf-8' ) as f:
      datawriter = csv.writer(f, delimiter=',')
      print(result_list)
      datawriter.writerows(result_list)
  

