from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/<name>')
def home(name):
    return render_template('app2.html',name=name)


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)