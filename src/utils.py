import os

def get_candidate_files(directory, starttext="processed"):
    """
    Get a list of candidate files starting with 'starttext' in the specified directory.
    starttext default: "processed"
    """
    return [
        os.path.join(directory, filename) 
        for filename in os.listdir(directory) 
        if filename.startswith(starttext)
    ]