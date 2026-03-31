#!/usr/bin/env python3

import argparse

parse_master5000=argparse.ArgumentParser(description="This script creates a slurm script for a job submission")

parse_master5000.add_argument("jobname",help="The name of the job")
parse_master5000.add_argument("time",help="The amount of time you need")
parse_master5000.add_argument("qname",help="The queue you want to use")
parse_master5000.add_argument("email",help="Your email address")

parse_master5000.add_argument("-n","--nodes",help="The number of nodes you want to use",type=int,default=1)

args=parse_master5000.parse_args()

# we are going to first prompt the user to input the job name
print("#!/bin/bash")
print()
print(f"#SBATCH --job-name={args.jobname}")
print(f"#SBATCH --partition={args.qname}")
if args.nodes > 1:
    print(f"#SBATCH --nodes={args.nodes}")
print(f"#SBATCH --nodes=1")
print(f"#SBATCH --qos=comp")
print(f"#SBATCH --tasks-per-node=32")
print(f"#SBATCH --time={args.time}")
print(f"#SBATCH -o test_%j.out")
print(f"#SBATCH -e test_%j.err")
print(f"#SBATCH --mail-type=ALL")
print(f"#SBATCH --mail-user={args.email}")
print()
print(f"export OMP_NUM_THREADS=32")
print()
print(f"module purge")
print(f"module load intel/18.0.1 impi/18.0.1 mkl/18.0.1")
print()
print(f"cd $SLURM_SUBMIT_DIR")
