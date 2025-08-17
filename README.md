# 🔐 Cryptools

Cryptools is a lightweight cryptography toolkit packaged as a `.deb` for easy installation on Debian/Ubuntu systems.  
It provides simple cryptographic utilities in a user-friendly interface.  

---

## 🖥️ Features
- 🔑 Cryptographic utilities for everyday use  
- 📦 Easy `.deb` installation  
- 🖼️ Desktop entry & application icon included  
- 🐧 Works on Ubuntu/Debian-based systems 

---

## 📥 Installation

You can install Cryptools from the [Releases](https://github.com/Ewsmyth/cryptools/releases) page, or via `wget`/`curl`.  

### Option 1: Download & Install Manually
```bash
wget https://github.com/Ewsmyth/cryptools/releases/download/v0.1.5/cryptools_0.1.5_amd64.deb
```
```bash
sudo apt install ./cryptools_0.1.5_amd64.deb
```

### Option 2: Using dpkg directly
```bash
sudo dpkg -i cryptools_0.1.5_amd64.deb
```
```bash
sudo apt -f install   # Fix dependencies if needed
```

### Option 3: Always install the latest Release (Scripted)
```bash
TAG=$(curl -s https://api.github.com/repos/Ewsmyth/cryptools/releases/latest \
  | grep -oP '"tag_name":\s*"\K[^"]+')
VER=${TAG#v}
```
```bash
wget -q "https://github.com/Ewsmyth/cryptools/releases/download/$TAG/cryptools_${VER}_amd64.deb" -O cryptools.deb
```
```bash
sudo apt install ./cryptools.deb
```
### ❌ Uninstallation

Remove Cryptools:
```bash
sudo apt remove cryptools
```
Remove Cryptools and configuration files:
```bash
sudo apt purge cryptools
```
If you want to manually clean up the app folder (only if still present):
```bash
sudo rm -rf /opt/cryptools
```

### 🛠️ Requirements
- Python 3.8+
- Debian/Ubuntu-based Linux system

### 📄 License
- This project is licensed under the MIT License — see LICENSE for details.

### 🙌 Contributing
Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.