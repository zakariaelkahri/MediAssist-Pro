from langchain_community.document_loaders import TextLoader

loader = TextLoader("../../data/processed/manual.md", encoding="utf-8")
docs = loader.load()