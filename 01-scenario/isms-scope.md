# İTİS-in əhatə dairəsi (ISMS Scope)

**Şirkət:** NovaTech Solutions
**Standart:** ISO/IEC 27001:2022
**Versiya:** 1.0
**Sənədin sahibi:** İnformasiya təhlükəsizliyi məsulu

## 1. Məqsəd
Bu sənəd NovaTech Solutions-ın İnformasiya Təhlükəsizliyi İdarəetmə
Sisteminin (İTİS) hansı aktivləri, proseslərı və məkanları əhatə etdiyini
və hansılarını əhatə etmədiyini müəyyən edir.

## 2. Əhatə dairəsinə daxildir
| Sahə | Təsvir |
|---|---|
| Bulud mühiti | AWS hesabı ("Dream It Ship It"), region: eu-north-1 (Stokholm) |
| Tətbiq | Onlayn sifariş platforması (veb server və saxlanılan məlumatlar) |
| Məlumatlar | Müştəri məlumatları (sintetik), mənbə kodu, loqlar, ehtiyat nüsxələr |
| İdentifikasiya | AWS IAM hesabları, MFA, giriş nəzarəti |
| Kriptoqrafiya | AWS KMS açarları, TLS sertifikatları, şifrələmə alətləri |
| Monitorinq | CloudTrail, CloudWatch, GuardDuty |
| İşçi iş stansiyaları | Developer və DevOps noutbukları |
| Proseslər | Risk idarəsi, insident idarəsi, ehtiyat nüsxə, giriş idarəsi |

## 3. Əhatə dairəsindən kənardır (əsaslandırma ilə)
| Sahə | Səbəb |
|---|---|
| Ofisin fiziki təhlükəsizliyi | Layihənin diqqəti buluda keçiddir; fiziki nəzarət sonrakı mərhələdir |
| Ödəniş provayderinin daxili sistemləri | Üçüncü tərəfin məsuliyyətidir, müqavilə ilə idarə olunur |
| AWS-in fiziki infrastrukturu (data mərkəzləri) | AWS-in məsuliyyətindədir (Shared Responsibility Model) |
| Şəxsi cihazlar (BYOD) | Şirkətdə icazə verilmir |

## 4. Məsuliyyət bölgüsü (AWS Shared Responsibility Model)
- **AWS məsuliyyət daşıyır:** fiziki data mərkəzləri, şəbəkə və hardware, virtuallaşdırma qatı
- **NovaTech məsuliyyət daşıyır:** IAM, məlumatların şifrələnməsi, şəbəkə konfiqurasiyası,
  əməliyyat sistemi, tətbiq, loqlama və monitorinq

## 5. Sərhədlər və asılılıqlar
- AWS (bulud provayderi), GitHub (mənbə kodu), e-poçt provayderi
- Daxili asılılıqlar: İT departamenti, DevOps, rəhbərlik

## 6. Məkan
- Ofis: Bakı, Azərbaycan
- Bulud: AWS eu-north-1 (Stokholm)
