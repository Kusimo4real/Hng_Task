from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Visitor')
    client_ip = request.remote_addr
    response = {
        "client_ip": client_ip,
        "greeting": f"Hello, {visitor_name}!"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

