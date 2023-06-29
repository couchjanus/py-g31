import json
import requests

result = requests.get('https://api.telegram.org/bot5917300614:AAGNx1fldIsc8_mt8zvb3l7I_ZXF1jeH1Sc/getMe')


print(result.json())