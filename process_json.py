import json
import os


# input_file_path = "/home/eric/Bai/MMLLM-evaluation/result/alpaca/Gaussian/256/processed/rescale/processed_speech_input.json"
input_file_path = "/home/eric/Bai/MMLLM-evaluation/result/alpaca/MUSAN-noise/256/processed/rescale"
output_folder = "/home/eric/Bai/PandaLM/data/alpaca/MUSAN-noise/256-rescale"


json_files = [os.path.join(input_file_path, pos_json) for pos_json in os.listdir(input_file_path) if pos_json.endswith('.json')]
print(json_files)
for file in json_files:
    output_file_name = os.path.basename(file)
    with open(file, "r") as file:
        all_data = json.load(file)
        
    results = []
    for data in all_data:
        # results.append({
        #     "instruction": data["question_gt"],
        #     "input": ""
        # })
        # results.append(data["gt"])
        results.append(data["response"])
        

    # output_file_path = os.path.join(output_folder, "question.json")
    # output_file_path = os.path.join(output_folder, "gt.json")
    
    
    output_file_path = os.path.join(output_folder, output_file_name)
    # Save detailed results to a JSON file
    with open(output_file_path, "w") as outfile:
        json.dump(results, outfile, indent=4)