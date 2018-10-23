#!/bin/bash

#### Set your arguments here ####
############## START ###################
PROJECT_HOME=~/www/bilm-tf
#TRAIN_ELMO_PY=$PROJECT_HOME/bin/train_elmo.py
TRAIN_PREFIX=$PROJECT_HOME/usr_dir/data/sejong.train.char*
#TRAIN_PREFIX=$PROJECT_HOME/usr_dir/word_benchmark_data/1-billion-word-language-modeling-benchmark-r13output/training-monolingual.tokenized.shuffled/*
VOCAB_FILE=$PROJECT_HOME/usr_dir/vocab/sejong.train.vocab.txt
#VOCAB_FILE=$PROJECT_HOME/usr_dir/word_benchmark_data/1-billion-word-language-modeling-benchmark-r13output/vocab-2016-09-10.txt
SAVE_DIR=$PROJECT_HOME/usr_dir/model/sejong
############## END #####################

echo 'train START'
export CUDA_VISIBLE_DEVICES=2
cd $PROJECT_HOME
python -u -m bin.train_elmo \
    --train_prefix=$TRAIN_PREFIX \
    --vocab_file=${VOCAB_FILE} \
    --save_dir=${SAVE_DIR}
echo 'train END'
