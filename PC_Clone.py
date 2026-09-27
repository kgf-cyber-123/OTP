import os
import sys
import asyncio
import subprocess

# ১. HWID পাওয়ার ফাংশন (অথবা আপনার নির্দিষ্ট HWID দিন)
def get_hwid():
    try:
        # Termux/Linux এর জন্য ডিভাইস ID বের করার কমান্ড
        cmd = "getprop ro.serialno || cat /sys/class/android_id/id"
        return subprocess.check_output(cmd, shell=True).decode().strip()
    except Exception:
        return "UNKNOWN_HWID"

hwid = get_hwid()

# ২. otp.so ফাইল লোড করে verify_auth চেক করা
try:
    import otp
except ImportError:
    print("[!] otp.so ফাইল পাওয়া যায়নি! দয়া করে git pull দিন।")
    sys.exit(1)

async def start_app():
    # .so ফাইলের verify_auth কল করা
    is_approved = await otp.verify_auth(hwid)
    if is_approved:
        print("[+] সিস্টেম ভেরিফাইড! মূল কাজ চালু হচ্ছে...")
        # এখানে আপনার পরবর্তী কোনো ফাংশন বা কোড থাকলে রান করতে পারেন

if __name__ == "__main__":

    try:
        asyncio.run(start_app())
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
