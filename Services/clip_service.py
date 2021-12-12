"""Module to use notion service"""
from services.notion_service import NotionService

CLIP_SEPARATOR = '=========='
HIGHLIGHT_IDENTIFIER = '- La subrayado'
NOTE_IDENTIFIER = '- La nota'
HIGHLIGHT_TYPE = 'Highlight'
NOTE_TYPE = 'Note'
MARK_TYPE = 'Mark'


class ClipService():
    """Class to process notes"""
    notion_service: NotionService = NotImplemented

    def __init__(self, notion_service):
        self.notion_service = notion_service

    def get_notes(self, file_content):
        """Function to get separated notes from the content of a file"""
        notes = file_content.split(CLIP_SEPARATOR)
        return notes

    def process_notes(self, notes):
        """Function to process the notes and post to notion"""
        unprocessed_notes = []

        for note in notes:
            filer_note = list(filter(None, note.splitlines()))
            book = filer_note[0]
            context = filer_note[1]

            if context.startswith(HIGHLIGHT_IDENTIFIER):
                clip_type = HIGHLIGHT_TYPE
            elif context.startswith(NOTE_IDENTIFIER):
                clip_type = NOTE_TYPE
            else:
                print('Mark Clip - Not processed')
                unprocessed_notes.append(note)
                continue

            clip = filer_note[2]

            response = self.notion_service.postNoteToNotion(
                book, clip, clip_type)
            if not response:
                unprocessed_notes.append(note)

        return unprocessed_notes
