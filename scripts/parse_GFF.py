#!/usr/bin/env python3
import argparse
import gff_functions

def lawyer():
    parse_master5000=argparse.ArgumentParser(description="Extracting sequence information from a "\
                                            "gff file and out put them into a fasta file")

    parse_master5000.add_argument("fasta",help="The name of the genome FASTA file")
    parse_master5000.add_argument("gff3",help="The name of the GFF3 file")
    parse_master5000.add_argument("-o","--output",help="The name of the output file")
    return parse_master5000.parse_args()

def main():
    args = lawyer()
    genome_sequence = gff_functions.read_fasta(args.fasta)
    gff_functions.read_gff(args.gff3)
    gff_functions.write_output()
#
if __name__ == "__main__":
    main()