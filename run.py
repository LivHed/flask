import os
from flask import Flask, render_template  #import the flask app, and the render_template()function.

app = Flask(__name__)  #then create an instance of this and storing it in the variable app. The argument __name__ is a built in python variable.

@app.route('/')   #the @ sign, the decorator (pie notation), is a way of wrapping functions.
def index():
    return render_template("index.html")
    
@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/contact')
def contact():
    return render_template("contact.html")
    
@app.route('/careers')
def careers():
    return render_template("careers.html")

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            