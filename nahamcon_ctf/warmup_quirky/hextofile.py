import binascii

<<<<<<< HEAD
with open("quirky2") as fd_in, open("test.png", "wb") as fd_out:
=======
with open("quirky") as fd_in, open("test", "wb") as fd_out:
>>>>>>> 369cc87cfd952ae3ccb1d0017e91549703634b6b
    for line in fd_in:
        chunk = binascii.unhexlify(line.rstrip())
        fd_out.write(chunk)