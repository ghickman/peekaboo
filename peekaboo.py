import json
import os
import sys
import time

import requests
import pync


types = {
    'comments': 'issuecomment',
    'commits': 'commitcomment',
    'pulls': 'issuecomment',
}

try:
    cache = []
    headers = {'Authorization': 'bearer {0}'.format(os.environ['GITHUB_TOKEN'])}
    since = None
    url = 'https://api.github.com/notifications'

    while True:
        params = {'since': since} if since else {}
        r = requests.get(url, headers=headers, params=params)
        if not r.ok:
            raise Exception('GitHub returned {0}'.format(r.status_code))

        since = time.strptime(r.headers['date'], '%a, %d %b %Y %H:%M:%S %Z')
        notifications = json.loads(r.content)
        if not notifications:
            cache = []

        for notification in notifications:
            if not notification['id'] in cache:
                latest_comment_id = notification['subject']['latest_comment_url'].split('/')[-1:][0]
                issue_url = notification['subject']['url'].replace('api.', '').replace('repos/', '')
                tipe = issue_url.split('/')[-2]
                issue_url = issue_url.replace(tipe, tipe[:-1])
                open_url = '{0}#{1}-{2}'.format(issue_url, types[tipe[:-1]], latest_comment_id)
                kwargs = {
                    'title': notification['repository']['full_name'],
                    'open': open_url,
                    'group': os.getpid(),
                }
                s = notification['subject']['url'].split('/')[-2:]
                pync.Notifier.notify('{0} #{1}'.format(s[0].title(), s[1]), **kwargs)

                cache.append(notification['id'])

        time.sleep(5)
except KeyboardInterrupt:
    sys.exit(0)

