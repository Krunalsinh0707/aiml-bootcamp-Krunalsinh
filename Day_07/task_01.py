import numpy as np

rng = np.random.default_rng(42)

sales = rng.integers(50,500 , size= (4,30,3))

#per shope

per_shop = sales.sum(axis=(1,2))

print(per_shop , per_shop.shape)

#avg daily sales 
avg_daily_cat = sales.sum(axis=(0,1))

print(avg_daily_cat , avg_daily_cat.shape)

#best day for every shop 

daily_totals = sales.sum (axis = 2)

best_day = daily_totals.argmax(axis=1)
print(best_day , best_day.shape)


#msot consistance day

shop_std = daily_totals.std(axis = 1)

consistent_shop = shop_std.argmin()


print(shop_std , shop_std.shape)

print(consistent_shop , consistent_shop.shape)

#category mean 

catogory_mean = sales.mean(axis = (0,1) , keepdims=True)
print(catogory_mean , catogory_mean.shape)
