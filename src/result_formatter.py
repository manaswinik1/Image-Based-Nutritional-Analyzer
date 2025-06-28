"""Format nutrition results for display."""

from __future__ import annotations

from typing import Tuple
import pandas as pd
import matplotlib.pyplot as plt



def summarize_nutrition(nutrition_df: pd.DataFrame) -> Tuple[str, plt.Figure]:
    """Generate a textual summary and pie chart of nutrition totals.

    Parameters
    ----------
    nutrition_df : pd.DataFrame
        DataFrame containing nutrition data for detected items.

    Returns
    -------
    Tuple[str, plt.Figure]
        Summary string and a matplotlib figure showing macronutrient
        distribution.
    """
    totals = nutrition_df[["calories", "protein_g", "fat_g", "carbs_g"]].sum()
    summary = (
        f"Total Calories: {totals['calories']:.0f} kcal\n"
        f"Protein: {totals['protein_g']:.1f} g\n"
        f"Fat: {totals['fat_g']:.1f} g\n"
        f"Carbohydrates: {totals['carbs_g']:.1f} g"
    )

    fig, ax = plt.subplots()
    macros = [totals["protein_g"], totals["fat_g"], totals["carbs_g"]]
    labels = ["Protein", "Fat", "Carbs"]
    ax.pie(macros, labels=labels, autopct="%1.1f%%")
    ax.set_title("Macronutrient Distribution")

    return summary, fig

