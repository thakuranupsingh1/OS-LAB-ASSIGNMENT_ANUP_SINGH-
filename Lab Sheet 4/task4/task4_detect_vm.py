#!/usr/bin/env python3
# task4_detect_vm.py - detect virtual machine environment

import subprocess
import os

def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True).strip()
    except:
        return ""

def check_systemd():
    if os.path.exists("/usr/bin/systemd-detect-virt"):
        return run("systemd-detect-virt")
    return ""

def check_cpuinfo():
    if os.path.exists("/proc/cpuinfo"):
        data = open("/proc/cpuinfo").read()
        if "hypervisor" in data:
            return "hypervisor flag detected"
    return ""

def check_dmi():
    paths = [
        "/sys/class/dmi/id/sys_vendor",
        "/sys/class/dmi/id/product_name",
        "/sys/class/dmi/id/product_version"
    ]
    found = []
    for p in paths:
        if os.path.exists(p):
            value = open(p).read().lower()
            if any(x in value for x in ["virtual", "vmware", "kvm", "qemu", "hyper-v", "virtualbox"]):
                found.append(value.strip())
    return found

if __name__ == "__main__":
    print("VM Detection:")

    s = check_systemd()
    print("systemd:", s if s else "No result")

    c = check_cpuinfo()
    print("cpuinfo:", c if c else "No hypervisor flag")

    d = check_dmi()
    print("dmi:", d if d else "No VM strings found")

    if s or c or d:
        print("\n=> System is likely running inside a VM.")
    else:
        print("\n=> Likely not a VM.")
