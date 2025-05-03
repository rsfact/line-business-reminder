import json
from fastapi import APIRouter, Request, Header, HTTPException
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage
import settings
import services


router = APIRouter()

line_bot_api = LineBotApi(settings.LINE_CH_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CH_SECRET)


@router.post("/message")
async def line_webhook(request: Request, x_line_signature: str = Header(None)):
    body_bytes = await request.body()
    body_str = body_bytes.decode('utf-8')
    body = json.loads(body_str)

    try:
        events = parser.parse(body_str, x_line_signature)
        print(json.dumps(body, indent=2))

        for event in events:
            if not isinstance(event, MessageEvent) or not isinstance(event.message, TextMessage):
                break
            user_id = event.source.user_id
            user_name = services.get_line_profile(user_id).get("displayName")
            message = event.message.text
            services.send_slack_notification(user_name, message)

        return {"message": "OK"}
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature")
    except Exception as e:
        raise Exception(f"{str(e)}")
