import binascii

with open("quirky2") as fd_in, open("test.png", "wb") as fd_out:
    for line in fd_in:
        chunk = binascii.unhexlify(line.rstrip())
        fd_out.write(chunk)