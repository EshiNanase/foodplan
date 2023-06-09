import stripe
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from dateutil.relativedelta import relativedelta
from authorization.models import CustomUser


def create_checkout_session(user, price, time):

    stripe.api_key = settings.STRIPE_SECRET_KEY
    response = stripe.Price.create(
        unit_amount=price*100,
        product=settings.TARIFF_API_ID,
        currency='rub',

    )
    price_id = response['id']

    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            metadata={'user_id': user.id, 'time': time},
            success_url='http://45.131.40.159/profile',
        )
    except Exception as e:
        print(str(e))
    return redirect(checkout_session.url, code=303)


@csrf_exempt
def stripe_webhook_view(request):

    stripe.api_key = settings.STRIPE_SECRET_KEY
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
              payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = stripe.checkout.Session.retrieve(
            event['data']['object']['id'],
            expand=['line_items'],
        )
        line_items = session.line_items
        user_id = session.metadata.user_id
        time = int(session.metadata.time)
        user = CustomUser.objects.get(id=user_id)
        user.tariff_ends_at = datetime.today() + relativedelta(months=time)
        user.save()

    return HttpResponse(status=200)
