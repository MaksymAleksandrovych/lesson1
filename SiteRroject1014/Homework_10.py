import sqlite3
connection = sqlite3.connect("itstep_DB.sl3", 4)#оголошує підключення до БД
#cursor загальнозаведена назва для об'єкта, який безпосередньо працює з підключенням,
# передаючи й обробляючи SQL-запити та зберігаючи в собі результат їхнього виконання.
cur = connection.cursor()
print(connection)
print(cur)
connection.close() #закриття підключення
import sqlite3
connection = sqlite3.connect("itstep_DB.sl3", 3)
cur = connection.cursor()
cur.execute("CREATE TABLE first_table (name TEXT);")
print(connection)
print(cur)
connection.close()
import sqlite3
connection = sqlite3.connect("itstep_DB.sl3", 2)
cur = connection.cursor()
cur.execute("SELECT rowid, name FROM first_table;") #rowid — унікальне ID запису
connection.commit()
#Вивід інформації
res = cur.fetchall()
print(res)
connection.close()
має контекстне меню
Створити
import sqlite3
connection = sqlite3.connect("itstep_DB.sl3",5)
cur = connection.cursor()
name = input("Введіть ім'я: ")
cur.execute("INSERT INTO first_table (name) VALUES (?)", (name,))
connection.commit()
connection.close()
---------------------DELETE
import sqlite3
connection = sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()
cur.execute("DELETE FROM first_table WHERE rowid=2;")
connection.commit()
cur.execute("SELECT rowid, name FROM first_table;")
connection.commit()
res = cur.fetchall()
print(res)
connection.close()
має контекстне меню
Створити

import cv2
image_path = 'cat.jpeg'
cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(image)
print(cat_face)
cv2.imshow("Cat", image)
cv2.waitKey()