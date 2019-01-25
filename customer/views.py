from django.http import JsonResponse
from handler.models import Handler
import logging

logger = logging.getLogger(__name__)


# Create your views here.
def customer(request):
    """
    Check status of each external service.
    Remember to keep everything lightweight and add short timeouts
    """
    result = {'status': 'ok'}
    logger.info('Performing customer')

    # Check DB making a lightweight DB query
    try:
        Handler.objects.first()
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
