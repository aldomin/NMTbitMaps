#!/bin/bash
#PBS -l nodes=1:ppn=24
#PBS -l walltime=24:00:00
#PBS -N session2_default
#PBS -A course
#PBS -q ShortQ

export THEANO_FLAGS=device=cpu,floatX=float32

#cd $PBS_O_WORKDIR

python ./translate.py -n -p 20 \
	./model_hal.npz  \
	/veu4/usuaris31/daldon/charnn/dl4mt-material/session1/corpus/train/train.un.zh.pkl \
	/veu4/usuaris31/daldon/charnn/dl4mt-material/session1/corpus/train/train.un.es.pkl \
	/veu4/usuaris29/mruiz/tfg-imagenes/test/test.un.zh \
	./test.trans.un.es
