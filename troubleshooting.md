## Permission Denied

Cause:

Incorrect ownership

Fix

sudo chown

sudo chmod

---

## Apache Not Starting

Check

systemctl status apache2

---

## MariaDB Won't Start

Check

systemctl status mariadb

Restart

sudo systemctl restart mariadb

---

## SSH Refused Connection

Check

systemctl status ssh

Check firewall

sudo ufw status
