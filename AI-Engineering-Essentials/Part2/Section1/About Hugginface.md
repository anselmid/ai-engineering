# About Huggingface

Huggingface has a hub for:

1. **Models**: Includes models such as Meta's Llama and DeepSeek, and also user models and user enhancements to say Llama and others to solve specific purposes.
2. **Spaces**: Spaces allows you to build applications and deploy them to HF for people to use them. Applications can be built with Streamlit.
3. **Data Sets**: Curated datasets that are uploaded for example by Nvidia and others. It is similar to Kaggle which also has a heap of open-source datasets.

Huggingface offers a compute service to deploy their models to, or it integrates with AWS or Azure. The naming convention is `company/model` e.g. `meta/llama-3.1`. To find a particular model you use the filters on the left.

## Section 1: Models

### Base Models and Instruct Models

A lot of model names have the word Instruct in them. For example `meta-llama/llama-3.1-8B` (the base model) and `llama/llama-3.1-8B-Instruct`. The base model is designed to generate content e.g. answer questions based on the context provided. The base models are fine tuned to follow instructions. Instruction models are further fine tuned to learn how to follow instructions. The key difference lies in their training and intended use:

#### Base Model (Llama-3.1-8B)

- Trained only on next-token prediction using large text corpora
- Completes text based on patterns it learned - it continues whatever you start
- Not aligned to follow instructions or have conversations
- Outputs can be unpredictable, might not answer questions directly
- Better for: fine-tuning for specific tasks, research, understanding raw model capabilities

#### Instruct Model (Llama-3.1-8B-Instruct)

- Takes the base model and adds additional training (typically RLHF - Reinforcement Learning from Human Feedback, or supervised fine-tuning)
- Trained to follow instructions, answer questions, and have helpful conversations
- Aligned with human preferences for helpfulness, harmlessness, and honesty
- Responds directly to queries rather than just completing text
- Better for: chatbots, Q&A, general assistant tasks, direct deployment

#### Example:

If you prompt: "The capital of France is"

- **Base model** might continue: "Paris, which is located in the north-central part of the country..."
- **Instruct model** might respond: "The capital of France is Paris."

If you prompt: "Write a poem about cats"

- **Base model** might just continue with random text or complete it oddly
- **Instruct model** will actually write you a poem about cats

The instruct model is what most people want for practical applications, while base models are primarily used by researchers or developers who want to fine-tune them for specialized tasks.

**Note:** Meta's models are gated in that you have to ask for access.

## Section 2: Data Sets

It is very similar to Kaggle. The datasets here are more large scale and custom made for heavy machine learning tasks. It has datasets from Amazon e.g. Amazon review for 2023.

They don't need to be downloaded. You can use the API to call these datasets programmatically.

## Section 3: Spaces

Spaces allow you to upload your applications built with Streamlit or Gradio.

Search on Arena to find rankings for different models. For example `lmarena-ai/chatbot-arena` ranks chatbots based on thousands of blind tests of human use.