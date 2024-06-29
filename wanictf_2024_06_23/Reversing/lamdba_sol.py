decflag = []
flag = "16_10_13_x_6t_4_1o_9_1j_7_9_1j_1o_3_6_c_1o_6r"

flag=(chr(int(c,36) +10) for c in flag.split('_') )

flag = ''.join(flag)

for c in flag: 
    c = chr((((ord(c)^123)-12+3) ) )
    decflag.append(c)
flag = ''.join(decflag)
print(flag ,end="\n") 
#FLAG{l4_1a_14mbd4}
