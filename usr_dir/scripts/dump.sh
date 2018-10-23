#!/bin/bash

#### Set your arguments here ####
############## START ###################
PROJECT_HOME=~/www/bilm-tf
SAVE_DIR=$PROJECT_HOME/usr_dir/model/sejong
OUTFILE=$PROJECT_HOME/usr_dir/output/sejong/weights.hdf5
############## END #####################

echo 'dump weight START'
export CUDA_VISIBLE_DEVICES=2
cd $PROJECT_HOME
python -u -m bin.dump_weights \
    --save_dir=$SAVE_DIR \
    --outfile=$OUTFILE