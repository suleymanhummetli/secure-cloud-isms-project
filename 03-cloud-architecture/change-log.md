# Dəyişiklik jurnalı (Change Log)

**Şirkət:** NovaTech Solutions
**Əlaqəli nəzarət:** ISO/IEC 27001:2022 Annex A 8.32 (dəyişikliklərin idarəsi)
**Aparan:** `Suleyman-admin` (MFA ilə), AWS CLI profili `novatech`
**Region:** eu-north-1 (Stokholm)

Hər dəyişiklik bir sətirdir: nə dəyişdi, niyə (tapıntı və risk), hansı Annex A nəzarətinə aiddir, sübut hansıdır. Bütün dəyişikliklər "before" skanından (2026-10-11, 20:47) **sonra** edilib.

| ID | Tarix | Dəyişiklik | Səbəb (tapıntı / risk) | Annex A | Geri qaytarma | Sübut |
|---|---|---|---|---|---|---|
| CH-01 | 2026-10-11 | S3 Block Public Access hesab səviyyəsində aktiv edildi (4 bayraq `true`) | BF-08 / R02 | 8.3, 5.23 | `aws s3control delete-public-access-block` | `04-01-account-hardening-verification.png` |
| CH-02 | 2026-10-11 | EBS default şifrələmə aktiv edildi (eu-north-1, AWS-in idarə etdiyi açar) | BF-07 / R03 | 8.24 | `aws ec2 disable-ebs-encryption-by-default` | `04-01-account-hardening-verification.png` |
| CH-03 | 2026-10-11 | IMDSv2 hesab səviyyəsində məcburi edildi (`HttpTokens: required`) | BF-06 / R10 | 8.8, 8.9 | `aws ec2 modify-instance-metadata-defaults --http-tokens optional` | `04-01-account-hardening-verification.png` |
| CH-04 | 2026-10-11 | IAM parol siyasəti qurulub (min. 14 simvol, mürəkkəblik, 90 gün müddət, 24 təkrar qadağası) | R01, R09 | 5.17 | `aws iam delete-account-password-policy` | `04-01-account-hardening-verification.png` |

## Qeydlər
- Bu dəyişikliklərin hamısı pulsuzdur və geri qaytarıla bilər
- EBS şifrələməsi Faza 6-da şirkətin idarə etdiyi KMS açarına keçiriləcək (ayrıca dəyişiklik kimi qeyd olunacaq)
- Növbəti dəyişikliklər (IAM modeli, VPC, Security Group, S3 parametrləri) eyni formatda əlavə olunur: CH-05, CH-06 və s.
