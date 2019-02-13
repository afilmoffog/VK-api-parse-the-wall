import requests
import json
import csv
from time import sleep


def write_data(data):
    with open('posts.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def to_json(post_dict):
    try:
        data = json.load(open('posts_data.json'))
    except:
        data = []
    data.append(post_dict)

    with open('posts_data.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def write_csv(data):
    with open('posts_data', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['likes'],
                         data['reposts'],
                         data['text']
                         ))


def get_data(post):
    try:
        post_id = post['id']
    except:
        post_id = 0
    try:
        likes = post['likes']['count']
    except:
        likes = 'zero'
    try:
        reposts = post['reposts']['count']
    except:
        reposts = 'zero'
    try:
        text = post['text']
    except:
        text = '***'

    data = {
        'id': post_id,
        'likes': likes,
        'reposts': reposts,
        'text': text
    }

    return(data)


def main():
    all_posts = []
    time_now = 1550072581  # your epoch time
    params = {
        'owner_id': -59857479,
        'count': 100,
        'offset': 0,
        'access_token': '',# your token
        'version': 5.92
    }

    while True:
        sleep(1)
        r = requests.get('https://api.vk.com/method/wall.get', params)
        posts = r.json()['response']
        all_posts.extend(posts)

        oldest_post_date = posts[-1]['date']

        offset += 100

        if oldest_post_date < time_now:
            break

        data_posts = []

        for posts in all_posts:
            post_data = get_data(post)
            write_csv(post_data)


if __name__ == '__main__':
    main()
