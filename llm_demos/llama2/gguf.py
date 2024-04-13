from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate
from langchain_community.llms import LlamaCpp
from llm_demos.llama2.imp_prompt import importance_prompt
import re

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
    importance = importance_prompt.replace("$OBSERVATION$", obs)
    importance = importance.replace("$QUERY$", query)
    response = llm.invoke(importance)
    number = re.findall(r'I: ([+-]?[0-9]*\.?[0-9]+)', response)
    if number:
        return float(number[0])
    else:
        return 0