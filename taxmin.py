import random


def taxmin1(x):
    random_son = random.randint(1, x)
    taxmin = 0
    urinish = 0
    while True:
        try:
            while taxmin != random_son:
                taxmin = int(input(f"1 dan {x} gacha son taxmin qiling: "))
                if taxmin < random_son:
                    print("kiritgan soningiz past!")
                elif taxmin > random_son:
                    print("Kiritgan soningiz yuqori!")
                urinish += 1
            print(f"\nSiz {urinish} urinishda topdingiz!")
            print(
                f"\nTabriklayman siz random sonni topdingiz, kiritgan {random_son} to'g'ri!!"
            )
            return str(taxmin)
        except:
            print("Iltimos son kiriting!!")
            urinish += 1


taxmin1(10000)
