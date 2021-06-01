from flask import Flask, render_template
app = Flask('app')


@app.route('/')
def index():
  return render_template("index.html")


# @app.route('/about')
# def about():
#   return render_template("about.html")

@app.route('/administrator')
def administrator():
  return render_template("administrator.html")

@app.route('/statistics')
def statistics():
  return render_template("statistics.html")
  
@app.route('/myTickets')
def myTickets():
  return render_template("myTickets.html")
  
@app.route('/manageFlights')
def manageFlights():
  return render_template("manageFlights.html")
  
@app.route('/manageAirports')
def manageAirports():
  return render_template("manageAirports.html")


app.run(host='0.0.0.0', port=8080)