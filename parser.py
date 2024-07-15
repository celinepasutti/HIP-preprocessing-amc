from asfamcparser import ParseAMC

parsed_amc = ParseAMC("C://coding//mocapPlayer//79_01.amc")

arr = []

for feature in parsed_amc.amc[0]:
    for val in parsed_amc.amc[0][feature]:
        arr.append(val)

print(len(arr))
print(arr)