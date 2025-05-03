import requests
import json
import settings
import os


def send_slack_notification(user_name, message):
    template_path = os.path.join("templates", "slack.txt")
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    content = template.format(
        user_name=user_name,
        message=message
    )

    response = requests.post(
        settings.SLACK_WEBHOOK_URL,
        data=json.dumps({
            "text": content
        }),
        headers={"Content-Type": "application/json"}
    )

    if response.status_code != 200:
        raise Exception(f"Slack通知の送信に失敗しました: ステータスコード {response.status_code}")

def get_line_profile(user_id):
    url = f"https://api.line.me/v2/bot/profile/{user_id}"
    headers = {
        "Authorization": f"Bearer {settings.LINE_CH_ACCESS_TOKEN}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"LINEプロファイルの取得に失敗しました: ステータスコード {response.status_code}")

    return response.json()
