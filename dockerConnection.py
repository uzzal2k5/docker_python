from docker import client

cli = client(base_url='unix://var/run/docker.sock')
cli.containers()
container = cli.create_container(image='ubuntu:latest', command='/bin/sleep 30')
print(container['Id'])
container_id = container['Id']
cli.inspect_container(container_id)['Name']


def restartContainer(container_id):
        try:
            cli.restart(container_id)
        except Exception as e:
            print(e)


# List All images and get details first  images
images = cli.images()
print(images[0])
image = images[0]
image_id = image['Id']
cli.inspect_image(image_id)



# volume

volumes = cli.volume()
print(volumes['Volumes'][0])

# Create volumes
volume = cli.create_volume(name='volume1', driver='local', driver_opts={})
print(volume)


# Using Volume
def createContainer(image_id, vol_name, mount_loc):
    try:
        container = cli.create_container(
            image_id,
            'ls',
            volumes=['/var/lib/docker/volumes/'+vol_name],
            host_config=cli.create_host_config(
                binds=['/var/lib/docker/volumes/volume1:'+mount_loc,]
            )
        )
        print(container)
    except Exception as e:
        print(e)


cli.inspect_volume('volume1')