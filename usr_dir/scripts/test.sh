#!/bin/sh

#### Set your arguments here ####
############## START ###################
PROJECT_HOME=$HOME/www/bilm-tf
TRAIN_PREFIX=$PROJECT_HOME/usr_dir/data/sejong.train.char-*-of-00010
VOCAB_FILE=$PROJECT_HOME/usr_dir/vocab/sejong.train.vocab.txt
SAVE_DIR=$PROJECT_HOME/usr_dir/model/sejong_bio
############## END #####################

cd $PROJECT_HOME
echo 'test START'
python -u -m bin.run_test \
    --test_prefix=$TRAIN_PREFIX \
    --vocab_file=$VOCAB_FILE \
    --save_dir=$SAVE_DIR
echo 'test END'