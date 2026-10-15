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
| CH-05 | 2026-10-13 | Default Security Group-dan (`sg-0e7d80d7f53588fce`) SSH `0.0.0.0/0` qaydası silindi | BF-02 / R04 | 8.20, 8.22 | Qaydanı konsolda yenidən əlavə etmək (tövsiyə olunmur) | `04-04-before-ssh-rule-found.png`, `04-05-ssh-rule-removed.png` |
| CH-06 | 2026-10-13 | `Suleyman-admin`-dən birbaşa `AdministratorAccess` çıxarıldı; icazələr `novatech-admins` qrupu (PowerUserAccess + IAMFullAccess, MFA tələb edən siyasət) üzərindən verilir | BF-01 / R09 | 5.18, 8.2, 8.5 | `aws iam attach-user-policy --user-name Suleyman-admin --policy-arn arn:aws:iam::aws:policy/AdministratorAccess` | `04-03-admin-least-privilege-verified.png` |

## Qeydlər
- CH-01 – CH-04: hesab səviyyəli sərtləşdirmə, pulsuz və geri qaytarıla bilər
- CH-02: EBS şifrələməsi Faza 6-da şirkətin idarə etdiyi KMS açarına keçiriləcək (ayrıca sətir kimi qeyd olunacaq: CH-0X)
- CH-05: `before-weak-ssh-sg` adlı ayrıca Security Group heç vaxt müstəqil mövcud olmayıb; SSH qaydası əslində default Security Group-un üzərində idi. Bu, Faza 3-dəki Prowler "before" skanında (BF-02) sübut olunub və skan nəticələri arxivdə saxlanılır
- CH-06: AWS Organizations-ın sahib rolu (`AccountFullAccessRole`) ayrıca break-glass (fövqəladə) giriş kimi saxlanılır, gündəlik işdə istifadə olunmur; bu, `risk-acceptance.md`-də əsaslandırılacaq
- Növbəti dəyişikliklər (VPC, Security Group, S3 parametrləri) eyni cədvələ CH-07 və sonrakı ID-lərlə əlavə olunur
