# Incident Response Plan & Incident Report

## 1. Incident Overview
* **Incident ID:** INC-2026-1015
* **Date/Time:** October 15, 2026
* **Severity:** Medium
* **Target Environment:** AWS eu-north-1 (NovaTech Infrastructure)

## 2. CloudWatch Alarms & Detection
* **NovaTech-RootUser-Activity-Alarm:** Monitored root account API actions.
* **NovaTech-SecurityGroup-Changed-Alarm:** Tracked network security group ingress/egress updates.

## 3. Response Strategy
* Automated triggering via CloudWatch Metrics.
* Alert notification sent to SOC Incident Response channel.