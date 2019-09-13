# CkipTagger interface
讓你更方便的使用CkipTagger
> 這只是一個接口，需要搭配[CkipTagger](https://github.com/ckiplab/ckiptagger)使用
## Usage
先安裝`CkipTagger`並與`CkipTagger`的`data資料夾`放在一起使用
> 可使用`down_data.py`下載data資料
### init 
```
ckip_tagger(ckip_data_path,custom_dict_path)
```
- ckip_data_path: 對應ckip data 資料夾路。
    - default : "./data"
- custom_dict_path: 所有資料夾底下的檔案會被載入作為`recommend_dictionary`
    - default: "./dict"
## parse
```
ct = ckip_tagger()
sentence_list = ["國民黨總統參選人韓國瑜8日大造勢","，主辦單位稱現場湧入35萬人"]
ct.parse(sentence_list)

# [[('國民黨', 'Nb'), ('總統', 'Na'), ('參選人', 'Na'), ('韓國瑜', 'Nb'), ('8日', 'Nd'), ('大', 'VH'), ('造勢', 'VB')],[('主辦', 'VC'), ('單位', 'Na'), ('稱', 'VG'), ('現場', 'Nc'), ('湧入', 'VCL'), ('35萬', 'Neu'), ('人', 'Na')]
```