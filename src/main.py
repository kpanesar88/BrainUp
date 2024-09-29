from flask import Flask
from flask_restful import Api, Resource, abort

import scraper
from src.hobby_extraction import create_pipeline

pipeline = create_pipeline()

app = Flask(__name__)
api = Api(app)

class hobby_card(Resource):
	def get(self, hobby, location):
		global pipeline

		# scrapper (downloads reels)

		# hobby = pipeline([all files downloaded])

		pre_result = scraper.scraper(location, hobby)
		result = {"hobby": hobby, "name": pre_result[0], "location": pre_result[1], "description": pre_result[2], "image": pre_result[3], "url": pre_result[4]}
		if not result:
			abort(404, message="Could not find any classes in your area")
		return result

api.add_resource(hobby_card, "/card/<string:hobby>/<string:location>/")

if __name__ == "__main__":
	app.run(debug=False)