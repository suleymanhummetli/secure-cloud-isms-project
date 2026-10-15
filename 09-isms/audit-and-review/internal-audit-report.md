# Internal Audit Report (ISO/IEC 27001:2022 Clause 9.2)
**Organization:** NovaTech Solutions  
**Date:** October 15, 2026  
**Auditor:** Lead ISMS Auditor (Süleyman Hümmətli)  

## 1. Objective
To evaluate the operational effectiveness and conformity of NovaTech Solutions cloud ISMS implemented in AWS `eu-north-1`.

## 2. Audit Findings & Summary
* **Total Automated Checks (Prowler v5):** 655
* **ISO 27001 Framework Compliance:** 68.48% PASS (126 passed, 58 failed/unresolved controls).
* **Non-Conformities Identified:** 
  1. Certain CloudWatch alarms lacked automated SNS action subscriptions during initial baseline.
  2. Documentation formatting required strict UTF-8 alignment.
* **Corrective Actions:** SNS topics configured, alarms mapped, and documentation restructured.