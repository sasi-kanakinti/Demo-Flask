from flask import *
app=Flask(__name__)

@app.route('/login', methods = ['POST'])
def login():
    uname=request.form['uname']
    passw=request.form['pass']
    if uname=='asi' and passw=='111':
        return "Welcome back %s" %uname
    else:
        return 'Invalid %s'%uname

if __name__=="__main__":
    app.run(debug=True) 