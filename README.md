# interface for CkipTagger 
[CkipTagger，工研院中文斷詞系統](https://github.com/ckiplab/ckiptagger)

讓你更方便的使用CkipTagger
> 這只是一個讓你方便使用CkipTagger的接口，所有斷詞功能與成果均與本人無關，任何接口以外的問題請至[CkipTagger](https://github.com/ckiplab/ckiptagger)尋找答案與幫助

## Usage
### Installation
- 安裝ckip-tagger
```
pip install -U ckiptagger[tf,gdown]
```
- 下載data(約2G)
```
python download_data.py
```

### Init 
```python
ckip_tagger(ckip_data_path,custom_dict_path)
```
- ckip_data_path: 對應ckip data 資料夾。
    - default : "./data"
- custom_dict_path: 所有資料夾底下的檔案會被載入作為`recommend_dictionary`
    - default: "./dict"
### Parse
```python
from ckip_tagger import ckip_tagger
ct = ckip_tagger()
sentence_list = ["國民黨總統參選人韓國瑜8日大造勢","，主辦單位稱現場湧入35萬人"]
print(ct.parse(sentence_list))

# [[('國民黨', 'Nb'), ('總統', 'Na'), ('參選人', 'Na'), ('韓國瑜', 'Nb'), ('8日', 'Nd'), ('大', 'VH'), ('造勢', 'VB')],[('主辦', 'VC'), ('單位', 'Na'), ('稱', 'VG'), ('現場', 'Nc'), ('湧入', 'VCL'), ('35萬', 'Neu'), ('人', 'Na')]
```
