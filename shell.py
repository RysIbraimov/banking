from credit.models import Credit,Client,Account
import datetime
import  random
#
# client1 = Client.objects.create(name='Бердиев.Н.Д',birth_year=datetime.date(1994,1,1),work_place='Codify')
# client2 = Client.objects.create(name='Уланов.Б.Д',birth_year=datetime.date(1991,1,1),work_place='Beeline')
def render_number():
    l = [random.randrange(1,100) for i in range(16)]
    return l


client = Client.objects.get(work_place='Codify')
client1 = Client.objects.get(work_place='Beeline')

accaunt = Account(number=render_number(),client=client)
accaunt.save()
accaunt1 = Account(number=render_number(),client=client1)
accaunt1.save()

print(accaunt1)
print(accaunt)