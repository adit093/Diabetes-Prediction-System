# 🩺 Diabetes Prediction System Using Machine Learning

## 📌 Project Overview

This project is a Machine Learning based web application that predicts whether a person is diabetic or not using medical parameters.

The model is trained using the **PIMA Indians Diabetes Dataset** and deployed using **Streamlit**.

This project demonstrates:

* Data preprocessing
* Feature scaling
* Model training
* Model evaluation
* Saving ML models using Pickle
* Web app deployment using Streamlit

---

# 🚀 Features

✅ Predicts diabetes based on patient health data
✅ User-friendly Streamlit web interface
✅ Machine Learning based prediction
✅ Fast and lightweight application
✅ Model and scaler saved using Pickle
✅ Ready for cloud deployment

---

# 🧠 Machine Learning Algorithm Used

This project uses:

## Support Vector Machine (SVM)

SVM is a supervised machine learning algorithm used for classification tasks.

### Why SVM?

* High accuracy
* Effective for binary classification
* Works well with structured datasets
* Good performance with scaled data

---

# 📂 Dataset Information

Dataset Used:

## PIMA Indians Diabetes Dataset

The dataset contains medical information of female patients.

### Input Features

| Feature                  | Description               |
| ------------------------ | ------------------------- |
| Pregnancies              | Number of pregnancies     |
| Glucose                  | Glucose level             |
| BloodPressure            | Blood pressure value      |
| SkinThickness            | Thickness of skin fold    |
| Insulin                  | Insulin level             |
| BMI                      | Body Mass Index           |
| DiabetesPedigreeFunction | Diabetes hereditary score |
| Age                      | Age of patient            |

### Target Variable

| Value | Meaning      |
| ----- | ------------ |
| 0     | Non-Diabetic |
| 1     | Diabetic     |

---

# 🛠️ Technologies Used

| Technology       | Purpose              |
| ---------------- | -------------------- |
| Python           | Programming language |
| NumPy            | Numerical operations |
| Pandas           | Data analysis        |
| Scikit-learn     | Machine learning     |
| Streamlit        | Web application      |
| Pickle           | Model serialization  |
| Jupyter Notebook | Model development    |

---

# 🌐 Streamlit Web Application

The project includes a Streamlit web app where users can:

* Enter patient information
* Click Predict
* Receive diabetes prediction instantly

---

# 📁 Project Structure

```text
Diabetes-Prediction-System/
│
├── app.py
├── Diabetes_prediction.ipynb
├── Trained_model.sav
├── scaler.sav
├── diabetes.csv
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone <your-github-repo-link>
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd Diabetes-Prediction-System
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

# 📦 requirements.txt

```text
streamlit
numpy
pandas
scikit-learn
```

---

# 📈 Model Prediction Process

1. User enters medical values.
2. Input data is converted into NumPy array.
3. Data is reshaped into 2D format.
4. Scaler standardizes the input.
5. SVM model predicts the output.
6. Result is displayed on the screen.

---

# 🔮 Future Improvements

Possible future enhancements:

* Add graphical dashboards
* Improve UI/UX design
* Add database connectivity
* Add user authentication
* Deploy using Docker
* Use advanced ML algorithms
* Add prediction probability
* Mobile responsive interface

---

# 📚 Learning Outcomes

This project helps understand:

* End-to-end ML workflow
* Data preprocessing
* Feature engineering
* Supervised learning
* Model deployment
* Streamlit application development
* Real-world ML project structure

---

# 💡 Use Cases

* Healthcare analytics
* Medical screening systems
* Educational ML projects
* Beginner ML deployment project
* Portfolio project for students

---

# 🤝 Contribution

Contributions are welcome.

You can improve:

* UI design
* Model accuracy
* Performance optimization
* Additional features

---

# 📄 License

This project is open-source and available under the MIT License.

---

# 👨‍💻 Author

Developed by Aditya Shende

---

# ⭐ If You Like This Project

Give this repository a star on GitHub and share it with others.
