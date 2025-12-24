🚚 Delivery Delay Prediction – ML + Streamlit Deployment

A simple end-to-end project where I built, trained, and deployed a machine learning model that predicts whether a package delivery will be delayed or not, based on shipment data.

This project was mainly done to learn deployment – taking a model out of Jupyter Notebook and actually putting it online where others can use it.

📌 Problem Statement

Logistics companies lose time and money when deliveries get delayed.
This project attempts to predict delivery delays before they actually happen, so action can be taken early (faster routing, notifying customers, etc.)

Input Example:
Product category, warehouse processing time, shipping distance, shipping speed, vendor rating, etc.

Output:
🔹 On-Time or
🔹 Delayed

🧱 What I Built (End-to-End Flow)
Dataset → Cleaning → Feature Engineering → Model Training → Evaluation →
Model Export (joblib) → Streamlit App → Deployment on Cloud

# Tech Stack
Python, Pandas, NumPy
scikit-learn
joblib (model persistence)
Streamlit (frontend UI)
GitHub + Cloud (deployment)

📂 Project Structure
Delivery_Delay_Pred/
│── app.py                 # Streamlit app
│── train.py               # Model training script
│── model.joblib           # Exported trained model
│── requirements.txt
│── data/
│    └── delivery_data.csv
└── README.md


📊 Model Approach 
Categorical encoding + numerical scaling using a Pipeline
Model used: Decision Tree Classifier (kept intentionally simple)
Exported using joblib.dump()
Loaded inside Streamlit using joblib.load()


🧪 How to Run Locally
git clone https://github.com/<your_repo_name>.git
cd Delivery_Delay_Pred

python -m venv venv
venv\Scripts\activate     # Windows
# or source venv/bin/activate (Mac/Linux)

pip install -r requirements.txt
streamlit run app.py


🌍 Live Demo
👉 https://deliverydelayriskpredictionapp-ep3keceh37qhfv7ev8b6vm.streamlit.app/

🧑‍💻 Why This Project Matters (My TL;DR)

Most ML projects never leave the notebook.
This one runs live — anyone can open a browser and try it.
For me, this project was about learning how to:
Package a model
Handle environment issues
Create a UI for users
Deploy publicly

🚀 What I Want to Improve Next
Add database logging (store predictions)
Train an improved model (XGBoost / Random Forest)
Add visual analytics dashboard

📬 Contact
If you want to discuss ML roles or collaboration:
Email: upeshkhairnar03@email
LinkedIn: https://www.linkedin.com/in/upesh-khairnar

