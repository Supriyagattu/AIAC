data = open("input.txt","w")
output = open("output.txt","w")
for line in data:
    output.write(line.upper())
output.close()
print("Processing done,")