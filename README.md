# Turing Makinesi ile PIN Doğrulama Simülasyonu

Bu proje, Turing makinesi kuramını kullanarak kullanıcıdan alınan 4 haneli PIN kodunun sistemde kayıtlı olan PIN ile eşleşip eşleşmediğini kontrol eden bir Python simülasyonudur. Bankamatik (ATM) cihazlarındaki PIN doğrulama mekanizması, Turing makinesi prensipleriyle modellenmiştir.

---

## 🎯 Proje Amacı

Turing makinesi kuramını gerçek yaşamla ilişkilendirmek ve bu kuramsal bilgiyi yazılımsal bir örnekle pekiştirmektir. Proje, karar süreçlerinin Turing makineleriyle nasıl modellenebileceğini ve algoritmik düşünmenin şerit ve geçiş fonksiyonları aracılığıyla nasıl geliştirilebileceğini göstermeyi hedefler.

---

## 🧠 Kuramsal Temel

Bu simülasyon, standart bir Turing makinesi modelini takip eder:

* **Alfabe**: `{'0', '1', ..., '9', '#', 'X', 'Y', 'B'}`
    * Rakamlar (`0-9`)
    * Ayırıcı/Başlangıç/Sonlandırıcı sembol (`#`)
    * İşaretleyiciler (`X`, `Y`)
    * Boş karakter (`B`)
* **Girdi Formatı**: Turing makinesi şeridi, kullanıcının girdiği PIN ve sistemde kayıtlı PIN'i aşağıdaki formatta içerir:
    `#KULLANICI_PINI#SİSTEM_PINI#`
    * Örnek: `#1234#1234#`
* **İşleyiş**: Turing makinesi, şerit üzerinde adım adım hareket ederek kullanıcı PIN'inin her bir hanesini sistem PIN'indeki karşılık gelen haneyle karşılaştırır. Eşleşen haneler, şerit üzerinde özel işaretleyicilerle (`X` ve `Y`) işaretlenir.
* **Durumlar**:
    * Eşleşme tamamlandığında ve tüm PIN haneleri doğru bir şekilde işaretlendiğinde makine **`q_accept`** (kabul) durumuna geçer.
    * Herhangi bir eşleşmezlik durumunda, yanlış formatta bir girdi alındığında veya PIN uzunlukları uyuşmadığında **`q_reject`** (reddet) durumuna geçer.

---

## ⚙️ Sistem Gereksinimleri

* **Python 3.x**

---

## Turing Makinesi Durum Geçiş Tablosu

| Mevcut Durum | Okunan Sembol | Yazılacak Sembol | Kafa Hareketi | Yeni Durum |
| :----------- | :------------ | :--------------- | :----------- | :--------- |
| `start`      | `B`           | `B`              | Sağ          | `find_user_pin_start` |
| `find_user_pin_start` | `#`           | `#`              | Sağ          | `compare_digit` |
| `compare_digit` | `0-9`         | `X`              | Sağ          | `find_separator` |
| `compare_digit` | `#`           | `#`              | Sağ          | `check_all_matched` |
| `find_separator` | `0-9`         | `0-9`            | Sağ          | `find_separator` |
| `find_separator` | `#`           | `#`              | Sağ          | `find_system_pin_digit` |
| `find_system_pin_digit` | `X`           | `X`              | Sağ          | `find_system_pin_digit` |
| `find_system_pin_digit` | `0-9`         | `Y`              | Sol          | `match_found_rewind` |
| `find_system_pin_digit` | `#`           | `#`              | Sağ          | `q_reject` (PIN uzunluğu uyuşmuyor) |
| `match_found_rewind` | `0-9`         | `0-9`            | Sol          | `match_found_rewind` |
| `match_found_rewind` | `#`           | `#`              | Sağ          | `compare_digit` |
| `check_all_matched` | `X`           | `X`              | Sağ          | `check_all_matched` |
| `check_all_matched` | `Y`           | `Y`              | Sağ          | `check_all_matched` |
| `check_all_matched` | `#`           | `#`              | Sağ          | `q_accept` |
| `check_all_matched` | `B`           | `B`              | Sol          | `q_accept` |
| Diğer durumlar | Herhangi biri | Herhangi biri    | -            | `q_reject` |

## 🚀 Projenin Çalıştırılması

Program sizden **4 haneli bir PIN kodu** girmenizi isteyecektir. Girdiğiniz PIN'e göre Turing makinesi simülasyonu adım adım şerit durumunu ve durum geçişlerini konsola yazdıracaktır.

## 🧪 Örnek Senaryolar

Aşağıda farklı senaryolar için programın beklenen çıktıları ve ekran görüntüsü yer tutucuları bulunmaktadır.

### Örnek Senaryo 1: Doğru PIN Girişi (`1234`)

Kullanıcı PIN'i: `1234`
Sistem PIN'i: `1234`

Beklenen Çıktı: "✅ Şifre doğru"

![image](https://github.com/user-attachments/assets/7df38fb9-0e19-44aa-aa1c-cccd3df58080)

### Örnek Senaryo 2: Yanlış PIN Girişi (`2569`)

Kullanıcı PIN'i: `2569`
Sistem PIN'i: `1234`

Beklenen Çıktı: "❌ Şifre hatalı"

![image](https://github.com/user-attachments/assets/4264ace6-7af7-4d64-86ec-eed7ffcd2517)

### Örnek Senaryo 3: Geçersiz Format (`asdfa`)

Kullanıcı PIN'i: `asdfa`
Sistem PIN'i: `1234`

Beklenen Çıktı: "Geçersiz PIN formatı."

![image](https://github.com/user-attachments/assets/0c591aeb-a249-441a-90a8-408489ae4783)
