from GMailClient import GMailClient
import requests
from pprint import pprint
import urllib
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import DriverManager as FirefoxDriverManager
from selenium_stealth import stealth

import time


base_url = 'https://gmail.googleapis.com'

oauth_url = 'https://accounts.google.com/o/oauth2/auth/oauthchooseaccount?'

oauth2_url = 'https://stackoverflow.com/users/login'


def get_oauth_test_token(client):

    query_string = {''}

def get_oauth2_token_stack(client):

    try:
        br = webdriver.Firefox(FirefoxDriverManager().install())
    except Exception as e:
        try:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("user-agent=DN")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            br = webdriver.Chrome(ChromeDriverManager().install(),options=options)
            stealth(br,
                    languages=["en-US", "en"],
                    vendor="Google Inc.",
                    platform="Win32",
                    webgl_vendor="Intel Inc.",
                    renderer="Intel Iris OpenGL Engine",
                    fix_hairline=True,
                    )
        except Exception as e:
            return None

    #br.get('https://accounts.google.com/signin/oauth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&as=JS6BM8cjL-8j9votansdkw&destination=https%3A%2F%2Fstackauth.com&approval_state=!ChRoYWVvLUlNMk5hSXJWUGlaSVl2WBIfc3lSa0lueENpb29lSU5vbEVpbVNxcUZGaGNkSEJoYw%E2%88%99AJDr988AAAAAXlBKc7PzEomxSzgNqd4wLptVlf0Ny3Qx&oauthgdpr=1&xsrfsig=ChkAeAh8T8JNDxCf2Zah5fb_rQ55OMiF8KmMEg5hcHByb3ZhbF9zdGF0ZRILZGVzdGluYXRpb24SBXNvYWN1Eg9vYXV0aHJpc2t5c2NvcGU&flowName=GeneralOAuthFlow')

    br.get('https://stackoverflow.com/')
    time.sleep(2)
    br.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a[1]').click()
    time.sleep(0.5)
    br.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/button[1]').click()
    time.sleep(0.5)
    br.find_element_by_id('Email').send_keys(client.userId)
    #print(Fore.YELLOW + ' SENT EMAIL LOGIN ')
    time.sleep(0.5)
    br.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/form/div/div/input').click()
    time.sleep(0.5)
    br.find_element_by_id('password').send_keys(client.password)
    #print(Fore.YELLOW + time_format() + ' SENT PASSWORD LOGIN ')
    br.find_element_by_id('submit').click()
    #print(Fore.BLUE + ' SUCCESSFULLY LOGGED IN ')
    logged = True




def get_oauth_2_token(client):

    try:
        br = webdriver.Firefox(FirefoxDriverManager().install())
    except Exception as e:
        try:
            br = webdriver.Chrome(ChromeDriverManager().install())
        except Exception as e:
            return None

    query_string = {'response_type': 'permission id_token',
                    'scope': client.convert_scopes(),
                    'redirect_uri': client.redirect_uri,
                    'client_id': client.client_id,
                    'ss_domain': client.redirect_uri,
                    'gsiwebsdk': 'shim',
                    'flowName': 'GeneralOAuthFlow'
                    }

    url = oauth_url + urllib.parse.urlencode(query_string)

    br.get(url)
    
    br.find_element_by_id('identifierId').send_keys(client.userId)

    #river.find_element_by_xpath("//input[@type='submit' and @value='something']").click()

    br.find_element_by_id("identifierNext").click()

    response = requests.get(url,params=query_string).json()

    pprint(response)







def get_gmail_profile(client):

    headers= {'Authorization' : 'Bearer : {}'.format(client.token)}

    url = base_url + '/gmail/v1/users/{}/profile'.format(client.userId)

    response = requests.get(url)

    pprint(response)


def stop_profile_receiving_push_notifications(client):

    headers = {'Authorization' : 'Bearer : {}'.format(client.token)}

    url = base_url + '/gmail/v1/users/{}/stop'.format(client.userId)

    response = requests.post(url,headers=headers)

    pprint(response)

def set_or_update_user_notification(client):

    headers = {'Authorization': 'Bearer : {}'.format(client.token)}

    url = base_url + '/gmail/v1/users/{}/watch'.format(client.userId)

    response = requests.post(url,headers=headers)

    pprint(response)


"""

    USERS.DRAFTS API    


"""


def create_draft_metadata(client):

    headers = {'Authorization': 'Bearer : {}'.format(client.token)}

    url = base_url + '/gmail/v1/users/{}/drafts'.format(client.userId)

    response = requests.post(url,headers=headers)

    pprint(response)



def create_draft_media(client):

    headers = {'Authorization': 'Bearer : {}'.format(client.token)}

    url = base_url + '/upload/gmail/v1/users/{}/drafts'.format(client.userId)

    response = requests.post(url,headers=headers)

    pprint(response)


def delete_draft(client):

    headers = {'Authorization': 'Bearer : {}'.format(client.token)}

    url = base_url + '/gmail/v1/users/{}/drafts/{}'.format(client.userId,client.draft_credentials.draft_id)

    response = requests.delete(url,headers=headers)

    pprint(response)


def get_draft(client):

    headers = {'Authorization': 'Bearer : {}'.format(client.token)}

    url = base_url + '/gmail/v1/users/{}/drafts/{}'.format(client.userId,client.draft_credentials.draft_id)

    response = requests.get(url,headers=headers)

    pprint(response)


def list_drafts(client):

    headers = {'Authorization': 'Bearer : {}'.format(client.token)}

    url = base_url + '/gmail/v1/users/{}/drafts'.format(client.userId)

    response = requests.get(url,headers=headers)

    pprint(response)


def send_draft_media(client):

    headers = {'Authorization': 'Bearer : {}'.format(client.token)}

    url = base_url + '/upload/gmail/v1/users/{}/drafts/send'.format(client.userId)

    response = requests.post(url,headers=headers)

    pprint(response)


def send_draft_metadata(client):

    headers = {'Authorization': 'Bearer : {}'.format(client.token)}

    url = base_url + '/gmail/v1/users/{}/drafts/send'.format(client.userId)

    response = requests.post(url,headers=headers)

    pprint(response)








if __name__ == '__main__':
    client = GMailClient('examplemail@gmail.com')
    client.token = 'KEW-SS-mdIw1TSCJUb6D8tXo'
    client.scopes.append('https://mail.google.com')
    client.scopes.append('https://www.googleapis.com/auth/gmail.compose')
    client.scopes.append('https://www.googleapis.com/auth/gmail.metadata')
    client.scopes.append('https://www.googleapis.com/auth/gmail.modify')
    client.scopes.append('https://www.googleapis.com/auth/gmail.readonly')
    client.redirect_uri = 'http://localhost:8888/callback/'
    pprint(client.draft_credentials.draft_id)

    client.client_id = '810912613065-6gvc11044kn505hlk8srfuiroh7sipgd.apps.googleusercontent.com'
    client.ss_domain = 'http://localhost:8888/callback/'
    
    get_oauth2_token_stack(client)
    
    get_oauth_2_token(client)

    get_gmail_profile(client)