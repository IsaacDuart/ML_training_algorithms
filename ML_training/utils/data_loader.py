from pathlib import Path
import pandas as pd

class DataLoader:

    def load_data(analisis):
        
        base_path = Path.cwd().parents[3] / "data" / "processed" / analisis
        
        X_train = pd.read_csv(base_path / "x_train.csv", header=None).values
        y_train = pd.read_csv(base_path / "y_train.csv", header=None).values.flatten()

        X = pd.read_csv(base_path / "x.csv", header=None).values
        y = pd.read_csv(base_path / "y.csv", header=None).values.flatten()

        X_test = pd.read_csv(base_path / "x_test.csv", header=None).values
        y_test = pd.read_csv(base_path / "y_test.csv", header=None).values.flatten()

        return X_train, y_train, X_test, y_test, X, y
    
    
    def export_data(analisis, X_train, X_test, X, y, y_train, y_test):
        
        base_path = Path.cwd().parents[1] / "data" / "processed" / analisis
        
        pd.DataFrame(X_train).to_csv(base_path / "x_train.csv" , index=False, header=False)
        pd.DataFrame(X_test).to_csv(base_path / "x_test.csv",  index=False, header=False)

        pd.DataFrame(X).to_csv(base_path / "x.csv",  index=False, header=False)
        pd.DataFrame(y).to_csv(base_path / "y.csv", index=False, header=False)

        pd.DataFrame(y_train).to_csv(base_path / "y_train.csv",  index=False, header=False)
        pd.DataFrame(y_test).to_csv(base_path / "y_test.csv",  index=False, header=False)