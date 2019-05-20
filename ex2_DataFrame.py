import pandas as pd
#
# users.to_excel(r'C:\Users\student1\proiect_utilizatori\Utilizatori.xlsx')
#
# print("Media number_of_login", users['number_of_login'].mean())
# print('\n', '--------------------')
# print("Standard deviation number_of_login", users['number_of_login'].std())

print('\n', '--------------------')
import sqlite3

with sqlite3.connect('db.sqlite3') as conn:
    utilizatori = pd.read_sql_query("SELECT * from Users", conn)
print(utilizatori)

utilizatori = utilizatori.set_index('id')
print(utilizatori)

utilizatori['full_name'] = utilizatori['first_name']+' '+utilizatori['last_name']
print(utilizatori)

utilizatori.to_excel(r'C:\Users\student1\proiect_utilizatori\Utilizatori_Nou.xlsx')
print('\n', '--------------------')
print("Media number_of_login", utilizatori['number_of_login'].mean())
print('\n', '--------------------')
print("Standard deviation number_of_login", utilizatori['number_of_login'].std())