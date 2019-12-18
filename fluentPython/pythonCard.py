
##collections是Python内建的一个集合模块，提供了许多有用的集合类
import collections 
from random import choice
## namedtuple返回的是一个类,类的名字叫"Card",类的属性是rank 和 suit 
Card = collections.namedtuple("Card",["rank","suit"])

class FrenchDeck:

    ## [n for n in range(2,11)] 快速建立列表的写法,n 放前面
    ## str(n)返回 object 的 字符串 版本,此处为n
    ## ranks输出值 ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    ## suits输出值 ['spades', 'diamonds', 'clubs', 'hearts'] 黑桃,方块,梅花,红心
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    #suits = 'spades diamonds clubs hearts'.split()
    suits = '黑桃 方块 梅花 红心'.split()

    ## 构造函数
    ## 实例化的时候,即生成一副牌
    def __init__(self):
        print("实例化开始","="*20)
        print(self)
        ## 私有变量_cards,是Card类组成的列表
        self._cards = [Card(rank,suit) for suit in self.suits 
                                       for rank in self.ranks ]
        
    ## len 方法
    def __len__(self):
        return len(self._cards)
    ## 获取器
    def __getitem__(self,position):
        return self._cards[position]

    
def main():
    ## 实例化
    deck = FrenchDeck()
    print(len(deck))##__len__方法
    #print(deck[0])##__getitem__方法
    #print(deck[-1])
    print("随机抽出的牌是:",choice(deck))

    print(deck[:3])
    print(deck[12::13])#切片从索引12开始,没隔13张抽取一张

main()