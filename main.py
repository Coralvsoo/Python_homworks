# son = 12

# sanoq =0
# while son != 0:
#     son = int(input("son kriting"))
#     sanoq += son
# print(sanoq)
   
# while 2

# a = int(input("a sonini kriting"))
# b = int(input("b d sonini kriting"))

# sanoq =0
# while a < b:
#     sanoq +=a
#     a +=1
# print(sanoq)

# while 3

# listm = [22,33,3,21]

# while True:
#     i = int(input("son kriting( chiqish uchun manfiy son kriting)"))
#     if i > 0:
#         listm.append(i)
#     else:
#         print(listm)

# while 4

# x =[1,2,3,14,5,6,6,7,3,22]
# katta = x[0]
# index = 1
# while index< len(x):
#     if katta < x[index]:
#         katta = x[index]
#     index +=1
# print(katta)

# while 5

# while 5

# x =[1,2,3,3,14,5,66,5,77]

# katta = x[0]
# index = 1

# while index < len(x):
#     if katta < x[index]:
#          katta = x[index]
#     index+=1
# print(x.index(katta))
   
# while 6

# son = int(input("Son kriting"))

# count = 0

# while son !=0:
#     son //=10
#     count +=1
# print(count)

# while 7
# x = [1 , 2 , 34 , 56 , 23]

# katta = x[0]
# kichik = x[0]
# index =1

# while index < len(x):
#     if katta < x[index]:
#         katta = x[index]
#     if kichik > x[index]:
#         kichik = x[index]
#     index +=1
# print(f"Kattasi: {katta}")
# print(f"Kichigi: {kichik}")

# while 8

# x = [ 1, 2, 33, 45,12]

# katta = x[0]
# kichik = x[0]

# index =1

# while index < len(x):
#     if katta < x[index]:
#         katta = x[index]
#     if kichik > x[index]:
#         kichik = x[index]
#     index += 1
# indexKa = x.index(katta)
# indexKi = x.index(kichik)
# x[indexKa], x[indexKi] = x[indexKi], x[indexKa]


# print(x)

# while 9
         
# son = int(input("son kriting"))

# my_list = [12,23,2,4,56,66]

# sircle = 0

# found =False
# while  sircle < len(my_list):
#     if my_list[sircle]== son :
#        found = True

   
   
#     sircle +=1
# if found:
#     print("Element bor ")
# else:
#     print("Element yoq")

# while 10
# a = int(input("a sonini kriting"))

# b = int(input("b sonini kriting"))

# while b!=0:
#     a , b = b, a % b # a ni b ga b ni esa qoldiqga o'zgarteish kerak

# print(f"Natija: {a}")

# while 11

# a = int(input("A soninini kriting"))
# b = int(input("B sonini kriting"))

# A = a
# B = b
# while b!=0:
#      a,b =b,a%b # a ni bga bni esa qoldiqga o'zgartrish kerak

# ekub = a
# print(ekub)
# ekuk  = abs(A*B)/ekub


    
# print(ekuk)

# a = int(input("a sonini kriring"))
# b = int(input("b sonini kriting"))

# i =1
# summaA = 0
# while i <= a:
#     if a % i == 0:
#         print(i)
#         summaA += i
#     i +=1
# print(f"a sonining summasi : {summaA}")


# j = 1
# summaB = 0
# while j <= b:
#     if b % j == 0:
#         print(j)
#         summaB += j
#     j += 1
# print(f"Summa B : {summaB}")

# if summaA == summaB:
#     print("Bular do'st sonlardir")
# else:
#     print("Bular do'st sonlar emas")

son = int(input("Son kriting"))

count = 0
son = abs(son)
son = len(str(son))

print(son)