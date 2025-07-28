#!/bin/bash

# Create model directory if it doesn't exist
mkdir -p model

# Download the model file
echo "Downloading LLaMA-2 GGUF model..."
wget -O model/llama-2-7b-chat.Q3_K_M.gguf \
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q3_K_M.gguf

echo "✅ Model downloaded to model/llama-2-7b-chat.Q3_K_M.gguf"