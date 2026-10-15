# Statement of Applicability (SoA) - ISO/IEC 27001:2022
**Organization:** NovaTech Solutions  
**Scope:** AWS Cloud Infrastructure (`eu-north-1`)  
**Date:** October 15, 2026  

## 1. Executive Summary
Bu sənəd NovaTech Solutions bulud mühiti üçün ISO/IEC 27001:2022 Annex A təhlükəsizlik idarəetmə mexanizmlərinin tətbiq olunma statusunu, əsaslandırmalarını (Justification) və texniki icra səviyyəsini müəyyən edir.

## 2. Annex A Control Mapping (Selected Core Controls)

| Control ID & Name | Applicable? | Implementation Status | Justification / Technical Control | Risk ID | Evidence |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **A.5.15 Access control** | Yes | Implemented | IAM Least Privilege, MFA enforcement for `Suleyman-admin` | RISK-01 | IAM Policies & MFA Config |
| **A.5.23 Information security for cloud services** | Yes | Implemented | AWS CIS Benchmark enforcement via Prowler audit | RISK-02 | Prowler Audit Reports |
| **A.7.1 Physical security perimeter** | No | Excluded | Managed by AWS (Shared Responsibility Model) | RISK-03 | AWS SOC 2 Reports |
| **A.8.3 Information access restriction** | Yes | Implemented | S3 Block Public Access & Bucket Policies | RISK-04 | S3 Configurations |
| **A.8.5 Secure authentication** | Yes | Implemented | IAM password policy & MFA | RISK-01 | IAM Settings |
| **A.8.7 Protection against malware** | Yes | Implemented | AWS GuardDuty enabled for threat detection | RISK-05 | GuardDuty Console |
| **A.8.12 Data leakage prevention** | Yes | Implemented | S3 Encryption & Macie discovery | RISK-04 | S3 & Macie Logs |
| **A.8.15 Logging** | Yes | Implemented | CloudTrail multi-region logging enabled | RISK-06 | CloudTrail Config |
| **A.8.16 Monitoring activities** | Yes | Partially Implemented | CloudWatch Metric Filters & Alarms | RISK-06 | CloudWatch Alarms |
| **A.8.20 Network security** | Yes | Implemented | VPC Subnet segregation & Security Groups | RISK-07 | VPC & SG Config |
| **A.8.24 Use of cryptography** | Yes | Implemented | AWS KMS CMK (AES-256) & TLS 1.3 in transit | RISK-08 | KMS & OpenSSL Checks |