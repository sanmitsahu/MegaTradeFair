import mysql.connector as mysql
from db_conn import connect
import table_details as td
con = connect()

def exist_db(existquery,form_values, index):
    try:
        mycursor = con.cursor()
        given_val=[]

        for i in index:
            given_val.append(form_values[i])

        given_tuple = tuple(given_val)
        
        mycursor.execute(existquery, given_tuple)
        result = mycursor.fetchall()

        return result[0][0]
        
    except Exception as ex:
        print("Error occured",ex)
        return ex

def insert_db(addquery,form_values):
    try:
        mycursor = con.cursor()

        given_val = tuple(form_values)

        mycursor.execute(addquery, given_val)
        con.commit()

        return 1
        
    except Exception as ex:
        print("Error occured",ex)
        return 0

def read_db(displayquery):
    try:
        mycursor = con.cursor()
        mycursor.execute(displayquery)
        records = mycursor.fetchall()

        return records

    except Exception as ex:
        return 0

def update_db(updatequery,form_values):
    try:
        mycursor = con.cursor()
        given_val = tuple(form_values)
        mycursor.execute(updatequery, given_val)
        con.commit()
        return 1
        
    except Exception as ex:
        print(ex)
        return 0

def disconnect():
    if con.is_connected():
        con.close()

def graph_exhibitor_industry(graph_no):
    cursor = con.cursor()
    if graph_no == 1:
        cursor.execute('''SELECT `industry`.industryname,COUNT(*) FROM `exhibitor` 
                        JOIN `industry`
                        ON `industry`.industry_id=`exhibitor`.industryid
                        GROUP BY `industryid`;''')

        rows = cursor.fetchall()
        str(rows)[0:300]
        return rows

    elif graph_no == 2:
        cursor.execute('''SELECT `industry`.industryname, sum(`booking`.totalamount)
                    FROM `industry`
                    JOIN exhibitor ON industry.industry_id = exhibitor.industryid
                    JOIN booking ON exhibitor.exhibitor_id = booking.exhibitorid
                    GROUP BY industry.industry_id;''')
        rows = cursor.fetchall()
        str(rows)[0:300]
        return rows


"""SELECT industry.industryname, count(*), sum(totalamount)
                    FROM industry
                    JOIN exhibitor ON industry.industry_id = exhibitor.industryid
                    JOIN booking ON exhibitor.exhibitor_id = booking.exhibitorid
                    GROUP BY industry.industry_id;"""