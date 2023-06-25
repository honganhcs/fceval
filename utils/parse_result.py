import json


def parse_result(result):
    scores = []
    reasons = []
    answers = json.loads(result)
    for a in answers:
        scores.append(int(a["entailed"]))
        reasons.append(a["reason"])
    num_eval = len(scores)
    return num_eval, scores, reasons
