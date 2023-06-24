import json
def parse_result(result):
    scores = []
    reasons = []
    answers = json.loads(result)
    for a in answers:
        scores.append(int(a["consistency"]))
        reasons.append(a["reason"])
    return scores, reasons
