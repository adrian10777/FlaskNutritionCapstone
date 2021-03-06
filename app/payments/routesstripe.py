from flask import Blueprint, jsonify, request, request
import os
import json
import stripe

payments = Blueprint('payments', __name__, url_prefix='/payments')

stripe.api_key= os.environ.get('STRIPE_SECRET_KEY')

@payments.route('/create-payment-intent', methods=['POST'])
def create_payment():
    try:
        data = json.loads(request.data)
        print(data)
        # Create a PaymentIntent with the order amount and currency
        if(data[1] !='guest'):
            try:
                user = stripe.Customer.retrieve(data[1]['uid'])
            except:
                user = stripe.Customer.create(email=data[1]['email'], name=data[1]['displayName'], id=data[1]['uid'])
            # include my customer data on this payment intent?
        else:
            user = None

        intent = stripe.PaymentIntent.create(
            amount=int(data[0]['total']*100),# i'll do this diff, I need to decide if I want to just use my cart total from the client or if I want to calculate total here
            currency='usd',
            customer=user,
            payment_method_types=['card']
        )
        print(intent)
        return jsonify({
            'clientSecret': intent['client_secret']
        })
        
    except Exception as e:
        return jsonify(error=str(e)), 403