import os

from webex_bot.webex_bot import WebexBot

from commands.docs import DocumentCommand
from commands.help import HelpCommand

# 웹엑스 팀 액세스 토큰
access_token = os.getenv("WEBEX_TEAMS_ACCESS_TOKEN")
# 명령어 허용 룸 ID 목록
approved_rooms = ['8b6f5250-2e98-11ef-950d-13c0a7ecfeb4', 'ce68dea0-42e4-11ee-8b81-23be9471d215',
                  'd4999ef0-8006-11ed-96f9-f3cc6cafff26']

# BOT 개체 만들기
bot = WebexBot(teams_bot_token=access_token,
               approved_rooms=approved_rooms,
               bot_name="RBot",
               include_demo_commands=False)

# 봇이 수신 대기할 새 명령을 추가합니다.
bot.add_command(DocumentCommand())
bot.add_command(HelpCommand(bot_name="RBot",
                            bot_help_subtitle="RBot 명령어 목록을 확인하세요.",
                            bot_help_image="https://i.ibb.co/3pKv3dz/hong.jpg"))

# 봇이 들어오는 메시지를 기다리도록 'run'을 호출합니다.
bot.run()
