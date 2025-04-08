# 使用label studio進行標記

### 創建或登入帳號
![Image of label studio login](/label_studio/readme_image/login.jpg)

### 建立專案
![Image of project creation](/label_studio/readme_image/create_project.jpg)

### 專案名稱命名
在Project Name為專案命名

![Image of project name tab](/label_studio/readme_image/project_name.jpg)

### 上傳照片
上傳要標記的照片，範例照片位於[sample_data](sample_data)

![Image of project image upload](/label_studio//readme_image/upload_images.jpg)

### 選擇要標記方式
此範例使用Object Detection with Bounding Boxes

![Image of project label setup](/label_studio/readme_image/label_setup.jpg)

### 新增標記類別
在Add label names新增要的類別，按Add，新增結束後右上角Save

![Image of adding label](/label_studio/readme_image/add_label.jpg)

### 標記
進入專案點擊照片進入標記，先點選標記在畫框，最後儲存

![Image of drawing box](/label_studio/readme_image/label.jpg)

### 匯出專案
此範例以yolo含圖像標記方式匯出專案

![Image of yolo format export](/label_studio/readme_image/yolo_format.jpg)

### 解壓縮並重新命名
此範例將檔案解壓縮並放置data\yolo_data資料夾底下。YOLO的格式資料夾樣式如下(路徑: data\yolo_data)

![Image of folder](/label_studio/readme_image/folder.jpg)