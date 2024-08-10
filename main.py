import requests  # Модуль для обработки URL
import math


def factorial (a):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    body={'number': a}
    link='https://qa-test.emcd.io/factorial'
    if isinstance(a, int) == False :
        return 'Please enter an integer'
    try:
        full_page = requests.post(link, data=body, headers=headers)
        full_page.raise_for_status()
        data = full_page.json()
        try:
            math.isinf(data['answer'])
        except OverflowError:
            data['answer']='Infinity'
        return data['answer']
    except requests.exceptions.HTTPError as errh:
        if full_page.status_code == 500:
            print("Server error: 500 Internal Server Error")
            return '500'
        else:
            print(f"HTTP Error: {errh}")

def get_elements():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    link = 'https://qa-test.emcd.io'
    if isinstance(a, int) == False:
        print("Please enter an integer")
        return
    try:
        full_page = requests.post(link, data=body, headers=headers)
        full_page.raise_for_status()
        data = full_page.json()
        print(data)
    except requests.exceptions.HTTPError as errh:
        if full_page.status_code == 500:
            print("Server error: 500 Internal Server Error")
    return

def hand_fact(n):
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result

#print(hand_fact(0))
#for i in range (0,3):
    #print(i, ' ', factorial(i))
print(factorial('1..5'))
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'}
    # full_page = requests.get(link, headers=headers)
    # if full_page.status_code == 200 and errno == 400:
    #     answer='Failed! it is 200, but must be 400!'
    #     print('Case #' + str(num) +': ',answer)
    #     return answer
    # if errno==200 and full_page.status_code==errno:
    #     data = full_page.json()
    #     if idu in data.get('idList'):
    #         answer = 'Passed!'
    #     else: answer = 'failed! it is 200, but ' + str(idu) + 'is not in answer'
    # elif full_page.status_code == errno and errno==400:
    #     data = full_page.json()
    #     if data.get('message')==idu:
    #         answer = 'Passed!'
    #     else: answer = 'Failed! it is 400, but message is different!'
    # if full_page.status_code == 500:
    #     answer = 'Failed! It is 500 Internal Server Error, but must be ' + str(errno)
    # print('Case #' + str(num) +': ',answer)
    # return answer

# def user_check(link, errno, idu, num):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'}
#     full_page = requests.get(link, headers=headers)
#     if full_page.status_code == 200 and errno != 200:
#         answer='Failed! it is 200, but must be ' + str(errno)+ '! User not found'
#         print('Case #' + str(num) +': ',answer)
#         return
#     if full_page.status_code == 200 and errno == 200:
#         data = full_page.json()
#         if idu==data.get('user', {}).get('id'):
#             answer='Passed!'
#             print('Case #' + str(num) +': ',answer)
#             return
#         else:
#             answer='Failed! It is 200, but response has a different ID'
#             print('Case #' + str(num) + ': ', answer)
#             return
#     if full_page.status_code == 400 and errno == 400:
#         data = full_page.json()
#         if data.get('errorMessage')==idu:
#             answer = 'Passed!'
#             print('Case #' + str(num) + ': ', answer)
#             return
#         else:
#             answer='Failed! it is 400, but message is different!'
#             print('Case #' + str(num) + ': ', answer)
#             return
#     if full_page.status_code == 500:
#         answer = 'Failed! It is 500 Internal Server Error, but must be ' + str(errno)
#         print('Case #' + str(num) + ': ', answer)
#         return
#
#
#
# link = 'https://hr-challenge.dev.tapyou.com/api/test/users'
# cases1 = [['?gender=male', 200, 15],
#          ['?gender=female', 200, 5],
#          ['?gender=magic', 200, 300],
#          ['?gender=McCloud', 200, 911],
#          ['?gender=other', 400,  "Invalid value for parameter 'gender'"],
#          ['?gender=any', 400, "Invalid value for parameter 'gender'"],
#          ['?gender', 400,"Gender value is required! Example gender=male"],
#          ['?gender=male&cast=test', 200, 15],
#          ['?city=test', 400, "Required String parameter 'gender' is not present"],
#          ['?gender=male&gender=female', 400, "Allowed only 1 value of gender"]]
# for i in range(len(cases1)):
#     gender_test(link + cases1[i][0], cases1[i][1], cases1[i][2], i+1)
# link = 'https://hr-challenge.dev.tapyou.com/api/test/user'
# user_check(link +'/5',200,5,i+2)
# user_check(link +'/3',404,'User not found!', i+3)
# user_check(link +'/5s-',400,'Only number is allowed, not string', i+4)
# user_check(link +'/2147483658',400,'This number is out from int32. Enter number 2147483647 or lower1. Or connect support with this problem', i+5)