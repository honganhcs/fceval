from get_human_scores import get_human_scores
from get_text import get_text_for_summarization
from parse_result import parse_result
from eval_test import generate_chat_completion
from write_to_csv import *

f = open("./key.txt")
API_KEY = f.read()
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

gpt_model = "gpt-3.5-turbo"

papers, sentences, evals = get_human_scores()
# write_1d_arr_to_csv(papers, 'paper_names.csv')
# write_to_csv(sentences, 'sentences.csv')
# write_to_csv(evals, './result/human_scores.csv')

f = open("./eval_instruction.txt")
instruction = f.read()

instruction_msg = {"role": "system", "content": instruction}

num_papers = len(papers)

scores = []
reasons = []

for np in range(12, num_papers):
    p = papers[np]
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
        sc, rs = parse_result(scores_for_paper)
        scores.append(sc)
        reasons.append(rs)
    except Exception as e: 
        print(e)
        break

append_to_csv(scores, "./result/gpt_scores.csv")
append_to_csv(reasons, "./result/gpt_reasons.csv")
