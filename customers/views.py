from django.http import JsonResponse
from location.models import Location
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)


# Create your views here.
@csrf_exempt
def update_location(request):
    deviceOs = request.META.get('HTTP_DEVICE_OS')
    appVersion = request.META.get('HTTP_APP_VERSION')

    logger.info('Performing Location')
    result = {'status': 'ok'}
    # Check DB making a lightweight DB query
    try:
        location = Location(latitude=request.POST.get("lat", 0),
                                       longitude=request.POST.get("lon", 0),
                                       device_type=deviceOs,
                                       version=appVersion,
                                       source='background',
                                       user_id=request.POST.get("userId", ''),
                                       current_city=request.POST.get("currentCity", ''))

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
