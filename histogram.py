import sys, getopt
import time
import gzip
import collections
import matplotlib.pyplot as plt

all_col = collections.Counter()


def read_file(file_name):
    start = time.time()
    count = 0
    is_string = 0
    if (file_name.find('.gz') != -1):
        f = gzip.open(file_name, 'r')
    else:
        f = open(file_name)
        is_string = 1

    for line in f:
        # print(line)
        if (is_string == 0):
            line_s = str(line, encoding='utf-8')
        else:
            line_s = line

        if (line_s[0] == ">"):
            print(line_s)
            continue
        count = count + 1
        hi = collections.Counter(line_s)
        all_col.update(hi)
        if (count % 500000 == 0):
            end = time.time()
            print(f'read line: {count} persintage:{int(100 * count / 51e6)}% spend time: {int(end - start)}')
            # break
    all_col.pop("\n")  # remove new line from dict
    end = time.time()
    '''plot the data'''
    gen_name = list(all_col.keys())
    gen_vale = list(all_col.values())
    plt.bar(range(len(all_col)), gen_vale, tick_label=gen_name)
    plt.show()
    '''print result'''
    print(all_col)
    print("Execution time in seconds: ", (end - start))
    print("No of lines printed: ", count)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    file_name = "GCA_000001405.29.fasta.gz"
    opts, args = getopt.getopt(sys.argv[1:], '', ['file'])
    print(args)
    try:
        file_name = args[0]

    except:
        file_name = "GCA_000001405.29.fasta.gz"
    print_hi('doc Read' + file_name)
    read_file(file_name)
