from ckiptagger_interface import ckiptagger      
if __name__ == "__main__":
    ckip = ckiptagger()
    sentence = [
        '國民黨總統參選人韓國瑜8日大造勢","主辦單位稱現場湧入35萬人',
        '民主進步黨，簡稱民進黨，是中華民國主要政黨之一，也是現時中華民國的執政黨及立法院最大黨']
    print(ckip.parse(sentence))
        
