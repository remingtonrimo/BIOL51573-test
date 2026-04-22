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

def read_gff(gff3_file, sequence):
    with open(gff3_file) as g:
        gff_library=csv.reader(g, delimiter="\t")
        for line in gff_library:
            start_pos= line[3]
            end_pos = line[4]
            feature_seq = sequence[int(start_pos)-1:int(end_pos)]
            # print(start_pos, end_pos, len(feature_seq), gene_name)
            
            gene_name = line[8]
            split_name = gene_name.split(";")
            gene_id = split_name[0].split("=")[1]
            write_output(gene_id, feature_seq)
            # alternatively store in a dictionary

def write_output(name,seq):
    print(f">{name}\n{seq}")

if __name__ == "__main__": 
    main()