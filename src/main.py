from flask import Flask, request
from flask_restful import Api, Resource, abort
from flask_cors import CORS

import json
from functional import seq
import time

from . import scraper
from src.hobby_extraction import create_pipeline
from src.brain_rot_extractor import extract_hrefs
from src.brain_rot_extractor.download import download_reels
from multiprocessing import freeze_support

import multiprocessing

def process_link(link):
    return download_reels(link)

pipeline = None
pipeline_in_use = False

app = Flask(__name__)
CORS(app)
# api = Api(app)


@app.route('/hobby_card', methods=['POST'])
def hobby_card():
	global pipeline

	# json = request.json

	# print(request.form)

	location = request.form['text']

	tmp = dict(request.form.items())

	del tmp['text']
	# files = []
	all_links = set()
	for key, value in tmp.items():
		value = json.loads(value.strip())

		extract_hrefs(
			value,
			all_links
		)
	all_links = list(all_links)
	print(all_links)

	with multiprocessing.Pool() as pool:
		all_videos = pool.map(process_link, all_links)

    # Flatten the list if necessary
	all_videos = [video for sublist in all_videos for video in sublist]

	print(all_videos)
	# all_links = list(all_links)
	# print(all_links)
	# all_videos = []
	# # print("AI TIME")
	# for link in all_links:
	# 	all_videos += download_reels(link)
	hobby = pipeline(all_videos)

	print(hobby)
		# files.append()
	# print(files)


	# print()
	# print(all_links)
	# print(type(request.form['files']))
	
	# files = [json.loads(file.strip()) for file in request.form['files']]


	# print(files)

	# return 200, "Hello world"

	# scrapper (downloads reels)

	

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