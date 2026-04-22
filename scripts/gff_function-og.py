#!/usr/bin/env python3

from collections import defaultdict
import argparse
import csv

def lawyer():
    parse_master5000=argparse.ArgumentParser(description="Extracting sequence information from a gff file and out put them into a fasta file")

    parse_master5000.add_argument("fasta",help="The name of the genome FASTA file")
    parse_master5000.add_argument("gff",help="The name of the GFF file")
    parse_master5000.add_argument("-o","--output",help="The name of the output file")
    return parse_master5000.parse_args()

def read_fasta():
    fasta_input = args.fasta
    with open(fasta_input, "r") as fasta_file:
        next(fasta_file)  # skip the header line
        genome_sequence = "".join(line.strip() for line in fasta_file)
    return genome_sequence

def read_gff():
    start_position=defaultdict(int)
    end_position=defaultdict(int)
    sequence_id=defaultdict(str)
    with open(args.gff) as gff_file:
        gff_library=csv.reader(gff_file, delimiter="\t")
        for line in gff_library:
            gene_name = line[8].strip()
            sequence_id[gene_name] = line[0].strip()
            start_position[gene_name] = line[3].strip()
            end_position[gene_name] = line[4].strip()
    return sequence_id, start_position, end_position

def write_output(sequence_id, start_position, end_position, genome_sequence):
    if args.output:
        outfile = open(f"{args.output}", "w")
    else:
        outfile = open(f"{args.fasta}-genes.fasta", "w")
    for key in sequence_id:
        outfile.write(f">{sequence_id[key]} {key}\n")   # chrom ID first, then gene name
        outfile.write(f"{genome_sequence[int(start_position[key]):int(end_position[key])]}\n")
    outfile.close()
    return(outfile)

def main():
    genome_sequence = read_fasta()
    sequence_id, start_position, end_position = read_gff()
    file = write_output(sequence_id, start_position, end_position, genome_sequence)
    print(file)

# ===== using lawyer function =====
args = lawyer()

if __name__ == "__main__":
    main()

