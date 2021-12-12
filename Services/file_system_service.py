from datetime import datetime

class FileSystemService():
    clipPath = ''

    def __init__(self, clipPath):
        self.clipPath = clipPath

    def getFileContent(self):
        with open(self.clipPath, 'r', encoding='utf8') as f:
            lines = f.read()
        return lines

    def backUpFile(self, fileContent):
        date = datetime.now().strftime("%d-%m-%Y -- %H-%M-%S")
        with open(f'./backups/backup-note-{date}', 'w', encoding='utf8') as f:
            f.write(fileContent)
        print('File was cloned')

    def saveUnprocessedNotes(self, unprocessedNotes):
        with open(self.clipPath, 'w', encoding='utf8') as f:
            f.writelines(unprocessedNotes)