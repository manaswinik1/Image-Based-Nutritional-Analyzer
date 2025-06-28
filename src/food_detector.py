"""Food detection utilities leveraging a YOLOv5 model."""

from typing import List, Dict
import numpy as np
from ultralytics import YOLO


class FoodDetector:
    """Wrapper around a YOLO model for food detection."""

    def __init__(self, model_path: str = "models/yolov5s.pt") -> None:
        """Load the YOLO model from the specified path."""
        self.model = YOLO(model_path)

    def detect_food(self, image: np.ndarray) -> List[Dict]:
        """Detect food items in an image.

        Parameters
        ----------
        image : np.ndarray
            Image in RGB format.

        Returns
        -------
        List[Dict]
            List of detection dictionaries containing bounding boxes,
            class labels, and confidence scores.
        """
        results = self.model(image)
        detections = []
        for r in results:
            boxes = r.boxes
            names = r.names
            for box in boxes:
                xmin, ymin, xmax, ymax = box.xyxy[0].tolist()
                label = names[int(box.cls)]
                conf = float(box.conf)
                detections.append(
                    {
                        "bbox": [xmin, ymin, xmax, ymax],
                        "label": label,
                        "confidence": conf,
                    }
                )
        return detections

