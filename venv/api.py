from flask import Flask, jsonify, request

main = Flask(__name__)

@main.route('/')
def main_page():
    return "<h1>Welcome to Flask Application<h1>"

@main.route('/', methods=['POST'])
def add_values():
    return "<h1>Welcome to Flask Application<h1><p>Fetching the data using  api</p>"

@main.route('/',methods=['PUT'])
def update_value():
    return "<h1>Welcome to Flask Application<h1><p>Fetching the data using flask api</p>"

@main.route('/',methods=['DELETE'])
def delete_value():
    return "<h1>Welcome to Flask Application<h1>"

if __name__ == '__main__':
    main.run(debug=True)
