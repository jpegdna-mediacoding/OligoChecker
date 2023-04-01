import argparse
from tools.fasta import get_oligos

def compute_data(data):
    """Checks the length of the oligos"""
    len_data = list(map(len, data))
    possible_lens = set(len_data)
    counter_lens = {}
    for el in possible_lens:
        counter_lens[el] = len_data.count(el)
    return counter_lens

def nice_print(stats):
    """Pretty print"""
    for el in stats.keys():
        print(f"{stats[el]} oligos have a length of {el}")


def main():
    """Checks the size of the formatted oligos"""
    parser = argparse.ArgumentParser()
    parser.add_argument('FNAME',
                        type=str,
                        help='Filename of the input fasta file')
    args = parser.parse_args()
    fname = args.FNAME
    data = get_oligos(fname)
    stats = compute_data(data)
    nice_print(stats)


if __name__ == '__main__':
    main()
