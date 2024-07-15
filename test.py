# from pandalm import EvaluationPipeline
# import os
# # pipeline = EvaluationPipeline(
# #     candidate_paths=["/home/eric/Bai/PandaLM/data/slue-gt.json", "/home/eric/Bai/PandaLM/data/slue-pred.json"], 
# #     input_data_path="/home/eric/Bai/PandaLM/data/slue-input.json",
# #     output_data_path = "/home/eric/Bai/PandaLM/data/slue-eval.json"
# # )
# # print(pipeline.evaluate())




# # candidate_files = [
# #     # "/home/eric/Bai/PandaLM/data/NMSQA/256-rescale/processed_question_audio_path_transcription_whisper-large-v3.json",
# #     "/home/eric/Bai/PandaLM/data/SLUE/256-rescale/processed_question_audio_transcription_whisper-medium.en.json",
# #     "/home/eric/Bai/PandaLM/data/SLUE/256-rescale/processed_question_audio_transcription_whisper-small.en.json",
# #     # "/home/eric/Bai/PandaLM/data/SLUE/256-rescale/processed_raw_question_text.json"
# #     ]
# input_file_path = "/home/eric/Bai/PandaLM/data/alpaca/Gaussian/256-rescale/candidates"
# candidate_files = [os.path.join(input_file_path, pos_json) for pos_json in os.listdir(input_file_path) if pos_json.startswith('processed')]

# print(candidate_files)


# gt_file = "/home/eric/Bai/PandaLM/data/alpaca/Gaussian/256-rescale/gt.json"
# question_file = "/home/eric/Bai/PandaLM/data/alpaca/Gaussian/256-rescale/question.json"
# output_eval_path = "/home/eric/Bai/PandaLM/data/alpaca/Gaussian/256-rescale/results"


# for candidate in candidate_files:
#     pipeline = EvaluationPipeline(
#         candidate_paths = [gt_file, candidate], 
#         input_data_path = question_file,
#         output_data_path = os.path.join(output_eval_path, f"{os.path.basename(candidate).split(".")[0]}_result.json")
#     )
#     print(pipeline.evaluate())




import os
from pandalm import EvaluationPipeline

def get_candidate_files(directory):
    """
    Get a list of candidate files starting with 'processed' in the specified directory.
    """
    return [
        os.path.join(directory, filename) 
        for filename in os.listdir(directory) 
        if filename.startswith('processed')
    ]

def evaluate_candidates(candidate_files, gt_file, question_file, output_dir):
    """
    Evaluate each candidate file and save the results in the specified output directory.
    """
    for candidate in candidate_files:
        output_file_path = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(candidate))[0]}_result.json")
        pipeline = EvaluationPipeline(
            # candidate_paths=[gt_file, candidate],
            candidate_paths=[candidate, gt_file],
            input_data_path=question_file,
            output_data_path=output_file_path
        )
        print(pipeline.evaluate())

def main():
    base_path = "/home/eric/Bai/PandaLM/data/alpaca/MUSAN-speech/256-rescale"
    
    input_file_path = os.path.join(base_path, "candidates")
    candidate_files = get_candidate_files(input_file_path)
    # candidate_files = [
    #     "/home/eric/Bai/PandaLM/data/SLUE/256-rescale/candidates/processed_question_audio_transcription_whisper-small.en.json"
    # ]
    
    gt_file = os.path.join(base_path, "gt.json")
    question_file = os.path.join(base_path, "question.json")
    output_eval_path = os.path.join(base_path, "reverse_order_candidate_first")
    
    evaluate_candidates(candidate_files, gt_file, question_file, output_eval_path)

if __name__ == "__main__":
    main()
