print('Bienvenido ')
region = input('Ingrese el estado donde vives ')
match region:
    case 'mexico'|'cancun'|'merida'|'playa'|'tabasco'|'yucatan'|'colima'|'sinaloa'|'michoacan'|'sonora'|'campeche'|'quintana roo':
        print('En estos momenmos hace mucho calor')
        print('esto se debe a distintos factores')
        print('1 altutud baja: la regiones al nivel del mar como las costeras tienden a ser mas calidos ')
        print('2 proximidades de cuerpo de agua : las areas cercanas al oceano tienen climas tropicales calidos')
        print('3 corrientes de aire calidos: los vientos que llegan desde el caribe y el pacifico aportan altas temperaturas ')
        print('recomiendo ir a la playa o prender el ventilador')
    case 'queretaro'|'puebla'|'zacatecas'|'durango'|'jalisco'|'chihuahua'|'veracruz'|'guanajuato'|'coahuila':
        print('En estos momentos hace fio')
        print('esto se debe a distintos factores')
        print('1 altitpud:las zonas altas normalmente son mas frias ')
        print('2 frentes frios:corrientes de aire polar probenientes del norte')
        print('3 relieve montañoso:las montañas modifican los climas y acumulan aire frio')
        print('usa chamarra y no salgas mucho')
    case 'baja california sur'|'nayarit'|'guerrero'|'cuidad de mexico':
        print('Hay un clima calido')
        print('esto se debe a distintos factores')
        print('1 altitud moderada : lugares con altitudes medias suelen tener temperaturas equilibradas')
        print('2 divercidad geografica:las montañas y las planices generan una variedad de microclimas ')
    case 'durango'|'baja california'|'baja california del sur'|'coahuila':
        print('en este lugar suele ser muy desertico')
        print('esto se debe a distintos factores')
        print('1 corrientes de aire seco:las masas de aire que circulsn en estas areas no contienen mucha humedad')
        print('2 alejamientos de cuerpo de agua:la distancia del oceano reduce la posibilidad de humedad del ambiente')
        print('3 radiacion solar: estas areas entan expuestas a mucha rediacion')