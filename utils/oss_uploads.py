# -*- coding: utf-8 -*-
import json
import os

import oss2

# 默认，外网访问
endpoint = os.environ.get('OSS_ENDPOINT', 'oss-cn-beijing.aliyuncs.com')
# ECS 访问
# endpoint = 'oss-cn-beijing-internal.aliyuncs.com'

# RAM user lottery-upload-oss
access_key_id = ''
access_key_secret = ''
bucket_name = ''

auth = oss2.Auth(access_key_id, access_key_secret)
bucket = oss2.Bucket(auth, endpoint, bucket_name)


def upload_text(key, text):
    return bucket.put_object(key, text)


def upload_json(key, json_obj):
    upload_text(key, json.dumps(json_obj, indent=4))


def delete(key):
    bucket.delete_object(key)

# Download
# bucket.get_object(key).read()

# Traverse all objects in the bucket
# for object_info in oss2.ObjectIterator(bucket):
#     print(object_info.key)


if __name__ == '__main__':
    value = {'key-%s' % i: i for i in range(8)}
    print(value)
    upload_json('tests/hello1.json', value)
