valido = False
print('ingrese su mail:')
mail = input()
if(not '@' in mail):
    print('mail invalido')
elif not '.' in mail.split('@')[1]:
    print('mail invalido')
elif len(mail.split('@')[0])==0:
    print('mail invalido')
elif(len(mail.split('.')[1])<2):
    print('mail invalido')
else:
    if '.' in mail[0] or '.' in mail[-1]:
        print('mail invalido')
    else:
        print('mail valido')