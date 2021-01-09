# import modules
from flask import Flask, render_template

# identify_pizza is a function that identifies the type of pizza
# and the estimated time it takes to eat the pizza
# the input consists of three integers
# the output is a dictionary

def identify_pizza(cheese=0, pepperoni=0, pineapple=0):

	type_of_pizza = ""
	eating_time = 60.0

	if cheese == 0 and pepperoni == 0 and pineapple == 0:
		type_of_pizza = "tomato pizza"

	elif cheese > 1 and pepperoni == 0 and pineapple == 0:
		type_of_pizza = "cheese pizza"

	elif cheese > 1 and pepperoni > 1 and pineapple == 0:
		type_of_pizza = "pepperoni pizza"

	elif cheese > 1 and pepperoni > 1 and pineapple > 1:
		type_of_pizza = "hawaiian pizza"

	else:
		type_of_pizza = "inventive pizza"

	eating_time = eating_time + 0.1*cheese + 1.0*pepperoni + 2.0*pineapple

	return {"type of pizza": type_of_pizza, "eating time (seconds)": eating_time}

# we create object app 
app = Flask(__name__)

# this route (example <url to website>/) will execute the home function
@app.route("/")
def home():
	# this renders the HTML file called index.html that must be placed in a folder 
	# called templates
	return render_template("index.html")

# this route (example <url to website>/identify/80/80/0) will execute the identify function
@app.route("/identify/<cheese_param>/<pepperoni_param>/<pineapple_param>")
def identify(cheese_param, pepperoni_param, pineapple_param):

	# we convert the URL parameters from string (text) type to int (integer) type 
	cheese_param = int(cheese_param)
	pepperoni_param = int(pepperoni_param)
	pineapple_param = int(pineapple_param)

	# we call the idenify_pizza() function and assign the resulting dictionary to result_dict
	result_dict = identify_pizza(cheese_param, pepperoni_param, pineapple_param)
	
	# this function outputs the content of result_dict in a web browser page
	return result_dict

# app.run() runs the Flask app
# the host address is '0.0.0.0' and the port number is 5000
# it's essential to specify these exact parameters to run Flask on Repl.it
app.run(host='0.0.0.0', port=5000)
