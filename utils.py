import os
import platform


def display_system_info():
    """Display system information including disk usage, memory, and uptime."""
    print("Current date and time:")
    os.system('date')
    
    # Check if we're on Windows and use appropriate commands
    if platform.system() == "Windows":
        print("\nDisk usage:")
        os.system("wmic logicaldisk get size,freespace,caption")
        print("\nMemory usage:")
        os.system("wmic OS get TotalVisibleMemorySize,FreePhysicalMemory /format:list")
        print("\nSystem uptime:")
        os.system("wmic os get lastbootuptime")
    else:
        # Unix/Linux commands
        print("\nDisk usage:")
        os.system("df -kh")
        print("\nMemory usage:")
        os.system("free")
        print("\nSystem uptime:")
        os.system("uptime")


if __name__ == "__main__":
    display_system_info()
