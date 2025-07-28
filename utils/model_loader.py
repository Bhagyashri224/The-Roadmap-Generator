from ctransformers import AutoModelForCausalLM

def load_model():
    model = AutoModelForCausalLM.from_pretrained(
        './model/llama-2-7b-chat.Q3_K_M.gguf',
        model_type='llama',
        config={'max_new_tokens': 512, 'temperature': 0.7}
    )
    return model