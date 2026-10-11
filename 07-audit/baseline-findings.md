# "Before" auditi: ilkin tapıntılar (Baseline Findings)

**Şirkət:** NovaTech Solutions
**Mərhələ:** Faza 3, "Before" vəziyyəti
**Versiya:** 1.0 (qaralama: medium və low tapıntılar servis səviyyəsindədir)
**Əlaqəli sənədlər:** `risk-register.md`, `asset-register.md`, `risk-methodology.md`

## 1. Audit parametrləri

| Parametr | Dəyər |
|---|---|
| Alət | Prowler 5.44.0 |
| Çərçivə | ISO27001_2022_AWS |
| Tarix | 2026-10-11, 20:47 |
| Hesab | [Account ID gizlədilib] |
| Region | eu-north-1 (Stokholm) |
| Skanı aparan identifikasiya | IAM istifadəçisi `Suleyman-admin` (MFA ilə) |
| İstifadə olunmayan resurslar | Skan edilir (`--scan-unused-services`) |
| Yoxlama sayı | 330 |
| Əmr | `prowler aws --region eu-north-1 --scan-unused-services -M html csv json-ocsf --compliance iso27001_2022_aws` |

> **Metodoloji qeyd.** İlk skan bu bayraq olmadan aparıldı (50 FAIL). Prowler heç nəyə bağlı olmayan resursları (məsələn, serverə qoşulmamış Security Group) atladığı üçün zəif SSH qrupu aşkarlanmadı. Bayraq əlavə edilərək skan təkrarlandı. **Rəsmi baza ikinci skandır.** "After" skanı (Faza 8) **eyni parametrlərlə** aparılmalıdır.

## 2. Ümumi nəticə

| Göstərici | Say |
|---|---|
| Ümumi nəticə | 119 |
| **FAIL** | **66** (55.46%) |
| PASS | 53 (44.54%) |
| Susdurulmuş (muted) | 0 |

| Ciddilik (yalnız FAIL) | Say |
|---|---|
| Critical | 1 |
| High | 15 |
| Medium | 39 |
| Low | 11 |
| **Cəmi** | **66** |

## 3. Servis üzrə bölgü (FAIL)

| Servis | FAIL | Critical | High | Medium | Low | Əsas risk (reyestr) |
|---|---|---|---|---|---|---|
| iam | 17 | 1 | 3 | 9 | 4 | R01, R09 |
| cloudwatch | 14 | 0 | 0 | 14 | 0 | R05, R12 |
| ec2 | 7 | 0 | 5 | 2 | 0 | R04, R10, R03 |
| vpc | 7 | 0 | 3 | 4 | 0 | R04 |
| s3 | 6 | 0 | 1 | 3 | 2 | R02, R03, R08 |
| cloudtrail | 4 | 0 | 0 | 1 | 3 | R05 |
| glue | 2 | 0 | 1 | 1 | 0 | Əhatədən kənar |
| accessanalyzer | 1 | 0 | 0 | 0 | 1 | R09 |
| account | 1 | 0 | 0 | 1 | 0 | Dəqiqləşdiriləcək |
| athena | 1 | 0 | 0 | 1 | 0 | Əhatədən kənar |
| backup | 1 | 0 | 0 | 0 | 1 | R08 |
| bedrock | 1 | 0 | 0 | 1 | 0 | Əhatədən kənar |
| config | 1 | 0 | 0 | 1 | 0 | R05, R10 |
| guardduty | 1 | 0 | 1 | 0 | 0 | R05 |
| networkfirewall | 1 | 0 | 0 | 1 | 0 | Əhatədən kənar |
| securityhub | 1 | 0 | 1 | 0 | 0 | R05 |
| **Cəmi** | **66** | **1** | **15** | **39** | **11** | |

## 4. Critical və High tapıntılar (detallı)

| ID | Yoxlama (CHECK_ID) | Ciddilik | Resurs sayı | Risk | Annex A | Qərar | Faza |
|---|---|---|---|---|---|---|---|
| BF-01 | `iam_aws_attached_policy_no_administrative_privileges` | **Critical** | 1 | R09 | 5.18, 8.2 | Azaltmaq | 4 |
| BF-02 | `ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_22` | High | 1 | R04 | 8.20, 8.22 | Azaltmaq | 4 |
| BF-03 | `ec2_networkacl_allow_ingress_any_port` | High | 1 | R04 | 8.20 | Azaltmaq | 4 |
| BF-04 | `ec2_securitygroup_default_restrict_traffic` | High | 1 | R04 | 8.20 | Azaltmaq | 4 |
| BF-05 | `vpc_subnet_no_public_ip_by_default` | High | 3 | R04 | 8.20, 8.22 | Azaltmaq | 4 |
| BF-06 | `ec2_instance_account_imdsv2_enabled` | High | 1 | R10 | 8.8, 8.9 | Azaltmaq | 4 |
| BF-07 | `ec2_ebs_default_encryption` | High | 1 | R03 | 8.24 | Azaltmaq | 6 |
| BF-08 | `s3_account_level_public_access_blocks` | High | 1 | R02 | 8.3, 5.23 | Azaltmaq | 4 |
| BF-09 | `iam_user_mfa_enabled_console_access` | High | 1 | R01 | 8.5, 5.17 | Azaltmaq | 4 |
| BF-10 | `iam_user_hardware_mfa_enabled` | High | 2 | R01 | 8.5 | Qəbul etmək (əsaslandırma ilə) | 9 |
| BF-11 | `guardduty_is_enabled` | High | 1 | R05 | 8.15, 8.16 | Azaltmaq | 5 |
| BF-12 | `securityhub_enabled` | High | 1 | R05 | 8.16 | Xərc-fayda qiymətləndirməsi | 5 |
| BF-13 | `glue_data_catalogs_connection_passwords_encryption_enabled` | High | 1 | Yoxdur | Yoxdur | Əhatədən kənar | 9 |

Cəmi: 1 critical + 15 high = 16 resurs sətri (BF-05 üç, BF-10 iki resursdan ibarətdir).

### Şərhlər
- **BF-01 (critical).** `AdministratorAccess` siyasəti birbaşa istifadəçiyə qoşulub. Ən az imtiyaz prinsipinə ziddir. Faza 4-də rol və qrup əsaslı, MFA tələb edən model qurulandan sonra həll olunacaq. Admin hüququ indi çıxarılmır ki, giriş itirilməsin.
- **BF-02.** Bilərəkdən yaradılmış `before-weak-ssh-sg` qrupu (SSH, `0.0.0.0/0`) bu tapıntıya cavab verir. Resurs adı HTML hesabatında təsdiqlənməlidir.
- **BF-05.** AWS-in avtomatik yaratdığı **default VPC**-nin üç subnet-i. Həll: öz VPC-miz, public və private subnet ayrılığı.
- **BF-09.** Gözlənilən resurs bilərəkdən yaradılmış `before-test-user` (MFA yoxdur). Resurs adı HTML hesabatında təsdiqlənməlidir.
- **BF-10.** Standart fiziki (hardware) MFA açarı tələb edir. Şirkət virtual MFA (telefon tətbiqi) istifadə edir. Kiçik şirkət üçün qəbul edilə bilər, `risk-acceptance.md` sənədinə əlavə olunacaq (əsaslandırma və kompensasiyaedici tədbirlər ilə).
- **BF-12.** Security Hub xərc yarada bilər. Qərar qiymət yoxlanışından sonra verilir (azaltmaq və ya qəbul etmək).
- **BF-13.** Glue xidməti istifadə edilmir.

## 5. Medium və Low tapıntılar

Servis səviyyəsində xülasə (bax: 3-cü bölmə). Hər tapıntının dəqiq yoxlama adı və qərarı `baseline-before-fails.csv` faylından bu sənədə əlavə ediləcək.

| Qrup | Tapıntı sayı | Qeyd |
|---|---|---|
| Monitorinq və loqlama (`cloudwatch`, `cloudtrail`, `config`) | 19 | Audit loqu və xəbərdarlıqlar qurulmayıb (R05). Faza 5 |
| IAM (medium və low) | 13 | Parol siyasəti, açar və hesab idarəsi (R01, R09). Faza 4 |
| S3 (medium və low) | 5 | Versioning, loqlama, HTTPS siyasəti (R02, R03, R08). Faza 4 |
| EC2 və VPC (medium) | 6 | Şəbəkə konfiqurasiyası (R04). Faza 4 |
| Backup, Access Analyzer | 2 | Ehtiyat nüsxə və giriş analizi (R08, R09). Faza 4, 5 |
| Əhatədən kənar (`athena`, `bedrock`, `glue` medium, `networkfirewall`) | 4 | İstifadə olunmayan xidmətlər |
| Hesab (`account`) | 1 | Dəqiqləşdiriləcək |

## 6. Qərarların xülasəsi

| Qərar | Tapıntılar | Kommentariya |
|---|---|---|
| Azaltmaq (nəzarət tətbiq etmək) | BF-01 ... BF-09, BF-11 | Faza 4, 5, 6 |
| Qəbul etmək | BF-10 | `risk-acceptance.md` |
| Xərc-fayda qiymətləndirməsi | BF-12 | Faza 5 |
| Əhatədən kənar (SoA-da "tətbiq olunmur") | BF-13, Athena, Bedrock, Network Firewall | Xidmətlər istifadə edilmir |

## 7. Növbəti addımlar
1. Medium və low tapıntıları CSV-dən bu sənədə əlavə etmək
2. HTML hesabatından BF-02 və BF-09 resurs adlarını təsdiqləmək
3. Faza 4: təhlükəsiz arxitekturanın qurulması
4. Faza 8: **eyni parametrlərlə** "after" skanı və müqayisə
