# Playwright-Python-Automation-Framework

A learning and practice project for building a **Python test automation framework** using **pytest** and **Playwright**.  
This repository demonstrates progression from basic pytest concepts → UI flow automation → API testing.

## 📂 Project Structure
```
Playwright-Python-Automation-Framework/
├── milestone1_pytest_basics   # Intro to pytest basics
├── milestone2_ui_flows        # Playwright UI flow tests
├── milestone3_api_tests       # Playwright API tests
├── pytest.ini                 # pytest configuration
├── requirements.txt           # project dependencies
└── .gitignore                 # ignored files (venv, cache, reports, etc.)
```

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/Playwright-Python-Automation-Framework.git
cd Playwright-Python-Automation-Framework
```

### 2. Create & activate a virtual environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run tests
```bash
pytest
```

To run a specific milestone:
```bash
pytest milestone2_ui_flows
```

## 🧪 Tech Stack
- **Python 3.x**
- **pytest** – testing framework
- **Playwright** – browser automation & API testing

## 📌 Roadmap
- [x] Milestone 1: Pytest basics  (Testing Mock RPG Functions)
- [x] Milestone 2: Playwright UI flows  
- [x] Milestone 3: Playwright API tests  
- [ ] Add CI/CD with GitHub Actions  
- [ ] Add test reporting & screenshots  
- [ ] Expand coverage with more complex scenarios  

## 🤝 Contributing
This is primarily a personal learning project, but suggestions and improvements are welcome.  
Feel free to open an **issue** or submit a **pull request**.

## 📄 License
MIT License – free to use, share, and learn from.