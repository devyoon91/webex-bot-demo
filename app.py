import os

from webex_bot.commands.echo import EchoCommand
from webex_bot.webex_bot import WebexBot

access_token = os.getenv("WEBEX_TEAMS_ACCESS_TOKEN")
approved_rooms = ['8b6f5250-2e98-11ef-950d-13c0a7ecfeb4','ce68dea0-42e4-11ee-8b81-23be9471d215']


# BOT 개체 만들기
bot = WebexBot(teams_bot_token=access_token,
               approved_rooms=approved_rooms,
               bot_name="봇테스트",
               include_demo_commands=True)

# 봇이 수신 대기할 새 명령을 추가합니다.
bot.add_command(EchoCommand())

# 봇이 들어오는 메시지를 기다리도록 'run'을 호출합니다.
bot.run()
