
from IPython.display import clear_output
from Methods import addQuestionToDb,removeQuestionFromDb,takeQuiz,updateScore,displayScores,verifyLogin
from User import Admin,Member


flag=True
while flag:
    clear_output()
    print('EdYoda Quiz Application',end='\n')
    print('1. Super User\n2. User\n3. Exit')
    Cnt=int(input('Login as :'))
    
    if Cnt==1:
        login=False
        while not login:
            name=input('Name: ')
            password=input('Password: ')
            login=verifyLogin(name,password)
            if login:
                break
            clear_output()
            print('Please provide correct details')
           
            
        clear_output()
        logged_in=True
        
        while logged_in:
            Option=int(input("""Enter 1 to Add a Question:\nEnter 2 to Remove a Question:\nEnter 3 to Disply Scores of Members:\nEnter 4 to exit\n
        """))
            
            if Option==1:
                clear_output()
                addQuestionToDb()
                clear_output()
                
            elif Option==2:
                clear_output()
                Question=input('Enter the Question you want to remove ')
                removeQuestionFromDb(Question)
                clear_output()
                
            elif Option==3:
                clear_output()
                displayScores()
                clear=input('Enter 1 to go back ')
                if clear==1:
                    clear_output()
                    continue
                    
            elif Option==4:
                logged_in=False

    elif Cnt==2:
        
        print('Enter your details to take the quiz: ')
        name=input('Name: ')
        age=int(input('Age: '))
        email=input('Email: ')
        member=Member(name,age,email)
        clear_output()
        
        test=input('Enter yes to take the test ')
        while test.lower()=='yes':
            clear_output()
            Score=takeQuiz()
            updateScore(name,Score)
            test=input('Do you want to take the quiz again ')
            if test.lower()=='no':
                print('thank you for taking the quiz. ')
            
            
    else:
        flag=False
        clear_output()
        print('thanks! Visit Again. ')
