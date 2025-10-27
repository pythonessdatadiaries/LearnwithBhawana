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

