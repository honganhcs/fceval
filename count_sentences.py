from utils.csv_to_array import ctoa
from utils.write_to_csv import *
sentences = ctoa("data/sentences.csv")

count = []
for sent in sentences:
    count.append(len(sent))

write_1d_arr_to_csv(count, 'data/num_sentences.csv')
