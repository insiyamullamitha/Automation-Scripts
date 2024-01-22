from os import path, listdir
from shutil import move
from pathlib import Path

home_dir = path.expanduser("~")
target_folder = path.join(home_dir, "Downloads")

extensions = {
    'Images': ['.jpg', '.png', '.jpeg', '.gif', '.tiff', '.psd'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.webm'],
    'Music': ['.mp3', '.wav', '.ogg', '.flac', '.m4a'],
    'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.csv', '.rtf'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Applications': ['.exe', '.dmg', '.pkg', '.deb', '.msi'],
    'Programming': ['.py', '.java', '.c', '.cpp', '.h', '.js', '.css', '.html', '.php', '.xml', '.json', '.sql'],
    'Others': []
}

extension_types = [item for sublist in extensions.values() for item in sublist]

# Move files to their respective folders and create folder if not exists
for file in listdir(target_folder):
    file_path = path.join(target_folder, file)
    if path.isfile(file_path):
        file_type = "." + file.split('.')[-1]
        if file_type in extension_types:
            folder = next((key for key, values in extensions.items() if file_type in values), None)
            destination_folder = path.join(target_folder, folder)
            Path(destination_folder).mkdir(parents=True, exist_ok=True)
            move(file_path, path.join(destination_folder, file))

