# 🚗 CarDekho Vehicle Dataset Analysis

This Python project provides an insightful analysis of the **CarDekho vehicle dataset**, leveraging `pandas` and `matplotlib` to uncover trends, patterns, and key insights about used car listings in India.

---

## 📁 Dataset Overview

The dataset includes comprehensive records of used cars, with features such as:

- **Car Name**
- **Year**
- **Selling Price**
- **Present Price**
- **Kilometers Driven**
- **Fuel Type**
- **Seller Type**
- **Transmission**
- **Owner**
- **Vehicle Age**

The data was sourced from [CarDekho](https://www.cardekho.com/) and is widely used in EDA (Exploratory Data Analysis) and machine learning exercises.

---

## 🧪 Script Features

The notebook and scripts offer:

- **Data Loading**: Reads the dataset using `pandas`.
- **Data Cleaning**: Handles null values and corrects data types.
- **Descriptive Statistics**: Summary of key metrics.
- **Data Visualization**:
  - Distribution of car prices
  - Fuel type comparisons
  - Transmission & seller type breakdowns
  - Vehicle age impact on price
- **Correlation Analysis**: Identify which features influence selling price.

---

## 🛠️ Tools & Technologies

- Python
- pandas
- matplotlib
- seaborn (optional)
- Jupyter Notebook

---

## 📊 Sample Insights

- **Diesel cars** dominated older listings but are declining in recent years.
- **Manual transmission** is more common but automatic listings fetch higher prices.
- **Dealer sales** tend to list newer and more expensive vehicles.
- **Age** of the car shows a strong negative correlation with selling price.

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/Mohammedaldaw/vehicle-analysis.git

# Navigate to project directory
cd vehicle-analysis

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the notebook
jupyter notebook
