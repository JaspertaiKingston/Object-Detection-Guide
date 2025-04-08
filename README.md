## Get Start

1. 建立和啟用python虛擬環境 (Windows)
```shell
python -m venv .env
.\.env\Scripts\activate # linux: source .env/bin/activate
```

2. 安裝labelstudio (服務啟動於: http://localhost:8080/)
```shell
# 方法一 
# 使用docker

mkdir data # 建立資料儲存的路徑
docker run -it -p 8080:8080 -v /data heartexlabs/label-studio:latest
```
<br>

```shell
# 方法二
# 安裝Python Package

pip install -U label-studio
label-studio
```

3. 使用label studio進行標記，參考[label-studio](label_studio)

4. 下載YOLO及訓練使用到的Python Package
```shell
pip install -r requirements.txt
```
5. 建立訓練用的YAML檔，此範例將檔案件在data/data.yaml. 詳細使用請參考[COCO8](https://docs.ultralytics.com/datasets/detect/coco8/)
```yaml
names:
- dog #類別名稱

train: D:\Jasper\yolo_guide\data\yolo_data\images # label-studio下載的訓練用圖片路徑
val: D:\Jasper\yolo_guide\data\yolo_data\images # 驗證用圖片路徑 (此為範例，實際不建議使用和train相同資料集)
```

5. 訓練模型
```bash
# 參數解釋
python train.py --help

# 訓練
python train.py
```

6. 訓練結果
<br>
跑完結果儲存至runs/detect/train中，模型位於runs/detect/train/weights中，包含best(最佳)和last(最後)。

7. 使用模型
```python
from ultralytics import YOLO
model = YOLO("PATH TO MODEL")
results = model("IMAGE TO EVALUATE")
# results 結果為list

for result in results:
    # box
    print(result.boxes)
    # 類別
    print(result.names)
```
