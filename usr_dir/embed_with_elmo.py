from allennlp.modules.elmo import Elmo, batch_to_ids
from allennlp.commands.elmo import ElmoEmbedder
import pdb
import hgtk
import preprocess

#PROJECT_HOME = 
options_file = '/Users/nhnent/www/bilm-tf/usr_dir/model/sejong_max_char_per_token_50/options.json'
weight_file = '/Users/nhnent/www/bilm-tf/usr_dir/output/sejong_max_char_per_token_50/weights.hdf5'


# use batch_to_ids to convert sentences to character ids

sentences = ['밥을 먹자', '퇴근하고 싶다...']
batch_sentences = []
for sentence in sentences:
    bio_tagged_token_list = preprocess.tag_bio(sentence)
    decomposed_token_list = []
    for tag, emj in bio_tagged_token_list:
        if hgtk.checker.is_hangul(emj):
            decomposed_token_list.append(tag + ''.join(hgtk.letter.decompose(emj)))   
        else:
            decomposed_token_list.append(tag + '' + emj)
    batch_sentences.append(decomposed_token_list)        

#decomposed_token_list = ["I", "ate", "an", "apple", "for", "breakfast"]
print('batch_sentences={}'.format(batch_sentences))


elmo = ElmoEmbedder(options_file, weight_file)

#vectors = elmo.embed_sentence(decomposed_token_list)
vectors = elmo.embed_batch(batch_sentences)
pdb.set_trace()
