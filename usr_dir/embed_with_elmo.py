from allennlp.modules.elmo import Elmo, batch_to_ids #pip instal allennlp
from allennlp.commands.elmo import ElmoEmbedder
import pdb
import hgtk #pip install hgtk
import preprocess
import numpy as np

#PROJECT_HOME = 
options_file = '/Users/nhnent/www/bilm-tf/usr_dir/model/sejong_max_char_per_token_50/options.json'
weight_file = '/Users/nhnent/www/bilm-tf/usr_dir/output/sejong_max_char_per_token_50/weights.hdf5'

# use batch_to_ids to convert sentences to character ids
sentences = ['밥을 먹자 123', '퇴근하고 싶다...AAA']
preprocessed_sentences = []
for sentence in sentences:
    preprocessed_sentences.append(preprocess.preprocess_and_tokenize(sentence))

print(preprocessed_sentences)
elmo = ElmoEmbedder(options_file, weight_file)

vectors = elmo.embed_batch(preprocessed_sentences) #return list
#vectors = elmo.embed_sentences(preprocessed_sentences) #return generator
