# Access Control Policy (ISO 27001 A.5.15 / A.8.5)
**Organization:** NovaTech Solutions  
**Status:** Implemented  

## 1. Purpose & Scope
Defines strict access control rules for AWS `eu-north-1` infrastructure following Least Privilege and MFA enforcement.
## 2. Rules
* Multi-Factor Authentication (MFA) is mandatory for `Suleyman-admin` and all privileged IAM users.
* Access keys are rotated regularly; hardcoded credentials are strictly prohibited.