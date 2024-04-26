# RAG Bot
This is a basic RAG based model(s) I've made just to learn how. I've left the `training-repos.txt` empty, so you'll need to populate it as is needed. (just pay attention to licensing if you intend on handing out your model) It reads top down, so just paste the repositories with no delimiters. (aka, paste then press enter) Note that unless you take additional steps, this will use your CPU.

First step is to hop in and run the notebook, then you can navigate to the streamlit container for the web application.

# Jupyter Notebook

- `podman build -t pytorch-jupyter -f docker/Dockerfile .`
- `podman run -p 8888:8888 -v $(pwd):/workspace:Z pytorch-jupyter`

- Navigate to: 
`http://localhost:8888/notebooks/Bot-Helper.ipynb#`

- If you installed the Nvidia Container Toolkit and wish to use GPU: (see https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

- `podman run --hooks-dir=/usr/share/containers/oci/hooks.d --gpus all -p 8888:8888 -v $(pwd):/workspace:z pytorch-jupyter`

NOTE: If you created this container and have since updated your drivers, you'll need to regenerate the CDI specification with `sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml`

# Streamlit Interface

- `podman build -t pytorch-jupyter-app -f appDocker/Dockerfile .`
- `podman run --user root -p 8501:8501 -p 5000:5000 -v $(pwd):/usr/src/app:Z -v $(pwd)/nltk_data:/root/nltk_data -v $(pwd)/data:/usr/src/app/data:Z pytorch-jupyter-app`

- Navigate to: 
`http://localhost:8501/`

# Useful links:
- https://pytorch.org/tutorials/beginner/introyt/modelsyt_tutorial.html
- https://pytorch.org/tutorials/recipes/recipes_index.html
- https://index.quantumstat.com/
- https://github.com/niderhoff/nlp-datasets
- https://paperswithcode.com/
- https://poshcode.gitbook.io/powershell-practice-and-style/style-guide/documentation-and-comments
- https://www.youtube.com/watch?v=tHL5STNJKag
