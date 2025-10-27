# 🪔 Diwali Sale Recommendation System (Myntra-Style)

A simple AI-based recommendation system built using Python to understand how machine learning recommends products — just like e-commerce sites do during festive sales!

## 🌟 Inspiration

This project explains how AI magically knows what you want before you search —
That’s the power of a Recommendation System!

## 🎯 Problem Statement
During Diwali, Myntra wants to recommend products to users based on their past purchase behavior and preferences.  
Our goal is to build a **recommendation system** that suggests relevant Diwali offers and products using product similarity.

## 🧠 Tech Stack / Libraries Used
- Python  
- pandas  
- numpy  
- scikit-learn  
- matplotlib (for quick visualization)

## 📊 Dataset
The dataset contains:
- `UserID`
- `Product`
- `Category`
- `Rating`
- `Price`

This helps us identify patterns such as which products are frequently bought together and which users share similar preferences.

## ⚙️ Approach
1. Load and preprocess dataset.  
2. Create a user-item matrix using pandas.  
3. Compute product similarity using **cosine similarity**.  
4. Recommend top N similar products to a given item.  

## 🧩 Example
If a user likes **"Diwali Kurta Set"**, the system might recommend:
- Matching Earrings  
- Jutti Shoes  
- Dupatta  
- Bangles Set


## 🚀 How to Run

### Option 1: Clone the Project
- Clone both the `.ipynb` (notebook) and `.csv` (dataset) files using:
  ```bash
  git clone https://github.com/pythonessdatadiaries/AI_With_Python_Resources/AI_Recommendation_System
  ```

- You can also directly download both files manually from the above repository.
- Install Jupyter Notebook by running: : https://jupyter.org/install
- Launch Jupyter Notebook and Open the file : diwali_recommendation_system.ipynb
- Locate the line in the code:
  ```bash
  data = pd.read_csv(r"/Users/bhawanasaxena/Downloads/diwali_products.csv", encoding_errors='ignore')
  ```
- Update the CSV path with your local file path, for example:
  ```bash
  data = pd.read_csv(r"C:/Users/YourName/Downloads/diwali_products.csv", encoding_errors='ignore')
  ```
- Run all cells (use Run All from the “Cell” menu or press Shift + Enter).
  
