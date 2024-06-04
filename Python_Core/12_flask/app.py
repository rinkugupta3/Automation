# First step to install "pip3 install Flask"
# Flask is lightweight framework
# setter and getter

from flask import Flask, render_template, request

app = Flask(__name__)

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

#getter method
#Form going to have a name - getter method
#property decleration and to get things
#_name or _age is reffer as getter



    @property
    def name(self):
        return self._name # self refer to the instance of the class and _name is the attribute which going to store the name value

    @property
    def age(self):
        return self._age

#setter method
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value



    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise TypeError("Age must be a non negative integer")
        self._age = value



@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))

        person = Person(name,age)

        return f"Name: {person.name}, Age: {person.age}"
    return render_template('/index.html')



if __name__ =="__main__":
    app.run(debug=True)

