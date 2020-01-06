punktid = 0
print("Mis on aeglasem kui tigu?")
print("vajutage 1, kui te arvate et James May")
print("vajutage 2, kui te arvate et vaese mehe Internet")
print("vajutage 3, kui te arvate et 2019.aasta Williamsi F1 auto")
vastus1 = input()
if vastus1 == "1":
    print("James Mayst on küll miskit aeglasemat...")
if vastus1 == "2":
    print("Vaese mehe Internetist on küll miskit aeglasemat...")
if vastus1 == "3":
    print("Muidugi on õige vastus 2019.aasta Williamsi F1 auto! Isegi minu pesumasin liigub mööda mu kööki kiiremini kui see")
    punktid = punktid+1
print("Mis või kes on kiirem kui Usain Bolt?")
print("vajutage 1, kui te arvate et hüperaktiivne laps")
print("vajutage 2, kui te arvate et tavaline laps, kes jõi just Red Bulli")
print("vajutage 3, kui te arvate et mu pesumasin, mis liigub mööda mu kööki")
vastus2 = input()
if vastus2 == "1":
    print("Vale, sest hüperaktiivne laps läks väga igavasse autosse ja jäi 3 minutiga magama...")
if vastus2 == "2":
    print("Vale, sest ta ema keelas seda juua...")
if vastus2 == "3":
    print ("Muidugi! Väga veider, et mu pesumasin pole Guniess Maailmarekordiraamatus...")
    punktid += 1
print("Mis on õige vastus")
print("vajutage 1, kui te arvate et jah")
print("vajutage 2, kui te arvate et ei")
print("vajutage 3, kui te ei tea")
vastus3 = input()
if vastus3 == "1":
    print("Sa pakkusid huupi! See läheb arvesse vale vastusena!")
if vastus3 == "2":
    print("Sa pakkusid huupi! See läheb arvesse vale vastusena!")
if vastus3 == "3":
    print("Muidugi sa ei tea! See läheb arvesse vale vastusena!")

if punktid == 3:
    print("Õnnitleme, sinu hinne on A")
else:
    print("proovi veel")
    


       