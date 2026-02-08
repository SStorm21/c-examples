import socket
#الهوست
host = '192.168.0.116'
port = 9099
#سوكيت السيرفر على تي سي بي 
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port)) # ضمان عمل السيرفر و تحويله من خلال البايند
server.listen(5) #نضعه على الأستماع و نحدد مرات التسجيل بخمس و ان زادت رفض التسجيل 

while 1: # عملية الموافقة 
    cummunacation_socket , address = server.accept()  #القبول
    
    print(f'connect to :{address}') # تأكيد الاتصال و عرض عنوان المتصل
    message = cummunacation_socket.recv(1024) # تحديد حزمة الاستلام ب 1024 بايت
    print(f'message form client is :{message}') # عرض رسالة المستخدم في الشاشة العامة
    cummunacation_socket.send(f'gpt ur message! thank u'.encode('utf-8')) # ارسال رسالة للمستخدم و تشفيرها 
    cummunacation_socket.close() # قفل السيرفر 