import re




class EvaluationParser:
    def __init__(self, error_logger):
        self.error_logger = error_logger
    
    def normalize_newlines(self, text):
        text = text.replace('\\n', '\n').replace('\t','').replace("###", "####").replace("N/A", "0/10")
        text = re.sub(r'^.*?\n\n', '### Evaluation:\n\n', text, flags=re.DOTALL)
        return text

    def parse_feedback_section(self, section):
        scores = {}
        feedbacks = {}
        try:
            current_metric = None
            for line in section.strip().split('\n'):
                if line.startswith('- '):
                    parts = line[2:].split(':', 1)
                    if '/' in parts[1]:
                        score = parts[1].strip()
                        score_value = int(score.split('/')[0])
                        scores[parts[0].strip()] = score_value
                        current_metric = parts[0].strip()
                    else:
                        feedback = parts[1].strip()
                        if current_metric:
                            feedbacks[current_metric] = feedback
                        current_metric = None
                elif line.startswith('**Total Score'):
                    total_score = line.split(':', 1)[1].strip().split('/')[0]
                    total_score = int(total_score)
                    scores['Total Score'] = total_score
        except Exception as e:
            raise ValueError(f"Error parsing feedback section: {e}")

        return {"scores": scores, "feedbacks": feedbacks}

    def parse_evaluation(self, llama3_response):
        
        try:
            # llama3_response = self.normalize_newlines(llama3_response)
            # sections = re.split(r'####\s', llama3_response)
            # evaluation = {"Reference Answer": "", "Winner": "", "Responses": {}}

            # for section in sections:
            #     # print(f"Parsing section: {section[:30]}...")  # Debugging statement
            #     if section.startswith('Feedback and Scores for Response'):
            #         response_id = section.split('\n')[0].split()[-1]
            #         evaluation["Responses"][response_id] = self.parse_feedback_section(section)
            #     elif section.startswith('Reference Answer:'):
            #         reference_answer = section.split('\n', 1)[1].strip()
            #         evaluation["Reference Answer"] = reference_answer
            
            # # Determine the winner by comparing total scores
            # response_scores = {key: value['scores']['Total Score'] for key, value in evaluation["Responses"].items()}
            
            # scores = list(response_scores.values())
            # if len(scores) > 1 and scores[0] == scores[1]:
            #     evaluation["Winner"] = "Tie"
            # else:
            #     winner = max(response_scores, key=response_scores.get)
            #     evaluation["Winner"] = winner[0]

            # return evaluation
        
        
            # Define patterns to extract scores and explanations
            score_pattern = re.compile(r'(\w+):\nScore:\s(\d+)\nExplanation:\s(.*?)\n', re.DOTALL)
            
            # Extract scores and explanations
            scores = {}
            feedbacks = {}
            
            for match in score_pattern.findall(llama3_response):
                category, score, explanation = match
                scores[category] = int(score)
                feedbacks[category] = explanation.strip()
            
            # Calculate total score
            total_score = sum(scores.values())
            scores['Total Score'] = total_score
            
            # Create the final dictionary
            result = {
                "scores": scores,
                "feedbacks": feedbacks
            }
            
            return result
        
        except Exception as e:
            self.error_logger.log_error({"error": str(e), "llama3_response": llama3_response})
            raise ValueError(f"Error parsing evaluation: {e}")