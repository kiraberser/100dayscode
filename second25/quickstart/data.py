import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php?", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]


columns = [
    [value for value in question_data[0]],
]

row = [
    [question["type"] for question in question_data],
    [question["difficulty"] for question in question_data],
    [question["category"] for question in question_data],
    [question["question"] for question in question_data],
    [question["correct_answer"] for question in question_data], 
]
