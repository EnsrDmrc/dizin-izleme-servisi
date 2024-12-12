# Test Sonuçları

Bu dosya, `directory_monitor.py` script'inin farklı senaryolarda test edilme sonuçlarını içerir.

## Test Senaryoları ve Sonuçlar

### 1. **Dosya Oluşturma**
- **Senaryo**: İzlenen dizine yeni bir dosya oluşturuldu (`test_dosya.txt`).
- **Beklenen Sonuç**: `logs/changes.json` dosyasına "created" tipi ile kaydedilmesi.
- **Sonuç**: ✔ Başarılı

### 2. **Dosya Silme**
- **Senaryo**: İzlenen dizindeki bir dosya silindi (`test_dosya.txt`).
- **Beklenen Sonuç**: `logs/changes.json` dosyasına "deleted" tipi ile kaydedilmesi.
- **Sonuç**: ✔ Başarılı

### 3. **Dosya Değiştirme**
- **Senaryo**: Bir dosya üzerinde değişiklik yapıldı (`yeni_dosya.txt`).
- **Beklenen Sonuç**: `logs/changes.json` dosyasına "modified" tipi ile kaydedilmesi.
- **Sonuç**: ✔ Başarılı

### 4. **Dosya Yeniden Adlandırma**
- **Senaryo**: Bir dosya yeniden adlandırıldı (`yeni_dosya.txt` → `yeniden_adlandirilan_dosya.txt`).
- **Beklenen Sonuç**: `logs/changes.json` dosyasına "moved" tipi ile kaydedilmesi.
- **Sonuç**: ✔ Başarılı

## Genel Değerlendirme
Script, tüm temel dosya sistemi olaylarını başarıyla algıladı ve log dosyasına doğru bir şekilde kaydetti.
