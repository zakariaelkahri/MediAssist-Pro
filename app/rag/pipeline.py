from app.rag.retriever import retriever
from app.rag.llm import llm
from app.rag.prompt import structured_prompt_template

def answer_question(user_question: str) -> str:
    docs = retriever.invoke(user_question)
    
    context = "\n\n".join([doc.page_content for doc in docs])
    
    formatted_prompt = structured_prompt_template.format(
        context=context,
        question=user_question
    )
    
    response = llm.generate_content(formatted_prompt)
    
    return response.text

answer = answer_question("CONDITIONS REQUISES POUR L'INSTALLATION de balances")
print(answer)
