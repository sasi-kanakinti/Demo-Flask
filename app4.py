from flask import *
app=Flask(__name__)

@app.route('/login', methods = ['GET'])
def login():
    uname=request.args.get('uname')
    passw=request.args.get('pass')
    if uname=='asi' and passw=='111':
        return "Welcome back %s" %uname
    else:
        return 'Invalid %s'%uname

if __name__=="__main__":
    app.run(debug=True) 