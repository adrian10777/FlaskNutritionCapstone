from flask_mail import Message

def send_contact_email(mail, email, first_name, last_name, message):
    try:
          # Verified sender email (must be registered in SMTP2GO)
        verified_sender_email = "sdanutrition@nutritionsda.com"
        # Create the email message
        msg = Message(
            subject="New SDA Nutrition Contact Form Submission",
          recipients=["sdanutrition@nutritionsda.com"],  # Recipient email
            sender="sdanutrition@nutritionsda.com",  # Sender email
            reply_to=email,  # Set the user's email as the reply-to
            body=f"""
            You have a new contact form submission:

            Name: {first_name} {last_name}
            Email: {email}
            Message: {message}
            """
        )

        # Send the email
        mail.send(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        raise e