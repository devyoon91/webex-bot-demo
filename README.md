# R5 Rbot

> Cisco Webex R5 Team Bot

## Installation

> docker, docker-compose 설치된 환경

```bash
$ git clone https://github.com/ecs-telecom/rbot.git
$ cd rbot
$ docker build -t rbot:v1 . 
$ docker image inspect rbot:v1
$ docker run -d --name rbot -e WEBEX_TEAMS_ACCESS_TOKEN=YOUR_TOKEN rbot:v1

```