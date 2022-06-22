from anticaptcha import *
import time


def generate_email():
    email = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox').text.replace('[', '').replace(']', '').replace('"', '')
    return email


def main():
    print("Work started, prepare to get money $$$")
    while True:
        email = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox').text.replace('[', '').replace(
            ']', '').replace('"', '')
        login, domain = email.split('@')
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
            'email': email,
            'recaptchaToken': process(),
        }

        response = requests.post('https://api.armoredkingdom.com/linkdrop/api/emailNftUrl/', headers=headers,
                                 json=json_data)

        time.sleep(20)
        try:
            mailbox = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}')
            mail_id = mailbox.json()[0]['id']
            read_mail = requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}'
                                     f'&id={mail_id}')
            dict = read_mail.json()['body'].split(' ')
            for i in dict[::-1]:
                if str(i).__contains__('https://u12149045.ct.sendgrid.net/ls/click?'):
                    url = str(i).split('"')[1]
                    response = requests.get(url)
                    if response.url == 'https://armoredkingdom.com/':
                        raise Exception
                    else:
                        with open('mint_urls.txt', 'a') as file:
                            file.write(f'{url}\n')
                        print('URL to claim was writen to "mint_urls.txt"')
                    break
        except Exception:
            print('Email not received or url not to claim... Retrying...')


if __name__ == "__main__":
    main()
