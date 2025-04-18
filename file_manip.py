ffile = input("Enter the file name: ")
try:
    fopen = open(ffile)
except:
    print("File not found")
    quit()

count = 0
for line in fopen:
    if line.startswith("By"):
        count += 1
print("There are", count, "lines in the file", ffile)

