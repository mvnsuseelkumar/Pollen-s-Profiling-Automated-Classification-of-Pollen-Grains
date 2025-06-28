# 🚀 Pollens Profiling Project - Executable Files

This folder contains the **complete project files** required to run the **Pollen's Profiling - Automated Classification of Pollen Grains** web application. It includes the Flask backend, trained model, dataset, frontend templates, and all static assets ready for execution.

---

## 📁 Project Directory Structure

```
pollens_profiling_project_executable_files/
├── flask/                                # 📦 Main Flask application directory
│   ├── app.py                            # 🧠 Main Flask backend script
│   ├── pollen_classification.ipynb       # 📊 Model training + evaluation notebook
│   ├── pollen_model.keras                # 🧠 Trained CNN model file
│   ├── labelencoder.pkl                  # 🔖 Label encoder (class mappings)
│   ├── requirements.txt                  # 📌 Python dependencies list
│   ├── templates/                        # 🧩 HTML templates (Jinja2 engine)
│   │   ├── index.html
│   │   ├── about.html
│   │   ├── prediction.html
│   │   ├── team.html
│   │   └── contact.html
│   ├── static/                           # 🎨 Static files (CSS, images)
│   │   ├── style.css                     #   └── Styling for all HTML pages
│   │   └── images/                       #   └── Logos, icons, profile pics
│   └── uploads/                          # 📂 Temporarily stored uploaded images
│
├── pollen_dataset/                       # 🌾 Dataset folder
│   ├── images/                           # 📷 Raw pollen grain images
│   ├── bboxes.csv                        # 📐 Bounding box labels for images
│   └── class_map.csv                     # 🗂 Class name to ID mapping
```

---

## ▶️ How to Run

1. Navigate to the `flask/` directory:

```bash
cd flask
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Start the Flask server:

```bash
python app.py
```

5. Open your browser and go to: `http://127.0.0.1:5000/`

---

## 📦 Contents Summary

* `flask/` → Complete web application (backend, UI, model)
* `pollen_dataset/` → Cropped training data and label files

---
