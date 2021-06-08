from flask import Flask, render_template, request, session
import sqlite3
import random
import urllib

app = Flask('app')
app.secret_key = '4Q8z\n\xec]/b_5#y2L"F'

@app.route('/')
def index():
  return render_template("index.html", loggedIn=isLoggedIn())

@app.route('/arrivalsDepartures')
def arrivalsDepartures():
  return render_template("arrivalsDepartures.html", loggedIn=isLoggedIn())

@app.route('/administrator')
def administrator():
  return render_template("administrator.html", loggedIn=isLoggedIn())

@app.route('/statistics')
def statistics():
  return render_template("statistics.html", loggedIn=isLoggedIn())

@app.route('/Tickets')
def Tickets():
  return render_template("tickets.html", loggedIn = isLoggedIn())

@app.route('/myTickets')
def myTickets():
  return render_template("myTickets.html", loggedIn=isLoggedIn())
  
@app.route('/manageFlights')
def manageFlights():
  return render_template("manageFlights.html", loggedIn=isLoggedIn())
  
@app.route('/manageAirports')
def manageAirports():
  return render_template("manageAirports.html", loggedIn=isLoggedIn())

@app.route('/login', methods=['POST'])
def login():
  with open("data/users.txt", "r") as file:
    data = file.readlines()
  for i in range(len(data)):
    if [request.form["email"], request.form["password"]] == [data[i].split()[0], data[i].split()[1]]:
      session['email'] = request.form["email"]
      return "Successful"
  return "Invalid login"

@app.route('/logout', methods=['POST'])
def logout():
  session.clear()
  return "Successful"

@app.route('/register', methods=['POST'])
def register():
  if request.form["password"] == "" or request.form["email"] == "":
    return ""
  if request.form["password"] == request.form["password2"]:
    with open("data/users.txt", "r") as file:
      data = file.readlines()
    for line in data:
      if request.form["email"] == line.split()[0]:
        return "Email already used"
    data.append(f'\n{request.form["email"]} {request.form["password"]}')
    with open("data/users.txt", "w") as file:
      file.writelines(data)
    return "Successful"
  return "Passwords do not match"

def isLoggedIn():
  with open("data/users.txt", "r") as file:
    data = file.readlines()
  flag = False
  for line in data:
    if 'email' in session and session['email'] == line.split()[0]:
      flag = True
      break
  return flag


@app.route('/database')
def database():
  con = sqlite3.connect('data/database.db')
  cur = con.cursor()
  # cur.execute('CREATE TABLE Users (UserId INTEGER PRIMARY KEY, FirstName varchar(20) NOT NULL, LastName varchar(20) NOT NULL)')
  # cur.execute('SELECT name FROM sqlite_master where type = "table"')
  # cur.execute('DELETE FROM Users')
  # for i in range(100):
  #   cur.execute('INSERT INTO Users (FirstName, LastName) VALUES (?, ?)', (randomFirstName(), randomLastName()))

  cur.execute('SELECT * FROM Users')
  con.commit() 
  return str(cur.fetchall())

def randomFirstName():
  url = "https://www.usna.edu/Users/cs/roche/courses/s15si335/proj1/files.php%3Ff=names.txt&downloadcode=yes"
  nameString = str(urllib.request.urlopen(url).read())
  names = [x for x in nameString.split('\\n')]
  return random.choice(names)

def randomLastName():
  url = "https://raw.githubusercontent.com/arineng/arincli/master/lib/last-names.txt"
  nameString = str(urllib.request.urlopen(url).read())
  names = [x for x in nameString.split('\\n')]
  return random.choice(names).capitalize()

app.run(host='0.0.0.0', debug=True, port=8080)