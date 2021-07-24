from pywebio.input import *
from pywebio.output import *
from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH

app=Flask(__name__)

def exam():
    c=0
    
    name=input("Enter your name:",type="text")
    
    a1=radio("Which language is an interpreted high level programming language?",["Python","HTML","JAVA","C++"])
    if a1=="Python":
        c+=1
    
    a2=radio("Assembly language is used in which generation?",["1st generation","2nd generation","3rd generation","4th generation"])
    if a2=="2nd generation":
        c+=1
    
    a3=radio("JAVA is an object oriented programming language?",["True","False"])
    if a3=="True":
        c+=1

    a4=radio("Which module is used for windows & frames in Python language?",["Turtle","Pandas","Tkinter","Numpy"])
    if a4=="Tkinter":
        c+=1

    a5=radio("Which type of file is used for create a webpage?",["Python file","HTML file","C file","JAVA file"])
    if a5=="HTML file":
        c+=1

    if c>3:
        put_text(name ,"your score is ",str(c))
        style(put_text("Result:Pass"),"color:green")
    else:
        put_text(name ,"your score is ",str(c))
        style(put_text("Result:Fail"),"color:red")
        
    put_text("Thanks for your participation")

app.add_url_rule("/","webioview",webio_view(exam),methods=["GET","POST","OPTIONS"])

app.run(host="localhost",port=5000)

exam()
