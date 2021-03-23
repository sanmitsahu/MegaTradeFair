import mysql.connector as mysql

def connect():
	try:
		con = mysql.connect(user='root', password="", host='127.0.0.1', database='megatradefair')
		# con = mysql.connect(user='root', password="root", host='127.0.0.1', port="3307", database='megatradefair')
		status = str(con.is_connected())
		#cursor = con.cursor()
		if status == "True":
			return con
		
	except Exception as e:
		print("Connection Error : ", e)
		exit()
		