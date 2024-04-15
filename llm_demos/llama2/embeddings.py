# from langchain_community.embeddings import LlamaCppEmbeddings
# from langchain_community.embeddings import llamacpp
# from llama_cpp import Llama
import numpy as np


# Make sure the model path is correct for your system!
# llm = llamacpp.LlamaCppEmbeddings(
#     model_path="/home/frattitamayo/memory_module/llm_demos/models/llama-2-13b.Q4_K_M.gguf",
#     # model_path="/home/frattitamayo/.cache/huggingface/hub/models--NousResearch--Hermes-2-Pro-Mistral-7B-GGUF/snapshots/594e3e33f57a2b8693972e6bf48ae4eff404f170/Hermes-2-Pro-Mistral-7B.Q5_K_M.gguf",
#     verbose=True,
#     n_gpu_layers=-1,
# )

from llama_cpp import Llama


llm = Llama(model_path="/home/frattitamayo/.cache/huggingface/hub/models--NousResearch--Hermes-2-Pro-Mistral-7B-GGUF/snapshots/594e3e33f57a2b8693972e6bf48ae4eff404f170/Hermes-2-Pro-Mistral-7B.Q5_K_M.gguf", embedding=True)

# Example texts.
texts = [
    "Hello, my name is Gene",
    "Goodbye, see you tomorrow",
    "This is a sentence"
]



# Run texts.

def llama_embed(texts):
    results = llm.create_embedding(texts)
    return np.array([r['embedding'] for r in results.get("data")])



individual_results = [
    llama_embed(text)
    for text
    in texts
]

