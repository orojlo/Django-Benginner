import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyProject3.settings')

import django
django.setup()

## Fake POP SCript
import random
from MyApp3.models import AccressRecord,Webpage,Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):

    for entry in range(N):

        # Get the Topics for the entry
        top = add_topic()

        # Create Fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create The New Webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # Create A Fake Access Record for that Webpage
        acc_rec = AccressRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__=='__main__':
    print("Populating Script!")
    populate(20)
    print("Populating Complate!")
