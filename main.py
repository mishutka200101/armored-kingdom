from anticaptcha import *


def main():
    while True:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Access-Control-Allow-Origin': '*',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # Already added when you pass json=
            # 'Content-Type': 'application/json',
            'DNT': '1',
            'Origin': 'https://armoredkingdom.com',
            'Pragma': 'no-cache',
            'Referer': 'https://armoredkingdom.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        json_data = {
            'type': 'Unlimited',
            'email': 'minima_9006@rambler.ru',
            'recaptchaToken': f'{process()}',
        }

        response = requests.post('https://api.armoredkingdom.com/linkdrop/api/emailNftUrl/', headers=headers,
                                 json=json_data, proxies=proxies)

        # if response.status_code == 200:
        #     print('Email sended')
        # else:
        #     print("ERROR, email not sended")
        print(response, response.text)


if __name__ == "__main__":
    main()
