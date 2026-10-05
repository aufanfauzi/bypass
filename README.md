# Origin Hunter

Tools untuk membantu menemukan kemungkinan IP origin dari sebuah domain
yang dilindungi CDN/WAF.
## ⚠️ Disclaimer

Tools ini hanya untuk digunakan pada:
- Domain/website milik sendiri
- Lab pribadi yang dikontrol penuh
- Target bug bounty yang mengizinkan di scope

Penggunaan pada aset orang lain tanpa izin tertulis adalah **ilegal**
dan melanggar UU ITE Pasal 30 & 46.

## Fitur
- Cek DNS history
- Cek certificate transparency (crt.sh)
- Enumerasi subdomain
- Verifikasi IP kandidat dengan Host header
- Bandingkan konten (hash) IP kandidat vs domain asli

## Instalasi
```bash
git clone https://github.com/USERNAME/origin-hunter.git
cd origin-hunter
pip install -r requirements.txt
