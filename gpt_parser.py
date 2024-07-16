from asfamcparser import ParseAMC
import math
import torch
import os

folder_path = "C://coding//HIP-preprocessing-amc//mocapPlayer"

batch_size = 32

master_list = []

def batching(amc, batch_size):
    flattened_frames = []

    # Flatten the frames
    for frame in amc:
        frame_arr = []
        for feature in frame:
            for f in frame[feature]:
                frame_arr.append(f)
        flattened_frames.append(frame_arr)

    # batched_arr = []
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
            # batch = flattened_frames[:padding_needed] + batch
            batch.extend(flattened_frames[:padding_needed])
        
        
        # batched_arr.append(batch)
        master_list.append(batch)
    # master_list.extend(batched_arr)

for filename in os.listdir(folder_path):
    if filename.endswith(".amc"):
        file_path = os.path.join(folder_path, filename)
        parsed_amc = ParseAMC(file_path).amc
        batching(parsed_amc, batch_size)


a_tensor =  torch.tensor(master_list, dtype=torch.float32)

print(a_tensor.shape)
