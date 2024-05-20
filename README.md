# RAG Bot
A few basic RAG books.

If you want to run the containers individually then see the [container document](https://github.com/nevermore23274/RagBot/blob/main/ContainerCommands.md), otherwise you should only need:

For CPU:
```
sudo docker-compose up --build
```

- NOTE: Only use GPU if you've installed https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

For GPU:
```
docker-compose -f docker-compose.yml -f docker-compose.gpu.yml up --build
```

This will build both containers, which will be located at either `127.0.0.1:8888` or `localhost:8501` in a browser.

# Useful links:
- https://pytorch.org/tutorials/beginner/introyt/modelsyt_tutorial.html
- https://pytorch.org/tutorials/recipes/recipes_index.html
- https://index.quantumstat.com/
- https://github.com/niderhoff/nlp-datasets
- https://paperswithcode.com/
- https://poshcode.gitbook.io/powershell-practice-and-style/style-guide/documentation-and-comments
- https://www.youtube.com/watch?v=tHL5STNJKag
