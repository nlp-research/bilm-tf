#!/bin/bash

#### Set your arguments here ####
############## START ###################
PROJECT_HOME=$HOME/www/bilm-tf
SAVE_DIR=$PROJECT_HOME/usr_dir/model/sejong_max_char_per_token_50
OUTDIR=$PROJECT_HOME/usr_dir/output/sejong_max_char_per_token_50
OUTFILE=$OUTDIR/weights.hdf5
############## END #####################

echo 'dump weight START'
mkdir $OUTDIR
export CUDA_VISIBLE_DEVICES=2
cd $PROJECT_HOME
python -u -m bin.dump_weights \
    --save_dir=$SAVE_DIR \
    --outfile=$OUTFILE