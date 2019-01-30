from django.http import JsonResponse
from user_locations.models import UserLocations
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)


# Create your views here.
@csrf_exempt
def update_location(request):
    deviceOs = request.META.get('HTTP_DEVICE_OS')
    appVersion = request.META.get('HTTP_APP_VERSION')

    logger.info('Performing user_locations')
    result = {'status': 'ok'}
    # Check DB making a lightweight DB query
    try:
        user_locations = UserLocations(latitude=request.POST.get("lat", 0),
                                       longitude=request.POST.get("lon", 0),
                                       device_type=deviceOs,
                                       version=appVersion,
                                       source='background',
                                       user_id=request.POST.get("userId", ''),
                                       current_city=request.POST.get("currentCity", ''))

        user_locations.save()
        result['db'] = {'status': 'ok'}
    except Exception as err:
        result['status'] = 'nok'
        err_msg = 'Error accessing DB: {}'.format(err)
        result['db'] = {
            'status': 'nok',
            'err_msg': err_msg,
        }
        logger.error(err_msg)

    logger.debug('UserLocations result {}'.format(result))

    status_code = 200
    if result['status'] != 'ok':
        logger.error('UserLocations result is bad')
        status_code = 500
    else:
        logger.info('UserLocations result is ok')

    response = JsonResponse(result)
    response.status_code = status_code
    return response


# Create your views here.
@csrf_exempt
def location(request):
    deviceOs = request.META.get('HTTP_DEVICE_OS')
    appVersion = request.META.get('HTTP_APP_VERSION')

    logger.info('Performing UserLocations')
    result = {'status': 'ok'}
    # Check DB making a lightweight DB query
    try:
        user_locations = UserLocations(latitude=request.POST.get("lat", 0),
                            longitude=request.POST.get("lon", 0),
                            device_type=deviceOs,
                            version=appVersion,
                            source='app_open',
                            user_id=request.POST.get("userId", ''),
                            current_city=request.POST.get("currentCity", ''))

        user_locations.save()
        result['db'] = {'status': 'ok'}
    except Exception as err:
        result['status'] = 'nok'
        err_msg = 'Error accessing DB: {}'.format(err)
        result['db'] = {
            'status': 'nok',
            'err_msg': err_msg,
        }
        logger.error(err_msg)

    logger.debug('UserLocations result {}'.format(result))

    status_code = 200
    if result['status'] != 'ok':
        logger.error('UserLocations result is bad')
        status_code = 500
    else:
        logger.info('UserLocations result is ok')

    response = JsonResponse(result)
    response.status_code = status_code
    return response


@csrf_exempt
def background(request):
    deviceOs = request.META.get('HTTP_DEVICE_OS')
    appVersion = request.META.get('HTTP_APP_VERSION')

    logger.info('Performing UserLocations')
    result = {'status': 'ok'}
    # Check DB making a lightweight DB query
    try:
        user_locations = UserLocations(latitude=request.POST.get("lat", 0),
                            longitude=request.POST.get("lon", 0),
                            device_type=deviceOs,
                            version=appVersion,
                            source='background',
                            user_id=request.POST.get("userId", ''),
                            current_city=request.POST.get("currentCity", ''))

        user_locations.save()
        result['db'] = {'status': 'ok'}
    except Exception as err:
        result['status'] = 'nok'
        err_msg = 'Error accessing DB: {}'.format(err)
        result['db'] = {
            'status': 'nok',
            'err_msg': err_msg,
        }
        logger.error(err_msg)

    logger.debug('UserLocations result {}'.format(result))

    status_code = 200
    if result['status'] != 'ok':
        logger.error('UserLocations result is bad')
        status_code = 500
    else:
        logger.info('UserLocations result is ok')

    response = JsonResponse(result)
    response.status_code = status_code
    return response
