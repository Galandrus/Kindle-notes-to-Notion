from Services.notion_service import NotionService

CLIP_SEPARATOR = '=========='
HIGHLIGHT_IDENTIFIER = '- La subrayado'
NOTE_IDENTIFIER = '- La nota'
HIGHLIGHT_TYPE = 'Highlight'
NOTE_TYPE = 'Note'
MARK_TYPE = 'Mark'

class ClipService():
    notion_service: NotionService = NotImplemented

    def __init__(self, notion_service):
        self.notion_service = notion_service

    def getNotes(self, fileContent):
        notes = fileContent.split(CLIP_SEPARATOR)
        return notes


    def processNotes(self, notes):
        unprocessedNotes = []

        for note in notes:
            filerNote =  list(filter(None, note.splitlines()))
            book = filerNote[0]
            context = filerNote[1]

            if context.startswith(HIGHLIGHT_IDENTIFIER): clipType = HIGHLIGHT_TYPE
            elif context.startswith(NOTE_IDENTIFIER): clipType = NOTE_TYPE
            else:
                print('Mark Clip - Not processed')
                unprocessedNotes.append(note)
                continue

            clip = filerNote[2]

            response = self.notion_service.postNoteToNotion(book, clip, clipType)
            if not response: unprocessedNotes.append(note)

        return unprocessedNotes