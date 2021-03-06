from flask_cors import CORS, cross_origin
from flask import Response

import flask
import json
import random
import requests

##from flask import render_template

app = flask.Flask(__name__)
cors = CORS(app)


YELP_SECRET = "mxbpTcR535q6bkblaytUq1C6Ytdul4XFrgdNWzgZxniuOwXMmAaztWvCVRRJk9YmDI4KK7LGSWR3_d1IfKWFuDzZ1zTW82K9BHTIPVAKTF-s5KrbLPVqcwJ6HKbXYXYx"

search_url = "https://api.yelp.com/v3/businesses/search?term=boba&location=la&limit=50"
headers = {
    "Authorization": f"Bearer {YELP_SECRET}"
}

@app.route('/', methods=['GET'])
@cross_origin()
def get_boba():
    print("Hello backend...")
    businesses = requests.get(
        search_url,
        headers=headers
    ).json()['businesses']
    random_business_id = random.choice(businesses)['id']

    business_data = requests.get(
        f"https://api.yelp.com/v3/businesses/{random_business_id}",
        headers=headers
    ).json()

    response = app.response_class(
    response=json.dumps(business_data, default=str),
    status=200,
    mimetype='application/json'
    )
    return response

   ## return render_template('json.html', json=json.dumps(business_data, default=str))
if __name__ == '__app__':
    app.run()