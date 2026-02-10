from langchain_huggingface import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline


model_id = "mistralai/Mistral-7B-Instruct-v0.2"
save_path = "./data/models"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
)


pipe = pipeline(
     "text-generation",
     model=model,
     tokenizer=tokenizer,
     max_new_tokens=512,
 )


llm = HuggingFacePipeline(pipeline=pipe)

# model.save_pretrained(save_path)
# tokenizer.save_pretrained(save_path)