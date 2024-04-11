from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate
from langchain_community.llms import LlamaCpp

# Callbacks support token-wise streaming
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

# Verbose is required to pass to the callback manager
# Make sure the model path is correct for your system!
llm = LlamaCpp(
    model_path="/home/frattitamayo/.cache/huggingface/hub/models--NousResearch--Hermes-2-Pro-Mistral-7B-GGUF/snapshots/594e3e33f57a2b8693972e6bf48ae4eff404f170/Hermes-2-Pro-Mistral-7B.Q5_K_M.gguf",
    callback_manager=callback_manager,
    verbose=True,
    n_ctx=2048,
#    f16_kv=True,
    n_gpu_layers=41,
)


# You can use this in any langchain prompt in place of your existing llm

def importance_f(query, obs):
    # Ensure the prompt is clear about only returning a number
    importance = importance_prompt
    
    #add examples, describe query and prior , description first, format, examples. (really nice or mean)
    
    # Invoke the model with the formatted prompt
    response = llm.invoke(importance)
    return response