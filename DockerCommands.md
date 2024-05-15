Jupyter Notebook

podman build -t pytorch-jupyter -f docker/Dockerfile .
podman run -p 8888:8888 -v $(pwd):/workspace:Z pytorch-jupyter

sudo docker buildx build -t pytorch-jupyter -f Dockerfile .
sudo docker run -p 8888:8888 -v $(pwd):/workspace pytorch-jupyter

Navigate to:
http://localhost:8888

If you installed toolkit and wish to use GPU:

podman run --hooks-dir=/usr/share/containers/oci/hooks.d --gpus all -p 8888:8888 -v $(pwd):/workspace:z pytorch-jupyter
sudo docker run --runtime=nvidia --gpus all -p 8888:8888 -v $(pwd):/workspace pytorch-jupyter
