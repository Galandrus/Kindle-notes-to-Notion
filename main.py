import json
from Services.file_system_service import FileSystemService
from Services.notion_service import NotionService
from Services.clip_service import ClipService

CLIP_PATH = "CLIP_PATH"
NOTION_SECRET_TOKEN = "NOTION_SECRET_TOKEN"
NOTION_MAIN_PAGE_ID = "NOTION_MAIN_PAGE_ID"
CONFIG = {
    CLIP_PATH: "",
    NOTION_SECRET_TOKEN: "",
    NOTION_MAIN_PAGE_ID: ""
}

def loadConfig():
    with open('config.json') as f:
        config = json.load(f)
    CONFIG[CLIP_PATH] = config[CLIP_PATH]
    CONFIG[NOTION_SECRET_TOKEN] = config[NOTION_SECRET_TOKEN]
    CONFIG[NOTION_MAIN_PAGE_ID] = config[NOTION_MAIN_PAGE_ID]

def main():
    loadConfig()
    file_system_service = FileSystemService(CONFIG[CLIP_PATH])
    notion_service = NotionService(CONFIG[NOTION_SECRET_TOKEN], CONFIG[NOTION_MAIN_PAGE_ID])
    clip_service = ClipService(notion_service)

    fileContent = file_system_service.getFileContent()
    file_system_service.backUpFile(fileContent)

    notes = clip_service.getNotes(fileContent)
    __deleteLastElement__ = notes.pop() #This is because the last element is empty

    unprocessedNotes = clip_service.processNotes(notes)
    file_system_service.saveUnprocessedNotes(unprocessedNotes)

main()
