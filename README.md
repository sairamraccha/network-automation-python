# 🛰️ Network Automation Using Python
A modular and extensible **Network Automation Toolkit** built using **Python**, **Netmiko**, **Nornir**, and **Jinja2**.  
It automates routine network engineering tasks such as **config backups**, **pushing configurations**, **device auditing**, and **parallel operations** across multi-vendor environments.

This project is designed for **Network Engineers**, **NOC Teams**, and **Automation Learners** looking to implement real-world automation workflows.

---

# 🚀 Features

### 🔹 **1. Automated Configuration Backup**
- Uses Netmiko SSH to fetch running-config  
- Saves timestamped backups  
- Multi-device & multi-vendor support  

### 🔹 **2. Template-based Config Deployment (Jinja2)**
- Push standardized configs  
- Dynamic variable support  
- Eliminates manual CLI errors  

### 🔹 **3. Parallel Execution (Nornir)**
- Run commands on all devices simultaneously  
- Faster results for large networks  

### 🔹 **4. YAML Inventory**
- Simple, centralized device list  
- Username / password / platform fields  

### 🔹 **5. Production-Grade Structure**
- Includes tests, CI workflows, and modular Python scripts  

---

# 🏗️ Architecture Overview

```
                   ┌──────────────────────────────┐
                   │       YAML Inventory          │
                   │   (inventory/hosts.yaml)      │
                   └──────────────┬───────────────┘
                                  │
                    ┌─────────────┴────────────┐
                    │                          │
       ┌────────────▼──────────┐    ┌──────────▼──────────┐
       │   Netmiko Engine      │    │    Nornir Engine     │
       │ (backup/push configs) │    │ (parallel execution) │
       └───────┬───────────────┘    └──────────┬──────────┘
               │                                │
     ┌─────────▼─────────┐          ┌───────────▼──────────┐
     │ Config Backups     │          │ Multi-device Cmd Exec │
     │ templates/config.j2│          │ show running-config   │
     └─────────┬─────────┘          └───────────┬──────────┘
               │                                │
        ┌──────▼──────────┐            ┌────────▼───────┐
        │   backups/      │            │ Output / Logs    │
        └─────────────────┘            └──────────────────┘
```

---

# 🧰 Tech Stack

| Component | Technology |
|----------|------------|
| Language | Python 3.x |
| SSH Automation | Netmiko |
| Parallel Execution | Nornir |
| Templates | Jinja2 |
| Inventory | YAML |
| Testing | PyTest |
| CI/CD | GitHub Actions |

---

# 📁 Folder Structure

```
network-automation-python/
│
├── inventory/
│   └── hosts.yaml
│
├── templates/
│   └── config.j2
│
├── src/
│   ├── backup_configs.py
│   ├── push_config.py
│   └── nornir_example.py
│
├── tests/
│   └── test_backup.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

# 🔧 Installation Guide

### **1. Clone the Repository**
```bash
git clone https://github.com/<your-username>/network-automation-python.git
cd network-automation-python
```

### **2. Create & Activate Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

---

# 📘 Usage Examples

## **1️⃣ Backup Configurations**
```bash
python src/backup_configs.py --inventory inventory/hosts.yaml --output backups/
```

### Output:
- Saves configs inside `backups/`
- Filenames include timestamps

---

## **2️⃣ Push Templated Config**
```bash
python src/push_config.py --host 192.0.2.10   --template templates/config.j2   --vars "hostname:leaf01,username:admin,password:admin"
```

Example Jinja template:

```jinja2
hostname {{ hostname }}
logging host {{ syslog_host | default('10.0.0.1') }}
```

---

## **3️⃣ Parallel Execution Using Nornir**
```bash
python src/nornir_example.py --inventory inventory/hosts.yaml
```

Runs **show running-config** on all devices simultaneously.

---

# 🧪 Testing

Run with:
```bash
pytest -q
```

---

# 🔄 CI/CD Pipeline

GitHub Actions workflow included at:
```
.github/workflows/ci.yml
```

Runs:
- Installation  
- PyTest  
- Code validation  

---

# 🛣️ Roadmap

- [ ] Add multi-vendor support (Arista, Juniper)  
- [ ] Add Netconf/Restconf (ncclient)  
- [ ] Add backup diff comparison  
- [ ] Add REST API wrapper (Flask/FastAPI)  
- [ ] Web dashboard (Streamlit)  
- [ ] Add GitOps workflow  

---

# 🤝 Contributing

1. Fork the repository  
2. Create a feature branch  
3. Commit changes  
4. Submit a Pull Request  

All contributions are welcome!

---

# 📜 License

Licensed under the **MIT License**.

---

# ⭐ Support  
If you like this project, **please star ⭐ the repository**.  
Your support encourages more network automation projects!
