from src.EXAMPLE_PROMPT import EXAMPLE_PROMPT
from src.ErrorLogger import ErrorLogger
from src.EvaluationParser import EvaluationParser
from src.FileManager import FileManager
from src.Llama3Evaluator import Llama3Evaluator
import json
import os



def read_json_file(filename):
    """Reads a JSON file and returns its content."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file {filename}.")
        return None
    except Exception as e:
        print(f"An error occurred while reading {filename}: {e}")
        return None

    
    
def main(_base_path):
    
    # Params setting
    base_path = _base_path
    
    error_logger = ErrorLogger()
    parser = EvaluationParser(error_logger)
    
    gt_file = read_json_file(os.path.join(base_path, "gt.json"))
    
    input_file_path = os.path.join(base_path, "candidates")
    candidate_files_path = FileManager.get_candidate_files(input_file_path)
    
    question_file = read_json_file(os.path.join(base_path, "question.json"))
    output_eval_path = os.path.join(base_path, "GPT4_Benchmark_Grading_Experiment_greedy") # result
    
    for candidate in candidate_files_path:
        output_file_path = os.path.join(output_eval_path, f"{os.path.splitext(os.path.basename(candidate))[0]}_result.json")
        candidate_file = read_json_file(candidate)
        
        assert len(candidate_file) == len(gt_file) == len(question_file)
        
        dataset = []
        for candidate, gt, question in zip(candidate_file, gt_file, question_file):
            dataset.append(
                {
                    "question": question["instruction"],
                    "rsp1": candidate,
                    "rsp2": gt
                }
            )
        
        results = []
        
        llama = Llama3Evaluator(dataset)
        try:
            for llama3_response in llama:
                try:
                    evaluation = parser.parse_evaluation(llama3_response)
                    results.append(evaluation)
                    # breakpoint()
                except ValueError as e:
                    print(e)
        finally:
            llama.release_resources()
                
        FileManager.save_evaluation_to_file(results, filename=output_file_path)




if __name__ == "__main__":
    main(_base_path = "/home/eric/Bai/PandaLM/data/alpaca/Gaussian/256-rescale")
    # main(_base_path = "/home/eric/Bai/PandaLM/data/SLUE/256-rescale" )