# Generative_AI_for_NLP
## Overview
Welcome to the repository that explores Generative Artificial Intelligence (AI) techniques in Natural Language Processing (NLP). This repository is a central hub for various research and works on generating and understanding human-like text using AI models.

## About
Generative AI has revolutionized Natural Language Processing by enabling machines to generate coherent and contextually relevant text. From language generation to translation, summarization, and dialogue systems, generative models have demonstrated remarkable capabilities in understanding and producing human-like language. This repository aims to showcase different approaches, and algorithms of Generative AI specifically tailored to the domain of NLP.

## Techniques
### 1. Transformers
### 2. Transformer based Architecture
#### 2a. Encoder-Decoder Architecture  
- The Encoder-Decoder architecture was the original transformer architecture introduced in the Attention Is All You Need paper.
- It works as follows: the encoder (on the left) processes the input sequence and generates a hidden representation that summarizes the input information. The decoder (on the right) uses this hidden representation to generate the desired output sequence.
  ![image](https://www.practicalai.io/wp-content/uploads/2023/02/encoder-decoder.png)
- Suitable for Language Translation, Text Summarization, Question Answering, etc.
- Example models using this architecture are:
    - T5 – [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/pdf/1910.10683)
    - BART: [Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://arxiv.org/abs/1910.13461)
    - Longformer: [The Long-Document Transformer](https://arxiv.org/pdf/2004.05150)

#### 2b. Encoder only Architecture  
- It only has the encoder part of the original transformer architecture.
- It is used when only encoding the input sequence is required and the decoder is not necessary.
- Here the input sequence is encoded into a fixed-length representation and then used as input to a classifier or a regressor to make a prediction.
- These models have a pre-trained general-purpose encoder but will require fine-tuning of the final classifier or regressor.
  ![image](https://www.practicalai.io/wp-content/uploads/2023/02/bert.png)
- Cannot generate text( only understand the text).
- Suitable for Text classification, Sentiment analysis, Named entity recognition, etc.
- Example models using this architecture are:
    - [BERT](https://arxiv.org/abs/1810.04805)
    - [DistilBERT](https://arxiv.org/abs/1910.01108)
    - [RoBERTa](https://arxiv.org/abs/1907.11692)

#### 2c. Decoder only Architecture  
- In the Decoder-only architecture, the model consists of only a decoder, which is trained to predict the next token in a sequence given the previous tokens. 
- The main contrast between Decoder-only and Encoder-Decoder architectures lies in how they handle input information. In Decoder-only models, there's no separate encoder to summarize input data. Instead, the decoder indirectly encodes this information within its hidden state as it generates output step by step.
- Suitable for Text completion, Text generation, Translation, Question-Answering, Generating image captions, etc.
- Example models using this architecture are:
    - [Generative Pre-Training models](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf) also called GPT models such as GPT-3, ChatGPT and GPT-J.
    - [Google LaMDA](https://arxiv.org/pdf/2201.08239)
    - OPT: [Open Pre-trained Transformer Language Models](https://arxiv.org/abs/2205.01068)
    - BLOOM: [BigScience Large Open-science Open-access Multilingual Language Model](https://bigscience.huggingface.co/blog/bloom)

### 3. Large Language Models
### 4. Vector Databases
### 5. Many More

## Contact
For questions, suggestions, or collaborations, feel free to reach out to the repository owner [suraj.karki500@gmail.com](mailto:suraj.karki500@gmail.com)

Happy Coding!
