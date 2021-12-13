"""Module Notion Service to interact with Notion API"""
from requests.structures import CaseInsensitiveDict
import requests


class NotionService():
    """Class to use Notion API"""
    secret_token = ''
    page_id = ''

    def __init__(self, secret_token, page_id):
        self.page_id = page_id
        self.secret_token = secret_token

    @staticmethod
    def notion_text(text, bold=False):
        """Function format a notion text block"""
        return {
            "type": "text",
            "text": {
                "content": text,
            },
            "annotations": {
                "bold": bold
            }
        }

    def post_clip_to_notion(self, book, reference, clip, clip_type):
        """Function to post clips into a notion page"""
        url = f"https://api.notion.com/v1/blocks/{self.page_id}/children"
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = f'Bearer {self.secret_token}'
        headers["Notion-Version"] = "2021-08-16"
        data = {
            "children": [
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "text": [
                            self.notion_text('Book: ', True),
                            self.notion_text(book),
                            self.notion_text('\nReference: ', True),
                            self.notion_text(reference),
                            self.notion_text(f'\n{clip_type}: ', True),
                            self.notion_text(clip)
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

        if resp.status_code != 200:
            print('An error occurred', resp.text)
            return False

        print('Note update successfully')
        return True
