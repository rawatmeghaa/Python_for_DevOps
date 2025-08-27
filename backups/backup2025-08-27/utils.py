import os 
import platform

print(os.system('date'))
# Check if we're on Windows and use appropriate commands
if platform.system() == "Windows":
    print("Disk usage:")
    os.system("wmic logicaldisk get size,freespace,caption")
    print("\nMemory usage:")
    os.system("wmic OS get TotalVisibleMemorySize,FreePhysicalMemory /format:list")
    print("\nSystem uptime:")
    os.system("wmic os get lastbootuptime")
else:
    # Unix/Linux commands
    print("Disk usage:")
    os.system("df -kh")
    print("\nMemory usage:")
    os.system("free")
    print("\nSystem uptime:")
    os.system("uptime")
