# RuSentNE-LLM-Benchmark • [![twitter](https://img.shields.io/twitter/url/https/shields.io.svg?style=social)](https://twitter.com/nicolayr_/status/1781330684289658933)

> **Update 23 June 2024**: All metrics in Development mode has been evaluated under `closest` mode which
> makes a decision of the result class by relying on the **first entry** of the label.
 
> **Update 11 June 2024**: Added evaluation mode that counts first label entry. See `eval-mode` parameter key.

This repository assess the LLMs reasoning capabilities in Targeted Sentiment Analysis on **[RuSentNE](https://arxiv.org/abs/2305.17679)** dataset proposed as a part of the 
[self-titled competition](https://github.com/dialogue-evaluation/RuSentNE-evaluation).

In particular, we use **pre-treained LLMs** for the following datset splits:
1. 🔓 **Development*~~~~*
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

`*` -- denotes evaluation in `first-entry` mode (seeking for the first entry).

| **Model**                    |lang| Mode      | F1(P,N) | F1(P,N,0) | N/A % | Answers   |
|------------------------------|----|-----------|---------|-----------|-------|-----------|
| **GPT-3.5-0613**             | 🇺🇸 | [CoT THoR](data/thor_cot_schema.json)  |43.46|46.16|0.21|[answers](data/answers/dev/valid_data_en.csv_gpt-3.5-turbo-0613-thor-cot.sqlite)
| **GPT-3.5-1106**             | 🇺🇸 | [CoT THoR](data/thor_cot_schema.json)  |40.83|39.91|0.49|[answers](data/answers/dev/valid_data_en.csv_gpt-3.5-turbo-1106-thor-cot.sqlite)
| **mistral-7b**               | 🇺🇸 | [CoT THoR](data/thor_cot_schema.json)  |42.34|51.43|0.04|[answers](data/answers/dev/valid_data_en.csv_open-mistral-7b-thor-cot.sqlite)

| **Model**                    |lang| Mode      | F1(P,N) | F1(P,N,0) | N/A % | Answers   |
|------------------------------|----|-----------|---------|-----------|-------|-----------|
|Proprietary|
| **GPT-4-turbo-2024-04-09**   | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |50.79|61.19|0.0|[answers](data/answers/dev/valid_data_en.csv_gpt-4-turbo-2024-04-09_prompt.sqlite)
| **GPT-3.5-0613**             | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |47.1|57.76|0.0|[answers](data/answers/dev/valid_data_en.csv_gpt-3.5-turbo-0613_prompt.sqlite)
| **GPT-3.5-1106**             | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |45.79|52.55|0.0|[answers](data/answers/dev/valid_data_en.csv_gpt-3.5-turbo-1106_prompt.sqlite)
| **mistral-large-latest**     | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |44.48|57.24|0.0|[answers](data/answers/dev/valid_data_en.csv_mistral-large-latest_prompt.sqlite)
| **gpt-4o**                   | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |42.84|56.19|0.0  |[answers](data/answers/dev/valid_data_en.csv_gpt-4o_prompt.sqlite)
|Open & Less 100B|
| **llama-3-70b-instruct**     | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |49.79|61.24|0.0  |[answers](data/answers/dev/valid_data_en.csv_meta_meta-llama-3-70b-instruct_prompt.sqlite)
| **mixtral-8x22b**            | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |46.09|58.24|0.0|[answers](data/answers/dev/valid_data_en.csv_open-mixtral-8x22b_prompt.sqlite)
| **Phi-3-small-8k-instruct**  | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |46.87|57.02|0.07 |[answers](data/answers/dev/valid_data_en.csv_microsoft_Phi-3-small-8k-instruct_prompt.sqlite)
| **mixtral-8x7b**             | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |47.33|56.36|0.07 |[answers](data/answers/dev/valid_data_en.csv_open-mixtral-8x7b_prompt.sqlite)   |
| **llama-2-70b-chat**         | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |42.42|54.25|13.44|[answers](data/answers/dev/valid_data_en.csv_meta_llama-2-70b-chat_prompt.sqlite)|
|Open & Less 10B|
| **llama-3-8b-instruct**      | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |45.25|54.43|0.0  |[answers](data/answers/dev/valid_data_en.csv_meta_meta-llama-3-8b-instruct_prompt.sqlite) |
| **Mistral-7B-Instruct-v0.3** | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |45.23|55.5 |0.0  |[answers](data/answers/dev/valid_data_en.csv_mistralai_Mistral-7B-Instruct-v0.3_prompt.sqlite)
| **Phi-3-mini-4k-instruct**   | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |44.62|54.71|0.0  |[answers](data/answers/dev/valid_data_en.csv_microsoft_Phi-3-mini-4k-instruct_prompt.sqlite)
| **Qwen1.5-7B-Chat**          | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |44.39|55.55|0.04 |[answers](data/answers/dev/valid_data_en.csv_Qwen_Qwen1.5-7B-Chat_prompt.sqlite)
| **google_flan-t5-xl**        | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |43.73|53.72|0.0  |[answers](data/answers/dev/valid_data_en.csv_google_flan-t5-xl_prompt.sqlite)
| **mistral-7b**               | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |43.11|53.64|0.11 |[answers](data/answers/dev/valid_data_en.csv_open-mistral-7b_prompt.sqlite)     |
| **Qwen2-7B-Instruct**        | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |39.74|48.11|3.87 |[answers](data/answers/dev/valid_data_en.csv_Qwen_Qwen2-7B-Instruct_prompt.sqlite)
| **Qwen2-1.5B-Instruct**      | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |33.88|48.59|0.0  |[answers](data/answers/dev/valid_data_en.csv_Qwen_Qwen2-1.5B-Instruct_prompt.sqlite)
| **Qwen1.5-1.8B-Chat**        | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |33.65|47.28|0.04 |[answers](data/answers/dev/valid_data_en.csv_Qwen_Qwen1.5-1.8B-Chat_prompt.sqlite)
|Open & Less 1B|
| **Flan-T5-large**            | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |36.72|24.51|0.0|[answers](data/answers/dev/valid_data_en.csv_google_flan-t5-large_prompt.sqlite)
| **Qwen2-0.5B-Instruct**      | 🇺🇸 | [zero-shot](data/prompt_v2_en.txt) |9.52 |33.0 |0.0|[answers](data/answers/dev/valid_data_en.csv_Qwen_Qwen2-0.5B-Instruct_prompt.sqlite)


| **Model**                    |lang|  Mode      | F1(P,N) | F1(P,N,0) | N/A % | Answers   |
|------------------------------|----|------------|---------|-----------|-------|-----------|
|Proprietary|
| **GPT-3.5-0613**             | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |44.15|53.63|1.51|[answers](data/answers/dev/valid_data.csv_gpt-3.5-turbo-0613_prompt.sqlite)     |
| **gpt-4o**                   | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |44.15|57.5 |0.0 |[answers](data/answers/dev/valid_data.csv_gpt-4o_prompt.sqlite)
| **GPT-4-turbo-2024-04-09**   | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |42.21|56.36|0.0 |[answers](data/answers/dev/valid_data.csv_gpt-4-turbo-2024-04-09_prompt.sqlite)
| **GPT-3.5-1106**             | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |41.34|46.83|0.46|[answers](data/answers/dev/valid_data.csv_gpt-3.5-turbo-1106_prompt.sqlite)     |
| **mistral-large-latest**     | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |22.33|43.07|0.04|[answers](data/answers/dev/valid_data.csv_mistral-large-latest_prompt.sqlite)          |
|Open & Less 100B|
| **llama-3-70b-instruct**     | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |45.89|58.73|0.0|[answers](data/answers/dev/valid_data.csv_meta_meta-llama-3-70b-instruct_prompt.sqlite)
| **mixtral-8x22b**            | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |42.64|54.91|0.0|[answers](data/answers/dev/valid_data.csv_open-mixtral-8x22b_prompt.sqlite)
| **mistral-7b**               | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |42.14|47.57|0.18|[answers](data/answers/dev/valid_data.csv_open-mistral-7b_prompt.sqlite)        |
| **mixtral-8x7b**             | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |41.11|53.75|0.18|[answers](data/answers/dev/valid_data.csv_open-mixtral-8x7b_prompt.sqlite)      |
| **llama-2-70b-chat**         | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |29.51|27.27|1.65|[answers](data/answers/dev/valid_data.csv_meta_llama-2-70b-chat_prompt.sqlite)   |
|Open & Less 10B|
| **Qwen2-7B-Instruct**        | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |42.16|51.13|0.25|[answers](data/answers/dev/valid_data.csv_Qwen_Qwen2-7B-Instruct_prompt.sqlite)
| **mistral-7B-Instruct-v0.3** | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |41.73|44.24|0.18|[answers](data/answers/dev/valid_data.csv_mistralai_Mistral-7B-Instruct-v0.3_prompt.sqlite)
| **Phi-3-small-8k-instruct**  | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |40.65|49.64|0.14|[answers](data/answers/dev/valid_data.csv_microsoft_Phi-3-small-8k-instruct_prompt.sqlite)
| **llama-3-8b-instruct**      | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |40.55|47.81|0.35|[answers](data/answers/dev/valid_data.csv_meta_meta-llama-3-8b-instruct_prompt.sqlite) |
| **Qwen1.5-7B-Chat**          | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |34.1 |45.05|0.25|[answers](data/answers/dev/valid_data.csv_Qwen_Qwen1.5-7B-Chat_prompt.sqlite)
| **Phi-3-mini-4k-instruct**   | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |33.79|24.33|0.04|[answers](data/answers/dev/valid_data.csv_microsoft_Phi-3-mini-4k-instruct_prompt.sqlite) |
| **Qwen2-1.5B-Instruct**      | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |20.5 |33.57|0.35|[answers](data/answers/dev/valid_data.csv_Qwen_Qwen2-1.5B-Instruct_prompt.sqlite)
| **Qwen1.5-1.8B-Chat**        | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt) |11.74|8.05 |0.42|[answers](data/answers/dev/valid_data.csv_Qwen_Qwen1.5-1.8B-Chat_prompt.sqlite)
|Open & Less 1B|
| **Qwen2-0.5B-Instruct**      | 🇷🇺 | [zero-shot](data/prompt_v2_ru.txt)  |11.76|18.12|0.25|[answers](data/answers/dev/valid_data.csv_Qwen_Qwen2-0.5B-Instruct_prompt.sqlite)

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

