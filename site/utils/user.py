import hashlib

from django.contrib.auth import get_user_model

User = get_user_model()


def make_username(first_name, last_name, email):

    hash_user = hashlib.sha1()

    hash_user.update(
        u"-".join([first_name, last_name, email]).encode('ascii', 'ignore'))
    username = hash_user.hexdigest()

    if User.objects.filter(username=username).exists():
        from random import randint
        email = u"{}_{}".format(email, randint(0, 1000))
        return make_username(first_name, last_name, email)

    return username[0:29]
