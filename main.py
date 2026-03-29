#!/usr/bin/python3
# Devender Singh | 24BAI10183
# My OSS Course Project - Linux Audit

import os
import platform
import subprocess
from datetime import datetime

def print_line():
    print("-" * 45)

def get_sys_info():

    print("\n[1] System Report:")
    print(f"OS Name: {platform.system()}")
    print(f"Version: {platform.release()}")
    print(f"Logged in as: {os.getlogin()}")
    print(f"Time: {datetime.now().strftime('%H:%M:%S')}")

def check_git():

    print("\n[2] Git Check:")
    try:
        out = subprocess.check_output(['git', '--version']).decode().strip()
        print(f"Found: {out}")
    except:
        print("Git is not installed on this machine.")

def check_folders():
    # checking folder permissions for etc and tmp
    print("\n[3] Folder Audit:")
    for folder in ["/etc", "/tmp", "/home"]:
        if os.path.exists(folder):
            perm = oct(os.stat(folder).st_mode)[-3:]
            print(f"Folder: {folder} | Perms: {perm}")
        else:
            print(f"Skipping {folder} (not found)")

def my_manifesto():

    print("\n[4] My OSS Manifesto:")
    print("I'm Devender. I think sharing code is important for learning.")
    print("Open source is about working together.")

if __name__ == "__main__":
    while True:
        print_line()
        print("   DEVENDER'S AUDIT TOOL (24BAI10183)")
        print_line()
        print("1. System Info\n2. Git Check\n3. Audit Folders\n4. Manifesto\n5. Exit")
        
        user_input = input("\nPick an option: ")
        
        if user_input == '1': get_sys_info()
        elif user_input == '2': check_git()
        elif user_input == '3': check_folders()
        elif user_input == '4': my_manifesto()
        elif user_input == '5': 
            print("Closing tool...")
            break
        else: 
            print("Wrong input, try again.")
