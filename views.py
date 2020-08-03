import os
from flask import Flask, render_template, request, jsonify

from grandpybot.wikipedia import Wiki
from grandpybot.google_maps import GMaps
from grandpybot.parser import Parser
from grandpybot.stop_words import STOP_WORDS
from grandpybot.messages import *



app = Flask(__name__)
google_api_key = "AIzaSyC71Qx-GXf4edGJ43FvsEw9e9Pr0qs5PFA"

parser = Parser(STOP_WORDS)
gmap = GMaps(google_api_key)
wiki = Wiki()


@app.route('/_get_json')
def get_json():
    user_input = request.args.get('userInput', type=str)
    parsed_input = parser.get_relevant_words(user_input)
    if parsed_input == "":
        failure_msg = return_failure()
        return jsonify(message1=failure_msg,
                       error=True)

    gmap_place = gmap.get_position(parsed_input)
    if gmap_place != "no result":
        wiki_result = wiki.get_wiki_result(
            gmap_place["latitude"], gmap_place["longitude"], parsed_input)
        msg_adress = return_address(gmap_place["address"])

        if wiki_result != "no result":
            msg_summary = return_story(wiki_result['summary'])

            return jsonify(lat=gmap_place["latitude"],
                           lng=gmap_place["longitude"],
                           message1=msg_adress,
                           message2=msg_summary,
                           url=wiki_result["url"],
                           error=False)

        failure_msg = return_failure()
        return jsonify(message1=failure_msg,
                       error=True)

    failure_msg = return_failure()
    return jsonify(message1=failure_msg,
                   error=True)


@app.route('/')
@app.route('/home_page')
def index():

    return render_template('home_page.html', api_key=google_api_key)
