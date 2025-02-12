# Harpie Auto Scan

![Harpie Logo](https://github.com/user-attachments/assets/829048f3-2045-4c1f-8a32-9ba87c2bddb6)

**Script ini mendukung banyak alamat Ethereum untuk pemindaian otomatis.**

> **PERINGATAN:** Resiko ditanggung oleh pengguna sepenuhnya. Pastikan Anda memahami risiko sebelum menggunakan script ini.

## Fitur
- Mendukung banyak alamat Ethereum.
- Pemindaian otomatis setiap 24 jam.

## Cara Menggunakan

### Prasyarat
1. **Daftar Akun Harpie**  
   Pastikan Anda mendaftar di Harpie melalui link referensi berikut:  
   [https://harpie.io/refer/pMs34a](https://harpie.io/refer/pMs34a)

2. **Install Python**  
   Pastikan Anda sudah menginstall Python versi 3.x. Jika belum, jalankan perintah berikut:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip -y
   ```

3. **Clone Repository**  
   Clone repository ini ke komputer Anda:
   ```bash
   git clone https://github.com/Semutireng22/harpie
   cd harpie
   ```

4. **Install Dependencies**  
   Install semua dependensi yang diperlukan menggunakan pip:
   ```bash
   pip install -r requirements.txt
   ```

5. **Jalankan Script**  
   Jalankan script dengan perintah berikut:
   ```bash
   python3 bot.py
   ```

---

## Menu Utama

Setelah menjalankan script, Anda akan melihat menu utama seperti berikut:

```
===========================================
=               Main Menu                 =
===========================================
1. Add new address
2. Start scanning
3. Exit
```

### Opsi Menu
1. **Add New Address**  
   Pilih opsi `1` untuk menambahkan alamat Ethereum baru. Jika Anda ingin menambahkan lebih dari satu alamat, ulangi proses ini dengan memilih opsi `1` lagi.

2. **Start Scanning**  
   Pilih opsi `2` untuk memulai pemindaian otomatis. Script akan melakukan pemindaian untuk semua alamat yang telah ditambahkan dan menjalankan pemindaian berikutnya setiap 24 jam.

3. **Exit**  
   Pilih opsi `3` untuk keluar dari program.

---

## Output Contoh

```
===========================================
=           HARPIE AUTO SCANNER           =
===========================================
=       Channel : t.me/ugdairdrop         =
===========================================

✅ Loaded 2 address(es) from file:
1. 0x1111111111111111111111111111111111111111
2. 0x2222222222222222222222222222222222222222

===========================================
=               Main Menu                 =
===========================================
1. Add new address
2. Start scanning
3. Exit

👉 Enter your choice: 2
🚀 Starting scanner for 2 address(es)...
⏳ Scanning address 0x1111111111111111111111111111111111111111... ✅ Scan successful!
📊 Percent Immune: 100%
✅ Percent Verified: 100%
📈 Activity Score: 100
✅ No alerts detected.

⏳ Scanning address 0x2222222222222222222222222222222222222222... ✅ Scan successful!
✅ No alerts detected.

⏰ Next scan will run in:
⏳ 23h 59m 59s
...
```

---

## Catatan Penting
- **Alamat Ethereum**: Pastikan alamat Ethereum yang dimasukkan valid (dimulai dengan `0x` dan memiliki panjang 42 karakter).
- **File JSON**: Alamat yang ditambahkan akan disimpan dalam file `addresses.json`. Anda dapat membuka file ini untuk memeriksa atau mengedit alamat secara manual.
- **Resiko**: Script ini hanya alat bantu. Pengguna bertanggung jawab penuh atas penggunaan script ini.

---

## Kontribusi
Jika Anda ingin berkontribusi atau melaporkan bug, silakan buka issue atau pull request di repository ini.

---

## Lisensi
Proyek ini dilisensikan di bawah [MIT License](LICENSE).
