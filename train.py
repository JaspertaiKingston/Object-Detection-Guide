from ultralytics import YOLO
import click

def training(yolo_model_name:str, data_folder:str, epochs:int, imgsz:int) -> None:
    """
    Trainer for yolo model
    
    Args:
        yolo_model_name: yolo model name. Supported model: https://docs.ultralytics.com/models/
        data_folder: path to labeled data json file
        epochs: run epochs
        imgzx: image size to convert while training
    """
    model = YOLO(yolo_model_name)
    result = model.train(data=data_folder, epochs=epochs, imgsz=imgsz)

@click.command()
@click.option("-m", "--model_name", "yolo_model_name", help="Yolo模型名稱或本地模型位置，支援模型: https://docs.ultralytics.com/models/", default="yolov8n.pt")
@click.option("-d", "--data_folder", "data_folder", help="標記資料json檔路徑", default="data/data3.yaml")
@click.option("-e", "--epochs", "epochs", help="訓練週期，此範例預設為1，蒐集夠多資料後，實際使用建議增加至10以上", type=int, default=1)
@click.option("-i", "--image_size", "imgsz", help="訓練時照片大小，值為單邊長度", default=512, type=int)
def run(yolo_model_name, data_folder, epochs, imgsz):
    training(yolo_model_name, data_folder, epochs, imgsz)

if __name__ == "__main__":
    run()
