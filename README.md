# Python miscellany

There are three areas where Python is used:

1. Advanced Python Syntax
2. Neural networks and deep learning
3. Python’s different ecosystems and libraries


## `# %%` python interactive window
[Jupyter code cells](https://code.visualstudio.com/docs/python/jupyter-support-py)

## regular expression and wildcards

## DS DeepSeek-Math deployment steps

This repository explains how to download and run the DeepSeek-Math 7B Instruct model locally. The instructions assume Ubuntu on x86 with an NVIDIA GPU (such as the 3080 Ti).

### 1. Create and activate a Conda environment
```bash
conda create -n deepseek python=3.11
conda activate deepseek
```

### 2. Install Python dependencies
```bash
pip install torch==2.2.1 transformers==4.40.2 accelerate==0.29.1 sentencepiece
```
Ensure that the correct NVIDIA drivers and CUDA toolkit are installed for GPU support.

### 3. Clone the model repository with Git LFS
```bash
sudo apt-get install git-lfs
git lfs install
git clone https://huggingface.co/deepseek-ai/deepseek-math-7b-instruct
```

If your network restricts access to `huggingface.co`, configure a proxy or otherwise obtain the model files.

### 4. Load the model in Python
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "deepseek-ai/deepseek-math-7b-instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto",
)

inputs = tokenizer("Your question here", return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=128)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### 5. Optional optimizations
For faster inference, you can explore Hugging Face's `accelerate` utilities, quantization with `bitsandbytes`, or specialized inference frameworks such as `vllm` or `text-generation-inference`.


