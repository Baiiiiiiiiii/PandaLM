import os
import json

def load_json_files(folder_path):
    json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
    return json_files

def calculate_average_total_score(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        
    total_scores = [entry['scores']['Total Score'] for entry in data]
    average_score = sum(total_scores) / len(total_scores) if total_scores else 0
    return average_score/50

def main(folder_path):
    json_files = load_json_files(folder_path)
    average_scores = {}
    
    for json_file in json_files:
        file_path = os.path.join(folder_path, json_file)
        average_score = calculate_average_total_score(file_path)
        average_scores[json_file] = average_score
    
    return average_scores

if __name__ == "__main__":
    folder_path = "/home/eric/Bai/PandaLM/data/alpaca/Gaussian/256-rescale/GPT4_Benchmark_Grading_Experiment_greedy"
    average_scores = main(folder_path)
    
    for json_file, avg_score in average_scores.items():
        print(f"File: {json_file}, Average Total Score: {avg_score:.2f}")
