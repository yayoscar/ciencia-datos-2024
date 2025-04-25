lista = ['tacos','carnitas','asada']
for lis in lista:
    archivo=open(f'{lis}.txt','w')
    archivo.write(lis)
    archivo.close()