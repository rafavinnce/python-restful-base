import signal
import os
import time
import requests
import json
import socket


def __wait_for_application(service_port):
    status_code = None
    while(status_code != 200):
        status_code = requests.get(f'http://localhost:{service_port}/v1/healthcheck').status_code
        time.sleep(5)


def __consul_register_service(service_id, service_port):
    local_machine_ip = socket.gethostbyname(socket.gethostname())
    status_code = None
    while(status_code != 200):
        r = requests.put('http://localhost:8500/v1/agent/service/register',
                        data=json.dumps({
                                        'Name': 'logger-service',
                                        'ID': service_id,
                                        'Address': local_machine_ip,
                                        'Port': service_port,
                                        'Tags': ['logger-service'],
                                        'Check': {
                                            'DeregisterCriticalServiceAfter': '1m',
                                            'HTTP': f'http://{local_machine_ip}:{service_port}/v1/healthcheck',
                                            'Interval': '10s'
                                            }
                                        }))
        status_code = r.status_code
        time.sleep(5)


def __consul_register():
    SERVICE_ID = os.environ.get("SERVICE_ID", None)
    SERVICE_PORT = int(os.environ.get('SERVICE_PORT', None))

    __wait_for_application(SERVICE_PORT)
    __consul_register_service(SERVICE_ID, SERVICE_PORT)


def __consul_deregister(signum, stack):
    SERVICE_ID = os.environ.get("SERVICE_ID", None)

    status_code = None
    while(status_code != 200):
        r = requests.put(f'http://localhost:8500/v1/agent/service/deregister/{SERVICE_ID}')
        status_code = r.status_code
        time.sleep(5)


__consul_register()

signal.signal(signal.SIGTERM, __consul_deregister)
signal.signal(signal.SIGINT, __consul_deregister)
signal.pause()
