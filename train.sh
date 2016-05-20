#!/bin/bash
#PBS -l nodes=1:ppn=20
#PBS -l walltime=168:00:00
#PBS -N session2_default
#PBS -A course
#PBS -q GpuQ

export THEANO_FLAGS=device=gpu2,floatX=float32

#cd $PBS_O_WORKDIR

python ./train_nmt.py


