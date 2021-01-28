from flask import jsonify
from flask import request
from ...main import app
from ...services.mutant_service import MutantService
from flask_restful import reqparse, abort, Api, Resource

@app.route("/mutant/")
def route_mutant():
    message_data = "Api mutant"
    return jsonify(message_data)

@app.route('/mutant', methods=['POST'])
def route_mutant_post():
    content = request.json
    dna = content['dna']
    ms = MutantService()
    if not ms.Is_mutant(dna):
      return abort(403, message="403-Forbidden")
    return jsonify("Es un mutante, ADN: " + str(dna))

