EXAMPLE_PROMPT = """
You will be given a question and two responses to evaluate. Your task is to assess the quality of each response based on criteria such as accuracy, completeness, clarity, relevance, and conciseness. Score each response on a scale of 1 to 10 for each criterion, then generate a reference answer for the question.

### Examples:

#### Example 1:
### Question:
What are the benefits of a healthy diet?

### Response 1:
A healthy diet provides numerous benefits, including improved mental clarity, better energy levels, and a stronger immune system. It also helps in maintaining a healthy weight, reducing the risk of chronic diseases such as diabetes and heart disease, and promoting overall well-being.

### Response 2:
Eating healthy is good for you. It makes you feel better and can prevent diseases.

### Evaluation:
#### Feedback and Scores for Response 1:
- Accuracy: 10/10
- Feedback: The response correctly identifies multiple benefits of a healthy diet.
- Completeness: 10/10
- Feedback: The response provides a thorough list of benefits.
- Clarity: 10/10
- Feedback: The response is clear and easy to understand.
- Relevance: 10/10
- Feedback: The response stays on topic and directly answers the question.
- Conciseness: 9/10
- Feedback: The response is concise but could be slightly shorter without losing meaning.

**Total Score for Response 1: 49/50**

#### Feedback and Scores for Response 2:
- Accuracy: 4/10
- Feedback: The response correctly identifies some benefits but is very vague.
- Completeness: 3/10
- Feedback: The response is incomplete and lacks detail.
- Clarity: 6/10
- Feedback: The response is somewhat clear but lacks detail.
- Relevance: 6/10
- Feedback: The response stays on topic but is too brief.
- Conciseness: 10/10
- Feedback: The response is very concise.

**Total Score for Response 2: 29/50**

#### Reference Answer:
A healthy diet provides numerous benefits, including improved mental clarity, better energy levels, a stronger immune system, maintaining a healthy weight, reducing the risk of chronic diseases such as diabetes and heart disease, and promoting overall well-being.

---

#### Example 2:
### Question:
Explain the importance of recycling.

### Response 1:
Recycling is good. It saves the environment and is something everyone should do to keep the planet clean.

### Response 2:
Recycling is important because it helps reduce waste in landfills, conserves natural resources, and reduces pollution. By recycling materials like paper, plastic, and metal, we can decrease the demand for new raw materials, save energy, and protect ecosystems. Additionally, recycling can create jobs and promote sustainable practices in communities.

### Evaluation:
#### Feedback and Scores for Response 1:
- Accuracy: 5/10
- Feedback: The response is somewhat accurate but lacks detail.
- Completeness: 4/10
- Feedback: The response is incomplete and misses several key points.
- Clarity: 6/10
- Feedback: The response is somewhat clear but too brief.
- Relevance: 7/10
- Feedback: The response is relevant but lacks depth.
- Conciseness: 10/10
- Feedback: The response is very concise.

**Total Score for Response 1: 32/50**

#### Feedback and Scores for Response 2:
- Accuracy: 10/10
- Feedback: The response accurately explains the importance of recycling.
- Completeness: 10/10
- Feedback: The response covers multiple aspects of the importance of recycling.
- Clarity: 10/10
- Feedback: The response is clear and detailed.
- Relevance: 10/10
- Feedback: The response directly addresses the question.
- Conciseness: 9/10
- Feedback: The response is concise but could be slightly shorter without losing detail.

**Total Score for Response 2: 49/50**

#### Reference Answer:
Recycling is important because it helps reduce waste in landfills, conserves natural resources, and reduces pollution. By recycling materials like paper, plastic, and metal, we can decrease the demand for new raw materials, save energy, and protect ecosystems. Additionally, recycling can create jobs and promote sustainable practices in communities.

---

"""

