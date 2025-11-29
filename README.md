# K_nearest_neighbor
Implementation of the k-Nearest Neighbors algorithm for classification and regression tasks.

K_nearest_neighbor is a implementation of the k-Nearest Neighbors (KNN) algorithm. It’s designed for learning, experimentation, and small-scale machine-learning projects involving classification or regression.

Features

1. KNN for classification and/or regression
2. Multiple distance metrics (Euclidean, Manhattan, etc.)
3. Adjustable k value

Install dependencies
pip install -r requirements.txt

Project Structure
K_nearest_neighbor/
│
├── K_nearest_neighbor/                                      
├── requirements.txt
└── README.md

How It Works

KNN is a distance-based learning method.
For each new sample:
1. Measure distances to all training points.
2. Select the k closest neighbors.
3. Classification: choose the majority label.
4. Regression: average the neighbor values.

License
MIT License