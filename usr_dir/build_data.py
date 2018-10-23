import argparse
import operator
import json
import glob
import os
import hgtk
import re


#1993/SN //SP 06/SN //SP 08/SN

def main(args):
    
    print(f'Removinf previous trauilin data files: {args.train_file}*')
    output_files = glob.glob(args.train_file + '*')
    for output_file in output_files:
        os.remove(output_file)
    vocab_count = dict()

    #news.en-00001-of-00100
    
    n_train_tokens = 0
    jaso_set = set()
    zeros = 5
    total_file_number = int(args.split_number)
    # #%# 엠마누엘 웅가로 / 의상서 실내 장식품으로… 디자인 세계 넓혀
    with open(args.raw_file, 'r', encoding='utf-8') as raw_f:
        for index, line in enumerate(raw_f):
            # for test
            if index == 100:
                None
                #break
                #None
            if not line.startswith('#%#'):
                continue

            line = line.replace('#%#', '').strip().replace(' ', '')
            emjs = list(line) #음절 
            emj_list_to_write = []
            for emj in emjs:
                #한자나 숫자일 경우
                if hgtk.checker.is_hanja(emj):
                    emj_list_to_write.append('H')
                elif re.findall(r'[\u4e00-\u9fff][\u3400-\u4DBF][\u20000-\u2A6DF][]', emj):
                    emj_list_to_write.append('h')
                elif hgtk.checker.is_latin1(emj):
                    emj_list_to_write.append('A')
                elif hgtk.checker.is_hangul(emj):
                    emj_list_to_write.append(''.join(hgtk.letter.decompose(emj)))
                else:
                    emj_list_to_write.append(emj)
            #jaso단위로
            for e in emj_list_to_write:
                vocab_count[e] = vocab_count.get(e, 0) + 1
                jaso_set.update(list(e))
            train_file_number = (index % total_file_number) + 1
            train_file_name = f'{args.train_file}-{str(train_file_number).zfill(zeros)}-of-{str(total_file_number).zfill(zeros)}'
            n_train_tokens += len(emj_list_to_write)
            with open(train_file_name, 'a', encoding='utf-8') as train_f:
                train_f.write(' '.join(emj_list_to_write) + '\n')

            # for log print
            if index % 10000 == 0:
                print(f"index={index}, line={line}, n_train_tokens={n_train_tokens}, train_file_name={train_file_name}")
                print(f'len(jaso_set)={len(jaso_set)}, jaso_set={jaso_set}')

    #print(args.vocab_json)
    sorted_vocab_count = sorted(vocab_count.items(), key=operator.itemgetter(1), reverse=True)
    info_json = {
        "n_train_tokens" : n_train_tokens
        , "n_tokens_vocab" : len(sorted_vocab_count)
        ,  "max_characters_per_token" : max([len(vocab) for vocab, count in sorted_vocab_count])
        , 'n_characters': len(jaso_set)
 
    }
    info_json_path = os.path.join(os.path.dirname(args.vocab_file), 'info.json')
    json.dump(info_json, open(info_json_path, 'w'), sort_keys=True, indent=1, ensure_ascii=False)

    with open(args.vocab_file, 'w', encoding='utf-8') as vocab_f:
        vocab_f.write('<S>\n</S>\n<UNK>\n')
        for char, count in sorted_vocab_count:
            vocab_f.write(f'{char}\n')
    print(f'n_train_tokens={n_train_tokens}, len(jaso_set)={len(jaso_set)}--------------')
    #print(jasos)

    return

def normalize(sentence):
    
    return


if __name__ == '__main__':
    

    parser = argparse.ArgumentParser()
    parser.add_argument('--raw_file', help='Location of raw file path')
    parser.add_argument('--train_file', help='Output train file')
    parser.add_argument('--vocab_file', help='Output vocabulary file')
    parser.add_argument('--split_number', help='split size', default=1)
    args = parser.parse_args()
    main(args)
