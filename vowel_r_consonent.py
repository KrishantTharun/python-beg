ya=input()
if ya.isalpha():
    print (ya)
    xa=ya.lower()
    if xa=='a' or xa=='e' or xa=='i' or xa=='o' or xa=='u':
        print("Vowel")
    else:
        print(" Consonant")
else:
    print("Invalid")
    

