from django.http import JsonResponse
from location.models import Location
from django.views.decorators.csrf import csrf_exempt
import logging
import json
from django.db import transaction

logger = logging.getLogger()


# Create your views here.
@csrf_exempt
@transaction.non_atomic_requests
def location(request):
    logger.info('Performing Location')
    result = {'status': 'ok'}

    data = json.loads(request.body)
    latitude = data['lat']
    longitude = data['lon']
    user_id = data['userId']
    current_city = data['currentCity']
    # Check DB making a lightweight DB query

    try:
        location = Location(latitude=latitude,
                            longitude=longitude,
                            device_type='',
                            version='',
                            source='app_open',
                            user_id=user_id,
                            current_city=current_city)

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


@csrf_exempt
@transaction.non_atomic_requests
def background(request):
    logger.info('Performing Location')
    result = {'status': 'ok'}
    # Check DB making a lightweight DB query

    data = json.loads(request.body)
    latitude = data['lat']
    longitude = data['lon']
    user_id = data['userId']
    current_city = data['currentCity']
    device_type = data['deviceType']
    version = data['appVersion']

    try:
        location = Location(latitude=latitude,
                            longitude=longitude,
                            device_type=device_type,
                            version=version,
                            source='background',
                            user_id=user_id,
                            current_city=current_city)

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
