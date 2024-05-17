# Jupyter Notebook

### Podman
- `podman build -t pytorch-jupyter -f docker/Model-Dockerfile .`
- `podman run -p 8888:8888 -v $(pwd):/workspace:Z pytorch-jupyter`

- If you installed the Nvidia Container Toolkit and wish to use GPU: (see https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

- `podman run --hooks-dir=/usr/share/containers/oci/hooks.d --gpus all -p 8888:8888 -v $(pwd):/workspace:z pytorch-jupyter`

NOTE: If you created this container and have since updated your drivers, you'll need to regenerate the CDI specification with `sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml`

### Docker
- `sudo docker buildx build -t pytorch-jupyter -f docker/Model-Dockerfile .`
- `sudo docker run -p 8888:8888 -v $(pwd):/workspace pytorch-jupyter` though on Windows you'll need to use Powershell and `docker run -p 8888:8888 -v ${PWD}:/workspace pytorch-jupyter`

- If you installed the Nvidia Container Toolkit and wish to use GPU: (see https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)
- `sudo docker run --runtime=nvidia --gpus all -p 8888:8888 -v $(pwd):/workspace pytorch-jupyter`
