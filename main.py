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

		for business in response['businesses']:
			foodlist.append([business['name'].encode('utf_8'), 
							business['location']['display_address']])
							
		show = random.choice(foodlist)

		showMsg = "Name: %s \nAddress: %s" % (show[0], ' '.join(show[1]))

		flask.flash(showMsg)

		return self.get()

		

app.add_url_rule('/', view_func=View.as_view('main'), methods=('GET', 'POST'))

app.debug = True
app.run()