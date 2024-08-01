import json
import os


class FileManager:
    @staticmethod
    def save_evaluation_to_file(evaluation, filename='evaluation_result.json'):
        try:
            with open(filename, 'w') as file:
                json.dump(evaluation, file, indent=4)
        except Exception as e:
            print(f"Failed to save evaluation result: {e}")
            
    @staticmethod
    def get_candidate_files(directory, starttext="processed"):
        """
        Get a list of candidate files starting with 'starttext' in the specified directory.
        starttext default value: "processed"
        """
        return [
            os.path.join(directory, filename) 
            for filename in os.listdir(directory) 
            if filename.startswith(starttext)
        ]