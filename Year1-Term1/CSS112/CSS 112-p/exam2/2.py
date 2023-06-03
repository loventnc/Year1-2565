def p2():

    icecream_msg = 'I like to buy ice cream: choco or may be cone otherwise sherbet'
    icecream_price = {'cone':'300', 'sherbet':'200', 'choco': '100'}
    #ExpectedAns = 'I like to buy ice cream: choco for 100 or may be cone for 300 otherwise sherbet for 200'

    decoded_icecream_list = [icecream_price.get(key, key) for key in icecream_msg.split()]
    Ans = ' '.join(decoded_icecream_list)
    return Ans
print(p2())