mas = [6,3,6,2,7,8,2,4,87,123,685,11,24,6,4,2,3,6,8,3,1,3,76]

def rasc():
    n = len(mas)
    step = n
    while step > 1 or flag:
       if step > 1:
           step = int(step / 1.247331)
       flag, i = False, 0
       while i + step < n:
          if mas[i] > mas[i + step]:
              mas[i], mas[i + step] = mas[i + step], mas[i]
              flag = True
          i += step
    return mas
rasc()
print(mas)

