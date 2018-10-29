# nlp-research/bilm-tf

This repository supports both (1) training ELMo representations and (2) using pre-trained ELMo representaions to your new model

## Installing packages for training
```
pip install tensorflow-gpu==1.2 h5py hgtk
```

## Insatlling packaages for using pre-trained ELMo
```
pip install allennlp hgtk
```

## Using pre-trained ELMo representatinos to your new model
See `usr_dir/embed_with_elmo.py` for detailed example.
Make sure to set `n_characters=262` example during prediction in the `options.json`.
See [here](https://github.com/allenai/bilm-tf#whats-the-deal-with-n_characters-and-padding).
```python
from allennlp.commands.elmo import ElmoEmbedder
import hgtk
import preprocess

options_file = 'path/to/options.json' # Make sure to set n_characters=262
weight_file = 'path/to/weights.hdf5'

elmo = ElmoEmbedder(options_file, weight_file) # create your ELMo class based on weight and option file

sentences = ['밥을 먹자', 'apple은 맛있다']
# normalize, split emj to jaso, add bio tag through preprocess.preprocess_and_tokenize()
preprocessed_sentences = []
for sentence in sentences:
    preprocessed_sentences.append(preprocess.preprocess_and_tokenize(sentence))
#[['Bㅂㅏㅂ', 'Iㅇㅡㄹ', 'Bㅁㅓㄱ', 'Iㅈㅏ'], ['BＡ', 'Iㅇㅡㄴ', 'Bㅁㅏㅅ', 'Iㅇㅣㅆ', 'Iㄷㅏ']]

# get ELMo vectors
vectors = elmo.embed_batch(preprocessed_sentences)

# return value 'vectors' is list of tensors.
# Each vector contains each layer of ELMo representations of sentences with shape (number of sentences, number of tokens(emjs), dimension).
# use elmo.embed_senteces(preprocessed_sentences) to return generator instead of list
```

