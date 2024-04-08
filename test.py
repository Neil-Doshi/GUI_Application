import os
 
path = 'C:\\Users\\abupt\\Downloads\\Lancaster'

# for count, f in enumerate(os.listdir()):
#     try:
#         if f.endswith('.pdf'):
#             new_name = f[:2]+"_"+f[3:]

#     except:
#         pass



rev = {}

curr = path + "\\DRAWING"
os.chdir(curr)
chk = []
for count, f in enumerate(os.listdir()):
    try:
        if f.endswith('.dwg'):
            if f[11:15] not in chk:
                chk.append(f[11:15])
                new_name = f[:2]+"_"+f[3:18]+"-"+"01.dwg"
            elif f[11:15] in chk:
                new_name = f[:2]+"_"+f[3:18]+"-"+"02.dwg"
        elif f.endswith('.pdf'):
            if f[11:15] not in rev:
                x = f[11:15]
                rev[x] = f[-5]
            new_name = f[:2]+"_"+f[3:]
        # print(new_name)
        # os.rename(f, new_name)
    except:
        pass

print("Drawings Done!")
# print(f"{rev = }")

curr = path + "\\BOM"
os.chdir(curr)
for count, f in enumerate(os.listdir()):
    try:
        if f.endswith('.pdf'):
            new_name = f[:2]+"_"+f[3:15]+"-CS-"+rev[f[11:15]]+"_BOM.pdf"
        # elif f.endswith('.xlsx'):
        #     new_name = f[:2]+"_"+f[3:15]+"-CS-"+rev[f[11:15]]+"_BOM.xlsx"
        # print(new_name)
        os.rename(f, new_name)
    except:
        pass

print("BOM Done!")

curr = path + "\\IO LIST"
os.chdir(curr)
for count, f in enumerate(os.listdir()):
    try:
        # new_name = f[:2]+"_"+f[3:15]+"-CS-"+rev[f[11:15]]+"_IO_List.xls"
        if f.endswith('.pdf'):
            new_name = f[:2]+"_"+f[3:15]+"-CS-"+rev[f[11:15]]+"_IO_List.pdf"
        # elif f.endswith('.xlsx'):
        #     new_name = f[:2]+"_"+f[3:15]+"-CS-"+rev[f[11:15]]+"_IO_List.xlsx"
        # print(new_name)
        # os.rename(f, new_name)
    except:
        pass

print("IO LIST Done!")
