# import mysql.connector as mc
# connect = None

# try:
#     connect = mc.connect(host="localhost", user="root", password="1234", database="practice_with_python1")
#     print("Tested Succesfully ",connect)
# except Exception as e:
#     print("Exception is : ", e)

# finally:
#     connect.close()

import pyodbc
conn =None
try:
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=AKASH\SQLEXPRESS;'
                      'Database=Personal_database;'
                      )

    cursor = conn.cursor()
    # insert=('insert into Author(AuthorName,IsDeleted) values(?,?)')
    # values = [('Akash Kumar',False),('Rahul Sharma',True),('Nitin Kumar',False)]
    # cursor.executemany(insert,values)
    # print("Inserted succesfully")
    select = cursor.execute('select * from Author')




    c=select.fetchall()
    for i in c:
        print(i)
    
    # for i in cursor:
    #     print(i)

except Exception as e:
    print("Error occurred while connecting to SQL server",e)


finally:
    conn.close()


