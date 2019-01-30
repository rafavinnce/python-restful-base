from django.http import JsonResponse
from event.models import Event
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)


# Create your views here.
@csrf_exempt
def merchant_view(request):
    logger.info('Performing Event')
    result = {'status': 'ok'}
    # Check DB making a lightweight DB query
    try:
        event = Event(user_id=request.POST.get("userId", ''),
                      merchant_id=request.POST.get("merchantId", ''),
                      hotdeal=request.POST.get("hotdeal", False),
                      promocode=request.POST.get("promocode", False))

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
