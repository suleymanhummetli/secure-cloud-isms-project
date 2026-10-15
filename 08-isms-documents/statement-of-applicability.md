# Statement of Applicability (SoA) - ISO/IEC 27001:2022

## ISO/IEC 27001:2022 Annex A Control Mapping

| Control Category | ISO 27001 Control | Applicable? | Implementation Status | Technical Control |
| :--- | :--- | :---: | :--- | :--- |
| **A.5 Organizational** | A.5.15 Access control | **Yes** | Implemented | IAM Least Privilege, MFA enforcement |
| **A.5 Organizational** | A.5.23 Cloud security | **Yes** | Implemented | AWS CIS Benchmark enforcement |
| **A.7 Physical** | A.7.1 Physical perimeter | **No** | Excluded | Managed by AWS (Shared Responsibility Model) |
| **A.8 Technological** | A.8.7 Protection against malware | **Yes** | Implemented | AWS GuardDuty enabled |
| **A.8 Technological** | A.8.12 Data leakage prevention | **Yes** | Implemented | S3 Block Public Access enabled |
| **A.8 Technological** | A.8.15 Logging | **Yes** | Implemented | CloudTrail multi-region & CloudWatch Logs |
| **A.8 Technological** | A.8.16 Monitoring activities | **Yes** | Implemented | CloudWatch Metric Filters & Alarms |
| **A.8 Technological** | A.8.24 Cryptography | **Yes** | Implemented | AWS KMS CMK & TLS 1.3 |