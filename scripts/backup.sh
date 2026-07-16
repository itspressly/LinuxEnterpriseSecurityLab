#!/bin/bash


DATE=$(date +%F)


sudo tar -czf /srv/techcorp_backup_$DATE.tar.gz /srv/techcorp


echo "Backup completed!"


