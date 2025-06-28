"""Match detected food items with nutrition information."""

from __future__ import annotations

from typing import List
import pandas as pd


class NutritionMatcher:
    """Matches detected items with nutritional data."""

    def __init__(self, lookup_path: str = "data/raw/nutrition_lookup.csv") -> None:
        self.lookup_df = pd.read_csv(lookup_path)

    def match_nutrition(self, detected_items: List[str]) -> pd.DataFrame:
        """Match detected item labels with nutrition lookup table.

        Parameters
        ----------
        detected_items : List[str]
            List of detected item labels.

        Returns
        -------
        pd.DataFrame
            DataFrame containing nutrition information for detected items.
        """
        df = self.lookup_df.copy()
        df = df[df["item_name"].isin(detected_items)].reset_index(drop=True)
        return df

