def convert_ms(n):
    hours = 0
    minutes = 0
    seconds = (n / 1000)
    if seconds >= 60:
        minutes = seconds // 60
        seconds = seconds % 60
    if minutes >= 60:
        hours = minutes // 60
        minutes = minutes % 60
    print('{}:{}:{}'.format(int(hours),int(minutes),int(seconds)))
convert_ms(555550000)