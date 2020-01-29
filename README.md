
# AzureFunction

## Introducción

El proyecto AzureFunction es aquel proyecto que define una función ejemplo de Azure Function.

La referencia documental de Azure Function se ubica en el [siguiente enlace](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#outputs).

## Instalación del paquete Azure Functions Tools

Desde la línea de comandos, ejecutar la siguiente secuencia de comandos:
 
```
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-ubuntu-$(lsb_release -cs)-prod $(lsb_release -cs) main" > /etc/apt/sources.list.d/dotnetdev.list'
sudo apt-get update
sudo apt-get install azure-functions-core-tools        
```

## Comandos de Azure Functions Tools

1.- Instalación del entorno virtual 

```
sudo apt-get install python3-venv
```

2.- Creación de un proyecto
```
func init MyFunctionProj
```

3.- Creación de una función
```
func new
```
  
4.- Ejecución del entorno local de desarrollo
  
```  
func host start
```  

## Despliegue del proyecto en Azure

1.- Crear una función en Azure.

2.- Ejecutar el siguiente comando:func azure functionapp publish <NOMBRE-FUNCIÓN> --build remote. Si la función creada 
en el apartado uno es test-app, el comando de despliegue es el siguiente:

```  
func azure functionapp publish test-app --build remote
```  
    

## Funciones ejemplo del proyecto

El proyecto contiene dos funciones como ejemplo de uso.

### FunctionBase

Función simple desencadenador HTTP. La función realiza la lectura de un campo fecha de las cabeceras y de un campo name del body.

+ Si se arranca la aplicación en modo local, el comando con la petición HTTP es el siguiente:

```  
curl -v  -w '\n' -d '{"name":"pp"}' -H 'DateData: 2019/11/26' -H 'Content-Type: application/json' -X POST  http://localhost:7071/api/FunctionDataFactory
```  
    
+ Si se despliega la función en Azure, el comando con la petición HTTP es la siguiente:

```  
curl -v  -w '\n' -d '{"name":"pp"}' -H 'DateData: 2019/11/26' -H 'Content-Type: application/json' -X POST  https://<URL-AZURE>.net/api/FunctionDataFactory?code=<FUNCTION_KEY>
```  
 

### FunctionStore

Función que realiza el copiado de un fichero, cuyo nombre es pasado por parámetro en una petición HTTP, en otro Store.
    
+ Si se arranca la aplicación en modo local, el comando con la petición HTTP es el siguiente:

```  
curl -v -w '\n' -H 'DateHeader: 2019/11/26' -d '{ "param1": "value1", "param2": "value2" }'   -X GET http://localhost:7071/api/FunctionEjemCore/watermark?name=11    
```

+ Si se despliega la función en Azure, el comando con la petición HTTP es la siguiente:  

```  
curl -v -w '\n' -H 'DateHeader: 2019/11/26' -d '{ "param1": "value1", "param2": "value2" }'   -X GET http://<URL-AZURE>.net/api/FunctionEjemCore/watermark?name=11    
```

---


# AzureFunction

## Introduction

The AzureFunction project is that project that defines an example Azure Function function.

The Azure Function documentary reference is located in the [following link](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#outputs).

## Azure Functions Tools package installation

From the command line, run the following script:
 
```
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-ubuntu-$(lsb_release -cs)-prod $(lsb_release -cs) main" > /etc/apt/sources.list.d/dotnetdev.list'
sudo apt-get update
sudo apt-get install azure-functions-core-tools        
```

## Azure Functions Tools Commands

1.- Virtual Environment Installation

```
sudo apt-get install python3-venv
```

2.- Creation of a project
```
func init MyFunctionProj
```

3.- Creation of a function
```
func new
```
  
4.- Execution of the local development environment
  
```  
func host start
```  

## Project deployment in Azure

1.- Create a function in Azure.

2.- Execute the following command: ** func azure functionapp publish <NAME-FUNCTION> --build remote **. If the function created
In section one it is test-app, the deployment command is as follows:

```  
func azure functionapp publish test-app --build remote
```  
    

## Functions project example

The project contains two functions as an example of use.

### FunctionBase

Simple HTTP trigger function. The function reads a date field of the headers and a field name of the body.

+ If the application is started in local mode, the command with the HTTP request is as follows:

```  
curl -v  -w '\n' -d '{"name":"pp"}' -H 'DateData: 2019/11/26' -H 'Content-Type: application/json' -X POST  http://localhost:7071/api/FunctionDataFactory
```  
    
+ If the function is deployed in Azure, the command with the HTTP request is as follows:

```  
curl -v  -w '\n' -d '{"name":"pp"}' -H 'DateData: 2019/11/26' -H 'Content-Type: application/json' -X POST  https://<URL-AZURE>.net/api/FunctionDataFactory?code=<FUNCTION_KEY>
```  
 

### FunctionEjemCore

Function that performs the copying of a file, whose name is passed by parameter in an HTTP request, in another Store.
    
+ If the application is started in local mode, the command with the HTTP request is as follows:

```  
curl -v -w '\n' -H 'DateHeader: 2019/11/26' -d '{ "param1": "value1", "param2": "value2" }'   -X GET http://localhost:7071/api/FunctionEjemCore/watermark?name=11    
```

+ If the function is deployed in Azure, the command with the HTTP request is as follows:

```  
curl -v -w '\n' -H 'DateHeader: 2019/11/26' -d '{ "param1": "value1", "param2": "value2" }'   -X GET http://<URL-AZURE>.net/api/FunctionEjemCore/watermark?name=11    
```


