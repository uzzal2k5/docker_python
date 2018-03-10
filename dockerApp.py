from docker_python.dockerConnect import cli
from docker_python.dockerClass import DockerPythonClass as dpc


print("Detail OF A Container - \n")
container = cli.containers()
containerId = container[0]['Id']
print(containerId)
print("INSPECT CONTAINER :", containerId, "\n\n", dpc.inspectContainer(containerId))


# print("DOCKER ENGINE INFORMATION  \n",cli.info())


#  DOCKER VOLUME
print("All Volume Details - \n")
volume_list = dpc.getAllVolumes(self='')
print(volume_list)



# ALL CONTAINER
print("All COntainer Information - ")
container_list = dpc.getAllContainers(self='')
print(container_list)

# ALL Images Details

print("All Images Details - ")
image_list = dpc.getAllImages(self='')
print(image_list)
