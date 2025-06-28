"""Streamlit application for the Image-Based Nutritional Analyzer."""

from __future__ import annotations

import io
from typing import List

import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image, ImageDraw

from src.image_loader import load_image
from src.food_detector import FoodDetector
from src.nutrition_matcher import NutritionMatcher
from src.result_formatter import summarize_nutrition


def draw_detections(image: Image.Image, detections: List[dict]) -> Image.Image:
    """Draw bounding boxes and labels on the image."""
    draw = ImageDraw.Draw(image)
    for det in detections:
        bbox = det["bbox"]
        label = det["label"]
        conf = det["confidence"]
        draw.rectangle(bbox, outline="red", width=2)
        draw.text((bbox[0], bbox[1] - 10), f"{label} {conf:.2f}", fill="red")
    return image


def main() -> None:
    st.title("Image-Based Nutritional Analyzer")
    st.sidebar.header("Upload Image")

    uploaded_file = st.sidebar.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        pil_image = Image.open(io.BytesIO(bytes_data)).convert("RGB")
        image_np = np.array(pil_image)

        detector = FoodDetector()
        detections = detector.detect_food(image_np)
        if detections:
            annotated = draw_detections(pil_image.copy(), detections)
            st.image(annotated, caption="Detected Items")

            labels = [d["label"] for d in detections]
            matcher = NutritionMatcher()
            nutrition_df = matcher.match_nutrition(labels)

            if not nutrition_df.empty:
                summary, fig = summarize_nutrition(nutrition_df)
                st.subheader("Nutrition Summary")
                st.text(summary)
                st.pyplot(fig)
            else:
                st.info("No nutrition information found for detected items.")
        else:
            st.warning("No food items detected.")


if __name__ == "__main__":
    main()

