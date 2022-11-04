# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'songcrud.settings')
#
# import django
# django.setup()
#
# # FAKE POP SCRIPT
# import random
# from musicapp.models import Artiste, Song, Lyric
# from faker import Faker
#
# fake_music = Faker()
# artiste_id = ['Tekno', 'Kiss Daniel', 'Olamide', 'Davido', 'Wizkid', 'Burna Boy', 'Tiwa Savage', 'Yemi Alade', 'Teni']
#
#
# def add_artiste():
#     a = Artiste.objects.get_or_create(stage_name=random.choice(artiste_id))[0]
