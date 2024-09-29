from flask import Flask, request
from flask_restful import Api, Resource, abort
from flask_cors import CORS

from . import scraper
from src.hobby_extraction import create_pipeline

from multiprocessing import freeze_support

pipeline = None
pipeline_in_use = False

app = Flask(__name__)
CORS(app)
# api = Api(app)

@app.route('/hobby_card', methods=['POST'])
def hobby_card():
	global pipeline

	# json = request.json

	print(request.form)

	location = request.form['text']
	files = request.form['files']

	print(location)
	print(files)

	return 200, "Hello world"

	# scrapper (downloads reels)

	# hobby = pipeline([all files downloaded])

	pre_result = scraper.scraper(location, hobby)
	result = {"hobby": hobby, "name": pre_result[0], "location": pre_result[1], "description": pre_result[2], "image": pre_result[3], "url": pre_result[4]}
	if not result:
		abort(404, message="Could not find any classes in your area")
	return result

# class hobby_card(Resource):
# 	def get(self, hobby, location):
# 		global pipeline

# 		print("")

# 		# scrapper (downloads reels)

# 		# hobby = pipeline([all files downloaded])

# 		pre_result = scraper.scraper(location, hobby)
# 		result = {"hobby": hobby, "name": pre_result[0], "location": pre_result[1], "description": pre_result[2], "image": pre_result[3], "url": pre_result[4]}
# 		if not result:
# 			abort(404, message="Could not find any classes in your area")
# 		return result

# api.add_resource(hobby_card, "/card/<string:hobby>/<string:location>/")

if __name__ == "__main__":
	freeze_support()
	pipeline = create_pipeline()
	app.run(debug=False, port=4000)