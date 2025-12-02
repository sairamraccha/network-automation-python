# 🛰️ Network Automation Using Python
A modular and extensible **Network Automation Toolkit** built using **Python**, **Netmiko**, **Nornir**, and **Jinja2**. It automates routine network engineering tasks such as **config backups**, **pushing configurations**, **device auditing**, and **parallel operations** across multi-vendor environments.

This project is designed for **Network Engineers**, **NOC Teams**, and **Automation Learners** looking to implement real-world automation workflows.

---

# 🚀 Features

### 🔹 **1. Automated Configuration Backup**  
- Uses Netmiko SSH to fetch running-config  
- Saves per-device timestamped backups  
- Supports multiple vendors (Cisco IOS by default)

### 🔹 **2. Template-based Config Deployment (Jinja2)**  
- Push consistent configs to devices  
- Dynamic variables support  
- Prevents manual CLI errors

### 🔹 **3. Parallel Task Execution (Nornir)**  
- Run commands on multiple devices simultaneously  
- Ideal for large-scale networks  
- Includes sample “show running-config” parallel job

### 🔹 **4. YAML-Based Inventory**  
Easy-to-manage inventory with fields:  
`hostname`, `platform`, `username`, `password`

### 🔹 **5. Clean Project Structure**  
Industry-standard layout for automation projects.

---

# 🏗️ Architecture Overview

