import tensorflow as tf
from ckiptagger import data_utils, construct_dictionary, WS, POS, NER
import os

class ckip_tagger():
    def __init__(self,ckip_data_path = './data', custom_dict_path='./dict', disable_cuda=True, cuda_memory_limit=2048):
        if (disable_cuda == False):
            gpus = tf.config.experimental.list_physical_devices('GPU')
            try:
                tf.config.experimental.set_virtual_device_configuration(gpus[0], [tf.config.experimental.VirtualDeviceConfiguration(cuda_memory_limit)])
            except RuntimeError as e:
                print(e)
        # Load model
        self.ws = WS(ckip_data_path, disable_cuda=disable_cuda)
        self.pos = POS(ckip_data_path, disable_cuda=disable_cuda)
        self.ner = NER(ckip_data_path, disable_cuda=disable_cuda)
        self.dictionary = construct_dictionary(self.__load_custom_dict(custom_dict_path))
        
    def __load_custom_dict(self,custom_dict_path):
        # load all file under path
        dicts = os.listdir(custom_dict_path)
        word_to_weight = {}
        for dic in dicts:
            with open(custom_dict_path + '/' + dic, 'r', encoding='utf-8') as f:
                while(True):
                    line = f.readline()
                    if(len(line)==0):
                        break
                    line_split = line.split()
                    word = line_split[0]
                    try:
                        word_weight = line_split[1]
                    except:
                        word_weight = 1
                    word_to_weight.update({word:word_weight})
        return word_to_weight

    def __get_word_pos_sentence(self,word_sentence, pos_sentence, ner_sentence):
        # Show results
        assert len(word_sentence) == len(pos_sentence)
        res = []
        for word, pos in zip(word_sentence, pos_sentence):
            #
            ner_tag = 'NONE'
            for ner_tag_infos in ner_sentence:
                ner_start,ner_end,_ner_tag,_ner_word = ner_tag_infos
                if(_ner_word == word):
                    ner_tag = _ner_tag
                    break
            #
            res.append((word,pos,ner_tag)) #(斷詞,詞性)
        return res
    
    def parse(self,sentence_list):
        word_sentence_list = self.ws(sentence_list,recommend_dictionary = self.dictionary)
        pos_sentence_list = self.pos(word_sentence_list)
        entity_sentence_list = self.ner(word_sentence_list, pos_sentence_list)
        # print(entity_sentence_list)
        res = []
        for i, sentence in enumerate(sentence_list):
            res.append(self.__get_word_pos_sentence(word_sentence_list[i],  pos_sentence_list[i], entity_sentence_list[i]))
        return res

            
if __name__ == "__main__":
    ckip = ckip_tagger()
    sentence = [
        '國民黨總統參選人韓國瑜8日大造勢","主辦單位稱現場湧入35萬人',
        '民主進步黨，簡稱民進黨，是中華民國主要政黨之一，也是現時中華民國的執政黨及立法院最大黨']
    print(ckip.parse(sentence))
        