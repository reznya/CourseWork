from main import Variables
def ydisk_backup():
    Variables.disk.upload("5 курс/Курсач/Курсовая/logs/logs.txt", "/logs.txt", overwrite = True)
    # Variables.disk.upload("5 курс/Курсач/Курсовая/logs/logs.txt", "/logs.txt", overwrite = True)
    Variables.disk.upload("5 курс/Курсач/Курсовая/hashes/files_hashes.json", "/backup_hashes.json", overwrite = True)