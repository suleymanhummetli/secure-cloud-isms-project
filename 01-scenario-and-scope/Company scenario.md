# NovaTech Solutions: Şirkət ssenarisi

**Sənəd:** company-scenario.md
**Versiya:** 1.0
**Standart:** ISO/IEC 27001:2022
**Qeyd:** NovaTech Solutions uydurma şirkətdir. Bütün məlumatlar təlim layihəsi üçün hazırlanıb.

## 1. Şirkət haqqında
NovaTech Solutions Bakıda yerləşən, kiçik və orta bizneslər üçün onlayn sifariş
platforması hazırlayan proqram şirkətidir. Şirkətdə 25 işçi çalışır.

| Departament | İşçi sayı |
|---|---|
| Proqram təminatı (developer) | 10 |
| DevOps | 3 |
| Müştəri dəstəyi | 4 |
| Satış | 3 |
| İdarəetmə | 3 |
| Maliyyə və HR | 2 |
| **Cəmi** | **25** |

## 2. İşlədilən məlumatlar
- Müştəri məlumatları: ad, e-poçt, telefon, sifariş tarixçəsi
- Ödəniş məlumatları (yalnız kartın son 4 rəqəmi, tam nömrə saxlanmır)
- Mənbə kodu və daxili sənədlər
- İşçi məlumatları (HR)

Layihə boyu istifadə olunan bütün "müştəri məlumatları" **sintetikdir** (saxta, proqramla yaradılmış). Real şəxsi məlumat istifadə edilmir.

## 3. Mövcud IT mühiti
Platforma ofisdəki fiziki serverlərdə işləyir. Ehtiyat nüsxələr sərbəst disklərdə
saxlanılır, giriş nəzarəti parol əsaslıdır, MFA tətbiq olunmur, mərkəzləşdirilmiş
loqlama yoxdur.

## 4. Buluda keçidin səbəbləri
- Serverlərin əlçatanlığını artırmaq
- Müştəri sayının artması ilə miqyaslanma
- Təhlükəsizlik səviyyəsini yüksəltmək

## 5. Layihənin məqsədləri
1. Bütün istifadəçi hesablarında MFA və ən az imtiyaz prinsipi
2. Bütün məlumatların şirkətin idarə etdiyi açarlarla şifrələnməsi
3. Bütün fəaliyyətlərin loqlanması və təhlükəli hadisələrin aşkarlanması
4. ISO/IEC 27001 əsasında İTİS-in qurulması və sübut edilməsi
5. Bulud mühitinin təhlükəsizlik auditində kritik tapıntı sayının sıfıra endirilməsi

## 6. Maraqlı tərəflər
Rəhbərlik, işçilər, müştərilər, bulud provayderi (AWS), tənzimləyici orqanlar.
Ətraflı: `stakeholders.md`.

## 7. Qəbul olunmuş ilkin fərziyyələr
- Bulud platforması: AWS, region eu-north-1 (Stokholm)
- Layihə mühiti: tək AWS iş hesabı ("Dream It Ship It")
- Şirkətin informasiya təhlükəsizliyi məsulu layihənin icraçısıdır
