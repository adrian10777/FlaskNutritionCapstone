from . import  mail
from flask import Blueprint, request, jsonify, render_template
from .email_service import send_contact_email
from flask_mail import Message
#This file is for handling API routes, were we handle incoming requests, like the the frontend submits a form

routes = Blueprint('routes', __name__)


# Define the route to handle contact form submissions
@routes.route('/send-email', methods=['POST'])
def send_email():
    try:

        data = request.get_json();
        print(f"Received data: {data}")

        if not data:
            return jsonify({"message": "No data provided"}), 400
        email = data.get("email")
        first_name = data.get("firstName")
        last_name = data.get("lastName")
        message = data.get("message")
        
        # Get JSON data from request
        print(f"Request heasders: {request.headers}")
        data = request.get_json()
        print(f"Received data:, {data}")

        email = data.get("email")
        first_name = data.get("firstName")
        last_name = data.get("lastName")
        message = data.get("message")  # Ensure you capture the message!

        # recipient_email = "sdanutrition@nutritionsda.com"

        print(f"Sending email from {email} ({first_name} {last_name}: {message}")

        if not all([email, first_name, last_name, message]):
                return jsonify({"message": "Missing required fields"}), 400
        # Call the function with ALL parameters
        send_contact_email(mail, email, first_name, last_name, message)

        print(" Email sent successfully!")
        return jsonify({"message": "Email sent successfully!"}), 200

    except Exception as e:
        print(f" Error sending email: {str(e)}")
        return jsonify({"message": f"Failed to send email: {str(e)}"}), 500

    # msg = Message (
    #     "New Contact Form Submission",
    #     recipients=["sdanutrition@nutritionsda.com"]
    # )

    # msg.body = f"""
    # you have a new contact form submission:

    # Name: {first_name} {last_name}
    # Email: {email}
    # Message: {message}
    # """

    # try:
    #     mail.send(msg)
    #     return jsonify({"message": "Email send successfully!"}), 200
    # except Exception as e:
    #     return jsonify({"message": f"Failed to send email: {str(e)}"}), 500







# @app.route('/')
# def home():
#     return render_template('index.html')

# # step 1: Create a Blueprint for the routes (modular organization)
# routes = Blueprint("routes", __name__)

# @routes.route("/send-email", methods=["POST"]) # POST route for sending emails
# def send_email():
#     """
#     This function handles the POST request from the contanct form.
#     It extracts data from the request and calls the email service to send the emails
#     """
#     #step 2: Extract form data from the incoming request
#     data = request.get_json() # Get the JSON data sent from frontend
#     email = data.get("email") #User's email
#     first_name = data.get("firstName") # User's first name
#     last_name = data.get("lastName") # User's Last name
#     message = data.get("message")

#     #step 3: Call the send_contact_email function to send the email

#     try:
#         send_contact_email(mail, email, first_name, last_name, message) #call function from email_service.py
#         return jsonify({"message": "Email sent successfully!"}, 200)
#     except Exception as e:
#         return jsonify({"message": "Failed to send email: {str(e)}"}), 500 # return error message
    
#     # The 'send_email' route listens for POST requests at "/send-email".
#     # it extracts the form data from incoming request
#     # The route then calls the 'send_Contact_email' function (defined in email_Service.py) to sned the email)