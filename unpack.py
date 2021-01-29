def unpack(x, z, y):
    res = x**z + y
    return res

my_list = [2, 2, 3]
print(unpack(*my_list)) #распакавка параметров из листа

my_dict = {"x": 3, "y": 3, "z": 3}

print(unpack(**my_dict)) #распакавка параметров из словаря