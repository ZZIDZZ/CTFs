origin = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C"
,"D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
enc = ["[","\\","]","^","_","`","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","v","6","7","8","9"
,":",";","<","=",">","?","@","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Q"]
ct = """6G:653"""

dec = ""
for char in ct:
    try:
        dec+=origin[enc.index(char)]
    except:
        dec+="_"
print(dec)

"""Tony_he_ad_oy_ot_cared_f_he_at_o_"""
"""TonyTheBadBoyGotScaredOfTheFatBo_"""