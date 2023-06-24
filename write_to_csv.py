import csv
from csv import *
from csv_to_array import ctoa

def write_to_csv(arr, name):
    with open(name, 'w+', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(arr)

def append_to_csv(arr, name):
    with open(name, 'a', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(arr)

def write_1d_arr_to_csv(arr, name):
    with open(name, 'w+', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        for x in arr: writer.writerow([x])   


def write_to_result(response):
  f = open("./result/result.txt", "a")
  f.write(response)
  f.close()  
