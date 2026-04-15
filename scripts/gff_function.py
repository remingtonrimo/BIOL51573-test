#!/usr/bin/env python3

import argparse
def lawyer():
    parse_master5000=argparse.ArgumentParser(description="Extracting sequence information from a gff file and out put them into a fasta file")

    parse_master5000.add_argument("fasta",help="The name of the genome FASTA file")
    parse_master5000.add_argument("gff",help="The name of the GFF file")
    parse_master5000.add_argument("-o","--output",help="The name of the output file",action="store_true")
    return parse_master5000.parse_args()


def main():
    answer = fib_master5000()
    print_output(answer)

# ===== using lawyer function =====
args = lawyer()

if __name__ == "__main__":
    main()

