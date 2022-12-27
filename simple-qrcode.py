import qrcode as qr

image=qr.make('''
              Name-        Krishnmohan
              Email-       krishnmohan0024@gmail.com
              Mobile-      7415373407
              Portpholiyo- https://krishnaaryan.netlify.app/
              ''')
image.save("my-qr.png")