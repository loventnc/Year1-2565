def p14():
    ddict = {'Amanda': 'Doctor', 
             'knew': 'now', 
             'how': 'in', 
             'joyous': 'great', 
             'could': 'threatening', 
             'be': 'danger,',
             'until': 'please', 
             'saw': 'need', 
             'face': 'help', 
             'leaps': 'beats', 
             'hummingbird': 'machine ', 
             'in': 'very', 
             'flight': 'alarmingly', 
             'time': 'hour,', 
             'see': 'need', 
             'you': 'the drug', 
             'inspires': 'causes', 
             "haven't": 'am'}

    
    letter="Dear Amanda I haven't knew how joyous life could be until I saw your face My heart leaps like a hummingbird in flight every time I see your face This is something I have never felt before and it is you that inspires it"
    list_letter = letter.split(" ")
    decoded_list = [ddict.get(key, key) for key in list_letter ]
    decoded_letter = ' '.join(decoded_list)
    # Expected ans-> decoded_letter = 'Dear Doctor I am now in great life threatening danger, please I need your help My heart beats like a machine  very alarmingly every hour, I need your help This is something I have never felt before and it is the drug that causes it'
    return decoded_letter
print(p14())