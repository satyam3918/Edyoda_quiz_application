import sqlite3

class User():
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
    
class Admin(User):
    def __init__(self,name,age,email,emp_id,password):
        super().__init__(name,age,email)
        self.emp_id=emp_id
        self.password=password
        t=(self.emp_id,self.name,self.age,self.email,self.password)
        sql="""INSERT INTO Admins (Emp_id,Name,Age,Email,Password)
                VALUES(?,?,?,?,?)"""
        conn=sqlite3.connect('Quiz.db')
        crsr=conn.cursor()
        crsr.execute(sql,t)
        conn.commit()
        conn.close()
        
class Member(User):
      def __init__(self,name,age,email,score=0):
        super().__init__(name,age,email)
        self.score=score
        t=(self.name,self.age,self.email,self.score)
        sql="""INSERT INTO Members (Name,Age,Email,Score)
                VALUES(?,?,?,?)"""
        conn=sqlite3.connect('Quiz.db')
        crsr=conn.cursor()
        crsr.execute(sql,t)
        conn.commit()
        conn.close()  
    
   