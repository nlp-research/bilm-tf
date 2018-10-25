#!/bin/bash

#### Set your arguments here ####
############## START ###################
PROJECT_HOME=$HOME/www/bilm-tf
BUILD_DATA_PY=$PROJECT_HOME/usr_dir/build_data.py
#RAW_FILE=$PROJECT_HOME/usr_dir/raw/sejong.train.morph.original
RAW_FILE=$PROJECT_HOME/usr_dir/raw/sejong_raw.txt
TRAIN_FILE=$PROJECT_HOME/usr_dir/data/sejong.train.char
VOCAB_FILE=$PROJECT_HOME/usr_dir/data/sejong.train.vocab.txt
#VOCAB_JSON=$PROJECT_HOME/usr_dir/data/sejong.train.vocab.json
SPLIT_NUMBER=50
############## END #####################

echo "building train file and vocab file START"
python -u $BUILD_DATA_PY \
    --raw_file=${RAW_FILE} \
    --train_file=${TRAIN_FILE} \
    --vocab_file=${VOCAB_FILE} \
    --split_number=${SPLIT_NUMBER}
echo "building train file and vocab file END"