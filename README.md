# lunh

# Calcula dígito verificador de IMEI.

Existe um testcase utilizando o módulo unittest, para executar:
```
python test.py -v
```

# Exemplo de uso:

```
import lunh

if __name__ == '__main__':

  # passe somente os 14 primeiros dígitos do IMEI
  digito = lunh.calc_dig_imei('35780502398494')
  
  print(digito)
```
