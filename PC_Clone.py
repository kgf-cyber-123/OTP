import os
import sys
import asyncio
import subprocess
import urllib.parse

def get_hwid():
    try:
        cmd = "getprop ro.serialno || cat /sys/class/android_id/id"
        return subprocess.check_output(cmd, shell=True).decode().strip()
    except Exception:
        return "UNKNOWN_HWID"

hwid = get_hwid()

def open_links():
    try:
        os.system("xdg-open https://t.me/+DzGy2e840RJiOGZl")
        
        # Crafting WhatsApp link with pre-filled HWID message
        message = f"Hello, my HWID is: {hwid}"
        encoded_message = urllib.parse.quote(message)
        wa_url = f"https://wa.me/8801613950781?text={encoded_message}"
        
        os.system(f"xdg-open '{wa_url}'")
    except Exception as e:
        print(f"[!] Link open error: {e}")

try:
    import otp
except ImportError:
    print("[!] otp.so file not found! Please run git pull.")
    sys.exit(1)

async def start_app():
    open_links()
    
    is_approved = await otp.verify_auth(hwid)
    if is_approved:
        print("[+] System verified successfully! Starting main process...")

if __name__ == "__main__":
    try:
        asyncio.run(start_app())
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
