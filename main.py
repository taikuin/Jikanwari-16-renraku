#モジュールのインポート
import requests

import cv2
import numpy as np

import time

#Notifyの定義
TOKEN = 'Notifyのアクセストークン'
api_url = 'https://notify-api.line.me/api/notify'
send_contents = '時間割が更新されました。スプレッドシート：https://docs.google.com/spreadsheets/d/128mFFj6w1drdDzxsKsoc9Xdba2FEWSffcM2iUSrnZ0c/edit?usp=sharing'
TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN} 
send_dic = {'message': send_contents}

#スプレッドシートのアイコン取得
img_url ='https://lh3.googleusercontent.com/fife/AAbDypBC_t8nxKsmIxBgoWVndw9tANplRT9g8fjO7FaVVt19m6Y4cogvkpBSeVWBjmJTX6Au3lOOy2DfHiO24tX9dlCW6LOxSkb9JVL-MkiqDcDcng_weogF0eugqPD355-q00FjkjT5A0Z8Bqa_I0EAr7vNm_6XAD6ss7WCgf0vOYF0UOO4FqQaedd9AVX-saMrr3SB65rweC_DpAS4Q7dB5AI4R5k0wkar9F6EnZipxhv2e4JFwIpLSKHgQUR9PvMH_TvfCsCHq4OTrYAak6jLRqraxBpmBBRsndfQHTAAZ3abLdmttmw3fnnEVQtTUeGGAk1mhcvAtsYwpdMKhi8Alvv9sKpHs1xQQSXP7cIvf8zBZWENEoFrfhan6_sUfKNDvlQUAnqw5_ounJil44l5AAGQX_qCOjQk7q2NugkFmS6UA_9qgq0585xTZ74va722yF4mLYouUZuPnWD7hZEx-KeyNBlQUxEr3zs96S3weJgaERG6LfdIPZxf5xRjFAe-fq-Sd5YyNzVqYtUFcUXz0Hj3L0rQTAh6Beupc-zO-jUfS3-90ZNZRUAcPmP68IQf6lc9CEbdyM-ekAErL2DEnhRXg_bBDVciGcVrHeUC7wFW8-fjRzoRWdQ_ux17HRkQ_Fmx2SCTZ8umnCH3xWv6LVJUgjtwHLJ8ORUEflx42m5whv_yMWLOYwxwR_2tlnIDUtB8319HXqZ3W7dAM1qLCBqTn-DGVXJvTV7AZpj4w9Dp7GbIVeIKfDIDhDyEmIo4XgGFKrtgjswNx4dMGnFCue5jHGUfc7b6xHajD-esRqw5pefRVVy8cgkL_q7F8iWGlBJ11ZUp_Ulwe74dc3ob3R-DWCUX8lfdtgzijVMi85pRskIKrqnSAOLMyglJyFZToEH-yKYbTPDXT048GJHLpinTh7fUgkqpDf_6TBy2Ewa8ob7jmZn8PDGiftR1jt-2gKuwpRJHPl-wJCuAJEztfrfiSRI8abKxEemHT1NmNNnILp6Prdx4Z7P5J53k2HAGiHjfYQ1q6eBoCfkORFye4zbpxNI34cGaF1XznyFJ_aitsQZW59CX7isWCYJMuHXFCyl_gGIl4qPCC2coXEVnkGJMzVleGtlmMP6wV6kFE5iIcuzN8fRU-xsodYV--iipwKr6K9yOzSuxzoEYao-WqY6-z_AIY11k8pw59za1NMitQChCRWmVPxQt_EV8MWduNclZm-JmhN_KUIfSOeg0r7jCx_rJkgt-1f62qLFrbI-xLxlEMs75cyRufWARihRmJ9miOB76eRvYHSeQvGx7d-XzjUv6rxZZVZWriguR9hLezHmBKxGZuBRFieiiUhRo9GCj1f0bmp5PLJA82ujsbU6lmQnaSGluW__TK0SwQ9TCJ0YnGrthEgkV-Rj8RJIVFhfuPyy8o6iQVLMf_T2theYGBoUB031UUem-tfCCrJl0BA0trhn5XjNsecjCZEjeTGvsLbEffDQ-BpRnrmnCRDIuxxEXgpw3rWkjRSM-CKgeUtRqN6XVE9uSuyEzVZ5MnIp0bCiak76ZKB5cs0APcpAn_rAK3EFYg3AYEkRKUQ-KCmHPTKmohEuNI0WSr-aUt5s86hMS1IQGHb4vYOgxSLSOceABjiIZDUS2dGGMsVWwl_ovbvYvFeAhgd6x-IFoT2I0zsVGPW_IK8yZACX4MpgpYHsgFb1TR_G2wlWCvjovD18=w416-h312-p'
response = requests.get(img_url)
image = response.content
file_name = "new.png"

with open(file_name, "wb") as f:
    f.write(image)

#現在の取得したアイコンの要素
img_diff_new = cv2.imread("new.png", cv2.IMREAD_GRAYSCALE)
whitePixels_new = np.count_nonzero(img_diff_new)
blackPixels_new = img_diff_new.size - whitePixels_new
element_new = whitePixels_new / img_diff_new.size * 100

#古いアイコンの要素
img_diff_old = cv2.imread("old.png", cv2.IMREAD_GRAYSCALE)
whitePixels_old = np.count_nonzero(img_diff_old)
blackPixels_old = img_diff_old.size - whitePixels_old
element_old = whitePixels_old / img_diff_old.size * 100

#アイコンの変化を認識
if element_new == element_old:
    print('変化なし')
else:
    image_file = 'new.png'
    binary = open(image_file, mode='rb')
    image_dic = {'imageFile': binary}
    requests.post(api_url, headers=TOKEN_dic, data=send_dic, files=image_dic)
    time.sleep(5)
    file_name2 = "old.png"
    with open(file_name2, "wb") as f:
        f.write(image)
    print('変化あり')
