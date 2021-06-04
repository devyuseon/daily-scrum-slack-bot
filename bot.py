import requests
from datetime import date

def post_message(slack_token, channel_id, msg):
    url = "https://slack.com/api/chat.postMessage"

    data = {'Content-Type': 'application/x-www-form-urlencoded',
        'token': slack_token,
        'channel': channel_id, 
        'text': msg
        }
     
    res = requests.post(url, data = data)
    print(res)

def make_msg():
    today = date.today()
    today_str = str(today.year) + "년 " + str(today.month) + "월 " \
        + str(today.day) + "일 Daily Scrum 입니다."

    msg = today_str + """
    - 오늘까지 내가 완수한 일
    - 내일까지 내가 하기로 한 일
    - 현재 곤란하고 어려운 일
에 대해 이야기 해 봅시다 :)
    """
    return msg

 
if __name__ == '__main__':
    slack_token = "xoxb-1216424344742-2140205972420-yTXCNVAYqgBDTFvfqtPj8MQb"
    channel_id = "C016HP1059B"
    msg = "Hello"
    post_message(slack_token, channel_id, make_msg())