import sqlite3

conn = sqlite3.connect(r'D:/tg_bot/UserBot/orders.db', check_same_thread=False)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid TEXT,
   userActive INT,
   userActiveS INT);
""")
conn.commit()

def register_user(id):
	data = (str(id), 1, 0)
	# cur.execute("SELECT * FROM users WHERE userActive = 1")
	# result = cur.fetchone()

	cur.execute("SELECT * FROM users WHERE userid ="+str(id))
	result = cur.fetchone()
	# print('re2', result2)
	# cur.execute("SELECT * FROM users WHERE userActiveS = 1")
	# result2 = cur.fetchone()
	print(result)

	if result == None:
		cur.execute("INSERT INTO users VALUES(?, ?, ?)", data)
		conn.commit()
		print('Пользователь создан!')
		result = 'None'
		return result
	else:
		if result[2] == 0:
			cur.execute("UPDATE users SET userActiveS =+ 1")
			conn.commit()
			result = 'second'
			return result
		elif result[2] == 1:
			cur.execute("UPDATE users SET userActiveS =+ 2")
			conn.commit()
			result = 'third'
			return result

# def info_user(id):
# 	cur.execute("SELECT AllSendMessage, AllJoinMessage  FROM users")
# 	result = cur.fetchone()
# 	print('user_bank -- ',result)
# 	return result

# def send_message()