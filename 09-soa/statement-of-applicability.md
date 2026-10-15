# Statement of Applicability (SoA) - NovaTech Solutions
**Document Version:** 1.0  
**ISO Standard:** ISO/IEC 27001:2022 (Annex A)  
**Scope:** AWS Cloud Infrastructure & Services (eu-north-1)  
**Date:** October 15, 2026  

---

## 1. Executive Summary
Bu s?n?d NovaTech Solutions bulud mühiti üçün ISO/IEC 27001:2022 Annex A t?hlük?sizlik kontrollarinin t?tbiq olunma statusunu (Applicability Status) v? onlarin icra mexanizml?rini mü?yy?n edir.

## 2. ISO/IEC 27001:2022 Annex A Control Mapping

| Control Category | ISO 27001 Control | Applicable? | Implementation Status | Justification / Technical Control |
| :--- | :--- | :---: | :--- | :--- |
| **A.5 Organizational** | A.5.15 Access control | **Yes** | Implemented | IAM Minimum Privilege Policy, MFA enforcement (Suleyman-admin) |
| **A.5 Organizational** | A.5.23 Information security for cloud services | **Yes** | Implemented | AWS CIS Benchmark enforcement via Prowler audit |
| **A.7 Physical** | A.7.1 Physical security perimeter | **No** | Excluded (AWS Shared Responsibility) | AWS manages physical datacenters; covered under AWS SOC 2 Type II reports |
| **A.8 Technological** | A.8.7 Protection against malware | **Yes** | Implemented | AWS GuardDuty enabled for threat detection and malware awareness |
| **A.8 Technological** | A.8.9 Configuration management | **Yes** | Implemented | Infrastructure as Code / Configured AWS Security Groups and VPC isolation |
| **A.8 Technological** | A.8.10 Information deletion | **Yes** | Implemented | S3 Lifecycle policies & secure object deletion |
| **A.8 Technological** | A.8.12 Data leakage prevention | **Yes** | Implemented | S3 Block Public Access enabled, Macie discovery configured |
| **A.8 Technological** | A.8.15 Logging | **Yes** | Implemented | CloudTrail multi-region logging & CloudWatch Log Groups enabled |
| **A.8 Technological** | A.8.16 Monitoring activities | **Yes** | Implemented | CloudWatch Metric Filters (RootAccountUsageFilter, SecurityGroupChangesFilter) & Alarms |
| **A.8 Technological** | A.8.20 Network security | **Yes** | Implemented | VPC Private/Public Subnet segregation, Security Groups & Port Security |
| **A.8 Technological** | A.8.24 Use of cryptography | **Yes** | Implemented | AWS KMS Customer Managed Keys (CMK), AES-256 S3 Encryption, TLS 1.3 in Transit |

## 3. Justification for Exclusions
* **Physical Security Controls (A.7):** AWS Bulud Ikiqütblü M?suliyy?t Modeline (Shared Responsibility Model) uygun olaraq, fiziki m?lumat m?rk?zinin t?hlük?sizliyi tamamil? AWS t?r?find?n t?min edilir. NovaTech Solutions bu riski AWS SOC 1/2 v? ISO 27001 sertifikatlari vasit?sil? q?bul edir.
