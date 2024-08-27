# Удалите из базы данных not_telegram.db запись с id = 6.
# Подсчитать общее количество записей.
# Посчитать сумму всех балансов.
# Вывести в консоль средний баланс всех пользователя.



import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users(email)')


for i in range(1,11):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)", (f'User{i}', f'example{i}@gmail.com', f'{i*10}', '1000'))

for i in range(1,11,2):
    cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f'User{i}'))


for i in range(1,11,3):
    cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{i}",))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))

users = cursor.fetchall()
for user in users:
    print(user)

cursor.execute("DELETE FROM Users WHERE id = ?", (6,)) #Удаление пользователя с id=6

cursor.execute("SELECT COUNT(*) FROM Users")
total = cursor.fetchone()[0]
print(f'Общее количество записей:  {total}')

cursor.execute("SELECT SUM(balance) FROM Users")
sum_balance = cursor.fetchone()[0]
print(f'Сумма всех балансов: {sum_balance}')

cursor.execute("SELECT AVG(balance) FROM Users")
avg_balance = cursor.fetchone()[0]
print(f'Средний баланс пользователей: {avg_balance} ')


connection.commit()
connection.close()