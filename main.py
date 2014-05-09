import flask, flask.views
from randomfood import yelpRequest
import random

app = flask.Flask(__name__)
app.secret_key = "" #enter your secret KEY

#API information
consumer_key = ""
consumer_secret = ""
token = ""
token_secret = ""

# early WEBAPP DONT BE MAD 
foodsURL = "http://api.yelp.com/v2/search?"
term = "food"
radius_filter ="16100"



class View(flask.views.MethodView):
	def get(self):
		return flask.render_template('index.html')

	def post(self):

		address = str(flask.request.form['location'])
		payload = {'term': term, 'radius_filter': radius_filter, 'location': address}
		response = yelpRequest(foodsURL, payload, consumer_key, consumer_secret,
								 token, token_secret)
		foodlist = []
		for i in range(0, len(response['businesses'])):
			foodlist.append(response['businesses'][i]['name'].encode('utf_8'))
							
			
		flask.flash(random.choice(foodlist))
		return self.get()

		

app.add_url_rule('/', view_func=View.as_view('main'), methods=('GET', 'POST'))

app.debug = True
app.run()