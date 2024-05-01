# RuSentNE-LLM-Benchmark • [![twitter](https://img.shields.io/twitter/url/https/shields.io.svg?style=social)](https://twitter.com/nicolayr_/status/1781330684289658933)

This repository assess the LLMs reasoning capabilities in Targeted Sentiment Analysis on **[RuSentNE](https://arxiv.org/abs/2305.17679)** dataset proposed as a part of the 
[self-titled competition](https://github.com/dialogue-evaluation/RuSentNE-evaluation).

In particular, we use **pre-treained LLMs** for the following datset splits:
1. 🔓 **Development**
2. 🔒 **Final**

The following **reasoning** we use [[quick-cot]](https://github.com/nicolay-r/quick_cot) to experiment with:
* Instruction Prompts
* Chain-of-Thoughts (THoR)

## 🔍 Accessing the results

All the `sqlite` results are stored in `contents` table.

**Option 1.** You may use [`sqlitebrowser`](https://sqlitebrowser.org/) for accessing the results for exporting into `CSV`.
![accessability](https://github.com/nicolay-r/RuSentNE-LLM-Benchmark/assets/14871187/aeb063e6-d4d8-43fb-9d26-c22b4ef29d0b)

**Option 2.** Use [`sqlite2csv.py`](sqlite2csv.py) script implemented in this repository.
 
## 🔓 Development Results
[![twitter](https://img.shields.io/twitter/url/https/shields.io.svg?style=social)](https://twitter.com/nicolayr_/status/1781330684289658933)

This is an **open-access dataset split** (sentiment labels available) utilized for the development stage and could be used anyone in evaluation checks. 

**Dataset**: **[valiation_data_labeled.csv](https://github.com/dialogue-evaluation/RuSentNE-evaluation/blob/main/validation_data_labeled.csv)**

| **Model**                    |lang| Mode      | F1(P,N) | F1(P,N,0) | N/A % | Answers   |
|------------------------------|----|-----------|---------|-----------|-------|-----------|
| **GPT-3.5-0613**             | 🇺🇸 | [CoT THoR](data/thor_cot_schema.json)  | 43.41   | 46.14     | -     | [answers](data/answers/dev/valid_data_en.csv_gpt-3.5-turbo-0613-thor-cot.sqlite) |
| **GPT-3.5-1106**             | 🇺🇸 | [CoT THoR](data/thor_cot_schema.json)  | 40.85   | 40.04     | -     | [answers](data/answers/dev/valid_data_en.csv_gpt-3.5-turbo-1106-thor-cot.sqlite) |
| **mistral-7b**               | 🇺🇸 | [CoT THoR](data/thor_cot_schema.json)  |42.74|51.77|0.04|[answers](data/answers/dev/valid_data_en.csv_open-mistral-7b_thor.sqlite)       |

| **Model**                    |lang| Mode      | F1(P,N) | F1(P,N,0) | N/A % | Answers   |
|------------------------------|----|-----------|---------|-----------|-------|-----------|
| **GPT-4-turbo-2024-04-09**   | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt)|50.83|61.25|0.0|[answers](data/answers/dev/valid_data_en.csv_gpt-4-turbo-2024-04-09_prompt.sqlite)|
| **GPT-3.5-0613**             | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |47.39|57.99|0.0 |[answers](data/answers/dev/valid_data_en.csv_gpt-3.5-turbo-0613_prompt.sqlite)  |
| **GPT-3.5-1106**             | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |45.73|52.54|0.0 |[answers](data/answers/dev/valid_data_en.csv_gpt-3.5-turbo-1106_prompt.sqlite)  |
| **mistral-large-latest**     | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |45.24|58.29|0.0 |[answers](data/answers/dev/valid_data_en.csv_mistral-large-latest_prompt.sqlite)          |
||
| **llama-3-70b-instruct**     | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |48.96|60.71|0.0 |[answers](data/answers/dev/valid_data_en.csv_meta_meta-llama-3-70b-instruct_prompt.sqlite)|
| **mixtral-8x22b**            | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |45.94|58.34|0.0 |[answers](data/answers/dev/valid_data_en.csv_open-mixtral-8x22b_prompt.sqlite)  |
| **mixtral-8x7b**             | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |46.31|56.1 |0.07|[answers](data/answers/dev/valid_data_en.csv_open-mixtral-8x7b_prompt.sqlite)   |
| **llama-3-8b-instruct**      | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |45.61|54.88|0.0 |[answers](data/answers/dev/valid_data_en.csv_meta_meta-llama-3-8b-instruct_prompt.sqlite) |
| **mistral-7b**               | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |42.87|53.69|0.11|[answers](data/answers/dev/valid_data_en.csv_open-mistral-7b_prompt.sqlite)     |
| **llama-2-70b-chat**         | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt)|41.97|53.98|13.44|[answers](data/answers/dev/valid_data_en.csv_meta_llama-2-70b-chat_prompt.sqlite)|

| **Model**                    |lang| Mode      | F1(P,N) | F1(P,N,0) | N/A % | Answers   |
|------------------------------|----|-----------|---------|-----------|-------|-----------|
| **GPT-3.5-0613**             | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |44.52|54.67|1.51|[answers](data/answers/dev/valid_data.csv_gpt-3.5-turbo-0613_prompt.sqlite)     |
| **GPT-3.5-1106**             | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |41.46|47.17|0.46|[answers](data/answers/dev/valid_data.csv_gpt-3.5-turbo-1106_prompt.sqlite)     |
| **GPT-4-turbo-2024-04-09**   | 🇷🇺 |[zero-shot](data/prompt_v2_ru.txt)|41.28|55.7 |0.0|[answers](data/answers/dev/valid_data.csv_gpt-4-turbo-2024-04-09_prompt.sqlite)   |
| **mistral-large-latest**     | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |<span style="color:red">22.35</span>|43.09|0.04|[answers](data/answers/dev/valid_data.csv_mistral-large-latest_prompt.sqlite)          |
||
| **llama-3-70b-instruct**     | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |45.21|58.32|0.0 |[answers](data/answers/dev/valid_data.csv_meta_meta-llama-3-70b-instruct_prompt.sqlite)|
| **mixtral-8x22b**            | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |41.49|54.55|0.0 |[answers](data/answers/dev/valid_data.csv_open-mixtral-8x22b_prompt.sqlite)     |
| **mixtral-8x7b**             | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |39.96|53.56|0.18|[answers](data/answers/dev/valid_data.csv_open-mixtral-8x7b_prompt.sqlite)      |
| **mistral-7b**               | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |41.71|47.57|0.18|[answers](data/answers/dev/valid_data.csv_open-mistral-7b_prompt.sqlite)        |
| **llama-3-8b-instruct**      | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |40.23|48.02|0.35|[answers](data/answers/dev/valid_data.csv_meta_meta-llama-3-8b-instruct_prompt.sqlite) |
| **llama-2-70b-chat**         | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt)|16.68|36.77|1.48 |[answers](data/answers/dev/valid_data.csv_meta_llama-2-70b-chat_prompt.sqlite)   |



## 🔒 Final Results
[![arXiv](https://img.shields.io/badge/arXiv-2404.12342-b31b1b.svg)](https://arxiv.org/abs/2404.12342)

This leaderboard and obtained LLM answers is a part of the experiments in paper:
[Large Language Models in Targeted Sentiment Analysis in Russian](https://arxiv.org/abs/2404.12342). 

**Dataset**: **[final_data.csv](https://github.com/dialogue-evaluation/RuSentNE-evaluation/blob/main/final_data.csv)**

| **Model**                    |lang| Mode      | F1(P,N) | F1(P,N,0) | N/A % | Answers   |
|------------------------------|----|-----------|---------|-----------|-------|-----------|
| **GPT-4-1106-preview**       | 🇺🇸 | [CoT THoR](data/thor_cot_schema.json)  | 50.13   | 55.93     | -     | [answers](data/answers/final/final_data_en.csv_gpt-4-1106-preview-thor-cot.sqlite) |
| **GPT-3.5-0613**             | 🇺🇸 | [CoT THoR](data/thor_cot_schema.json)  | 44.50   | 48.17     | -     | [answers](data/answers/final/final_data_en.csv_gpt-3.5-turbo-0613-thor-cot.sqlite) |
| **GPT-3.5-1106**             | 🇺🇸 | [CoT THoR](data/thor_cot_schema.json)  | 42.58   | 42.18     | -     | [answers](data/answers/final/final_data_en.csv_gpt-3.5-turbo-1106-thor-cot.sqlite) |
||
| **GPT-4-1106-preview**       | 🇺🇸 | [zero-shot (short)](data/prompt_v2_short_en.txt) | 54.59   | 64.32     | -     | [answers](data/answers/final/final_data_en.csv_gpt-4-1106-preview.sqlite) |
| **GPT-3.5-0613**             | 🇺🇸 | [zero-shot (short)](data/prompt_v2_short_en.txt) | 51.79   | 61.38     | -     | [answers](data/answers/final/final_data_en.csv_gpt-3.5-turbo-0613-en-se.sqlite) |
| **GPT-3.5-1106**             | 🇺🇸 | [zero-shot (short)](data/prompt_v2_short_en.txt) | 47.04   | 53.19     | -     | [answers](data/answers/final/final_data_en.csv_gpt-3.5-turbo-1106.sqlite) |
||
| **Mistral-7B-instruct-v0.1** | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) | 49.46   | 58.51     | -     | [answers](data/answers/final/final_data_en.csv_mistralai_Mistral-7B-Instruct-v0.1.sqlite) |
| **Mistral-7B-instruct-v0.2** | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) | 44.82   | 56.04     | -     | [answers](data/answers/final/final_data_en.csv_mistralai_Mistral-7B-Instruct-v0.2.sqlite) |
| **DeciLM**                   | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) | 43.85   | 53.65     | 1.44  | [answers](data/answers/final/final_data_en.csv_Deci_DeciLM-7B-instruct.sqlite) |
| **Microsoft-Phi-2**          | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) | 40.95   | 42.77     | 3.13  | [answers](data/answers/final/final_data_en.csv_microsoft_phi-2.sqlite) |
| **Gemma-7B-IT**              | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) | 40.96   | 44.63     | -     | [answers](data/answers/final/final_data_en.csv_google_gemma-7b-it.sqlite) |
| **Gemma-2B-IT**              | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) | 31.75   | 45.96     | 2.62  | [answers](data/answers/final/final_data_en.csv_google_gemma-2b-it.sqlite) |
| **Flan-T5-xxl**              | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) | 36.46   | 42.63     | 1.90  | [answers](data/answers/final/final_data_en.csv_google_flan-t5-xxl.sqlite) |

| **Model**                    |lang| Mode      | F1(P,N) | F1(P,N,0) | N/A % | Answers      |
|------------------------------|----|-----------|---------|-----------|-------|--------------|
| **GPT-4-1106-preview**       | 🇷🇺 | [zero-shot (short)](data/prompt_v2_short_ru.txt) | 48.04   | 60.55     | 0.0   | [answers](data/answers/final/final_data.csv_gpt-4-1106-preview.sqlite) |
| **GPT-3.5-0613**             | 🇷🇺 | [zero-shot (short)](data/prompt_v2_short_ru.txt) | 45.85   | 57.36     | 0.0   | [answers](data/answers/final/final_data.csv_gpt-3.5-turbo-0613.sqlite) |
| **GPT-3.5-1106**             | 🇷🇺 | [zero-shot (short)](data/prompt_v2_short_ru.txt) | 35.07   | 48.53     | 0.0   | [answers](data/answers/final/final_data.csv_gpt-3.5-turbo-1106.sqlite) |
||
| **Mistral-7B-Instruct-v0.2** | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) | 42.60   | 48.05     | 0.0   | [answers](data/answers/final/final_data.csv_mistralai_Mistral-7B-Instruct-v0.2.sqlite) |


### References

If you find the results and findings in **Final Results** section valuable 💎, feel free to cite the related work as follows:
```bibtex
@misc{rusnachenko2024large,
      title={Large Language Models in Targeted Sentiment Analysis}, 
      author={Nicolay Rusnachenko and Anton Golubev and Natalia Loukachevitch},
      year={2024},
      eprint={2404.12342},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

