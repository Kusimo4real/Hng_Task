from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Guest')
    client_ip = request.remote_addr
    # For simplicity, we'll use a fixed location; in a real scenario, you'd use a service to determine the location from the IP address
    location = "New York"  

    response = {
        "client_ip": client_ip,
        "location": location,
        "greeting": f"Hello, {visitor_name}!"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

