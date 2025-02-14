from flask import Flask, request, jsonify #import Flask and helper modules
from app import create_app
# step 1: Create the flask app instance
app = create_app() # initialize the flask app

@app.before_request
def handle_preflight():
    """Automatically handle preflight OPTIONS requests."""
    if request.method == "OPTIONS":
        response = jsonify({"message": "CORS preflight successful"})
        response.status_code = 200
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "Content-type, Authorization")
        response.headers.add("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        return response

if __name__ == "__main__":
    # app.run(debug=True) # run app in debug mode
    app.run(debug=True, host="127.0.0.1", port=5000)
