import os
import datetime

rd, wd = os.pipe() 
r, w = os.fdopen(rd, 'rb', 0), os.fdopen(wd, 'wb', 0)  
pid = os.fork()

if pid:  #padre
    w.close()
    while True:
        fecha_hora = r.readline()
        if not fecha_hora:
            break  
        print(fecha_hora.decode())

else:  
    r.close()
    fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
    w.write(fecha_hora_actual.encode('utf8'))
    
    