from asfamcparser import ParseAMC

parsed_amc = ParseAMC("C://coding//mocapPlayer//79_01.amc")

arr = []

for frame in parsed_amc.amc:
    frame_arr = []
    for feature in frame:
        for f in frame[feature]:
            frame_arr.append(f)

    arr.append(frame_arr)

print(arr)
print(len(arr))
print(len(arr[0]))