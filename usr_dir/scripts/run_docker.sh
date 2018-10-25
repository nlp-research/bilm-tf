#!/bin/bash

#### Set your arguments here ####
############## START ###################
VOLUME=$HOME/www/bilm-tf:/root/www/bilm-tf
PORT=9000:9000
IMAGE=allennlp/bilm-tf:training-gpu
NAME=elmo
############## END #####################

#nvidia-docker run -it -v ~/www/bilm-tf:/root/www/bilm-tf allennlp/bilm-tf:training-gpu /bin/bash
echo "starting docker container for $NAME"
sudo nvidia-docker run -it -p $PORT -v $VOLUME --name=$NAME $IMAGE /bin/bash