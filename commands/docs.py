import logging
import os
from pathlib import Path

from webex_bot.models.command import Command
from webex_bot.models.response import Response

log = logging.getLogger(__name__)


class DocumentCommand(Command):

    def __init__(self):
        super().__init__(
            command_keyword="docs",
            help_message="문서 모음")

    def pre_execute(self, message, attachment_actions, activity):
        """
        (optional function). execute 함수를 실행하기 전에 실행되는 함수.
        :param message:
        :param attachment_actions:
        :param activity:
        :return:
        """
        log.info(f"pre_execute: {message}")
        pass

    def execute(self, message, attachment_actions, activity):
        """
        명령어 수행 시 실행되는 함수.
        :param message:
        :param attachment_actions:
        :param activity:
        :return:
        """
        # text1 = TextBlock("문서 모음", weight=FontWeight.BOLDER, size=FontSize.MEDIUM)
        # text2 = TextBlock("Type in something here and it will be echo'd back to you. How useful is that!",
        #                   wrap=True, isSubtle=True)
        # input_text = Text(id="message_typed", placeholder="Type something here", maxLength=30)
        # input_column = Column(items=[input_text], width=2)
        #
        # card = AdaptiveCard(
        #     body=[ColumnSet(columns=[Column(items=[text1, text2], width=2)]),
        #           ColumnSet(columns=[input_column]),
        #           ])
        #
        with open('commands/docs_table.md', 'r', encoding='utf-8') as f:
            documents = f.read()
        return documents

