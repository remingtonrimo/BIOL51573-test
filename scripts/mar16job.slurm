#!/bin/bash

#SBATCH --job-name=blastjob
#SBATCH --partition=comp01
#SBATCH --nodes=1
#SBATCH --qos=comp
#SBATCH --tasks-per-node=32
#SBATCH --time=00:00:10
#SBATCH -o test_%j.out
#SBATCH -e test_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=rmotte@uark.edu

export OMP_NUM_THREADS=32

module purge
module load intel/18.0.1 impi/18.0.1 mkl/18.0.1
module load blast

blastn -query watermelon.fsa -subject watermelon.fsa > wat.vs.wat.blastn