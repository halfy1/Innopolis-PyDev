import json

# TODO решите задачу
def task() -> float:
    with open("input.json") as file:
        data = json.load(file)
    sum_multiply = sum(d['score'] * d['weight'] for d in data)
    sum_multiply = round(sum_multiply,3)

    return sum_multiply



print(task())
