class FeatureEngineer:
    def __init__(self, df):
        self.df = df

    def preprocess(self):
        df = self.df.copy()

        # Drop irrelevant columns
        df = df.drop(columns=['Datetime'], errors='ignore')  # Remove timestamp if present
        df = df.dropna(axis=1)  # Drop columns with NaNs

        # Handle fault_type
        if 'fault_type' in df.columns:
            X = df.drop(columns=['fault_type'])
            y = df['fault_type']
        else:
            X = df
            y = None

        return X, y
