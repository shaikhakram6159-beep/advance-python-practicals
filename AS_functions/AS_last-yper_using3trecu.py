def display_percentage(percentage,count):
    if count==0:
        return
    print("last year percentage:",percentage)
    display_percentage(percentage,count-1)
display_percentage(72.5,3)
