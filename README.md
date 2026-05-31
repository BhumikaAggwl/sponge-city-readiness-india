# 🌧 Sponge City Readiness Index (SCRI) for India

## IEEE GRSS Earth Day Hackathon 2026 — PS-5

A machine learning and geospatial analytics framework for assessing Sponge City Readiness across India using long-term rainfall observations, rainfall downscaling, explainable AI, and interactive visualization.

---

# 📌 Project Overview

Urban flooding and rainfall variability are increasing due to climate change and rapid urbanization.

This project develops a data-driven Sponge City Readiness Index (SCRI) that integrates:

- Long-term rainfall observations
- Geospatial indicators
- Machine Learning
- Explainable AI
- Interactive Dashboard

to identify vulnerable regions and support climate-resilient planning.

---

# 🖼 Project Architecture

![Architecture](figures/fig01_methodology_pipeline.png)

---

# 🎯 Objectives

- Develop a Sponge City Readiness Index (SCRI)
- Perform rainfall spatial downscaling using Machine Learning
- Identify climate-risk hotspots
- Improve interpretability using SHAP
- Provide decision-support through an interactive dashboard

---

# 🌍 Dataset

## Primary Dataset

### India Meteorological Department (IMD)

| Parameter | Value |
|------------|--------|
| Resolution | 0.25° × 0.25° |
| Coverage | Entire India |
| Period | 1981–2023 |
| Format | NetCDF |

### Auxiliary Datasets

- GEBCO Elevation
- SoilGrids Soil Clay Content
- SoilGrids Soil Organic Carbon
- JRC Global Surface Water

---

# ⚙️ Methodology

```text
IMD Rainfall Data
        ↓
Feature Engineering
        ↓
Random Forest Downscaling
        ↓
Environmental Feature Integration
        ↓
SCRI Computation
        ↓
Risk Classification
        ↓
SHAP Explainability
        ↓
Interactive Dashboard
```

---

# 🗺 SCRI Spatial Distribution

![SCRI Map](figures/fig02_scri_map.png)

The generated SCRI map highlights geographical variability in rainfall resilience and identifies regions requiring priority interventions.

---

# 📊 SCRI Distribution Analysis

![SCRI Distribution](figures/fig03_scri_distribution.png)

The distribution of readiness scores indicates substantial variation across Indian regions.

---

# 🚨 SCRI Risk Categories

![SCRI Classes](figures/fig04_scri_classes.png)

Regions are classified into:

- 🟢 Low Risk
- 🟡 Moderate Risk
- 🟠 High Risk
- 🔴 Critical Risk

---

# 🎯 Priority Intervention Zones

![Priority Zones](figures/fig06_priority_zones.png)

Low-readiness regions are highlighted for targeted climate adaptation and sponge-city planning.

---

# 🤖 Machine Learning

## Random Forest Classification

### Confusion Matrix

![Confusion Matrix](figures/fig07_confusion_matrix.png)

### Feature Importance

![Feature Importance](figures/fig08_rf_feature_importance.png)

Dry-day frequency and rainfall variability emerge as dominant climate-risk drivers.

---

# 🌧 Rainfall Spatial Downscaling

## Feature Importance

![Downscaling Importance](figures/fig11_downscaling_feature_importance.png)

## Validation Results

![Downscaling Validation](figures/fig10_downscaling_validation.png)

Performance:

- R² = 0.867
- Random Forest Regressor

The model successfully captures spatial rainfall variability and improves rainfall representation.

---

# 🔍 Explainable AI

## SHAP Analysis

![SHAP Summary](figures/fig09_shap_summary.png)

SHAP quantifies the contribution of individual indicators and improves transparency in climate-risk predictions.

---

# 📊 Interactive Dashboard

## Dashboard Overview

### SCRI Map

![Dashboard Map](figures/dashboard_map.png)

## Distribution Analytics


## Priority Zones & Feature Explorer


## Dataset Explorer


The dashboard enables interactive exploration of readiness patterns, hotspot identification, and geospatial analysis.

---

# 📂 Repository Structure

```text
.
├── notebooks/
│   ├── 01_rainfall_feature_engineering.ipynb
│   ├── 02_scri_development_and_risk_mapping.ipynb
│   ├── 03_climate_risk_modeling.ipynb
│   ├── 04_model_explainability_shap.ipynb
│   └── 05_interactive_decision_dashboard.ipynb
│
├── data/
├── figures/
├── dashboard/
├── report/
└── README.md
```

---

# 🛠 Technology Stack

- Python
- Xarray
- Rasterio
- GeoPandas
- Scikit-Learn
- Random Forest
- SHAP
- Streamlit
- Plotly

---

# 🏆 Key Results

- National-scale Sponge City Readiness Assessment
- Machine Learning Rainfall Downscaling
- Climate Risk Hotspot Identification
- Explainable AI Analysis
- Interactive Decision-Support Platform

---

# 👩‍💻 Author

**Bhumika Aggarwal**

IEEE GRSS Earth Day Hackathon 2026
