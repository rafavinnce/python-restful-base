from django.http import JsonResponse
from customer.models import Customer
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)


# Create your views here.
@csrf_exempt
def location(request):
    deviceOs = request.META.get('HTTP_DEVICE_OS')
    appVersion = request.META.get('HTTP_APP_VERSION')

    logger.info('Performing customer')
    result = {'status': 'ok'}
    # Check DB making a lightweight DB query
    try:
        customer = Customer(latitude=request.POST.get("lat", 0),
                            longitude=request.POST.get("lon", 0),
                            device_type=deviceOs,
                            version=appVersion,
                            source='app_open',
                            user_id=request.POST.get("userId", ''),
                            current_city=request.POST.get("currentCity", ''))

        customer.save()
        result['db'] = {'status': 'ok'}
    except Exception as err:
        result['status'] = 'nok'
        err_msg = 'Error accessing DB: {}'.format(err)
        result['db'] = {
            'status': 'nok',
            'err_msg': err_msg,
        }
        logger.error(err_msg)

    logger.debug('Customer result {}'.format(result))

    status_code = 200
    if result['status'] != 'ok':
        logger.error('Customer result is bad')
        status_code = 500
    else:
        logger.info('Customer result is ok')

    response = JsonResponse(result)
    response.status_code = status_code
    return response


@csrf_exempt
def background(request):
    deviceOs = request.META.get('HTTP_DEVICE_OS')
    appVersion = request.META.get('HTTP_APP_VERSION')

    logger.info('Performing customer')
    result = {'status': 'ok'}
    # Check DB making a lightweight DB query
    try:
        customer = Customer(latitude=request.POST.get("lat", 0),
                            longitude=request.POST.get("lon", 0),
                            device_type=deviceOs,
                            version=appVersion,
                            source='background',
                            user_id=request.POST.get("userId", ''),
                            current_city=request.POST.get("currentCity", ''))

        customer.save()
        result['db'] = {'status': 'ok'}
    except Exception as err:
        result['status'] = 'nok'
        err_msg = 'Error accessing DB: {}'.format(err)
        result['db'] = {
            'status': 'nok',
            'err_msg': err_msg,
        }
        logger.error(err_msg)

    logger.debug('Customer result {}'.format(result))

    status_code = 200
    if result['status'] != 'ok':
        logger.error('Customer result is bad')
        status_code = 500
    else:
        logger.info('Customer result is ok')

    response = JsonResponse(result)
    response.status_code = status_code
    return response
