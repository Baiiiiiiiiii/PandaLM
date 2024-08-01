import re
import json
import os
import transformers
import torch
from .EXAMPLE_PROMPT import EXAMPLE_PROMPT
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer, AutoModelForCausalLM


class EvaluationDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]


class Llama3Evaluator:
    def __init__(self, dataset, batch_size=4):
        self.dataset = dataset
        self.batch_size = batch_size
        self.max_new_tokens = 1024
        self.model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_id,
            torch_dtype=torch.bfloat16,
            device_map="auto",
        )
        self.current_index = 0

    def prompt_setter(self, question, response_to_eval, gt_answer):
        prompt = f"""Given the following components:

        **Question**: {question}

        **Reference Answer (Groundtruth)**: {gt_answer}

        **Response to Evaluate**: {response_to_eval}

        Evaluate the similarity of the response to the reference answer based on the following criteria. For each criterion, provide a score on a scale of 1 to 10, with 10 being the highest level of similarity and 1 being the lowest. Include a brief explanation for the score of each criterion.
                                                
        Criteria for Evaluation:

        1. Accuracy: How accurately does the response reflect the information in the reference answer?
        Score: [1 to 10]
        Explanation: [Brief explanation for the accuracy score]

        2. Completeness: How completely does the response cover the points mentioned in the reference answer?
        Score: [1 to 10]
        Explanation: [Brief explanation for the completeness score]

        3. Clarity: How clear and understandable is the response?
        Score: [1 to 10]
        Explanation: [Brief explanation for the clarity score]

        4. Relevance: How relevant is the response to the question and the reference answer?
        Score: [1 to 10]
        Explanation: [Brief explanation for the relevance score]

        5. Conciseness: How concise is the response while maintaining the necessary information?
        Score: [1 to 10]
        Explanation: [Brief explanation for the conciseness score]
        
        Give me your evaluation strictly following the below format:
        
        1.Accuracy:
        Score: [1 to 10]
        Explanation: [Brief explanation for the accuracy score]

        2.Completeness:
        Score: [1 to 10]
        Explanation: [Brief explanation for the completeness score]

        3.Clarity:
        Score: [1 to 10]
        Explanation: [Brief explanation for the clarity score]

        4.Relevance:
        Score: [1 to 10]
        Explanation: [Brief explanation for the relevance score]

        5.Conciseness:
        Score: [1 to 10]
        Explanation: [Brief explanation for the conciseness score]
        
        Give me your evaluation strictly following the below format:
        
        1.Accuracy:
        Score: [1 to 10]
        Explanation: [Brief explanation for the accuracy score]

        2.Completeness:
        Score: [1 to 10]
        Explanation: [Brief explanation for the completeness score]

        3.Clarity:
        Score: [1 to 10]
        Explanation: [Brief explanation for the clarity score]

        4.Relevance:
        Score: [1 to 10]
        Explanation: [Brief explanation for the relevance score]

        5.Conciseness:
        Score: [1 to 10]
        Explanation: [Brief explanation for the conciseness score]

        """              
    #     prompt = EXAMPLE_PROMPT + f"""
    # ### Now evaluate the following question and responses:

    # ### Question:
    # {question}

    # ### Response 1:
    # {response_to_eval}

    # ### Response 2:
    # {gt_answer}
    # """
        return prompt

    def generate_llama3_answer(self):
        if self.current_index >= len(self.dataset):
            raise StopIteration("End of dataset reached.")
        
        data = self.dataset[self.current_index]
        prompt = self.prompt_setter(data["question"], data["rsp1"], data["rsp2"])

        messages = [
            {"role": "system", "content": "You are a helpful assistant who always generates formatted responses following the given instructions."},
            {"role": "user", "content": prompt},
        ]

        input_ids = self.tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            return_tensors="pt"
        ).to(self.model.device)
        
        terminators = [
            self.tokenizer.eos_token_id,
            self.tokenizer.convert_tokens_to_ids("<|eot_id|>")
        ]

        outputs = self.model.generate(
            input_ids,
            max_new_tokens=self.max_new_tokens,
            eos_token_id=terminators,
            do_sample=False,
            # do_sample=True,
            # temperature=0.6,
            # top_p=0.9,
        )
        
        response = outputs[0][input_ids.shape[-1]:]        
        self.current_index += 1

        return self.tokenizer.decode(response, skip_special_tokens=True)
    
    
    def release_resources(self):
        # del self.pipeline
        torch.cuda.empty_cache()

    def __iter__(self):
        return self

    def __next__(self):
        return self.generate_llama3_answer()