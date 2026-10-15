# Risk reyestri

| ID | Aktiv | Təhdid | Zəiflik | E | T | Bal | Səviyyə | Müalicə | Nəzarət (Annex A) | Faza |
|---|---|---|---|---|---|---|---|---|---|---|
| R01 | A04 AWS hesabı və IAM | Hesabın ələ keçirilməsi | MFA yoxdur, zəif parollar | 4 | 5 | 20 | Kritik | Azaltmaq | 5.17, 8.5, 8.2 | 4 |
| R02 | A01 Müştəri məlumatları | Təsadüfən açıq saxlanma | Səhv konfiqurasiya olunmuş S3 | 3 | 5 | 15 | Yüksək | Azaltmaq | 8.3, 5.23, 8.9 | 3, 4 |
| R03 | A01 Müştəri məlumatları | Məlumatın oğurlanması | Saxlama zamanı şifrələmə yoxdur | 3 | 4 | 12 | Yüksək | Azaltmaq | 8.24 | 6, 7 |
| R04 | A03 Veb server | Brute-force hücumu | SSH hamıya açıqdır (0.0.0.0/0) | 4 | 4 | 16 | Yüksək | Azaltmaq | 8.20, 8.22 | 4 |
| R05 | A07 Loqlar | Hücumun aşkarlanmaması | Mərkəzləşdirilmiş loqlama yoxdur | 4 | 4 | 16 | Yüksək | Azaltmaq | 8.15, 8.16 | 5 |
| R06 | A02 Mənbə kodu | Gizli məlumatın sızması | Kodda sərt yazılmış açarlar | 4 | 4 | 16 | Yüksək | Azaltmaq | 8.4, 8.28, 5.17 | 5 |
| R07 | A05 Kriptoqrafik açarlar | Açarın itirilməsi və ya sui-istifadə | Açar siyasəti və rotasiya yoxdur | 2 | 5 | 10 | Yüksək | Azaltmaq | 8.24, 5.18 | 7 |
| R08 | A08 Ehtiyat nüsxələr | Məlumatın bərpa edilməməsi | Ehtiyat nüsxə yoxdur və ya qorunmur | 3 | 4 | 12 | Yüksək | Azaltmaq | 8.13 | 4 |
| R09 | A04 IAM identifikasiyaları | İmtiyazların sui-istifadəsi | Həddən artıq geniş icazələr | 3 | 4 | 12 | Yüksək | Azaltmaq | 5.18, 8.2 | 4 |
| R10 | A03 Veb server | Zəifliklərin istismarı | Yenilənməmiş proqram təminatı | 3 | 4 | 12 | Yüksək | Azaltmaq | 8.8 | 8 |
| R11 | A06 TLS sertifikatları | Açarın oğurlanması və ya müddətin bitməsi | Sertifikat idarəsi yoxdur | 2 | 4 | 8 | Orta | Azaltmaq | 8.24 | 7 |
| R12 | A04 AWS hesabı | Açar sızması ilə kriptomaynınq | Billing xəbərdarlığı və monitorinq yoxdur | 3 | 3 | 9 | Orta | Azaltmaq | 8.16 | 0, 5 |
| R13 | A09 Noutbuklar | İtirilmə və ya oğurlanma | Disk şifrələməsi yoxdur | 3 | 3 | 9 | Orta | Azaltmaq | 8.1 | 9 |
| R14 | A10 HR məlumatları | E-poçtla təsadüfən göndərmə | Məlumat sızması nəzarəti yoxdur | 2 | 4 | 8 | Orta | Azaltmaq | 8.12, 6.3 | 9 |
| R15 | A03 Veb server | AWS xidmətinin dayanması | Tək nöqtəli arxitektura | 2 | 3 | 6 | Orta | Qəbul etmək | 5.30 | 9 |

E = Ehtimal, T = Təsir.
