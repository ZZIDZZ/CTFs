from Crypto.Util.number import long_to_bytes as l2b, bytes_to_long as b2l

ergb = [117, 158, 183]
flag = "}"
print(ergb)

new_val = l2b(ergb[2]*ord(flag))
print(f"{ergb[2]} * {ord(flag)} = {bin(ergb[2]*ord(flag))}")

ergb[0] = new_val[0]
if len(new_val) > 1:
    ergb[1] = new_val[1]
ergb[2] = 0

def combineInt(a,b):
    return int("".join([str(bin(i)[2:]).zfill(8) for i in [a,b]]), 2)

new_val = combineInt(80,16)
print(new_val, ergb)