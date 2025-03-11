# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). 
# Определите наибольшую длину цепочки символов, среди которых нет символов K и L, стоящих рядом.
f=open('24_2.txt').readline()
#f = 'AKBVCLKR'
# k=0
# c=0
# for i in range(0,len(f)-1):
#     if f[i]+f[i+1] in ('KL', 'LK'):
#         k=0
#     else:
#         k+=1
#         if k>c:
#             c=k
# print(c+1)     

f = f.replace('KL', 'K L')
f = f.replace('LK', 'L K')
f = f.split()
f = max(f, key=len)
print(len(f))