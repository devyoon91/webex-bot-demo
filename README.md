# R5 Rbot

> Cisco Webex R5 Team Bot

## Installation

> docker, docker-compose 설치된 환경

- 처음 빌드 할때

```bash
$ git clone https://github.com/ecs-telecom/rbot.git
$ cd rbot
$ export WEBEX_TEAMS_ACCESS_TOKEN=YOUR_TOKEN
$ docker compose up -d
```

- 다시 배포 할때

```bash
$ cd rbot
$ export WEBEX_TEAMS_ACCESS_TOKEN=YOUR_TOKEN
$ docker compose up --build --force-recreate -d
```


## Reference
- [Webex Teams API](https://developer.webex.com/docs/api/getting-started)
- [github - webex_bot](https://github.com/fbradyirl/webex_bot)
- [github - webexteamssdk](https://github.com/WebexCommunity/WebexPythonSDK/tree/master)