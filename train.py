from ultralytics import YOLO
import os

model = YOLO('yolov8n-cls.pt')  # load a pretrained model (recommended for training)
current_dir = os.getcwd()
print(current_dir)
full_path = os.path.join(current_dir, 'my_dataset')
print("@@@full_path",full_path)
# Train the model
results = model.train(data=full_path, epochs=10, imgsz=64, batch=32)
