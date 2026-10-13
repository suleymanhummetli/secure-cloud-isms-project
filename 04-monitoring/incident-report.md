# İnsidentlərin İdarə Edilməsi və Monitorinq Hesabatı
**Şirkət:** NovaTech Solutions  
**Standart:** ISO/IEC 27001:2022 (Annex A.16)  
**Məsul şəxs:** Süleyman Hümmətli  

## 1. Giriş
NovaTech Solutions bulud infrastrukturuna keçdikdən sonra bütün API çağırışları, təhdidlər və şübhəli fəaliyyətlər mərkəzləşdirilmiş şəkildə izlənilir. Bu hesabat Faza 5 çərçivəsində qurulan monitorinq və aşkarlama arxitekturasını əhatə edir.

## 2. Tətbiq Edilən Monitorinq Alətləri
* **AWS CloudTrail (`novatech-trail`):** Bütün multi-region API fəaliyyətlərini qeydə alır, loq fayllarının bütövlüyü kriptoqrafik olaraq doğrulanır (`LogFileValidation: true`) və xüsusi S3 bucket-ində saxlanılır.
* **AWS GuardDuty:** Hesab daxilindəki anomal davranışı, icazəsiz port skanlarını və zərərli IP ünvanlarından gələn cəhdləri avtomatik aşkarlayan təhdid aşkarlama sistemi aktivdir (`Status: ENABLED`).
* **Amazon CloudWatch & Alarms:** CloudTrail loqları üzərindən metrik filtrlər qurulmuşdur. Root hesabından istifadə edildikdə dərhal xəbərdarlıq yaratmaq üçün `RootAccountUsageAlarm` konfiqurasiya edilmişdir.

## 3. İnsident Simulyasiyası və Aşkarlama Ssenarisi
* **Ssenari:** Kənar şəxsin və ya oğurlanmış identifikasiyanın Root və ya imtiyazlı hesab vasitəsilə sistemə giriş cəhdi.
* **Reaksiya Mexanizmi:** 
  1. CloudTrail hadisəni dərhal qeydə alır və CloudWatch Log Group-a ötürür.
  2. `RootAccountUsageFilter` filtrivə uyğun gələn hadisəni yaxalayır.
  3. `RootAccountUsageAlarm` aktivləşərək təhlükəsizlik məsuluna siqnal göndərir.
  4. GuardDuty şübhəli aktivliyi analiz edərək tapıntı (`Finding`) yaradır.

## 4. Nəticə
Qurulan bu çoxqatlı monitorinq sistemi sayəsində Prowler auditində aşkar edilən CloudWatch və CloudTrail üzrə mövcud tapıntılar bağlanmış, şirkətin təhlükəsizlik səviyyəsi tələb olunan ISO 27001 standartına uyğunlaşdırılmışdır.
