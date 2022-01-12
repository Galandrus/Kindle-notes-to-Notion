"""Module Main"""
import json
import os.path
from services.file_system_service import FileSystemService
from services.notion_service import NotionService
from services.clip_service import ClipService

CLIP_PATH = "CLIP_PATH"
NOTION_SECRET_TOKEN = "NOTION_SECRET_TOKEN"
NOTION_MAIN_PAGE_ID = "NOTION_MAIN_PAGE_ID"
CONFIG = {
    CLIP_PATH: "",
    NOTION_SECRET_TOKEN: "",
    NOTION_MAIN_PAGE_ID: ""
}
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

def load_config():
    """Function load config variables"""
    config_file_path = PROJECT_PATH + '/config.json'
    with open(config_file_path, 'r') as file:
        config = json.load(file)
    CONFIG[CLIP_PATH] = config[CLIP_PATH]
    CONFIG[NOTION_SECRET_TOKEN] = config[NOTION_SECRET_TOKEN]
    CONFIG[NOTION_MAIN_PAGE_ID] = config[NOTION_MAIN_PAGE_ID]


def main():
    """Main program"""
    load_config()
    file_system_service = FileSystemService(CONFIG[CLIP_PATH], PROJECT_PATH)
    notion_service = NotionService(
        CONFIG[NOTION_SECRET_TOKEN], CONFIG[NOTION_MAIN_PAGE_ID])
    clip_service = ClipService(notion_service)

    file_content = file_system_service.get_file_content()
    file_system_service.backup_file(file_content)

    notes = clip_service.get_notes(file_content)
    # This is because the last element is empty
    notes.pop()

    unprocessed_notes = clip_service.process_notes(notes)
    file_system_service.save_unprocessed_notes(unprocessed_notes)


main()
