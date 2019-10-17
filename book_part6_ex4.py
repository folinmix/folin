a='Где это? Кто это? Когда это?'

b=a.replace("?","?$")
b=b.split("$")
b=b[0:-1]


print(b)
