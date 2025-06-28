# Image-Based Nutritional Analyzer

A computer vision pipeline that detects food items from an image and estimates calorie and macronutrient content using a reference nutrition database.

## Overview
Upload a food image and receive estimated calories and macros. The application uses a YOLOv5 model for object detection and matches detected items with nutritional information stored in `data/raw/nutrition_lookup.csv`.

## Key Features
- **Image upload via Streamlit**
- **YOLO-based food detection**
- **Nutrition table matching**
- **Dashboard interface with summary charts**

## Setup Instructions
```
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

## Folder Structure
```
├── data/
│   └── raw/
│       ├── images/
│       └── nutrition_lookup.csv
├── models/
│   └── yolov5s.pt
├── src/
│   ├── image_loader.py
│   ├── food_detector.py
│   ├── nutrition_matcher.py
│   └── result_formatter.py
├── app/
│   └── streamlit_app.py
├── requirements.txt
├── README.md
└── LICENSE
```

## Sample Screenshot
![sample](docs/sample_screenshot.png)

## Disclaimer
This tool provides nutritional estimates only and is not intended for medical or dietary advice.

