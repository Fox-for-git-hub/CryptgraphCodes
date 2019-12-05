import random
import math

#暗号化する平文
message = 777


########################
###### 公開鍵の作成 ######
########################

#素数配列の作成
p_candidates = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149]
q_candidates = [151, 157, 163, 167, 173, 179, 181, 191, 193, 197]

#randomモジュールの関数でランダムに要素を1つ選択
p = random.choice(p_candidates)
q = random.choice(q_candidates)

#数Nを作成
N = p * q

#関数lcm(最小公倍数を求める)を用意
def lcm(x, y):
    # f(x,y) = (x*y) // xとyの最大公約数
    # math.gcdは最大公約数を求める
    return (x * y) // math.gcd(x, y)

#関数lcmの引数にp-1とq-1を指定し、Lに代入
# L = p-1とq-1の最小公倍数
L = lcm(p - 1, q - 1)

#引数は「2」以上「L」未満の1刻みの乱数発生
E = random.randrange(2, L)

#最大公約数が1出なければ
while math.gcd(E, L) != 1:
    #再度乱数を発生
    E = random.randrange(2, L)


########################
###### 秘密鍵の作成 ######
########################

for i in range (2, L):
    if (E * i) % L == 1:
        D = i
        break


########################
######## 暗号化 ########
########################

cipher = pow(message, E) % N

print ('crypted message is : ' + str(cipher) + '\n')


########################
######### 復号 #########
########################

decipher = pow(cipher, D) % N

print ('decrypted message is : ' + str(decipher) + '\n')
