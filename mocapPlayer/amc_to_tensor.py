import torch
import os
def _read_line(stream, idx):
    if idx >= len(stream):
        return None, idx
    line = stream[idx].strip().split()
    idx += 1
    return line, idx
def parse_amc(file_path):
    with open(file_path) as f:
        content = f.read().splitlines()
    for idx, line in enumerate(content):
        if line == ':DEGREES':
            content = content[idx + 1:]
            break
    frames = []
    total_frames = 1
    idx = 0
    line, idx = _read_line(content, idx)
    assert line[0].isnumeric(), line  # Ensure the first line starts with a frame number
    EOF = False  # End of file
    while not EOF:
        joint_degree = {}
        while True:
            line, idx = _read_line(content, idx)
            if line is None:
                EOF = True  # Set EOF flag if no more lines
                break
            if line[0].isnumeric():
                total_frames +=1
                break  # Break if the line starts with a frame number
            joint_degree[line[0]] = [float(deg) for deg in line[1:]]  # Parse joint degrees
        frames.append(joint_degree)
    print(f"Total number of frames: {total_frames}")
    return frames

parsed_amc = parse_amc('79_90.amc')