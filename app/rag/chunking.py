from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter
)

def hybrid_chunk(text):

    # STEP 1 — structure split
    md_splitter = MarkdownHeaderTextSplitter([
        ("#", "Chapter"),
        ("##", "Section"),
        ("###", "Subsection"),
    ])
    
    structured_docs = md_splitter.split_text(text)

        # STEP 2 — recursive semantic split
    recursive_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    
    final_chunks = []

    for doc in structured_docs:
        sub_chunks = recursive_splitter.split_text(doc.page_content)

        for chunk in sub_chunks:
            final_chunks.append({
                "content": chunk,
                "metadata": doc.metadata
            })

    return final_chunks

