from allennlp.commands.elmo import ElmoEmbedder
import hgtk #pip install hgtk
import preprocess

#PROJECT_HOME = 
options_file = '/Users/nhnent/www/bilm-tf/usr_dir/model/sejong_max_char_per_token_50/options.json'
weight_file = '/Users/nhnent/www/bilm-tf/usr_dir/output/sejong_max_char_per_token_50/weights.hdf5'

# use batch_to_ids to convert sentences to character ids
sentences = ['밥을 먹자','apple은 맛있다']
preprocessed_sentences = []
for sentence in sentences:
    print(sentence)
    preprocessed_sentences.append(preprocess.preprocess_and_tokenize(sentence))

elmo = ElmoEmbedder(options_file, weight_file)
vectors = elmo.embed_batch(preprocessed_sentences) #return list
#vectors = elmo.embed_sentences(preprocessed_sentences) #return generator