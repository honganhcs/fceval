from call_gpt import *

gpt_model = "gpt-3.5-turbo"


f = open("./eval_instruction.txt")
instruction_msg = f.read()
messages = [
    {"role": "system", "content": instruction_msg},
    {
        "role": "user",
        "content": "Text: Paris is a city in France.",
    },
    {"role": "user", "content": "Sentence 1: Paris is in Italy."},
    {"role": "user", "content": "Sentence 2: France contains a city called Paris."},
    {"role": "user", "content": "Sentence 3: Paris is a beautiful city."},
    {"role": "user", "content": "Sentence 4: The Effiel tower is in Paris"},
    {"role": "user", "content": "Sentence 5: I love Paris"},
]

response = generate_chat_completion(messages)

f = open("result_test.txt", "a")
f.write(response)
f.close()
