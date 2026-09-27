import os
import sys
import asyncio

try:
    import otp
except ImportError:
    print("[!] otp.so file not found! Please run git pull.")
    sys.exit(1)

if __name__ == "__main__":
    try:
        # async main() ফাংশনটিকে সরাসরি রান করার সঠিক উপায়
        asyncio.run(otp.main())
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
