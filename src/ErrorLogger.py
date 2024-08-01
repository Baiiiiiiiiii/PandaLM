import json
import os




class ErrorLogger:
    def __init__(self, filename='error_log.json'):
        self.filename = filename

    def log_error(self, error_data):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    error_log = json.load(file)
            else:
                error_log = []

            error_log.append(error_data)

            with open(self.filename, 'w') as file:
                json.dump(error_log, file, indent=2)
        except Exception as e:
            print(f"Failed to log error: {e}")