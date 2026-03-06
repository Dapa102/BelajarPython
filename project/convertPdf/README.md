# DOCX to PDF Converter

Program sederhana untuk mengkonversi file DOCX (Microsoft Word) menjadi PDF.

## 📋 Daftar Isi
- [Fitur](#fitur)
- [Persyaratan Sistem](#persyaratan-sistem)
- [Instalasi](#instalasi)
  - [Windows](#windows)
  - [Linux](#linux)
- [Cara Penggunaan](#cara-penggunaan)
- [Troubleshooting](#troubleshooting)
- [Struktur Proyek](#struktur-proyek)

## ✨ Fitur
- Konversi file DOCX ke PDF
- Dukungan untuk Windows dan Linux
- Otomatis mendeteksi sistem operasi
- Interface sederhana dan mudah digunakan

## 💻 Persyaratan Sistem

### Windows
- Python 3.6 atau lebih tinggi
- Microsoft Word (sudah terinstall)

### Linux
- Python 3.6 atau lebih tinggi
- LibreOffice (untuk konversi)

## 📦 Instalasi

### Windows

1. **Install Python**
   - Download Python dari [python.org](https://www.python.org/downloads/)
   - Pastikan mencentang "Add Python to PATH" saat instalasi

2. **Clone atau download proyek ini**
   ```bash
   git clone <repository-url>
   cd convertPdf
   ```

3. **Install dependencies**
   ```bash
   pip install docx2pdf
   ```

4. **Pastikan Microsoft Word sudah terinstall**
   - Program ini memerlukan Microsoft Word untuk berfungsi di Windows

### Linux

1. **Install Python** (biasanya sudah terinstall)
   ```bash
   # Cek versi Python
   python3 --version
   
   # Jika belum ada, install:
   # Ubuntu/Debian
   sudo apt update
   sudo apt install python3 python3-pip
   
   # Fedora
   sudo dnf install python3 python3-pip
   
   # Arch
   sudo pacman -S python python-pip
   ```

2. **Clone atau download proyek ini**
   ```bash
   git clone <repository-url>
   cd convertPdf
   ```

3. **Install LibreOffice**
   ```bash
   # Ubuntu/Debian
   sudo apt update
   sudo apt install libreoffice
   
   # Fedora
   sudo dnf install libreoffice
   
   # Arch
   sudo pacman -S libreoffice-fresh
   ```

4. **Install dependencies Python**
   ```bash
   pip3 install docx2pdf
   ```

## 🚀 Cara Penggunaan

1. **Jalankan program**
   
   Windows:
   ```bash
   cd src
   python main.py
   ```
   
   Linux:
   ```bash
   cd src
   python3 main.py
   ```

2. **Masukkan path file DOCX**
   ```
   Masukkan path file DOCX (contoh: docs/contoh.docx): docs/mydocument.docx
   ```

3. **Masukkan path output PDF**
   ```
   Masukkan path file PDF (contoh: docs/contoh.pdf): pdf/mydocument.pdf
   ```

4. **Tunggu proses konversi selesai**
   ```
   ✅ Convert berhasil!
   ```

### Contoh Penggunaan

```bash
# Dari folder src
python main.py

# Input
Masukkan path file DOCX (contoh: docs/contoh.docx): ../docs/laporan.docx
Masukkan path file PDF (contoh: docs/contoh.pdf): ../pdf/laporan.pdf
```

## 🔧 Troubleshooting

### ❌ Error: "File DOCX tidak ditemukan!"

**Penyebab:** Path file yang dimasukkan salah atau file tidak ada.

**Solusi:**
1. Pastikan path file benar (gunakan path relatif atau absolute)
2. Cek apakah file benar-benar ada di lokasi tersebut
   ```bash
   # Linux/Mac
   ls -la path/ke/file.docx
   
   # Windows
   dir path\ke\file.docx
   ```
3. Gunakan path absolute jika masih error:
   - Windows: `C:\Users\YourName\Documents\file.docx`
   - Linux: `/home/username/documents/file.docx`

### ❌ Error: "LibreOffice tidak ditemukan" (Linux)

**Penyebab:** LibreOffice belum terinstall di sistem Linux.

**Solusi:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install libreoffice

# Fedora
sudo dnf install libreoffice

# Arch
sudo pacman -S libreoffice-fresh

# Verifikasi instalasi
libreoffice --version
```

### ❌ Error: "No module named 'docx2pdf'"

**Penyebab:** Package `docx2pdf` belum terinstall.

**Solusi:**
```bash
# Windows
pip install docx2pdf

# Linux
pip3 install docx2pdf

# Jika masih error, coba dengan --user flag
pip install --user docx2pdf
```

### ❌ Error: "Microsoft Word is not installed" (Windows)

**Penyebab:** Program memerlukan Microsoft Word untuk konversi di Windows.

**Solusi:**
1. Install Microsoft Word/Office
2. Alternatif: Gunakan WSL (Windows Subsystem for Linux) dan ikuti instruksi Linux
3. Alternatif lain: Gunakan aplikasi konversi online

### ❌ Error: Permission Denied saat save PDF

**Penyebab:** Tidak ada permission untuk menulis di folder tujuan.

**Solusi:**
```bash
# Linux - ubah permission folder
chmod 755 /path/to/output/folder

# Atau simpan di folder dengan write permission
# Misal: di home directory atau folder documents
```

### ❌ Error: "Gagal convert via LibreOffice" (Linux)

**Penyebab:** LibreOffice gagal memproses file atau file DOCX corrupt.

**Solusi:**
1. Coba buka file DOCX di LibreOffice Writer secara manual
2. Jika bisa dibuka, save as PDF dari menu File → Export as PDF
3. Jika file corrupt, coba buka dan perbaiki di Microsoft Word dulu
4. Pastikan LibreOffice versi terbaru:
   ```bash
   sudo apt update
   sudo apt upgrade libreoffice
   ```

### ❌ Error: "python/python3 tidak dikenali sebagai perintah"

**Penyebab:** Python belum terinstall atau tidak ada di PATH.

**Solusi:**

Windows:
1. Install Python dari [python.org](https://www.python.org/downloads/)
2. Centang "Add Python to PATH" saat instalasi
3. Restart Command Prompt
4. Verifikasi: `python --version`

Linux:
```bash
# Install Python
sudo apt install python3 python3-pip  # Ubuntu/Debian
sudo dnf install python3 python3-pip  # Fedora
sudo pacman -S python python-pip      # Arch

# Verifikasi
python3 --version
```

### ⚠️ File DOCX memiliki format kompleks (tabel, gambar, dll)

**Catatan:** Konversi mungkin tidak sempurna untuk dokumen dengan:
- Format kompleks
- Banyak gambar
- Tabel rumit
- Font khusus yang tidak terinstall

**Solusi:**
1. Buka file di aplikasi aslinya (MS Word/LibreOffice)
2. Export langsung ke PDF dari menu File → Export as PDF
3. Ini akan memberikan hasil terbaik untuk dokumen kompleks

### 📊 File PDF hasil konversi tidak sesuai harapan

**Solusi:**
1. Pastikan font yang digunakan di DOCX terinstall di sistem
2. Install font Microsoft di Linux:
   ```bash
   sudo apt install ttf-mscorefonts-installer
   ```
3. Untuk hasil terbaik di Linux, gunakan LibreOffice GUI:
   ```bash
   libreoffice --writer file.docx
   # Kemudian File → Export as PDF
   ```

## 📁 Struktur Proyek

```
convertPdf/
├── docs/              # Folder untuk file DOCX input
├── pdf/               # Folder untuk file PDF output
├── src/
│   ├── converter.py   # Modul konversi DOCX ke PDF
│   ├── main.py        # Program utama
│   └── __pycache__/   # Python cache (auto-generated)
└── README.md          # Dokumentasi ini
```

## 📝 Lisensi

Proyek ini bebas digunakan untuk keperluan pribadi dan komersial.

## 🤝 Kontribusi

Silakan buat pull request atau issue jika menemukan bug atau ingin menambah fitur.

## 📧 Kontak

Jika ada pertanyaan, silakan buat issue di repository ini.

---

**Selamat menggunakan! 🎉**
