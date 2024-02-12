
Sigma1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Sigma2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'k']
Sigma3 = ['x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4', 'x5', 'y5']

S1 = ''.join(Sigma1)
S2 = ''.join(Sigma2)
S3 = ''.join(Sigma3)
S3Inversat = ''.join(Sigma3)
def concat(s1,s2):
    return s1+s2

def repet(s, n):
    sir_repetat = "".join([s for _ in range(n)])
    return sir_repetat

def inverse(s):
    return s[::-1]

def extract(s, i, j):
    return s[i:j+1]

def replace(s, sub, new_sub):
    index = s.find(sub)
    if index != -1:
        return s[:index] + new_sub + s[index+len(sub):]
    else:
        return s

print("Concatenarea lui S1 si S3 : ", concat(S1,S3))
print("Sirul S2 de 5 ori : ", repet(S2,5))
print("Inversul sirului Sigma3 este : " ,inverse(S2))
print("Subsecventa lui S2 de la pozitia 2 pana la pozitia 5", extract(S2, 2, 5))
print("Noul sir inlocuit a lui s2 este: ", replace(S2,'cde','XXX'))