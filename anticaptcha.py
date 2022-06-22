import requests
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask

api_key = ''
url = 'https://armoredkingdom.com/'
client = AnticaptchaClient(api_key)
session = requests.Session()


def get_form_html():
    return session.get(url).text


def get_token(form_html):
    site_key = '6Lf7lXsgAAAAAK34WnPfX30hw78U4IUiR6RLXZ-G'
    task = NoCaptchaTaskProxylessTask(website_url=url, website_key=site_key)
    job = client.createTaskSmee(task, timeout=10 * 60)
    return job.get_solution_response()


def form_submit(token):
    return requests.post(url, data={"g-recaptcha-response": token}).text


def process():
    html = get_form_html()
    token = get_token(html)
    return token
