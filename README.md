# Obtener GEO Localización
### Estructura básica para obtener coordenadas a partir de una dirección con calle y número
Este ejemplo es funcional pero requiere de trabajo adicional para una solución productiva. Es un script básico en lenguaje Python para que a partir de un archivo .CSV que contiene al menos un campo "Direccion", se genere un nuevo archivo .CSV que contenga una columna con las coordenadas geográficas. 
Se utiliza Flask como micro framework web para generar una página que permita subir un archivo CSV para procesarlo, invocando el servicio "direcUnica" de IDE para cada valor del campo "Direccion", obteniendo su geolocalización (coordenadas latitud, longitud).

