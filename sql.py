import sqlite3
from IPython.display import clear_output
""" connection=sqlite3.connect("Quiz.db")

sql_cmd=\"""CREATE TABLE questions(
        Question VARCHAR(50),
        Option_A  VARCHAR(20),
        Option_B  VARCHAR(20),
        Option_C  VARCHAR(20),
        Option_D  VARCHAR(20),
        Corr_Ans  INTEGER,
        Level     VARCHAR(20),
        Topic     VARCHAR(20))\"""
crsr=connection.cursor()

crsr.execute(sql_cmd)
connection.commit()
connection.close() """

# crsr.execute('select * from questions')
# ans=crsr.fetchall()

# print(ans)

# connection.close()

#Add some questions

""" questions=[
           ('What is part of a database that holds only one type of information?','Report','Field','Record','File',2,'medium','Computer Science'),
           ('OS computer abbreviation usually means ?','Order of Significance','Open Software','Operating System','Optical Sensor',3,'medium','Computer Science'),]
sql=\"""INSERT INTO questions (Question,Option_A,Option_B,Option_C,Option_D,Corr_Ans,Level,Topic)
                 VALUES(?,?,?,?,?,?,?,?)\"""
conn=sqlite3.connect('Quiz.db')
crsr=conn.cursor()
crsr.executemany(sql,questions)
crsr.execute("SELECT * FROM questions")
result=crsr.fetchall()
for x in result:
    print(x)
conn.commit()
conn.close() """

""" conn=sqlite3.connect("Quiz.db")
cur=conn.cursor()
cur.execute("DROP TABLE questions")
conn.commit()
conn.close()
 """
""" conn=sqlite3.connect('Quiz.db')
crsr=conn.cursor()
crsr.execute(\"""CREATE TABLE Admins(
            Emp_id INTEGER PRIMARY KEY,
            Name  VARCHAR(30),
            Age  INTEGER,
            Email VARCHAR(30),
            Password VARCHAR(20))
             \""")

crsr.fetchall()
conn.commit()
conn.close() """

""" conn=sqlite3.connect('Quiz.db')
crsr=conn.cursor()
crsr.execute(\"""CREATE TABLE Members(
            Name  VARCHAR(30),
            Age  INTEGER,
            Email VARCHAR(30),
            Score INTEGER DEFAULT 0)
              \""")

crsr.fetchall()
conn.commit()
conn.close() """

""" conn=sqlite3.connect("Quiz.db")
cur=conn.cursor()
cur.execute("DROP TABLE Admins")
conn.commit()
conn.close() """
