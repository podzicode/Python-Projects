import random;
class Cards(object):
    def __init__(self, cards=['A','2','3','4','5','6','7','8','9','10','K','J','Q','A','2','3','4','5','6','7','8','9','10','K','J','Q','A','2','3','4','5','6','7','8','9','10','K','J','Q','A','2','3','4','5','6','7','8','9','10','K','J','Q',]):
        self.cards = cards;


class Player(object):

    def __init__(self, name,balance=1000000000,count=0):
        self.Name=name;
        self.balance=balance;
        self.count=count;
    def get_balance(self):
        return self.balance;

    def set_balance(self, balance):
        self.balance=balance;


class Dealer(Player):
    def __init__(self,name,cards):
        Player.__init__(self,name)
        self.cards=Cards();

    def deal(self,x):
        n=1
        y=[]
        while(n<=x):
            y.append(random.choice(self.cards.cards));
            n+=1;
        return y;


def playJack():
    print("Welocome to the game")
    print("Hi I am Lynda your dealer for today")
    print("==============================================")
    name=raw_input("PLease Enter your Name: ")
    dealer="Lynda"
    print("===============================================")
    print("HI"+" "+name+" "+"Welcome to the game again lets play")
    sys=[]
    pla=[]
    cash=int(raw_input(("Place the amount you want to bet: ")));
    count=0;
    c=Cards();
    p=Player(name,cash,count);
    d=Dealer(dealer,c);
    print("Dealing cards to "+name)
    pla=d.deal(2);
    sys=d.deal(2);
    for i in pla:
        print(i);
        if (i.lower() == 'a'):
            i = 10
            p.count += int(i);
        elif (i.lower() == 'k'):
            i = 10
            p.count += int(i);
        elif (i.lower() == 'j'):
            i = 10
            p.count += int(i);
        elif (i.lower == 'q'):
            i = 10
            p.count += int(i);
        else:
            p.count += int(i);


    print("present player count is ",p.count);
    while(True):
        resp=raw_input("Do you want to draw card 'Y' or 'N'")
        if(resp.lower()=='y'):
            pla+=d.deal(1)
            print("Now you're cards are: ")
            p.count=0
            for i in pla:
                print(i);
                if (i.lower() == 'a'):
                    i = 10
                    p.count += int(i);
                    continue
                elif (i.lower() == 'k'):
                    i = 10
                    p.count += int(i);
                    continue
                elif (i.lower() == 'j'):
                    i = 10
                    p.count += int(i);
                    continue
                elif (i.lower == 'q'):
                    i = 10
                    p.count += int(i);
                    continue
                else:
                    p.count += int(i);
                continue
        else:
            break;
    print("Check with dealers cards")
    print("Dealers current cards are: ")
    sys2=set(sys)
    for i in sys2:
        print(i);
        d.count+=1;
    if(d.count<17):
        while(d.count<17):
            sys+=(d.deal(1))
            d.count=0;
            for i in sys:
                print(i);
                if (i.lower() == 'a'):
                    i = 10
                    d.count += int(i);
                elif(i.lower() == 'k'):
                    i = 10
                    d.count += int(i);
                elif(i.lower() == 'j'):
                    i = 10
                    d.count += int(i);
                elif(i.lower == 'q'):
                    i = 10
                    d.count += int(i);
                else:
                    d.count += int(i);
        print("Comparing the Values")
        if(d.count>21):
            print("The Dealer got bust Congrats You Win")

        elif(d.count>p.count):
            print("Sorry Try next time")
        else:
            print("Congrats you win your money is doubled")
            p.balance+=p.balance
            d.balance-=d.balance



playJack()



