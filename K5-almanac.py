#K5 tehtävä 1:Maanviljelijän almanakka
from datetime import datetime

def add_info(sanakirja):
    array=[]
    
    date=input("Add date:")
    pvm=datetime.strptime(date,"%d.%m.%Y")
    if date in sanakirja.keys():
        print("Date already exists.")
        
    else:    
        sanakirja[date]=array
        
        weather=input("weather prognosis:")
        if weather=="":
            print("you need to fill the weather prognosis.")
            weather=input("weather prognosis:")
        tapahtumat=input("what should be done:")
        sanonta=input("saying:")
        print("New date was added.")
        array.append(weather)
        array.append(tapahtumat)
        array.append(sanonta)
        
def search_date(sanakirja):
    search=input("What date?")
    if search not in sanakirja:
        print("No info in the calendar.")
    else:
        for key,value in sanakirja.items():
            sanakirja[key]=value
            if search==key:
                print(search,":",sanakirja[search])
    
def show_calendar(sanakirja):
    print(sanakirja)    
def käyttöliitymä():
    sanakirja={} 
    
    while True:
        try:
            what=input("What do you want to do?\n1. add new date(D.M.YYYY)\n2. search by date(D.M.YYYY)\n3. show calendar\n4.end\n")
            if what=="1":
                add_info(sanakirja)
            elif what=="2":
                search_date(sanakirja)   
            elif what=="3":
                show_calendar(sanakirja)  
            elif what=="4":
                print("See you next time!")
                break
        except:
            print("Virheellinen syöte")        
if __name__=="__main__":
    käyttöliitymä()
