"""Module to use datetime"""
from datetime import datetime


class FileSystemService():
    """Class with function about file functions"""
    clip_path = ''

    def __init__(self, clip_path):
        self.clip_path = clip_path

    def get_file_content(self):
        """Function to get the content of a file"""
        with open(self.clip_path, 'r', encoding='utf8') as file:
            lines = file.read()
        return lines

    def backup_file(self, file_content):
        """Function to save the file content in other file"""
        date = datetime.now().strftime("%d-%m-%Y -- %H-%M-%S")
        with open(f'./backups/backup-note-{date}', 'w', encoding='utf8') as file:
            file.write(file_content)
        print('File was cloned')

    def save_unprocessed_notes(self, unprocessed_notes):
        """Function overwrite the file with the unprocessed notes"""
        with open(self.clip_path, 'w', encoding='utf8') as file:
            file.writelines(unprocessed_notes)
