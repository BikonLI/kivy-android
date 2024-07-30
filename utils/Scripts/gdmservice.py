# Turn off/on the graphical interface
# 关闭图形化界面与启动图形化界面脚本
import sys
import time
import subprocess

options_dict = {
    "open": [['sudo', 'systemctl', 'set-default', 'graphical.target'], ['sudo', 'systemctl', 'enable', 'gdm']],
    "close": [['sudo', 'systemctl', 'set-default', 'multi-user.target'], ['sudo', 'systemctl', 'disable', 'gdm']],
}

def main(*args):
    
    if len(args) < 2:
        print("Invalid args")
        return -1
        
    try:
        complete_p1 = subprocess.run(options_dict[args[1]][0])
        complete_p2 = subprocess.run(options_dict[args[1]][1])
    except KeyError as e:
        print("Invalid args")
        return -1
    except Exception as e:
        print(f"{e}")
        return -2
    
    if complete_p1.returncode == 0 and complete_p2.returncode == 0:
        print("Success!")
        for i in range(3):
            print(f"\rReboot in {3 - i} seconds, 'ctrl + c' to shut down.", end='')
            time.sleep(1)
        subprocess.run(["sudo", "reboot"])
        return 0
    
    else:
        print("ERROR: Please retry")
        return -2
    

if __name__ == "__main__":
    main(*sys.argv)
    
