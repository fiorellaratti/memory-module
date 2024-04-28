from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate
from langchain_community.llms import LlamaCpp
from llm_demos.llama2.imp_prompt import importance_prompt
import re
import json
# Callbacks support token-wise streaming
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

# Verbose is required to pass to the callback manager
# Make sure the model path is correct for your system!
# llm = LlamaCpp(
#     model_path="/home/frattitamayo/.cache/huggingface/hub/models--NousResearch--Hermes-2-Pro-Mistral-7B-GGUF/snapshots/594e3e33f57a2b8693972e6bf48ae4eff404f170/Hermes-2-Pro-Mistral-7B.Q5_K_M.gguf",
#     callback_manager=callback_manager,
#     verbose=True,
#     n_ctx=2048,
#     max_new_tokens = 16,
# #    f16_kv=True,
#     n_gpu_layers=-1,        
# )
llm = LlamaCpp(
    model_path="/home/frattitamayo/.cache/huggingface/hub/models--NousResearch--Hermes-2-Pro-Mistral-7B-GGUF/snapshots/594e3e33f57a2b8693972e6bf48ae4eff404f170/Hermes-2-Pro-Mistral-7B.Q5_K_M.gguf",
    callback_manager=callback_manager,
    verbose=True,
    n_ctx=2048,
    n_gpu_layers=33, # How many layers to offload to gpu?
)



# You can use this in any langchain prompt in place of your existing llm
def chatml_sys_user_prompt(prompt: str):
    p_lines = prompt.split("\n")
    sys, user = p_lines[0], "\n".join(p_lines[1:])
    return f"""
<|im_start|>system
{sys}<|im_end|>
<|im_start|>user
{user}<|im_end|>
<|im_start|>assistant
"""

def importance_f(query, obs):
    print(query, obs)
    importance_str = importance_prompt.replace("$OBSERVATION$", obs)
    importance_str = importance_str.replace("$QUERY$", query)
    while True:
        response = llm.invoke(chatml_sys_user_prompt(importance_str))
        number = re.findall(r'I: ([+-]?[0-9]*\.?[0-9]+)', response)
        if number and 10 >= float(number[0]) >= 0 : # 
            importance = float(number[0])/10
            return importance


__NOTEBANK_REGEX = re.compile(r'\`\`\`json([^\`]*)\`\`\`')
def classification(prompt):
    while True:
        response = llm.invoke(chatml_sys_user_prompt(prompt))
        regex_match = __NOTEBANK_REGEX.findall(response)  
        if regex_match:
            regex_match = regex_match[0].replace("```json", "").replace("```", "").strip()
        prompt_data = regex_match if regex_match else response
        try:
            actions = json.loads(prompt_data)
            if "intent" in actions:
                return actions["intent"]
            if "uptake" in actions:
                return actions["uptake"]
            if "question" in actions:
                return actions["question"]
        except:
            continue