#!/bin/bash

#### Set your arguments here ####
############## START ###################
PROJECT_HOME=$HOME/www/bilm-tf
TRAIN_PREFIX=$PROJECT_HOME/usr_dir/data/sejong.train.char*
VOCAB_FILE=$PROJECT_HOME/usr_dir/data/sejong.train.vocab.txt
SAVE_DIR=$PROJECT_HOME/usr_dir/model/sejong_unroll_steps_40
############## END #####################

echo 'train START-------------------'
export CUDA_VISIBLE_DEVICES=1,2,3
cd $PROJECT_HOME
echo "making model save_dir=$SAVE_DIR"
mkdir $SAVE_DIR
python -u -m bin.train_elmo \
    --train_prefix=$TRAIN_PREFIX \
    --vocab_file=${VOCAB_FILE} \
    --save_dir=${SAVE_DIR}
echo 'train END---------------------'