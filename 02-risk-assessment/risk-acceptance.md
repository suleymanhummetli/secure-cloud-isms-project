# Riskin qəbulu sənədi (Risk Acceptance)

**Şirkət:** NovaTech Solutions
**Standart:** ISO/IEC 27001:2022, bənd 6.1.3 və 8.3
**Versiya:** 1.0
**Tarix:** 2026-10-10
**Sənədin sahibi:** İnformasiya təhlükəsizliyi məsulu
**Əlaqəli sənədlər:** `risk-methodology.md`, `risk-register.md`

## 1. Məqsəd
Bu sənəd müalicə olunmadan (nəzarət tətbiq edilmədən) qəbul edilən riskləri,
qəbulun əsaslandırmasını və təsdiq edən şəxsi qeyd edir. Qəbul qərarı rəsmi
şəkildə sənədləşdirilməlidir; səssiz qəbul İTİS tələblərinə uyğun deyil.

## 2. Qəbul meyarları
| Risk balı | Səviyyə | Kim qəbul edə bilər |
|---|---|---|
| 1-4 | Aşağı | Risk sahibi |
| 5-9 | Orta | Risk sahibi və informasiya təhlükəsizliyi məsulu |
| 10-16 | Yüksək | Yalnız rəhbərlik, yazılı əsaslandırma ilə |
| 17-25 | Kritik | Qəbul edilə bilməz, dərhal müalicə məcburidir |

Əsas qayda: balı 10 və yuxarı olan risk müalicə olunmadan qəbul edilmir
(metodologiyaya uyğun olaraq).

## 3. Qəbul edilmiş risklər

### R15: AWS xidmətinin dayanması
| Sahə | Məzmun |
|---|---|
| Aktiv | A03 Veb tətbiq serveri |
| Təhdid | AWS xidmətinin və ya zonasının dayanması |
| Zəiflik | Tək nöqtəli arxitektura (bir zona, bir server) |
| İlkin risk | Ehtimal 2 × Təsir 3 = **6 (Orta)** |
| Müalicə qərarı | **Qəbul etmək** |
| Əsaslandırma | Çox zonalı (multi-AZ) arxitekturanın aylıq xərci layihə miqyasında risk dəyərindən yüksəkdir. AWS-in region səviyyəsində uzunmüddətli dayanması ehtimalı aşağıdır. Dayanma qısamüddətli iş pozulması yaradır, məlumat itkisi yaratmır. |
| Kompensasiyaedici tədbirlər | Ehtiyat nüsxələr ayrıca S3 bucket-də saxlanılır; infrastruktur kodla (Terraform) təsvir olunub və başqa zonada sürətlə yenidən qurula bilər; AWS Health bildirişləri izlənir |
| Qalıq risk | 6 (Orta), dəyişməz qəbul edilir |
| Risk sahibi | DevOps rəhbəri |
| Təsdiq edən | Rəhbərlik (CEO): [Ad Soyad] |
| Təsdiq tarixi | 2026-10-10 |
| Növbəti baxış | 2027-04-10 (6 aydan sonra) və ya arxitektura dəyişəndə |
| Status | Qüvvədədir |

## 4. Qəbul şərtləri
- Qəbul müvəqqətidir və növbəti baxış tarixinə qədər qüvvədədir.
- Risk balı artarsa (məsələn, müştəri sayı sürətlə böyüyərsə), qəbul ləğv olunur və risk yenidən qiymətləndirilir.
- Qəbul edilən risklər illik rəhbərlik icmalında təqdim olunur.

## 5. Təsdiq
| Rol | Ad Soyad | İmza | Tarix |
|---|---|---|---|
| Risk sahibi (DevOps rəhbəri) | [Ad Soyad] | | |
| İnformasiya təhlükəsizliyi məsulu | [Ad Soyad] | | |
| Rəhbərlik (CEO) | [Ad Soyad] | | |

## 6. Yeni risk qəbulu üçün şablon
| Sahə | Məzmun |
|---|---|
| Risk ID və ad | |
| Aktiv, təhdid, zəiflik | |
| İlkin risk (E × T) | |
| Qəbulun əsaslandırması | |
| Kompensasiyaedici tədbirlər | |
| Risk sahibi | |
| Təsdiq edən və tarix | |
| Növbəti baxış tarixi | |
