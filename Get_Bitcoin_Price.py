from bs4 import BeautifulSoup
import requests
import time

# https://www.google.com/search?q=ethereum+price&rlz=1C5CHFA_enUS719US744&sxsrf=ALiCzsYvuzCgA6aH6nqIVacQ1gRFFv_3Yg%3A1653710478081&ei=jp6RYpPMBMaxkvQP2KmxkAE&ved=0ahUKEwiTy-3Mp4H4AhXGmIQIHdhUDBIQ4dUDCA4&uact=5&oq=ethereum+price&gs_lcp=Cgdnd3Mtd2l6EAMyDwgAELEDEIMBEEMQRhCCAjIKCAAQsQMQgwEQQzIKCAAQsQMQgwEQQzIECAAQQzIKCAAQsQMQgwEQQzILCAAQgAQQsQMQgwEyCggAELEDEIMBEEMyCggAELEDEIMBEEMyBAgAEEMyBAgAEEM6BwgAEEcQsAM6BwgAELADEEM6BggAEB4QBzoICAAQsQMQkQI6CwgAELEDEIMBEJECSgQIQRgASgQIRhgAUOoGWIMSYNsTaAJwAXgAgAFZiAGYBJIBATiYAQCgAQHIAQrAAQE&sclient=gws-wiz
# chainlink uniswap link: https://info.uniswap.org/#/tokens/0x514910771af9ca656af840dff83e8264ecf986ca
# chainlink sushiswap link: https://app.sushi.com/analytics/tokens/0x514910771af9ca656af840dff83e8264ecf986ca?chainId=1
# apecoin uniswap link: https://info.uniswap.org/#/tokens/0x4d224452801aced8b2f0aebe155379bb5d594381
# apecoin sushiswap link: https://app.sushi.com/analytics/tokens/0x4d224452801aced8b2f0aebe155379bb5d594381?chainId=1
# aave uniswap link: https://info.uniswap.org/#/tokens/0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9
# aave sushiswap link: https://app.sushi.com/analytics/tokens/0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9?chainId=1
url = 'https://www.google.com/search?q=bitcoin+price&rlz=1C5CHFA_enUS719US744&sxsrf=ALiCzsagui9AnvfHa05wTgM3AltvmxnPSg%3A1653710349799&ei=DZ6RYvypMMWHwbkPsIOziA8&oq=bitcoin&gs_lcp=Cgdnd3Mtd2l6EAMYADIPCAAQsQMQgwEQQxBGEIICMgoIABCxAxCDARBDMgoIABCxAxCDARBDMgoIABCxAxCDARBDMgoIABCxAxCDARBDMgoIABCxAxCDARBDMgoIABCxAxCDARBDMgQIABBDMgcIABCxAxBDMgcIABCxAxBDOgcIABBHELADOgcIABCwAxBDOgoIABDkAhCwAxgBOhIILhDHARDRAxDIAxCwAxBDGAI6BAgjECc6EQguEIAEELEDEIMBEMcBEKMCOgUIABCABEoECEEYAEoECEYYAVC4CFjlEWC3G2gDcAF4AIABRIgBmAOSAQE3mAEAoAEByAERwAEB2gEGCAEQARgJ2gEGCAIQARgI&sclient=gws-wiz'

HTML = requests.get(url)

soup = BeautifulSoup(HTML.text, 'html.parser')
print(soup.prettify())
# <div class="BNeawe iBp4i AP7Wnd">
# Create a function to get price of crypto

def get_crypto_price(coin):
    # https://www.google.com/search?q=ethereum+price&rlz=1C5CHFA_enUS719US744&sxsrf=ALiCzsYvuzCgA6aH6nqIVacQ1gRFFv_3Yg%3A1653710478081&ei=jp6RYpPMBMaxkvQP2KmxkAE&ved=0ahUKEwiTy-3Mp4H4AhXGmIQIHdhUDBIQ4dUDCA4&uact=5&oq=ethereum+price&gs_lcp=Cgdnd3Mtd2l6EAMyDwgAELEDEIMBEEMQRhCCAjIKCAAQsQMQgwEQQzIKCAAQsQMQgwEQQzIECAAQQzIKCAAQsQMQgwEQQzILCAAQgAQQsQMQgwEyCggAELEDEIMBEEMyCggAELEDEIMBEEMyBAgAEEMyBAgAEEM6BwgAEEcQsAM6BwgAELADEEM6BggAEB4QBzoICAAQsQMQkQI6CwgAELEDEIMBEJECSgQIQRgASgQIRhgAUOoGWIMSYNsTaAJwAXgAgAFZiAGYBJIBATiYAQCgAQHIAQrAAQE&sclient=gws-wiz
    url = 'https://www.google.com/search?q='+coin+'+price&rlz=1C5CHFA_enUS719US744&sxsrf=ALiCzsagui9AnvfHa05wTgM3AltvmxnPSg%3A1653710349799&ei=DZ6RYvypMMWHwbkPsIOziA8&oq=bitcoin&gs_lcp=Cgdnd3Mtd2l6EAMYADIPCAAQsQMQgwEQQxBGEIICMgoIABCxAxCDARBDMgoIABCxAxCDARBDMgoIABCxAxCDARBDMgoIABCxAxCDARBDMgoIABCxAxCDARBDMgoIABCxAxCDARBDMgQIABBDMgcIABCxAxBDMgcIABCxAxBDOgcIABBHELADOgcIABCwAxBDOgoIABDkAhCwAxgBOhIILhDHARDRAxDIAxCwAxBDGAI6BAgjECc6EQguEIAEELEDEIMBEMcBEKMCOgUIABCABEoECEEYAEoECEYYAVC4CFjlEWC3G2gDcAF4AIABRIgBmAOSAQE3mAEAoAEByAERwAEB2gEGCAEQARgJ2gEGCAIQARgI&sclient=gws-wiz'

    HTML = requests.get(url)

    soup = BeautifulSoup(HTML.text, 'html.parser')
    #find the current price
    text = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'} ). find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    return text
price = get_crypto_price('bitcoin')
print(price)

#create a function to consistently show the price of the cryptocurrency when it changes
def main():
    last_price = -1
    crypto = 'bitcoin'
    price = get_crypto_price(crypto)
    while price != last_price:
        time.sleep(2)
        print(crypto+' price: ', price)
main()







