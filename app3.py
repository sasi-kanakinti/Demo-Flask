from flask import *

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('app3.html')


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)