"""
Lunh
Cálcula digito verificador do IMEI
Genésio Sátiro
"""

import sys


# Os valores que foram dobrados devem ser
# somados se este possuírem mais de um digito.
def soma_digitos(str_num):    
    
    return sum([int(i) for i in str_num])


# Cálcula e retorna dígito verificador do
# IMEI     
# Passe somente as 14 primeiras posições
def calc_dig_imei(IMEI):

    # Soma os números não dobrados
    soma = sum([int(i) for i in IMEI[::2]])

    # Soma os números dobrados
    soma += sum([soma_digitos(str(int(i)*2)) for i in IMEI[1::2]])

    # Cálcula o resto da divisão da soma por 10
    resto = (soma % 10)

    # Cálcula o dígito IMEI
    digito = 0 if resto == 0 else (10 - resto)

    return digito


# Rotina principal
if __name__ == '__main__':    

    # Testa argumento(IMEI) passado via linha de comando
    if sys.argv[1:]:

        # Pega número IMEI
        IMEI_NUMERO = sys.argv[1]

        # Cálcula o dígito IMEI
        digito = calc_dig_imei(sys.argv[1][:-1])

        print('Digito IMEI passado  : {}'.format(IMEI_NUMERO[-1]))
        print('Digito IMEI calculado: {}'.format(digito))        

        if (digito == int(IMEI_NUMERO[-1])):
            print('IMEI: {} é válido!'.format(IMEI_NUMERO))
        else:
            print('IMEI: {} é inválido!'.format(IMEI_NUMERO))

    else:

        print('Uso: python lunh "IMEI numero"')
        