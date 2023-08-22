bs = int(input())
if (bs<=10000):
    da = 0.80*bs
    hra = .20*bs
elif (bs <= 20000):
    da = 0.9*bs
    hra = .25*bs
elif (bs> 20000):
    da = .95*bs
    hra = .3*bs
gross = bs+da+hra
print(f"{gross:.2f}")