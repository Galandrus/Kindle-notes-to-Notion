import requests
from requests.structures import CaseInsensitiveDict

class NotionService():
    secret_token = ''
    page_id = ''

    def __init__(self, secret_token, page_id):
        self.page_id = page_id
        self.secret_token = secret_token

    def notionText(self, text, bold = False):
        return {
            "type": "text",
            "text": {
                "content": text,
            },
            "annotations": {
                "bold": bold
            }
        }

    def postNoteToNotion(self, book, clip, clipType):
        url = f"https://api.notion.com/v1/blocks/{self.page_id}/children"
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = f'Bearer {self.secret_token}'
        headers["Notion-Version"] = "2021-08-16"
        data={
            "children": [
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "text": [
                            self.notionText('Book: ', True),
                            self.notionText(book),
                            self.notionText(f'\n{clipType}: ', True),
                            self.notionText(clip)
                        ],
                    }
                },
                {
                    "type": "divider",
                    "divider": {}
                }
            ]
        }

        resp = requests.patch(url, headers=headers, json=data)

        if (resp.status_code != 200):
            print('An error occurred', resp.text)
            return False

        print('Note update successfully')
        return True