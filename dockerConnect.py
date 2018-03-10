from docker import Client
try:
    cli = Client(base_url='unix://var/run/docker.sock')
except ConnectionError as e:
    print(e)