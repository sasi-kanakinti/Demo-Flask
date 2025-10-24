from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/admin')
def admin():
    return 'hello this is admin'

@app.route("/staff")
def staff():
    return 'Hello this is staff'

@app.route("/students")
def students():
    return 'Hello this is students'
@app.route('/user/<name>')
def user(name):
    if name =='admin':
        return redirect(url_for('admin'))
    if name =='staff':
        return redirect(url_for('staff'))
    if name =='students':
        return redirect(url_for('students'))

if __name__ == '__main__':
    app.run(port=5000,debug=True)