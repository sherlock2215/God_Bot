import json
from wsgiref.validate import header_re

import requests
from config import API_KEY,API_URL

class god_kr:

    def __init__(self):
        self.api_key = API_KEY
        self.api_url = API_URL

    def ask(self,user_input):
        if not self.api_key:
            raise ValueError("API key is missing")

        headers={
            "Content-Type": "application/json",
            "X-goog-api-key": self.api_key
        }

        data={"contents":[
            {
                "parts":[
                    {
                        "text": f"You are Lord Krishna."
                                f"Answer wisely with wisdom. Just like krishna would.\n\n"
                                f"User:{user_input}"
                    }
                ]
            }
        ]}
        response = requests.post(self.api_url,headers=headers,data=json.dumps(data))

        if response.status_code!=200:
            return f"Error: {response.status_code}-{response.text}"

        try:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except Exception:
            return "Unexpected response format"

if __name__ == "__main__":
    bot=god_kr()
    print(bot.ask("Krishna, how should I deal with stress?"))