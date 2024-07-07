FROM python:3.9.13

# 파이썬 패키지 업그레이드
RUN pip install --upgrade pip

# 작업 디렉터리 설정
WORKDIR /app

# 필요한 파일 복사
ADD requirements.txt /app

# 필요한 라이브러리 설치
RUN pip install -r requirements.txt

# 모든 소스 파일 등을 추가합니다.
ADD . /app

# 컨테이너 실행 시 실행할 명령어
CMD [ "python", "./app.py" ]
