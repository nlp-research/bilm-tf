#from allennlp.modules.elmo import Elmo, batch_to_ids
from allennlp.commands.elmo import ElmoEmbedder
import pdb
import hgtk

#PROJECT_HOME = 
options_file = '/Users/nhnent/www/bilm-tf/usr_dir/model/sejong/options.json'
weight_file = '/Users/nhnent/www/bilm-tf/usr_dir/output/sejong/weights.hdf5'



# use batch_to_ids to convert sentences to character ids
sentences = ['않다', '밥을먹자']
decomposed_sentences = []
for sentence in sentences:
    decomposed_sentence = []
    for emj in list(sentence):
        try:
            decomposed_sentence.append(''.join(hgtk.letter.decompose(emj)))
        except Exception as e:
            print(e, emj)
            decomposed_sentence.append((emj,))
    decomposed_sentences.append(decomposed_sentence)
print('decomposed_sentence=',decomposed_sentences)

elmo = ElmoEmbedder(options_file=options_file, weight_file=weight_file)
vectors = elmo.embed_sentence(decomposed_sentences[0])
pdb.set_trace()
#character_ids = batch_to_ids(decomposed_sentences)

#print(character_ids)
#elmo = Elmo(options_file, weight_file, 2, dropout=0)
#embeddings = elmo(character_ids)

#pdb.set_trace()
#print(embeddings)