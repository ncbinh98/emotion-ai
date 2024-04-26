# YOLOv5 Object Detection Project

This project is an implementation of YOLOv5, a popular deep learning algorithm for real-time object detection, using Python. YOLOv5 is a state-of-the-art object detection model that achieves high accuracy and fast inference speed.

## Requirements

- Python 3.x
- PyTorch
- OpenCV
- NumPy

You can install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Create venv

```bash
python -m venv env
```

2. Use env

```bash
source env/bin/activate
```

3. Preprocessing data

```bash
python pre_processing.py
```

4. Train model

```bash
python train.py
```

5. Predict

```bash
python predict.py
```

## References

- YOLOv5 GitHub repository: [https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5)
- YOLOv5 paper: [YOLOv5: A Universal Object Detector](https://arxiv.org/abs/2104.06867)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
