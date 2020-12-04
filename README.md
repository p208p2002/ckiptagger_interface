# interface for CkipTagger 
[CkipTagger，中研院中文斷詞系統](https://github.com/ckiplab/ckiptagger)

讓你更方便的使用CkipTagger
> 這只是一個讓你方便使用CkipTagger的接口，所有斷詞功能與成果均與本人無關，任何接口以外的問題請至[CkipTagger](https://github.com/ckiplab/ckiptagger)尋找答案與幫助

## Installation
**請確保已經安裝tensorflow**

- 安裝ckip-tagger
```
pip install -U ckiptagger
```

- 安裝 interface for CkipTagger
```
pip install git+https://github.com/p208p2002/ckiptagger_interface.git
```

- 下載data(約2G)
```
pip install gdown
python download_data.py
```

### Manual download model files
The model files are available on several mirror sites.
- [iis-ckip](http://ckip.iis.sinica.edu.tw/data/ckiptagger/data.zip)
- [gdrive-ckip](https://drive.google.com/drive/folders/105IKCb88evUyLKlLondvDBoh7Dy_I1tm)
- [gdrive-jacobvsdanniel](https://drive.google.com/drive/folders/15BDjL2IaX3eYdFVzT422VwCb743Hrbi3)

## Usage
### Init 
```python
def __init__(self,ckip_data_path, custom_dict_path, disable_cuda, cuda_memory_limi):
```
- ckip_data_path: 對應ckip data 資料夾。
    - default : "./data"
- custom_dict_path: 所有資料夾底下的檔案會被載入作為`recommend_dictionary`
    - default: "./dict"
- disable_cuda: 禁用cuda device
    - default: True
- cuda_memory_limi: cuda device 顯存限制(MB)
    - default: 2048

### Parse
```python
from ckiptagger_interface import ckiptagger
ckip = ckiptagger()
sentence = [
    '國民黨總統參選人韓國瑜8日大造勢","主辦單位稱現場湧入35萬人',
    '民主進步黨，簡稱民進黨，是中華民國主要政黨之一，也是現時中華民國的執政黨及立法院最大黨']
print(ckip.parse(sentence))

# [[('國民黨', 'Nb', 'ORG'), ('總統', 'Na', 'NONE'), ('參選人', 'Na', 'NONE'), ('韓國瑜', 'Nb', 'PERSON'), ('8日', 'Nd', 'DATE'), ('大', 'VH', 'NONE'), ('造勢', 'VB', 'NONE'), ('"', 'FW', 'NONE'), (',', 'COMMACATEGORY', 'NONE'), ('"', 'FW', 'NONE'), ('主辦', 'VC', 'NONE'), ('單位', 'Na', 'NONE'), ('稱', 'VG', 'NONE'), ('現場', 'Nc', 'NONE'), ('湧入', 'VCL', 'NONE'), ('35萬', 'Neu', 'CARDINAL'), ('人', 'Na', 'NONE')], [('民主進步黨', 'Nb', 'ORG'), ('，', 'COMMACATEGORY', 'NONE'), ('簡稱', 'VG', 'NONE'), ('民進黨', 'Nb', 'ORG'), ('，', 'COMMACATEGORY', 'NONE'), ('是', 'SHI', 'NONE'), ('中華民國', 'Nc', 'GPE'), ('主要', 'A', 'NONE'), ('政黨', 'Na', 'NONE'), ('之', 'DE', 'NONE'), ('一', 'Neu', 'NONE'), ('，', 'COMMACATEGORY', 'NONE'), ('也', 'D', 'NONE'), ('是', 'SHI', 'NONE'), ('現時', 'Nd', 'NONE'), ('中華民國', 'Nc', 'GPE'), ('的', 'DE', 'NONE'), ('執政黨', 'Na', 'NONE'), ('及', 'Caa', 'NONE'), ('立法院', 'Nc', 'ORG'), ('最', 'Dfa', 'NONE'), ('大', 'VH', 'NONE'), ('黨', 'Na', 'NONE')]]
```
