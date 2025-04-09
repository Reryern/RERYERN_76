# A program to show the name and age, residence and occupation and next of kin on a web page using the flask framework

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():

    name = "Mina"
    age = 25
    residence = "Kisumu"
    occupation = "Software Developer"
    next_of_kin = "John"

    return render_template('index.html', name=name, age=age, residence=residence, occupation=occupation, next_of_kin=next_of_kin)

if __name__ == '__main__':

    app.run(debug=True)

# End of program

@app.route('/about')
def about():
    return render_template('about.html')
