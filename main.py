import base64

import requests

import cv2
import numpy as np

import time


def hello_pubsub(event, context):
  TOKEN = 'K4xJ3pnAMlsS8miF1qSM3jnKG3sCs453OEzakNn4llR'
  api_url = 'https://notify-api.line.me/api/notify'
  send_contents = '時間割が更新されました。'
  TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN} 
  send_dic = {'message': send_contents}
  time.sleep(3)

  img_url = 'https://lh3.googleusercontent.com/fife/AAbDypDcJB3vl5myOW9j29BCbxkueRq0wYNWrp05cNUe_tBNIA1uFbKfpmvXS7-fS9wHmScEzOfQv2vSP1xkcU1-6h80IVSSAy8JJY0gI7ipCspiWLPdUw6XSDNRLWh7mfdS_boINCweVzPNZLsiaTM05LSbzhn2N5L3lu66cT3sbX9A-89zZCOduemTiW_2W74i2aes3RwSx9vivVdtavDYv--ZdSTRCNzMJNqYcS8wOredqVPm7itMNbZ-PysHmFXLNl7XeOh7HEGBFmLOaArk6cq6iEIntNviu_-MdvvXmOqniRN1GzYHOARrgXKoyCRJfRVNywlX17f9K1QoTUkZr_1OA_A35yo6NeYpCBsE1-u-PNjR5oYxfDWlpXs94bmzlxCyD9Lf8gvuN9cCOWk1br-499C4CgiVW0TjOOlZRQwdbjpfAw6yU7hYuNY8IQatNFh9lNByQcHugfeDeNfW16VmX96M7SC3IZwNDSzstv6Tfi4GE50bwDA7J8ksVK61P51UPuZfMa3cq8SSn3XFgjFlyn2nWsxOejGuAx9rUP_mHJogiOK5wsbQf5aJNS-n7r-_c4Hqc-hrKziKPVtmmYZvhwbLVVUI9cAL-IuDVPSA-OT6UhnwgOFkwBtqVpZ4vN_ZZDfxhcryfzjIRSEkcupdncOSmEq8dAiSBAhUTVuB7NypyCHsEd2YxqfzE-9YvIED4OVj3ksHUi7XIqha44cpY2iPLe_5RI1x_biiyOW7WQzKxKs9EkeG9-_hZ6dZAqSaMMrM4JYcGzY_-Uft0wu6h7DEpJMKUIkXJJOE1i_-mmalNDZKuXOvTjCvypAg8diWcBzcW2BRnl5-GGjp6LcpI26jh8GnWYdygiLtNVWRTo8mPZGqiCplU70V2bp5hsCb1zqa4ly02_gb-XCjqglAgUfhkk38faEz5ODdtcYrxUzM-hcHgkfpLNp4rGfOAcZTdibVHPl_CFAY_pXlMyb5_cB7Yfj0hUuRVJK-qn_M_Vc7q0dQ8xKpdxKzwm22Fm_kY4Z2ID68GOQd91cy1Kde_90JbgR4139XcGCdjdnCU6L2Djqip2YMxO7_5z13i2K7Xx59VBcdJvvEyS9_MolfpNanGkoOW9DMzNjHD5VUWvJQtGj67nj1Ccn9mH7Wj-pZ1hybsQgGmjBQk1r-VUpkAOx65jEzcGJsd9CPDnfRmwBhxaosi9JS7JcXFTP-BXUoTn74LifkWXb5OYxRqWcKwZoSiXVw-JllbNYlhX-DAmOolriUbUwbWZhpoHXNjhsEbXExQNzCffcuxdCt-Vwjx1u_vHuTwzE8768qL6mvzw-q5qOpwao6iUI4zqVwKU_SqfaWe9h6FtQNTZIjU_ghcBRA_D6A1uojaFbAYKMokKs-PFU4KxkfhKIICLynmFfjYRxVridNazfYEt6yOcIh-bNj7OsGmeG-jcw-T5rAtabv_-p7eGgbTtvRbcDvP_LxRDKJk1U-C1w1W9t24ygvauB0afKY8dVpr_o6mAR4o5LAI0WJmDdEOOjkGx8Fz2ofW0Sjidw56KSQQfj6K6bIW5oZ-X4MvA-0vqIZANa7trZEaWax65B5y1Sb5Mv8hxYncFH4-r9M20aPT630rMQCd3wuubVlvh7ndtxU0GXmS9mb0LRoCz4thbOI-S7iI9cirU5PhGrK7rJxaHJysiH4EKINIDeRxYL_oZEsnOIJLw=w416-h312-p'

  response = requests.get(img_url)
  image = response.content
  file_name = "new.png"
  with open(file_name, "wb") as f:
    f.write(image)
  time.sleep(5)
  img_diff_new = cv2.imread("new.png", cv2.IMREAD_GRAYSCALE)
  whitePixels_new = np.count_nonzero(img_diff_new)
  blackPixels_new = img_diff_new.size - whitePixels_new
  element_new = whitePixels_new / img_diff_new.size * 100
  time.sleep(2)

  img_diff_old = cv2.imread("old.png", cv2.IMREAD_GRAYSCALE)
  whitePixels_old = np.count_nonzero(img_diff_old)
  blackPixels_old = img_diff_old.size - whitePixels_old
  element_old = whitePixels_old / img_diff_old.size * 100
  time.sleep(2)

  if element_new == element_old:
    print('no change')
  else:
    image_file = 'new.png'
    binary = open(image_file, mode='rb')
    image_dic = {'imageFile': binary}
    requests.post(api_url, headers=TOKEN_dic, data=send_dic, files=image_dic)
    time.sleep(5)
    file_name2 = "old.png"
    with open(file_name2, "wb") as f:
      f.write(image)
    print('change')