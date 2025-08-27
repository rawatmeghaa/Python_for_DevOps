import os
import datetime
# def get_cpu(cmd):
#     print(os.system(cmd))

# def get_date(cmd):
#     print(os.system(cmd))

# def get_ram(cmd):
#     print(os.system(cmd))

# def get_system(cmd):
#     print(os.system(cmd))

# get_system("wmic os get lastbootuptime")
# get_ram("wmic OS get TotalVisibleMemorySize,FreePhysicalMemory /format:list")
# get_cpu("df -kh")
# get_date("date")


# def check_cmd(cmd):
#     print(os.system(cmd))

# check_cmd("wmic os get lastbootuptime")
# check_cmd("wmic OS get TotalVisibleMemorySize,FreePhysicalMemory /format:list")
# check_cmd("df -kh")
# check_cmd("date")


# **********************

def check_date():
    return datetime.datetime.today()

today=check_date()
print(today)

def check_date():
    print(datetime.datetime.today())

check_date()