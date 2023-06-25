from utils.csv_to_array import *
import numpy as np
from sklearn.metrics import cohen_kappa_score

human_scores = ctoa("result/human_scores.csv")
gpt_scores = ctoa("result/gpt_scores.csv")

human_scores_flat = []
gpt_scores_flat = []

count = 0
for p in human_scores:
    if count == 15: break
    for s in p:
        human_scores_flat.append(int(s))
    count += 1

for p in gpt_scores:
    for s in p:
        gpt_scores_flat.append(int(s))
     


kappa = cohen_kappa_score(human_scores_flat, gpt_scores_flat)
print(kappa)