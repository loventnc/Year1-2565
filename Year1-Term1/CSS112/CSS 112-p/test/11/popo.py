def Problem1_1(a): ##ข้อที่ 1.1
    return True if a in (set(i for i in range(2,a+1)).difference(set(i for i in range(1,a+1) for j in range(2,i) if i%j== 0))) else False
  
def Problem1_2(M): ##ข้อที่ 1.2
    return sum(list(sum([j for j in a[i] if j%2 == 1]) for i in range(len(M))))

def Problem1_3(Purchase_list): ##ข้อ 1.3
    icecream_price_dict =   {"cone": 300 , 
                            "sherbet": 200, 
                            "choco" : 100}
    return sum(list(icecream_price_dict.get(i) for i in list_a if i in icecream_price_dict.keys()))

##ข้อที่ 2
class Item:
    def __init__(self,energy):
        self.energy = energy

class Robot(Item):
    def serve(self):
        return "serve with {} Electrical energy need is {} Watt - Hour".format(self.__class__.__name__, self.item.energy)

class Armhand(Item):
    def __init__(self, energy,length):
        super().__init__(energy)
        self.length = length

class IndustrialArmRobot(Robot):
    def __init__(self,height,energy,length):
        self.height = height
        self.item = Armhand(energy,length)


def Problem2():
    anIndustrialArmRobot = IndustrialArmRobot(170,213,2)
    msg = anIndustrialArmRobot.serve()
    print(msg)

##ข้อที่ 3.1
def Problem3_1(max_prime):
    prime_list_1 = (set(i for i in range(3,max_prime+1)).difference(set(i for i in range(1,max_prime+1) for j in range(2,i) if i%j== 0)))
    prime_list_2 = (set(i for i in range(5,max_prime+1)).difference(set(i for i in range(1,max_prime+1) for j in range(2,i) if i%j== 0)))
    return list((i,j) for i,j in zip(prime_list_1,prime_list_2))