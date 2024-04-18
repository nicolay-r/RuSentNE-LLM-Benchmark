# RuSentNE-LLM-Benchmark
[![arXiv](https://img.shields.io/badge/arXiv-2305.17679-b31b1b.svg)]()


This repository assess the LLMs reasoning capabilities in Targeted Sentiment Analysis on [RuSentNE](https://arxiv.org/abs/2305.17679) dataset proposed as a part of the [self-titled competitions](https://github.com/dialogue-evaluation/RuSentNE-evaluation). 

In particular, we use **pre-treained LLMs** for the following datset splits:
1. 🔓 [Development](#development-results)
2. 🔒 [Final](#final-results) [![arXiv](https://img.shields.io/badge/arXiv-2305.17679-b31b1b.svg)]()

The following **reasoning** are used:
* Instruction Prompts
* Chain-of-Thoughts (THoR)

## 🔓 Development Results


## 🔒 Final Results
[![arXiv](https://img.shields.io/badge/arXiv-2305.17679-b31b1b.svg)]()

| **Model**                    |lang| Mode      | F1(P,N) | F1(P,N,0) | N/A % | Answers   |
|------------------------------|----|-----------|---------|-----------|-------|-----------|
| **GPT-4-1106-preview**       | 🇺🇸 | zero-shot | 54.59   | 64.32     | -     | [answers](data/answers/final/final_data_en.csv_gpt-4-1106-preview.sqlite) |
| **GPT-3-0613**               | 🇺🇸 | zero-shot | 51.79   | 61.38     | -     | [answers](data/answers/final/final_data_en.csv_gpt-3.5-turbo-0613-en-se.sqlite) |
| **GPT-3-1106**               | 🇺🇸 | zero-shot | 47.04   | 53.19     | -     | [answers](data/answers/final/final_data_en.csv_gpt-3.5-turbo-1106.sqlite) |
| **Mistral-7B-instruct-v0.1** | 🇺🇸 | zero-shot | 49.46   | 58.51     | -     | [answers](data/answers/final/final_data_en.csv_mistralai_Mistral-7B-Instruct-v0.1.sqlite) |
| **Mistral-7B-instruct-v0.2** | 🇺🇸 | zero-shot | 44.82   | 56.04     | -     | [answers](data/answers/final/final_data_en.csv_mistralai_Mistral-7B-Instruct-v0.2.sqlite) |
| **DeciLM**                   | 🇺🇸 | zero-shot | 43.85   | 53.65     | 1.44  | [answers](data/answers/final/final_data_en.csv_Deci_DeciLM-7B-instruct.sqlite) |
| **Microsoft-Phi-2**          | 🇺🇸 | zero-shot | 40.95   | 42.77     | 3.13  | [answers](data/answers/final/final_data_en.csv_microsoft_phi-2.sqlite) |
| **Gemma-7B-IT**              | 🇺🇸 | zero-shot | 40.96   | 44.63     | -     | [answers](data/answers/final/final_data_en.csv_google_gemma-7b-it.sqlite) |
| **Gemma-2B-IT**              | 🇺🇸 | zero-shot | 31.75   | 45.96     | 2.62  | [answers](data/answers/final/final_data_en.csv_google_gemma-2b-it.sqlite) |
| **Flan-T5-xxl**              | 🇺🇸 | zero-shot | 36.46   | 42.63     | 1.90  | [answers](data/answers/final/final_data_en.csv_google_flan-t5-xxl.sqlite) |

| **Model**                    | lang | Mode      | F1(P,N) | F1(P,N,0) | N/A % | Answers      |
|------------------------------|------|-----------|---------|-----------|-------|--------------|
| **GPT-4-1106-preview**       |  🇷🇺  | zero-shot | 48.04   | 60.55     | 0.0   | [answers](data/answers/final/final_data.csv_gpt-4-1106-preview.sqlite) |
| **GPT-3-0613**               |  🇷🇺  | zero-shot | 45.85   | 57.36     | 0.0   | [answers](data/answers/final/final_data.csv_gpt-3.5-turbo-0613.sqlite) |
| **GPT-3-1106**               |  🇷🇺  | zero-shot | 35.07   | 48.53     | 0.0   | [answers](data/answers/final/final_data.csv_gpt-3.5-turbo-1106.sqlite) |
| **Mistral-7B-Instruct-v0.2** |  🇷🇺  | zero-shot | 42.60   | 48.05     | 0.0   | [answers](data/answers/final/final_data.csv_mistralai_Mistral-7B-Instruct-v0.2.sqlite) |