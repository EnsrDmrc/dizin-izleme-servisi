# Dizin İzleme Servisi

Bu proje, bir dizindeki dosya değişikliklerini (oluşturma, silme, değiştirme, yeniden adlandırma) algılayan ve bu değişiklikleri bir log dosyasına kaydeden bir Python uygulamasıdır.

## Özellikler
- Dosya ve klasör oluşturma, silme, değiştirme ve yeniden adlandırma işlemlerini algılar.
- Değişiklikleri JSON formatında log dosyasına kaydeder.
- Kullanıcı dostu bir şekilde değişiklikleri terminale de yazar.

## Gereksinimler
- Python 3.x
- Watchdog kütüphanesi

## Kurulum ve Çalıştırma

1. **Gerekli kütüphaneleri yükleyin**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Dizin yapısını kontrol edin**:
    - `directory_monitor.py`: Ana Python dosyası.
    - `logs/`: Log dosyalarının saklandığı klasör.
    - İzlenecek dizini (örneğin, `test/`) oluşturun ve dosyaları burada test edin.

3. **Script'i çalıştırın**:
    ```bash
    python3 directory_monitor.py
    ```

4. **Değişiklikleri test edin**:
    - İzlenen dizinde yeni bir dosya oluşturun.
    - Bir dosyayı silin veya yeniden adlandırın.
    - Log dosyasında yapılan değişikliklerin kaydedildiğini kontrol edin.

## Kullanım Senaryosu
- **Dosya sistemi değişikliklerini izlemek**: Sistem yöneticileri veya geliştiriciler, belirli dizinlerdeki değişiklikleri takip etmek için bu aracı kullanabilir.
- **Otomatik yedekleme veya işlem tetikleme**: Değişiklik algılandığında başka bir işlemi tetiklemek için temel olarak kullanılabilir.

## Proje Yapısı
