# ExamenMeli-MagnetoApi
El Proyecto MagnetoAPI consiste en un API REST que permite identificar si es un humano o mutante dado la secuencia de ADN, adicionalmente almacena los datos y muestra la cantidad de humanos y mutantes que se han identificado. 


Para acceder a la aplicación accede a esta URL:
http://magneto-api-2701.eastus2.azurecontainer.io/

Para consumir el endPoint Mutant ingresar a la  URL:
http://magneto-api-2701.eastus2.azurecontainer.io/mutant
 
con el siguiente body:

```json
{
"dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
}
```

Si la validación resulta ser un mutante el response retorna el mensaje "Es un mutante" concatenado con la secuencia de ADN
En caso de que no retorna Error 403 Forbidden 
