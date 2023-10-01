import time
import numpy as np
import gzip

def count_elements(seq) -> dict:
    hist={}
    for i in seq:
        hist[i]=hist.get(i,0)+1
    return hist

def ascii_histogram(seq) ->None:
    counted = count_elements(seq)
    # print(counted)
    return counted
    # for k in sorted(counted):
    #     print (f'K: {k} count{counted[k]}')

def read_file():
    start = time.time()
    count = 0
    f = gzip.open("GCA_000001405.29.fasta.gz", 'r')
    # with gzip.open("GCA_000001405.29.fasta"+"GCA_000001405.29.fasta", 'r') as file:
    all_hist={}
    for line in f:
        # print(line)
        count = count + 1
        c1 = ascii_histogram(line)
        c2 = all_hist.copy()
        all_hist = {key: c1.get(key, 0) + c2.get(key, 0) for key in set(c1) | set(c2)}
        if(count%10000==0):
            end = time.time()
            print(f'count{count} persintage:{int(100*count/51e6)} spend time: {int(end-start)}')

    end = time.time()
    print(all_hist)
    print("Execution time in seconds: ",(end-start))
    print("No of lines printed: ",count)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('DR:Read "File GCA_000001405.29.fasta.gz"')
    read_file()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
