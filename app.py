
import requests
from getTiktokDict import getDict
from flask import Flask, request, jsonify

app = Flask(__name__)

def create_header(parse_dict) -> dict:
    cookies = {
        'PHPSESSID': parse_dict['PHPSESSID'],
        # 'popCookie': parse_dict['popCookie'],
    }
    headers = {
        'authority': 'ttdownloader.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://ttdownloader.com',
        'referer': 'https://ttdownloader.com/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'url': '',
        'format': '',
        'token': parse_dict['token'],
    }
    return cookies, headers, data

def get_video_link(tiktok_url, cookies, headers, data) -> str:
    data['url'] = tiktok_url
    response = requests.post('https://ttdownloader.com/search/',
                             cookies=cookies, headers=headers, data=data)
    link_parse = [i for i in str(response.text).split() if i.startswith("href=")][0]

    video_response = requests.get(link_parse[6:-10])
    # with open("./name.mp4", "wb") as f:
    #     f.write(video_response.content)
    print("FFFSDSDSDSD")
    return video_response.url

@app.route('/get_video_link')
def get_video_link_api():
    try:
        tiktok_url = request.args.get('tiktok_url')
        print("URRLLLLLL")
        print(tiktok_url)
        parse_dict = getDict()  # You need to define the getDict function
        cookies, headers, data = create_header(parse_dict)
        video_link = get_video_link(tiktok_url, cookies, headers, data)
        return jsonify({'video_link': video_link})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
