# Methods to Use
from sql import *
from User import Admin,Member
from IPython.display import clear_output
def addQuestionToDb():
    l=['Question','Option_A','Option_B','Option_C','Option_D','Corr_Ans','Level','Topic']
    t=(tuple([input(f'Enter {x}: ') for x in l]))
    print(t)
    sql="""INSERT INTO questions (Question,Option_A,Option_B,Option_C,Option_D,Corr_Ans,Level,Topic)
                    VALUES(?,?,?,?,?,?,?,?)"""
    conn=sqlite3.connect('Quiz.db')
    crsr=conn.cursor()
    crsr.execute(sql,t)
    conn.commit()
    conn.close()
    print('question has been added successfully!')

def removeQuestionFromDb(Question):
    sql="DELETE FROM questions WHERE Question=?"
    conn=sqlite3.connect('Quiz.db')
    crsr=conn.cursor()
    crsr.execute(sql,(Question,))
    conn.commit()
    conn.close()
    print('question has been removed successfully!')
    
def takeQuiz():
    Score=0
    conn=sqlite3.connect("Quiz.db")
    crsr=conn.cursor()
    crsr.execute("SELECT * FROM questions ORDER BY random() limit 5")
    result=crsr.fetchall()
    conn.close()
    for x in result:
        clear_output()
        print(f'Question:{x[0]}')
        print(f'Option 1:{x[1]}')
        print(f'Option 2:{x[2]}')
        print(f'Option 3:{x[3]}')
        print(f'Option 4:{x[4]}')
        answer=int(input('Enter the option: '))
        if answer==x[5]:
            Score+=1
    clear_output()
    for x in result:
        print(f'Question:{x[0]}')
        print(f'Correct Answer:{x[5]}')
        print(f' your score is {Score}')
    return Score

def updateScore(name,Score):
    sql="UPDATE Members SET Score=? WHERE Name=?"
    conn=sqlite3.connect("Quiz.db")
    crsr=conn.cursor()
    crsr.execute(sql,(Score,name))
    conn.commit()
    conn.close()
    return ('Score has been updated successfully!')

def displayScores():
    conn=sqlite3.connect('Quiz.db')
    crsr=conn.cursor()
    crsr.execute('select * from Members;')
    results=crsr.fetchall()
    conn.commit()
    conn.close()
    print ("{:<30} {:<30} {:<30} {:<30}".format('Name','Age','Email','Score')) 
    for x in results:
        print ("{:<30} {:<30} {:<30} {:<30}".format(x[0],x[1],x[2],x[3])) 
    print('\n')

def verifyLogin(name,password):
    sql="SELECT Password from Admins WHERE Name=?"
    conn=sqlite3.connect("Quiz.db")
    crsr=conn.cursor()
    crsr.execute(sql,(name,))
    result=crsr.fetchall()
    return result[0][0]==password
