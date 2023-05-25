import requests
from datetime import datetime
import traceback
import time
import json


def write_json_line(handle, obj):
    handle.write(json.dumps(obj))
    handle.write("\n")

def download_from_url(filename, url_base, start_datetime, end_datetime):
    print(f"Saving to {filename}")
    count = 0
    with open(filename, 'w', encoding='UTF-8') as handle:
        previous_epoch = int(start_datetime.timestamp())
        break_out = False
        while True:
            new_url = url_base+str(previous_epoch)
            print(new_url)
            json_text = requests.get(new_url, headers={'User-Agent': "Post downloader by Serhii_Miroshnychenko"})
            time.sleep(1)
            try:
                json_data = json_text.json()
            except json.decoder.JSONDecodeError:
                time.sleep(1)
                continue

            if 'data' not in json_data:
                break
            objects = json_data['data']
            if len(objects) == 0:
                break

            for obj in objects:
                previous_epoch = obj['created_utc'] - 1
                if end_datetime is not None and datetime.utcfromtimestamp(previous_epoch) < end_datetime:
                    break_out = True
                    break
                count += 1
                try:
                    write_json_line(handle, obj)
                except Exception as err:
                    if 'permalink' in obj:
                        print(f"Couldn't print object: https://www.reddit.com{obj['permalink']}")
                    else:
                        print(f"Couldn't print object, missing permalink: {obj['id']}")
                    print(err)
                    print(traceback.format_exc())
            if break_out:
                break
            print(f"Saved {count} through {datetime.fromtimestamp(previous_epoch).strftime('%Y-%m-%d')}")
        print(f"Saved {count}")


if __name__ == "__main__":
    subreddit = "r/ideavim"
    output_format = "json"
    start_time = datetime.strptime("01/25/2023", "%m/%d/%Y")
    end_time = datetime.strptime("01/20/2023", "%m/%d/%Y")
    filter_string = f"subreddit={subreddit}"
    url_template = "https://api.pushshift.io/reddit/{}/search?limit=1000&order=desc&{}&before="
    download_from_url("../comments.txt", url_template.format("comment", filter_string), start_time, end_time)
    