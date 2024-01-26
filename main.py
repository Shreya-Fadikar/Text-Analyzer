from flask import Flask, render_template,request

app=Flask(__name__)
@app.get("/")
def showpage():
    return render_template('index.html')
@app.post('/analyze')
def analyze():
    text = request.form['text']
    action=request.form['action']
    answer=""
    if(action == "cntchr"):
        answer=f"the number of characters are:- {len(text)}"
    if(action == "cntws"):
        answer=f"the number of white spaces are:- {text.count(' ')}"
    if(action == "up"):
        answer=f" String Upper Case are:- {text.upper()}"
    if(action == "lw"):
        answer= f"Strinf in lower case are:-{text.lower()}"
    if(action == "strp"):
        answer =f"Stripped String:- {text.strip()}"
    if(action =="rstrip"):
        answer=f"Stripped String from right:- {text.rstrip()}"
    if(action =="lstrip"):
        answer=f"Stripped String from left:- {text.lstrip()}"
    if(action =="split"):
        answer=f"splited string are:- {text.split()}"
    if(action =="cap"):
        answer=f"Capitalise  string:- {text.capitalize()}"
    if(action== "ian"):
        answer=f"isalnum:- {text.isalnum()}"
    if(action =="isalp"):
        answer=f"Is alphabet:- {text.isalpha()}"
    if(action =="islw"):
        answer=f"Is String is lowercase:-{text.islower()}"  
    if(action =="isup"):
        answer=f"Is String is uppercase:-{text.isupper()}" 
    if(action =="swap"):
        answer=f"Swap the Case:-{text.swapcase()}" 
    
    
    return render_template('index.html', output= answer)

app.run(debug=True)