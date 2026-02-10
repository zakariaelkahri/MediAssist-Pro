# from langchain_community.llms import HuggingFacePipeline
# from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
# from app.rag.llm import model, tokenizer

# save_path = "./data/models"

# tokenizer = AutoTokenizer.from_pretrained(save_path)
# model = AutoModelForCausalLM.from_pretrained(
#     save_path,
#     device_map="auto",
# )

# pipe = pipeline(
#      "text-generation",
#      model=model,
#      tokenizer=tokenizer,
#      max_new_tokens=512,
#  )


# llm = HuggingFacePipeline(pipeline=pipe)

# print("LLM loaded successfully")