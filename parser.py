from asfamcparser import ParseAMC

parsed_amc = ParseAMC("C://coding//mocapPlayer//79_01.amc")

def batching(amc, batch_size):
    batched_arr = []
    for frame in amc:
        frame_arr = []
        for feature in frame:
            for f in frame[feature]:
                frame_arr.append(f)
        batched_arr.append(frame_arr)

    return batched_arr



print(batching(parsed_amc.amc, 32))