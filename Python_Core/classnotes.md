**## 03/24/2024**
Boiler plate code

- Class is blueprint
  - Class has variable and actions and method
  - set () >>>>>> Construct
- Object >>>>> set help construct to build object
  - set([])
- Funtion --- is a set of statement that take input and do some specific computation and produces output
  - def greet_user():
  - """Display a simple greeting."""
  - print("Hello!")
  - greet_user()
  
- Break - exist of the loop
- Contuine - skip next code and start of beginning
- If
- For loop
- While loop
- Arthematic operators + - * / // % Modules% (retuns the remainder of the division operation) ** (raise the first operand to the second)
- Comparision operators == (equal to) ! = (not equal to) < > >= <=
- Logical operators--- 
  - AND and (true if both operand are True), 
  - NOT not (True if operand is false)
- Assignement Oprator Assignment = addition assignement += subtraction assignement - = division assignement
  - enumerate() is build in function that allows to iterate over a sequence while keeping track of the index of each item - example 
    - 101 virginia 
    - 102 new jersey 
    - 103 north carolina 
    - 104 california

- Collection - List is the collection which store and reterive data and used in square bracket
    - Store different data type - int, float, char, varchar
    - Manuplating 
    - Keep similar items together that make - Easy to accessbile and finding things
      - Organize color or size
      - Sort item
      - More efficiency
      - Trouble shoot
      - Add or Change/modify (mutable items)
  - List
    - append
    - extend
    - insert
    - delete - will delete whole object
    - remove 
    - pop
    - sort
    - temp sort
    - reversed order
    - copy()
      - shallow copy - original list + copy (mutable) list
      - Deep copy - copy will not impact original list
    - list() constructor
    - slicing () copy small list of items
    - Remove + copy
    - clear funtion - clear() - will remove or delete items from the list
  
**## 04/07/2024**
- List>>>>Ordered colletion of items
  - []
- Set>>>>Unorderd collections of items
  - Set will not allow duplicate and are unique
  - {}
  - 
- Convert List to Set>>>>use construct 
- List >>>> append()
- Set >>>> add()
- Inner join
  - will print which are common
  - 1 2 3 3 4 5
  - Output >>>> 3
- outer join
  - will print all items but not duplicate
  - 1 2 3 3 4 5
  - Output >>>> 1 2 3 4 5
- SET >>>> ADD, Remove, UPDATE
-Inner Join >>>> with operator >>>> & (apersend) >>>>>>>>>will list are items which are comman
-Outer Join >>> with operator >>>>> | (pipe) >>>>> will list all items but not duplicate
-difference method >>>> will return new set containing elements that are present in first set but not in th second set
-symetric difference = retuns a new set that contains elements that are in either of the set but not in the intersection
-gotchas #output >>>> will cause an error as can't mix in list
- Dictonary
  - dictionaries allow you to store and reterive data using key value pairs
  - unordered
  - key have to be unique
  - can store different data types
  - using {}
  - Get method >>>> help to reterive values
  - dictionary inside a dictionary
  - list of values
-Tuple
  - Tuple similar to list 
  - Tuple can't be modified and are immutable - once they are created their elements can't be modified
  - using paranthesis ()
-Funtion 
    - Function is a block of reusable code - does a specific task
    - Organize code into logical units - easy to read, manage and understand
    - def key work >>>> funtion_name ():
    - Funtion can accept parameters
    - Function can also return values
    - Function can set default values
    - (*args = positional args)
    - double args **kwargs = keyword args = takes the keyword and the values

**## 04/14/2024**
-Variable are 4 types
  Local Scope - Defined inside function
  Enclosing Scope - nested function
  Global Scope - Defined outside
  Built in Scope
-Exception Handelling
  with try - NOT to break code and display message
  different exception to handle
-Error Handelling

****## 04/21/2024**
serv.py
-Start/Create Server
-Stop Server
-Shutdown Server
Host Localhost
Port # 8080 or 8001
localhost:8000
127.0.0.1:8000
http://localhost:8000/index.html
In index.hmtl copy embedded link:
<div class='tableauPlaceholder' id='viz1714327703210' style='position: relative'><noscript><a href='#'><img alt='12. Yearly Happiness Score Changes ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wo&#47;WorldHappiness_16003108197090&#47;12_YearlyHappinessScoreChanges&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='WorldHappiness_16003108197090&#47;12_YearlyHappinessScoreChanges' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wo&#47;WorldHappiness_16003108197090&#47;12_YearlyHappinessScoreChanges&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1714327703210');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>

****## 04/28/2024**
Python object-oriented programming.

Class: This is like the blueprint or the instruction manual for creating a
block. It defines what the block should look like and what it can do. In
Python, a class might look like this:

Class is blueprint....eg working on puzzle or playing with set of building blocks
Each block should look like and what it can do and help to build object.

class Block:
def __init__(self, color, size): (use dundder)
 self.color = color (self.color is attribute and color is parameter)
 self.size = size

Object: This is an instance of a class. When you follow the blueprint to
create a block, the block you create is an object. In Python, you might
create an object like this:
• my_block = Block("red", "large")

****## 05/05/2024**
SQL Lite database
Run following from visual studio:
Install SQL Lite viewer
Create and run file>>13_db>>>01_UsingSQLLite.py
View table 
View Table rows and colums

****## 05/19/2024** build window application
tKinter is the standard GUI library for python
tKinter allows to create dialogs - - windows Desk Top application
Create the application
widgets - button, labels....
pack the widgets to the window
start the application
Boiler plate code