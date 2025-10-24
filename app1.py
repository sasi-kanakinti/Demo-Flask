from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/user/<name>')
def home(name):
    return 'Hello'+name


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)