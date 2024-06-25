# llm-rag-workshop

-> MAIN DOCUMENTATION https://github.com/alexeygrigorev/llm-rag-workshop

-> pipenv wird benutzt, wenn wir nicht über Codespaces (GitHub) gehen
-> pip install ... elasticsearch wenn wir das über Codespaces machen (zuerst Repo erstellen, dann ein Codespace)
-> openai-Konto ist auch wichtig, allerdings kann man es durch eine OpenSource ersetzen (eventuell HuggingFace?)
-> man kann es auch lokal laufen lasen, vor allem wenn man über virenv vorgeht, und zwar mit Docker

-> creating a .envrc file, out a secret OpenAI-key in it with the following code "export OPENAI_API_KEY="TOKEN" "
    ignore it in .gitignore

-> install some libs 
    sudo apt update
    sudo apt install direnv 
    direnv hook bash >> ~/.bashrc
-> then reset the terminal
    and write direnv allow
    we should get the message
    "direnv: loading /workspaces/llm-rag-workshop/.envrc
    direnv: export +OPENAI_API_KEY"

-> then run the command "pipenv run jupater notebook"
-> now we create an elastic search (is a text search engine) image (Docker) with the following code in a new terminal:
    docker run -it \
    --rm \
    --name elasticsearch \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    docker.elastic.co/elasticsearch/elasticsearch:8.4.3

-> If you get "Elasticsearch has quit unexpectedly", give it more RAM:

    docker run -it \
    --rm \
    --name elasticsearch \
    -m 2G \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    docker.elastic.co/elasticsearch/elasticsearch:8.4.3

-> Then we change the host:
    curl http://localhost:9200

-> Further steps are dosumented in Jupyter Notebook

-> Analyzer in elastic search is by default case insensitive an dturns everything in lower case.
    It also drops all the "meaningless" words like 'a', 'the', probably 'can', etc.





