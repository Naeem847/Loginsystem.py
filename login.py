users={'naeem':'1234','ali':'234','hasi':'567'}#create the Dictionary name users
def login():
 attempts=3
 while attempts>0:#this statement coomtinue the continue the input 3 > 0 times
    username=input("enter your name:\n")
    password=input("enter your password:\n")
    if username in users and users[username]==password:#if the username & password match and exists in the Dictionary 
     print("login successfully!!!")#then login successfully!!
     break#break statement break the print statement
    else:
        attempts-=1#this statement 1 decrement
        if attempts>0:
           print(f"invalid username or password you have  {attempts} more attempts please try again!!!")
        else:
           print("you have axceeded maximum time of attempts please try agian later!!!")
login()