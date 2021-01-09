from flask import Flask, render_template

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

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/identify/<cheese_param>/<pepperoni_param>/<pineapple_param>")
def identify(cheese_param, pepperoni_param, pineapple_param):

	cheese_param = int(cheese_param)
	pepperoni_param = int(pepperoni_param)
	pineapple_param = int(pineapple_param)

	result_dict = identify_pizza(cheese_param, pepperoni_param, pineapple_param)
	return result_dict

app.run(host='0.0.0.0', port=5000)
