from django.shortcuts import render, redirect
from django.conf import settings
import stripe
from django.views import View
from .models import Payment
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin

stripe.api_key = settings.STRIPE_SECRET_KEY
YOUR_DOMAIN = "http://localhost:8000"

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs.get('product_id')
        amount = 10.00  # In a real app, you would get this from your product model
        
        try:
            # Include session_id in the success URL to identify the payment
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': 'Test Product',
                            },
                            'unit_amount': int(amount * 100),  # Convert to cents
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=YOUR_DOMAIN + '/payments/success/?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=YOUR_DOMAIN + '/payments/cancel/',
                # Optionally pass client metadata
                metadata={
                    'product_id': product_id,
                    'user_id': request.user.id,
                },
            )

            # Save session info in database
            Payment.objects.create(
                stripe_checkout_session_id=checkout_session['id'],
                amount=amount
            )

            return JsonResponse({
                'id': checkout_session.id
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})

def success(request):
    """Handle successful payment by checking session status"""
    session_id = request.GET.get('session_id')
    
    if session_id:
        try:
            # Verify the payment status directly with Stripe
            session = stripe.checkout.Session.retrieve(session_id)
            
            if session.payment_status == 'paid':
                # Update the payment record in the database
                payment = Payment.objects.get(stripe_checkout_session_id=session_id)
                payment.paid = True
                payment.stripe_payment_intent_id = session.payment_intent
                payment.save()
                
                return render(request, 'payments/success.html')
            else:
                # Payment not completed yet
                return render(request, 'payments/pending.html')
                
        except Exception as e:
            # Error handling
            return render(request, 'payments/error.html', {'error': str(e)})
    
    # No session_id provided
    return redirect('/')

def cancel(request):
    """Handle canceled payment"""
    return render(request, 'payments/cancel.html')


def checkout_page(request, product_id):
    """Render the checkout page with the Stripe public key"""
    context = {
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
        'product_id': product_id
    }
    return render(request, 'payments/checkout.html', context)

