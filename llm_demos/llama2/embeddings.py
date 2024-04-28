# from langchain_community.embeddings import LlamaCppEmbeddings
# from langchain_community.embeddings import llamacpp
from llama_cpp import Llama
import numpy as np
# from llama_cpp import Llama


llm = Llama(
    model_path="/home/frattitamayo/.cache/huggingface/hub/models--NousResearch--Hermes-2-Pro-Mistral-7B-GGUF/snapshots/594e3e33f57a2b8693972e6bf48ae4eff404f170/Hermes-2-Pro-Mistral-7B.Q5_K_M.gguf", 
            embedding=True,
            n_gpu_layers=16
            )

# Example texts.
texts = [
    "Hello, my name is Gene",
    "Goodbye, see you tomorrow",
    "This is a sentence"
]

# Run texts.

def llama_embed(texts):
    if isinstance(texts, str):
        print("Wrapping")
        texts = [texts]
    results = llm.create_embedding(texts)
    return np.array([r['embedding'] for r in results.get("data")])

# individual_results = np.array([
#     llama_embed(text)
#     for text
#     in texts
# ])

results = llama_embed("Gene Kim is awesome")

print(results, results.shape)
# print(group_results, individual_results.shape)


