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

-> then run the command "pipenv run jupyter notebook"
-> now we create an elastic search (is a text search engine) image (Docker) with the following code in a new terminal:
    docker run -it \
    --rm \
    --name elasticsearch \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    docker.elastic.co/elasticsearch/elasticsearch:8.4.3
-> --rm \ is for deleting the container once we ended our CodeSpace

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

-> To commit something (for the whole project):
    OPTIONAL
        cd path/to/your/project
    Only for some docs
        git add path/to/file
    For all docs in the branch
        git add .
    git commit -m "Fixed bug in user login feature"
    git push

-> Groq instead of OpenAI...
-> Building an interface with streamlit
-> TRY TO ANALYZE why I do not have the same answers like he: I should have a look on the document_context

Now it's time for an opensource LLM:
-> ollama
    curl -fsSL https://ollama.com/install.sh | sh
    ollama start
    ollama serve phi3

-> we created a new codespace for it (more powerfull)

-> run jupyter notebook, indexing the data, run the app, because indexing is made in Jupater Notebook
    -> It is surely possible to programme an index in the VCS





