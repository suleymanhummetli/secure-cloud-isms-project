# Cloud Security Incident Report - NovaTech Solutions
**Incident ID:** INC-2026-001  
**Date/Time:** October 15, 2026  
**Detection Source:** AWS CloudWatch Metric Filter & CloudTrail  
**Severity:** Medium / Controlled Simulation  
**Status:** Resolved / Verified  

---

## 1. Incident Overview (Insidentin Xülas?si)
NovaTech Solutions bulud infrastrukturunun monitorinqi zamani simulyasiya m?qs?dil? t?hlük?sizlik qrupunda (Security Group) icaz?siz konfiqurasiya d?yisikliyi h?yata keçirilmisdir. Bu d?yisiklik CloudTrail t?r?find?n qeyd? alinmis v? CloudWatch SecurityGroupChangesFilter vasit?sil? d?rhal deteksiya olunmusdur.

## 2. Detection & Monitoring Mechanism (Askarlama Mexanizmi)
* **Log Group:** \/aws/cloudtrail/novatech-trail\
* **Metric Filter:** \SecurityGroupChangesFilter\
* **Metric Namespace:** \NovaTechSecurityMetrics\
* **Alarm Name:** \NovaTech-SecurityGroup-Changed-Alarm\

## 3. Impact Assessment (T?sirin Qiym?tl?ndirilm?si)
* **Affected Resources:** AWS VPC Security Groups (eu-north-1)
* **Data Loss:** None
* **Unauthorized Access:** None (Simulation test only)

## 4. Remediation & Corrective Actions (Aradan Qaldirma T?dbirl?ri)
1. Security Group d?yisikliyi yoxlanildi v? test qaydasi t?mizl?ndi.
2. CloudWatch Alarm-in isl?m?si v? siqnal verm?si dogrulandi.
3. ISO/IEC 27001 (Annex A.12 / A.16) t?l?bl?rin? uygun olaraq insident qeyd? alindi.
