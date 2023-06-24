from csv_to_array import ctoa
from math import floor


def get_human_scores():
    f1 = ctoa("1.csv")
    f2 = ctoa("2.csv")
    f3 = ctoa("3.csv")

    paper_count = -1

    papers = []
    sentences = []
    evals = []

    rows = len(f1)

    sent_indices = [1, 3, 5]

    for r in range(rows):
        row = f1[r]
        if any(row):
            if row[0]:
                paper_count += 1
                papers.append(row[0].split(".pdf")[0])
                sentences.append([])
                evals.append([])
            for i in sent_indices:
                if row[i] and row[i] != "" and row[i + 1] and row[i + 1] != "":
                    sentences[paper_count].append(row[i])
                    score = floor(
                        (float(row[i + 1]) + float(f2[r][i + 1]) + float(f3[r][i + 1]))
                        / 3
                    )
                    evals[paper_count].append(score)
    return papers, sentences, evals
