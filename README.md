# RuSentNE-LLM-Benchmark
[![arXiv](https://img.shields.io/badge/arXiv-2305.17679-b31b1b.svg)](https://arxiv.org/abs/2305.17679)

This repository assess the LLMs reasoning capabilities in Targeted Sentiment Analysis on [RuSentNE](https://arxiv.org/abs/2305.17679) dataset proposed as a part of the 
[self-titled competition](https://github.com/dialogue-evaluation/RuSentNE-evaluation) with results mentioned in paper:
[RuSentNE-2023: Evaluating Entity-Oriented Sentiment Analysis on Russian News Texts](https://arxiv.org/abs/2305.17679)


In particular, we use **pre-treained LLMs** for the following datset splits:
1. 🔓 **Development**
2. 🔒 **Final**

The following **reasoning** we use [[quick-cot]](https://github.com/nicolay-r/quick_cot) to experiment with:
* Instruction Prompts
* Chain-of-Thoughts (THoR): 

## 🔓 Development Results

**Dataset**: [valiation_data_labeled.csv](https://github.com/dialogue-evaluation/RuSentNE-evaluation/blob/main/validation_data_labeled.csv)

| **Model**                    |lang| Mode      | F1(P,N) | F1(P,N,0) | N/A % | Answers   |
|------------------------------|----|-----------|---------|-----------|-------|-----------|
| **GPT-3-0613**               | 🇺🇸 | [CoT THoR](data/thor_cot_schema.json)  | 43.41   | 46.14     | -     | [answers](data/answers/dev/valid_data_en.csv_gpt-3.5-turbo-0613-thor-cot.sqlite) |
| **GPT-3-1106**               | 🇺🇸 | [CoT THoR](data/thor_cot_schema.json)  | 40.85   | 40.04     | -     | [answers](data/answers/dev/valid_data_en.csv_gpt-3.5-turbo-1106-thor-cot.sqlite) |

## 🔒 Final Results
[![arXiv](https://img.shields.io/badge/arXiv-2404.12342-b31b1b.svg)](https://arxiv.org/abs/2404.12342)

**Dataset**: [final_data.csv](https://github.com/dialogue-evaluation/RuSentNE-evaluation/blob/main/final_data.csv)

| **Model**                    |lang| Mode      | F1(P,N) | F1(P,N,0) | N/A % | Answers   |
|------------------------------|----|-----------|---------|-----------|-------|-----------|
| **GPT-4-1106-preview**       | 🇺🇸 | [CoT THoR](data/thor_cot_schema.json)  | 50.13   | 55.93     | -     | [answers](data/answers/final/final_data_en.csv_gpt-4-1106-preview-thor-cot.sqlite) |
| **GPT-3-0613**               | 🇺🇸 | [CoT THoR](data/thor_cot_schema.json)  | 44.50   | 48.17     | -     | [answers](data/answers/final/final_data_en.csv_gpt-3.5-turbo-0613-thor-cot.sqlite) |
| **GPT-3-1106**               | 🇺🇸 | [CoT THoR](data/thor_cot_schema.json)  | 42.58   | 42.18     | -     | [answers](data/answers/final/final_data_en.csv_gpt-3.5-turbo-1106-thor-cot.sqlite) |
||
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
