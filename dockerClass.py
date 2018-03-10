from docker_python.dockerConnect import cli


class DockerPythonClass:

    def getAllImages(self):
        try:
            images = cli.images()
            for i in range(len(images)):
                print('Image[', i, ']', images[i]['Id'])
                image_list = images[i]['Id']
            print('First Image Details : \n\n ', (images[0]))
            return image_list
        except Exception as e:
            print(e)


    # Get Container
    def getAllContainers(self):
        try:
            print("\n\nCONTAINER INFORMATION \n\n")
            container = cli.containers()
            for i in range(len(container)):
                container_list = container[i]
                print(container_list)
                print('\n')
            return container_list
        except Exception as e:
            print(e)


    #  DOCKER VOLUME
    def getAllVolumes(self):
        try:
            print("Docker Volume \n\n")
            volumes = cli.volumes()
            count = len(volumes)
            print('Number of Volumes :', count)
            for i in range(count):
                volume_list = volumes['Volumes'][i]
                print("\nName :", volume_list['Name'], "\nMoutn Point : ", volume_list['Mountpoint'], "\nLabels :",
                      volume_list['Labels'], '\n')
                # volumes = cli.volume()
            print('FIrst Volume: \n\n', volumes['Volumes'][0])
            return volume_list
        except Exception as e:
            print(e)

    # CONTAINER INSPECT
    def inspectContainer(resourceId):
        try:
            return cli.inspect_container(resourceId)
        except ResourceWarning as e:
            print(e)
