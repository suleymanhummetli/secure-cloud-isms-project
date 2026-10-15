# Statement of Applicability (SoA) - ISO/IEC 27001:2022
**Organization:** NovaTech Solutions  
**Scope:** AWS Cloud Infrastructure (`eu-north-1`)  
**Standard:** ISO/IEC 27001:2022 Annex A (Complete 93 Controls Mapping)  

## 1. Complete Annex A Control Register

| Control ID | Control Name | Category | Applicable? | Status | Justification / Technical Control | Risk ID | Evidence / Reference |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- | :--- |
| **A.5.1** | Policies for information security | Organizational | Yes | Implemented | Approved ISMS Policies framework | RISK-01 | `09-isms/policies/` |
| **A.5.2** | Information security roles | Organizational | Yes | Implemented | RACI matrix defined | RISK-01 | `01-scenario/` |
| **A.5.3** | Segregation of duties | Organizational | Yes | Implemented | IAM policy separation | RISK-02 | IAM Policies |
| **A.5.4** | Management responsibilities | Organizational | Yes | Implemented | Simulated Mgmt Review | RISK-01 | `09-isms/audit-and-review/` |
| **A.5.5** | Contact with authorities | Organizational | Yes | Implemented | Escalation path documented | RISK-01 | `05-monitoring/` |
| **A.5.6** | Contact with special interest groups | Organizational | Yes | Implemented | AWS Security Bulletins monitored | RISK-01 | `01-scenario/` |
| **A.5.7** | Threat intelligence | Organizational | Yes | Implemented | AWS GuardDuty threat feeds | RISK-06 | GuardDuty Console |
| **A.5.8** | Information security in project management | Organizational | Yes | Implemented | Infrastructure-as-Code checks | RISK-03 | Terraform / Repo |
| **A.5.9** | Inventory of information and other associated assets | Organizational | Yes | Implemented | Asset Register established | RISK-03 | `01-scenario/asset-register.md` |
| **A.5.10** | Acceptable use of information and other associated assets | Organizational | Yes | Implemented | Acceptable Use Policy | RISK-01 | `09-isms/policies/` |
| **A.5.11** | Return of assets | Organizational | Yes | Implemented | Offboarding procedure | RISK-01 | `01-scenario/` |
| **A.5.12** | Classification of information | Organizational | Yes | Implemented | Data labeling scheme | RISK-05 | `02-risk/` |
| **A.5.13** | Labelling of information | Organizational | Yes | Implemented | AWS Resource Tagging | RISK-05 | AWS Console |
| **A.5.14** | Information transfer | Organizational | Yes | Implemented | TLS 1.3 encrypted transfer | RISK-09 | `07-tls-kms/` |
| **A.5.15** | Access control | Organizational | Yes | Implemented | IAM Least Privilege & MFA | RISK-02 | IAM Policies |
| **A.5.16** | Identity management | Organizational | Yes | Implemented | AWS IAM Identity Center | RISK-02 | IAM Settings |
| **A.5.17** | Authentication information | Organizational | Yes | Implemented | KMS Key management & Secrets | RISK-02 | `07-tls-kms/` |
| **A.5.18** | Access rights | Organizational | Yes | Implemented | IAM Role-based access (RBAC) | RISK-02 | IAM Config |
| **A.5.19** | Information security in supplier relationships | Organizational | Yes | Implemented | AWS Shared Responsibility Model | RISK-04 | AWS SOC 2 |
| **A.5.20** | Addressing information security within supplier agreements | Organizational | Yes | Implemented | AWS Customer Agreement | RISK-04 | AWS Terms |
| **A.5.21** | Managing information security in the ICT supply chain | Organizational | Yes | Implemented | Cloud Service Evaluation | RISK-04 | `01-scenario/` |
| **A.5.22** | Monitoring, review and change management of supplier services | Organizational | Yes | Implemented | AWS Health Dashboard monitoring | RISK-04 | AWS Health |
| **A.5.23** | Information security for cloud services | Organizational | Yes | Implemented | AWS CIS Benchmark via Prowler | RISK-03 | Prowler Reports |
| **A.5.24** | Information security incident management planning and preparation | Organizational | Yes | Implemented | Incident Response Plan | RISK-07 | `05-monitoring/incident-report.md` |
| **A.5.25** | Assessment and decision on information security events | Organizational | Yes | Implemented | CloudWatch Alarms & Severity Matrix | RISK-07 | `05-monitoring/` |
| **A.5.26** | Response to information security incidents | Organizational | Yes | Implemented | Automated SOC Alerting | RISK-07 | `05-monitoring/` |
| **A.5.27** | Learning from information security incidents | Organizational | Yes | Implemented | Post-incident review template | RISK-07 | `05-monitoring/` |
| **A.5.28** | Collection of evidence | Organizational | Yes | Implemented | CloudTrail audit log retention | RISK-07 | CloudTrail Config |
| **A.5.29** | Information security during disruption | Organizational | Yes | Implemented | Multi-AZ Availability | RISK-08 | VPC Config |
| **A.5.30** | ICT readiness for business continuity | Organizational | Yes | Implemented | AWS S3 Versioning & Backups | RISK-08 | S3 Config |
| **A.5.31** | Legal, statutory, regulatory and contractual requirements | Organizational | Yes | Implemented | ISO 27001 & GDPR mapping | RISK-01 | `01-scenario/` |
| **A.5.32** | Intellectual property rights | Organizational | Yes | Implemented | IP Protection policies | RISK-01 | `01-scenario/` |
| **A.5.33** | Protection of records | Organizational | Yes | Implemented | CloudTrail S3 Object Lock / KMS | RISK-05 | S3 Bucket Policy |
| **A.5.34** | Privacy and protection of PII | Organizational | Yes | Implemented | Synthetic PII generation & Encryption | RISK-05 | `06-crypto-tool/` |
| **A.5.35** | Independent review of information security | Organizational | Yes | Implemented | Prowler automated auditing | RISK-03 | `03-baseline-audit/` |
| **A.5.36** | Compliance with policies and standards for information security | Organizational | Yes | Implemented | Continuous Prowler scanning | RISK-03 | `08-after-audit/` |
| **A.5.37** | Documented operating procedures | Organizational | Yes | Implemented | SOP Documentation in repo | RISK-01 | `00-docs/` |
| **A.6.1** | Screening | People | Yes | Implemented | Background verification process | RISK-01 | HR Docs |
| **A.6.2** | Terms and conditions of employment | People | Yes | Implemented | Confidentiality agreements | RISK-01 | HR Docs |
| **A.6.3** | Information security awareness, education and training | People | Yes | Implemented | Security Awareness Program | RISK-01 | Training Logs |
| **A.6.4** | Disciplinary process | People | Yes | Implemented | Disciplinary Policy | RISK-01 | HR Docs |
| **A.6.5** | Responsibilities after termination or change of employment | People | Yes | Implemented | IAM Access Revocation checklist | RISK-02 | IAM Procedure |
| **A.6.6** | Confidentiality or non-disclosure agreements | People | Yes | Implemented | NDAs for all administrators | RISK-01 | HR Docs |
| **A.6.7** | Remote working | People | Yes | Implemented | VPN & Encrypted sessions | RISK-02 | Network Config |
| **A.6.8** | Information security event reporting | People | Yes | Implemented | Incident reporting escalation | RISK-07 | `05-monitoring/` |
| **A.7.1** | Physical security perimeters | Physical | No | Excluded | Managed by AWS (Shared Model) | RISK-04 | AWS SOC 2 |
| **A.7.2** | Physical entry | Physical | No | Excluded | Managed by AWS (Shared Model) | RISK-04 | AWS SOC 2 |
| **A.7.3** | Securing offices, rooms and facilities | Physical | No | Excluded | Managed by AWS (Shared Model) | RISK-04 | AWS SOC 2 |
| **A.7.4** | Physical security monitoring | Physical | No | Excluded | Managed by AWS (Shared Model) | RISK-04 | AWS SOC 2 |
| **A.7.5** | Protecting against physical and environmental threats | Physical | No | Excluded | Managed by AWS (Shared Model) | RISK-04 | AWS SOC 2 |
| **A.7.6** | Working in secure areas | Physical | No | Excluded | Managed by AWS (Shared Model) | RISK-04 | AWS SOC 2 |
| **A.7.7** | Clear desk and clear screen | Physical | Yes | Implemented | Screen lock policies | RISK-01 | Security Policy |
| **A.7.8** | Equipment siting and protection | Physical | No | Excluded | Managed by AWS | RISK-04 | AWS SOC 2 |
| **A.7.9** | Security of assets off-premises | Physical | Yes | Implemented | Encrypted administrator laptops | RISK-01 | Device Policy |
| **A.7.10** | Storage media | Physical | Yes | Implemented | EBS / S3 AES-256 Encryption | RISK-05 | `07-tls-kms/` |
| **A.7.11** | Supporting utilities | Physical | No | Excluded | Managed by AWS Data Centers | RISK-04 | AWS SOC 2 |
| **A.7.12** | Cabling security | Physical | No | Excluded | Managed by AWS Data Centers | RISK-04 | AWS SOC 2 |
| **A.7.13** | Equipment maintenance | Physical | No | Excluded | Managed by AWS Data Centers | RISK-04 | AWS SOC 2 |
| **A.7.14** | Secure disposal or re-use of equipment | Physical | No | Excluded | Managed by AWS Data Centers | RISK-04 | AWS SOC 2 |
| **A.8.1** | User endpoint devices | Technological | Yes | Implemented | Endpoint security controls | RISK-01 | IT Policy |
| **A.8.2** | Privileged access rights | Technological | Yes | Implemented | IAM Admin role restrictions | RISK-02 | IAM Policies |
| **A.8.3** | Information access restriction | Technological | Yes | Implemented | S3 Block Public Access | RISK-05 | S3 Bucket Config |
| **A.8.4** | Access to source code | Technological | Yes | Implemented | GitHub Repository permissions | RISK-02 | Git Config |
| **A.8.5** | Secure authentication | Technological | Yes | Implemented | IAM MFA & Password Policy | RISK-02 | IAM Settings |
| **A.8.6** | Capacity management | Technological | Yes | Implemented | AWS Auto Scaling & Quotas | RISK-08 | CloudWatch Metrics |
| **A.8.7** | Protection against malware | Technological | Yes | Implemented | GuardDuty & Systems Manager | RISK-06 | GuardDuty Console |
| **A.8.8** | Management of technical vulnerabilities | Technological | Yes | Implemented | Prowler Vulnerability Scans | RISK-03 | `08-after-audit/` |
| **A.8.9** | Configuration management | Technological | Yes | Implemented | AWS Config & Infrastructure as Code | RISK-03 | AWS Config |
| **A.8.10** | Information deletion | Technological | Yes | Implemented | S3 Lifecycle Rules | RISK-05 | S3 Config |
| **A.8.11** | Data masking | Technological | Yes | Implemented | Synthetic Data Generation | RISK-05 | `04-architecture/data/` |
| **A.8.12** | Data leakage prevention | Technological | Yes | Implemented | S3 GuardDuty & Macie checks | RISK-05 | S3 Config |
| **A.8.13** | Information backup | Technological | Yes | Implemented | AWS Backup / S3 Versioning | RISK-08 | AWS Backup |
| **A.8.14** | Redundancy of information processing facilities | Technological | Yes | Implemented | Multi-AZ Deployment | RISK-08 | VPC Architecture |
| **A.8.15** | Logging | Technological | Yes | Implemented | CloudTrail Multi-Region Logs | RISK-07 | CloudTrail Config |
| **A.8.16** | Monitoring activities | Technological | Yes | Partially | CloudWatch Metric Filters & Alarms | RISK-07 | CloudWatch Alarms |
| **A.8.17** | Clock synchronization | Technological | Yes | Implemented | AWS NTP Synchronization | RISK-07 | AWS System Time |
| **A.8.18** | Use of privileged utility programs | Technological | Yes | Implemented | AWS SSM Session Manager | RISK-02 | SSM Config |
| **A.8.19** | Installation of software on operational systems | Technological | Yes | Implemented | Systems Manager Patch Manager | RISK-03 | SSM Config |
| **A.8.20** | Network security | Technological | Yes | Implemented | VPC Security Groups & Subnets | RISK-08 | VPC Config |
| **A.8.21** | Security of network services | Technological | Yes | Implemented | AWS Shield & WAF | RISK-08 | AWS WAF |
| **A.8.22** | Segregation of networks | Technological | Yes | Implemented | VPC Public/Private Subnets | RISK-08 | VPC Config |
| **A.8.23** | Web filtering | Technological | Yes | Implemented | AWS Network Firewall / Egress rules | RISK-08 | VPC Config |
| **A.8.24** | Use of cryptography | Technological | Yes | Implemented | AWS KMS CMK (AES-256) & TLS 1.3 | RISK-09 | `07-tls-kms/` |
| **A.8.25** | Secure development life cycle | Technological | Yes | Implemented | Git Commit signing & PR reviews | RISK-03 | Repo Config |
| **A.8.26** | Application security requirements | Technological | Yes | Implemented | OWASP Top 10 hardening | RISK-03 | App Config |
| **A.8.27** | Secure system architecture and engineering principles | Technological | Yes | Implemented | AWS Well-Architected Framework | RISK-03 | `04-architecture/` |
| **A.8.28** | Secure coding | Technological | Yes | Implemented | Python PEP8 & Bandit SAST | RISK-03 | `06-crypto-tool/` |
| **A.8.29** | Security testing in development and acceptance | Technological | Yes | Implemented | Prowler Automated Audits | RISK-03 | `08-after-audit/` |
| **A.8.30** | Outsourced development | Technological | Yes | Implemented | Code Review Guidelines | RISK-01 | Repo Rules |
| **A.8.31** | Separation of development, test and production environments | Technological | Yes | Implemented | AWS Multi-Account / VPC Isolation | RISK-02 | VPC Config |
| **A.8.32** | Change management | Technological | Yes | Implemented | Architecture Change Log | RISK-03 | `04-architecture/change-log.md` |
| **A.8.33** | Test information | Technological | Yes | Implemented | Synthetic Data only (no real PII) | RISK-05 | `04-architecture/data/` |
| **A.8.34** | Protection of information systems during audit testing | Technological | Yes | Implemented | Read-Only Audit IAM Roles | RISK-03 | IAM Roles |