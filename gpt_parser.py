from asfamcparser import ParseAMC
import math

folder_path = 

batch_size = 32

master_list = []

for filename in os.listdir(folder_path)
    if filename.endswith(".amc")
        file_path = os.path.join(folder_path, filename)
        parsed_amc = ParseAMC(file_path)
        batching(parsed_amc, batch_size)


def batching(amc, batch_size):
    flattened_frames = []

    # Flatten the frames
    for frame in amc:
        frame_arr = []
        for feature in frame:
            for f in frame[feature]:
                frame_arr.append(f)
        flattened_frames.append(frame_arr)

    batched_arr = []
    total_frames = len(flattened_frames)
    num_batches = math.ceil(total_frames / batch_size)  # Calculate number of batches

    # Create batches with padding for the last batch if necessary
    for i in range(num_batches):
        start_idx = i * batch_size
        end_idx = start_idx + batch_size
        batch = flattened_frames[start_idx:end_idx]
        
        # Check if padding is needed for the last batch
        if len(batch) < batch_size:
            padding_needed = batch_size - len(batch)
            batch = flattened_frames[:padding_needed] + batch
        
        batched_arr.append(batch)
    
    master_list = master_list.append(batched_arr)



print(len(batching(parsed_amc.amc, 32)[19]))
