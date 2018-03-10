import docker

client = docker.from_env()
client.containers.run('ubuntu:latest','echo Hello World!',detach=True)
client.containers.list()

# Get Container by ID
container = client.containers.get('container_id')
attribute = container.attrs['Config']['Image']
container_log = container.log()
container.stop()

# Images
image = client.images.pull('nginx')
image_list = client.images.list()