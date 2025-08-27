import os
import datetime
import shutil

def backup_files(source , destination):
    today = datetime.date.today()
    backup_file_name= os.path.join(destination, f"backup{today}")
    print(backup_files)
    shutil.make_archive(backup_file_name , 'zip', source)


source = r"C:\Users\Megha.rawat\Downloads\MEGHA\PROJECT\PYTHON"
destination= r"C:\Users\Megha.rawat\Downloads\MEGHA\PROJECT\PYTHON\backups"

backup_files(source , destination)