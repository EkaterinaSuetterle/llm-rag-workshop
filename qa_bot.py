import os
from groq import Groq
from elasticsearch import Elasticsearch
#from groq_key import GROQ_API_KEY


client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

es = Elasticsearch("http://localhost:9200")
index_name = "course-questions"


context_template = """
Section: {section}
Question: {question}
Answer: {text}
""".strip()


prompt_template = """
You're a course teaching assistant.
Answer the user QUESTION based on CONTEXT - the documents retrieved from our FAQ database.
Also use other information outside of the provided CONTEXT,
in case you do not have the CONTEXT.

QUESTION: {user_question}

CONTEXT:

{context}
""".strip()


def retrieve_documents(
        query,
        index_name="course-questions",
        max_results=5,
        course="data-engineering-zoomcamp"
    ):
    search_query = {
        "size": max_results,
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": query,
                        "fields": ["question^3", "text", "section"],
                        "type": "best_fields"
                    }
                },
                "filter": {
                    "term": {
                        "course": course
                    }
                }
            }
        }
    }
    
    response = es.search(index=index_name, body=search_query)
    documents = [hit['_source'] for hit in response['hits']['hits']]
    return documents


def build_context(documents):
    context_result = ""
    
    for doc in documents:
        doc_str = context_template.format(**doc)
        context_result += ("\n\n" + doc_str)
    
    return context_result.strip()


def build_prompt(user_question, documents):
    context = build_context(documents)
    prompt = prompt_template.format(
        user_question=user_question,
        context=context
    )
    return prompt


def ask_groq(prompt, model="llama3-8b-8192"):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    answer = response.choices[0].message.content
    return answer


def qa_bot(user_question):
    context_docs = retrieve_documents(user_question)
    prompt = build_prompt(user_question, context_docs)
    answer = ask_groq(prompt)
    return answer
