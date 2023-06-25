from utils.get_text import get_text_for_summarization
from utils.parse_result import parse_result
from call_gpt import *
from utils.write_to_csv import *
from utils.csv_to_array import ctoa

f = open("./key.txt")
API_KEY = f.read()
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

gpt_model = "gpt-3.5-turbo"

papers = ctoa("data/paper_names.csv")
sentences = ctoa("data/sentences.csv")
human_scores = ctoa("result/human_scores.csv")

f = open("./eval_instruction.txt")
instruction = f.read()

instruction_msg = {"role": "system", "content": instruction}

num_papers = len(papers)

scores = []
reasons = []

for np in range(5, num_papers):
    p = papers[np][0]
    messages = [instruction_msg]
    text = get_text_for_summarization(p)
    sent = sentences[np]
    num_sent = len(sent)
    for ns in range(num_sent):
        s = sent[ns]
        sentence_msg = {"role": "user", "content": "Sentence {}: {}".format(ns + 1, s)}
        messages.append(sentence_msg)
    scores_for_paper = generate_chat_completion(messages)
    write_to_result(scores_for_paper)
    try:
        ns, sc, rs = parse_result(scores_for_paper)
        if ns != num_sent:
            print(
                "wrong number of sentences for paper {}, expected {}, got {}".format(
                    np, num_sent, ns
                )
            )
            break
        scores.append(sc)
        reasons.append(rs)
    except Exception as e:
        print(e)
        break

append_to_csv(scores, "./result/gpt_scores.csv")
append_to_csv(reasons, "./result/gpt_reasons.csv")
