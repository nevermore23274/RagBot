# RAG Bot
A few basic RAG books.

# Jupyter Notebook

### Podman
- `podman build -t pytorch-jupyter -f docker/Dockerfile .`
- `podman run -p 8888:8888 -v $(pwd):/workspace:Z pytorch-jupyter`

- Navigate to: 
`http://localhost:8888/`

- If you installed the Nvidia Container Toolkit and wish to use GPU: (see https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

- `podman run --hooks-dir=/usr/share/containers/oci/hooks.d --gpus all -p 8888:8888 -v $(pwd):/workspace:z pytorch-jupyter`

NOTE: If you created this container and have since updated your drivers, you'll need to regenerate the CDI specification with `sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml`

### Docker
- `sudo docker buildx build -t pytorch-jupyter -f docker/Dockerfile .`
- `sudo docker run -p 8888:8888 -v $(pwd):/workspace pytorch-jupyter`

- Navigate to: 
`http://localhost:8888/`

- If you installed the Nvidia Container Toolkit and wish to use GPU: (see https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)
- `sudo docker run --runtime=nvidia --gpus all -p 8888:8888 -v $(pwd):/workspace pytorch-jupyter`

# Useful links:
- https://pytorch.org/tutorials/beginner/introyt/modelsyt_tutorial.html
- https://pytorch.org/tutorials/recipes/recipes_index.html
- https://index.quantumstat.com/
- https://github.com/niderhoff/nlp-datasets
- https://paperswithcode.com/
- https://poshcode.gitbook.io/powershell-practice-and-style/style-guide/documentation-and-comments
- https://www.youtube.com/watch?v=tHL5STNJKag
