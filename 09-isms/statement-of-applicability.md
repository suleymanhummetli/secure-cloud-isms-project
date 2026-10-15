# Statement of Applicability (SoA) - ISO/IEC 27001:2022
**Organization:** NovaTech Solutions  
**Scope:** AWS Cloud Infrastructure (`eu-north-1`)  
**Standard:** ISO/IEC 27001:2022 Annex A  

## 1. Executive Summary
Bu sənəd NovaTech Solutions bulud mühiti üçün ISO/IEC 27001:2022 Annex A çərçivəsində mövcud olan bütün 93 idarəetmə mexanizminin (controls) tətbiq olunma statusunu, əsaslandırmalarını (Justification) və texniki sübutlarını ehtiva edir.

## 2. Comprehensive Annex A Control Mapping (93 Controls Summary)

| Control ID | Control Name | Category | Applicable? | Status | Justification / Technical Control | Risk ID | Evidence |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- | :--- |
| **A.5.1** | Policies for information security | Organizational | Yes | Implemented | ISMS Policy framework established | RISK-01 | `09-isms/policies/` |
| **A.5.2** | Information security roles and responsibilities | Organizational | Yes | Implemented | Defined security roles & RACI matrix | RISK-01 | `01-scenario/` |
| **A.5.15** | Access control | Organizational | Yes | Implemented | IAM Least Privilege, MFA for `Suleyman-admin` | RISK-02 | IAM Policies |
| **A.5.23** | Information security for cloud services | Organizational | Yes | Implemented | AWS CIS Benchmark enforcement via Prowler | RISK-03 | Prowler Reports |
| **A.7.1** | Physical security perimeter | Physical | No | Excluded | Managed by AWS (Shared Responsibility) | RISK-04 | AWS SOC 2 Reports |
| **A.8.3** | Information access restriction | Technological | Yes | Implemented | S3 Block Public Access & Bucket Policies | RISK-05 | S3 Configs |
| **A.8.5** | Secure authentication | Technological | Yes | Implemented | IAM Password Policy & MFA enforced | RISK-02 | IAM Settings |
| **A.8.7** | Protection against malware | Technological | Yes | Implemented | AWS GuardDuty threat detection enabled | RISK-06 | GuardDuty Console |
| **A.8.12** | Data leakage prevention | Technological | Yes | Implemented | S3 Encryption & Macie discovery | RISK-05 | S3 & Macie Logs |
| **A.8.15** | Logging | Technological | Yes | Implemented | CloudTrail multi-region logging active | RISK-07 | CloudTrail Config |
| **A.8.16** | Monitoring activities | Technological | Yes | Partially | CloudWatch Metric Filters & Alarms | RISK-07 | CloudWatch Alarms |
| **A.8.20** | Network security | Technological | Yes | Implemented | VPC Subnet segregation & Security Groups | RISK-08 | VPC Config |
| **A.8.24** | Use of cryptography | Technological | Yes | Implemented | AWS KMS CMK (AES-256) & TLS 1.3 | RISK-09 | KMS & OpenSSL |
*(Note: Remaining controls A.5.3 through A.8.34 are systematically mapped, implemented or risk-accepted within the ISMS risk register).*