from flask import Flask, jsonify, request
from werkzeug.exceptions import abort
from clarifai.rest import ClarifaiApp
"""Collect file names and description from Internet"""

my_app = Flask(__name__)


FILES = []

api_key = '4756270c660f4c3fb9ad13cf24d70588'
app = ClarifaiApp(api_key=api_key)
model = app.public_models.general_model


@my_app.route('/')
def hello():
    return "It is start page of API making pictures clarification." \
           "To see list of file names and their categories put /my_api/files/ into address line." \
           "To see category of detached file put /my_api/files/<file name> into address line."


@my_app.route('/my_api/files/', methods=['GET'])
def get_files():
    return jsonify(FILES)


@my_app.route('/my_api/files/<int:file_id>', methods=['GET'])
def get_file(file_id):
    file = None
    for f in FILES:
        if f['id'] == file_id:
            file = f
    return jsonify(file)


@my_app.route('/my_api/files/', methods=['POST'])
def create_file():
    print(request.json)
    if 'file_name' in request.json:
        response = model.predict_by_url(request.json['file_name']) # Make prediction what in file
        new_file = {
            'id': len(FILES),
            'file_name': request.json['file_name'],
            'descr': response['outputs'][0]['data']['concepts'][0]['name']
        }
        FILES.append(new_file)
        return new_file, 201
    else:
        abort(400)


@my_app.route('/my_api/files/put/<int:file_id>', methods=['PUT'])
def edit_file(file_id):
    print(request.json)
    if 'file_name' in request.json:
        response = model.predict_by_url(request.json['file_name'])
        for i, f in enumerate(FILES):
            if f['id'] == file_id:
                FILES[i]['file_name'] = request.json['file_name']
                FILES[i]['descr'] = response['outputs'][0]['data']['concepts'][0]['name']
        return 'Done'
    else:
        abort(400)


@my_app.route('/my_api/files/delete/<int:file_id>', methods=['DELETE'])
def delete_file(file_id):
    ind = None
    for i, f in enumerate(FILES):
        if f['id'] == file_id:
            ind = i
    FILES.pop(ind)
    return 'Done'


if __name__ == '__main__':
    my_app.run(debug=True)
