#!/usr/bin/env python3
import requests
import socket
import sys

def get_cf_ips():
    """Ambil daftar IP resmi Cloudflare"""
    try:
        resp = requests.get("https://www.cloudflare.com/ips-v4")
        return set(resp.text.strip().splitlines())
    except:
        return set()

def resolve_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except:
        return None

def is_cloudflare(ip, cf_ips):
    return ip in cf_ips

def main(domain):
    cf_ips = get_cf_ips()
    ip = resolve_ip(domain)
    
    if not ip:
        print(f"[!] Gagal resolve {domain}")
        return

    print(f"[+] {domain} → {ip}")
    
    if is_cloudflare(ip, cf_ips):
        print("[⚠] Dilindungi Cloudflare")
        
        # Coba subdomain umum
        common_subs = ["direct", "origin", "dev", "staging", "test", "admin", "mail"]
        for sub in common_subs:
            test_domain = f"{sub}.{domain}"
            ip_sub = resolve_ip(test_domain)
            if ip_sub and not is_cloudflare(ip_sub, cf_ips):
                print(f"[✅] Origin ditemukan: {test_domain} → {ip_sub}")
                return
        
        print("[?] Coba metode lain: crt.sh, SecurityTrails, atau historical DNS")
    else:
        print("[✅] Tidak dilindungi Cloudflare — ini mungkin origin!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 cf-bypass.py <domain>")
        sys.exit(1)
    main(sys.argv[1])
