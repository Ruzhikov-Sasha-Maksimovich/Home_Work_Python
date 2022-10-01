intervalx = int(input("x: "))
intervaly = int(input("y: "))
if intervalx > 0 and intervaly > 0:
    print("2")
if intervalx < 0 and intervaly > 0:
    print("1")
if intervalx < 0 and intervaly < 0:
    print("3")
if intervalx > 0 and intervaly < 0:
    print("4")