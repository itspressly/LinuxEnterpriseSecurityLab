# Linux Enterprise Security Lab Installation Guide

> **Version:** 1.0
>
> **Operating System:** Ubuntu 24.04 LTS
>
> **Difficulty:** Beginner – Intermediate
>
> **Estimated Setup Time:** 2–3 Hours

---

# Table of Contents

1. Project Overview
2. Requirements
3. Creating the Virtual Machine
4. Installing Ubuntu
5. Updating Ubuntu
6. Installing Required Packages
7. Creating the Project Directory
8. Installing Apache
9. Installing MariaDB
10. Installing Python
11. Configuring SSH
12. Configuring the Firewall
13. Creating the Enterprise Directory Structure
14. Running the Project Scripts
15. Testing the Installation
16. Troubleshooting

---

# 1. Project Overview

The Linux Enterprise Security Lab simulates a small company's Linux infrastructure.

This project demonstrates practical Linux administration skills including:

- Ubuntu Administration
- User & Group Management
- Linux Permissions
- Access Control Lists (ACLs)
- Bash Scripting
- Python Automation
- Apache Web Server
- MariaDB Database
- SSH
- Firewall Configuration
- Network Analysis
- System Hardening

By the end of this guide you will have a fully working Linux enterprise lab running inside an Ubuntu virtual machine.

---

# 2. Requirements

Hardware

- 4 GB RAM minimum
- 25 GB Storage
- Internet Connection

Software

- Ubuntu Desktop 24.04 LTS
- VirtualBox or VMware
- Git
- Python 3
- Apache2
- MariaDB

---

# 3. Create the Virtual Machine

Recommended Settings

| Setting | Value |
|----------|------|
| RAM | 4096 MB |
| CPU | 2 Cores |
| Storage | 30 GB |
| Network | NAT (Bridged optional) |

Install Ubuntu using the default installation settings.

---

# 4. Update Ubuntu

Open Terminal

Run

```bash
sudo apt update
sudo apt upgrade -y
```

Reboot the system if required.

---

# 5. Install Required Software

Install all required packages.

```bash
sudo apt install \
git \
curl \
wget \
vim \
tree \
htop \
net-tools \
openssh-server \
ufw \
zip \
unzip \
python3 \
python3-pip \
apache2 \
mariadb-server \
wireshark \
tcpdump \
nmap \
fail2ban \
acl \
-y
```

Verify installations.

```bash
git --version
python3 --version
apache2 -v
mysql --version
```

---

# 6. Create the Project Directory

Navigate to your home directory.

```bash
cd ~
```

Create the project.

```bash
mkdir LinuxEnterpriseSecurityLab
```

Enter the project.

```bash
cd LinuxEnterpriseSecurityLab
```

Create the project folders.

```bash
mkdir docs
mkdir scripts
mkdir website
mkdir configs
mkdir database
mkdir screenshots
mkdir packet-captures
mkdir reports
mkdir diagrams
```

---

# 7. Configure SSH

Enable the SSH service.

```bash
sudo systemctl enable ssh
sudo systemctl start ssh
```

Verify.

```bash
systemctl status ssh
```

---

# 8. Configure the Firewall

Enable UFW.

```bash
sudo ufw enable
```

Allow SSH.

```bash
sudo ufw allow ssh
```

Allow HTTP.

```bash
sudo ufw allow 80
```

Allow HTTPS.

```bash
sudo ufw allow 443
```

Verify.

```bash
sudo ufw status
```

---

# 9. Install Apache

Start Apache.

```bash
sudo systemctl enable apache2
sudo systemctl start apache2
```

Verify.

```bash
systemctl status apache2
```

Open Firefox.

Visit

```
http://localhost
```

The Apache default page should appear.

---

# 10. Install MariaDB

Enable MariaDB.

```bash
sudo systemctl enable mariadb
sudo systemctl start mariadb
```

Secure the installation.

```bash
sudo mysql_secure_installation
```

Follow the recommended secure configuration.

Create the database.

```sql
CREATE DATABASE techcorp;
```

Select the database.

```sql
USE techcorp;
```

---

# 11. Install Python Packages

Create a virtual environment.

```bash
python3 -m venv venv
```

Activate it.

```bash
source venv/bin/activate
```

Install the MySQL connector.

```bash
pip install mysql-connector-python
```

---

# 12. Create Enterprise Directories

Create the enterprise folder.

```bash
sudo mkdir -p /srv/techcorp/company
```

Create department folders.

```bash
sudo mkdir /srv/techcorp/company/HR
sudo mkdir /srv/techcorp/company/Finance
sudo mkdir /srv/techcorp/company/IT
sudo mkdir /srv/techcorp/company/Public
```

---

# 13. Configure Users

Create users.

```bash
sudo adduser alice
sudo adduser bob
sudo adduser charlie
sudo adduser diana
```

Create groups.

```bash
sudo groupadd hr
sudo groupadd finance
sudo groupadd it
sudo groupadd developers
```

Assign users.

```bash
sudo usermod -aG hr alice
sudo usermod -aG finance bob
sudo usermod -aG it charlie
sudo usermod -aG developers diana
```

---

# 14. Run the Project Scripts

Navigate to the scripts folder.

```bash
cd ~/LinuxEnterpriseSecurityLab/scripts
```

Make every script executable.

```bash
chmod +x *.sh
```

Run the scripts.

```bash
./hello.sh
```

```bash
./system_report.sh
```

```bash
./backup.sh
```

Python scripts.

```bash
python3 employee_report.py
```

```bash
python3 add_employee.py
```

---

# 15. Verify the Installation

Complete the following checks.

## Apache

```bash
systemctl status apache2
```

Expected

```
active (running)
```

---

## MariaDB

```bash
systemctl status mariadb
```

Expected

```
active (running)
```

---

## SSH

```bash
systemctl status ssh
```

Expected

```
active (running)
```

---

## Firewall

```bash
sudo ufw status
```

Expected

```
Status: active
```

---

## Python

```bash
python3 --version
```

---

## Git

```bash
git --version
```

---

# 16. Troubleshooting

## Permission Denied

Check ownership.

```bash
ls -l
```

Fix.

```bash
sudo chown
sudo chmod
```

---

## Apache Will Not Start

```bash
sudo systemctl restart apache2
```

Check logs.

```bash
journalctl -u apache2
```

---

## MariaDB Will Not Start

Restart.

```bash
sudo systemctl restart mariadb
```

Check logs.

```bash
journalctl -u mariadb
```

---

## SSH Connection Refused

Verify SSH.

```bash
systemctl status ssh
```

Check the firewall.

```bash
sudo ufw status
```

---

## Python Cannot Connect to MariaDB

Verify.

- MariaDB is running.
- Username is correct.
- Password is correct.
- Database exists.
- MySQL Connector is installed.

---

# Project Successfully Installed

If every verification step passes, the Linux Enterprise Security Lab has been successfully deployed.

Congratulations!

You now have a functional Ubuntu enterprise lab featuring:

- Ubuntu Linux Administration
- User & Group Management
- Enterprise File Structure
- Bash Automation
- Apache Web Server
- MariaDB Database
- Python Administration Tools
- Firewall Configuration
- SSH Remote Access
- Network Analysis
- System Hardening
