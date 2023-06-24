from transformers import T5Tokenizer, T5ForConditionalGeneration
from csv_to_array import *

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")


def get_text_for_summarization(paper):
    filename = "./text/" + paper + "_body.txt"
    f = open(filename, errors="ignore")
    text = f.read()
    inputs = tokenizer(text, truncation=True).input_ids
    res = tokenizer.batch_decode(inputs)

    return " ".join(res)
