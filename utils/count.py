import json
import os


def check_conflict(predictions, reversed_predictions):
    assert len(predictions) == len(reversed_predictions)
    win_count = 0
    tie_count = 0
    lose_count = 0
    for i in range(len(predictions)):
        pred = predictions[i]["pandalm_result"]
        reversed_pred = reversed_predictions[i]["pandalm_result"]
        # all conditions of 'Tie'
        if pred == "Tie" or reversed_pred  == "Tie" or pred==reversed_pred:
                tie_count += 1
        else:
            if pred =='2':
                win_count += 1
            elif pred=='1':
                lose_count += 1
    return win_count, tie_count, lose_count 



if __name__ == "__main__":
    
    
    # # calculate single result
    # # =================================================================================================================================================
    # # arg:
    # file_path="/home/eric/Bai/PandaLM/data/NMSQA/256-rescale/results/processed_question_audio_path_transcription_whisper-large-v3_result.json"
    # reversed_file_path = "/home/eric/Bai/PandaLM/data/NMSQA/256-rescale/reverse_order_candidate_first/processed_question_audio_path_transcription_whisper-large-v3_result.json"



    # with open(file_path, "r") as f:
    #     predictions = json.load(f)
        
    # with open(reversed_file_path, "r") as f:
    #     reversed_predictions = json.load(f)
    
    # win_count, tie_count, lose_count = check_conflict(predictions, reversed_predictions)

    # print(f'win_count = {win_count}, ratio = {win_count/len(predictions)}')
    # print(f'tie_count = {tie_count}, ratio = {tie_count/len(predictions)}')
    # print(f'lose_count = {lose_count}, ratio = {lose_count/len(predictions)}')
    # print(f"total number of data = {win_count+tie_count+lose_count}")
    
    # # ==========================================================================================================
    
    
    # calculate results in 2 folders
    # arg: 
    pred_folder = "/home/eric/Bai/PandaLM/data/alpaca/MUSAN-noise/256-rescale/results"
    reversed_pred_folder = "/home/eric/Bai/PandaLM/data/alpaca/MUSAN-noise/256-rescale/reverse_order_candidate_first"
    
    
    
    
    json_files = sorted([pos_json for pos_json in os.listdir(pred_folder) if pos_json.endswith('.json')])
    # print(json_files)
    
    pred_files = [os.path.join(pred_folder, file) for file in json_files]
    reversed_pred_files = [os.path.join(reversed_pred_folder, file) for file in json_files]
    
    assert len(pred_files) == len(reversed_pred_files), 'json files in pred_folder and reversed_pred_folder are mismatch'
    
    print(f"claculate bwtween {pred_folder.split('/data/')[-1]} and {reversed_pred_folder.split('/data/')[-1]}")
    
    for i in range(len(pred_files)):

        file_path = pred_files[i]
        reversed_file_path = reversed_pred_files[i]

        with open(file_path, "r") as f:
            predictions = json.load(f)
            
        with open(reversed_file_path, "r") as f:
            reversed_predictions = json.load(f)
        
        win_count, tie_count, lose_count = check_conflict(predictions, reversed_predictions)

        print(f"result of {file_path.split('/results/')[-1]}")
        print(f'win_count = {win_count}, ratio = {win_count/len(predictions)}')
        print(f'tie_count = {tie_count}, ratio = {tie_count/len(predictions)}')
        print(f'lose_count = {lose_count}, ratio = {lose_count/len(predictions)}')
        print(f"total number of data = {win_count+tie_count+lose_count}\n")