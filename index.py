#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from flask import Flask, jsonify, make_response, render_template, url_for
import os
from werkzeug.exceptions import HTTPException
from flask import jsonify, request
from flask import Flask, render_template, abort
from models.list_of_comics import getListofComicsInfo
from models.all_comic_book_detail import getAllComicBookDetail

# Global Flask Application Variable: app
app = Flask(__name__)

# global strict slashes
app.url_map.strict_slashes = False

# flask server environmental setup
host =  '0.0.0.0'
port =   5000


@app.errorhandler(404)
def handle_404(exception):
    """
    handles 404 errors, in the event that global error handler fails
    """
    code = exception.__str__().split()[0]
    description = exception.description
    message = {'error': description}
    return make_response(jsonify(message), code)


@app.errorhandler(400)
def handle_400(exception):
    """
    handles 400 errros, in the event that global error handler fails
    """
    code = exception.__str__().split()[0]
    description = exception.description
    message = {'error': description}
    return make_response(jsonify(message), code)

@app.route('/')
def index():
    "Main page for list of comics"
    return render_template('comics_list.html', listofcomics=getListofComicsInfo())

@app.route('/comic_info/<api_id>', methods=['GET'])
def comic_info(api_id):
    """
    function to return detail info render of a comic
    """
    return render_template('index.html', comic_info=getAllComicBookDetail(api_id))

@app.route('/status', methods=['GET'])
def status():
    """
    function for status route that returns the status
    """
    if request.method == 'GET':
        resp = {"status": "OK"}
        return jsonify(resp)


if __name__ == "__main__":
    """
    MAIN Flask App
    """
    # start Flask app
    app.run(host=host, port=port,debug=True)