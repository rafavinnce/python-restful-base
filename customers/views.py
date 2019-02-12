from django.http import JsonResponse
from location.models import Location
from django.views.decorators.csrf import csrf_exempt
import logging
import json
import jwt

logger = logging.getLogger(__name__)


# Create your views here.
@csrf_exempt
def update_location(request):
    deviceOs = request.META.get('HTTP_DEVICE_OS')
    appVersion = request.META.get('HTTP_APP_VERSION')
    auth = request.META.get('HTTP_AUTHORIZATION')
    items = auth.split()

    if len(items) > 1 and ((items[0].strip() == 'Bearer') or items[0].strip() == 'bearer'):
        token = items[1]
    else:
        token = auth

    options = {'verify_aud': False, 'verify_exp': False}
    decoded = jwt.decode(token, 'da39a3ee5e6b4b0d3255bfef95601890afd80709', algorithms=['HS256'], options=options)
    user_id = decoded['beblueUser_']

    data = json.loads(request.body)
    latitude = data['lat']
    longitude = data['lon']

    logger.info('Performing Location')
    result = {'status': 'ok'}
    # Check DB making a lightweight DB query
    try:
        location = Location(latitude=latitude,
                                       longitude=longitude,
                                       device_type=deviceOs,
                                       version=appVersion,
                                       source='background',
                                       user_id=user_id,
                                       current_city='')

        location.save()
        result['db'] = {'status': 'ok'}
    except Exception as err:
        result['status'] = 'nok'
        err_msg = 'Error accessing DB: {}'.format(err)
        result['db'] = {
            'status': 'nok',
            'err_msg': err_msg,
        }
        logger.error(err_msg)

    logger.debug('Location result {}'.format(result))

    status_code = 200
    if result['status'] != 'ok':
        logger.error('Location result is bad')
        status_code = 500
    else:
        logger.info('Location result is ok')

    response = JsonResponse(result)
    response.status_code = status_code
    return response
