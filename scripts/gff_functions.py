#!/usr/bin/env python3

import csv

def read_fasta(fasta_file):
    seq=''
    with open(fasta_file, "r") as f:
        for line in f:
            if line.startswith(">"):
                continue
            else:
                seq += line.strip()
    return seq

def read_gff(gff3_file):
    with open(gff3_file) as g:
        gff_library=csv.reader(g, delimiter="\t")
        for line in gff_library:
            print(line)

def write_output(seq,gff3_data,filename):
    print("This is the write_output function")

if __name__ == "__main__": 
    main()