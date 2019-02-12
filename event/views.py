from django.http import JsonResponse
from event.models import Event
from django.views.decorators.csrf import csrf_exempt
import logging
import json

logger = logging.getLogger(__name__)


# Create your views here.
@csrf_exempt
def merchant_view(request):
    auth = request.META.get('HTTP_AUTHORIZATION')
    items = auth.split()

    if len(items) > 1 and ((items[0].strip() == 'Bearer') or items[0].strip() == 'bearer'):
        token = items[1]
    else:
        token = auth

    options = {'verify_aud': False, 'verify_exp': False}
    decoded = jwt.decode(token, 'da39a3ee5e6b4b0d3255bfef95601890afd80709', algorithms=['HS256'], options=options)
    user_id = decoded['beblueUser_']

    logger.info('Performing Event')
    result = {'status': 'ok'}

    data = json.loads(request.body)
    merchant_id = data['merchantId']
    hotdeal = data['hotdeal']
    promocode = data['promocode']
    # Check DB making a lightweight DB query
    try:
        event = Event(user_id=user_id,
                      merchant_id=merchant_id,
                      hotdeal=hotdeal,
                      promocode=promocode)

        event.save()
        result['db'] = {'status': 'ok'}
    except Exception as err:
        result['status'] = 'nok'
        err_msg = 'Error accessing DB: {}'.format(err)
        result['db'] = {
            'status': 'nok',
            'err_msg': err_msg,
        }
        logger.error(err_msg)

    logger.debug('Event result {}'.format(result))

    status_code = 200
    if result['status'] != 'ok':
        logger.error('Event result is bad')
        status_code = 500
    else:
        logger.info('Event result is ok')

    response = JsonResponse(result)
    response.status_code = status_code
    return response
