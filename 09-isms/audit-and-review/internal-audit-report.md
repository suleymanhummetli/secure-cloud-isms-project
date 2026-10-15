# Internal Audit Report / Self-Assessment (ISO/IEC 27001:2022 Clause 9.2)
**Organization:** NovaTech Solutions  
**Evaluation Type:** Internal Self-Assessment (Academic / Practical Lab Exercise)  
**Evaluator:** Süleyman Hümmətli (Lead Engineer & Implementer - Note: Independence is limited due to single-operator lab scope)  
**Date:** October 15, 2026  

## 1. Objective & Methodology
To evaluate the technical readiness and security posture of the AWS `eu-north-1` environment using automated Prowler v5 checks (655 total checks executed).

## 2. Audit Findings & Non-Conformities
* **Framework Compliance:** 68.48% PASS score achieved.
* **Identified Gaps (Non-Conformities):**
  1. *Monitoring Gap:* Initial CloudWatch alarms lacked active SNS notification endpoints during baseline testing.
  2. *Documentation Integrity:* Git repository experienced character encoding corruption (resolved via strict UTF-8 enforcement).
* **Corrective Actions Taken:** SNS topics configured, metric filters refined, and repository structure normalized.