import pandas as pd
import glob
import os

class DataLoader:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_file(self, filename, fault_type):
        df = pd.read_csv(os.path.join(self.data_dir, filename))
        df['fault_type'] = fault_type
        return df

    def load_labeled_data(self):
        # Map file names to fault labels
        file_labels = {
            "PFPU_ReheatVLVStuck_0%.csv": 0,
            "PFPU_ReheatVLVStuck_50%.csv": 1,
            "PFPU_ReheatVLVStuck_100%.csv": 1
        }
        frames = []
        for file, label in file_labels.items():
            df = self.load_file(file, label)
            frames.append(df)
        return pd.concat(frames, ignore_index=True)
