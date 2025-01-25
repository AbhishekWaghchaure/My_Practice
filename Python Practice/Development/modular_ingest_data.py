import os
import zipfile
from abc import ABC, abstractmethod
import pandas as pd

## Interface for data ingestor
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        pass

class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path:str) -> pd.DataFrame:
        if not file_path.endswith('.zip'):
            raise ValueError("The provided file is not a .zip file")
        
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall("extracted_data")
            
        extracted_files = os.lisdir("extracted_data")
        csv_files = [f for f in extracted_files if f.endswith(".csv")]
        
        if len(csv_files) == 0:
            raise FileNotFoundError("No CSV file found in the extracted data.")
        if len(csv_files) > 1:
            raise ValueError("Multiple CSV files found.")
        
        csv_file_path = os.path.join("extracted_data", csv_files[0])
        df = pd.readcsv(csv_file_path)
        
        return df
    
    class Direct_CSV_Data_Ingestor(DataIngestor):
        def ingest(self, file_path:str)-> pd.DataFrame:
            ## if direct csv path is given
            if not file_path.endswith('.csv'):
                raise ValueError('The provided file is not a csv file.')
            
            if file_path.endswith(".csv"):
                df = pd.DataFrame(file_path)
            
            ## if folder path is given which has the csv then
            folder = file_path.str.split('/').str[-1]
            files = os.listdir(folder)
            
            csv_files = [f for f in files if f.ends_with(".csv")]
            
            if len(csv_files) == 0:
                raise FileNotFoundError("No CSV file found in the extracted data.")
            
            if len(csv_files) > 0:
                raise ValueError("Multiple CSV files found.")
            
            csv_file_path = os.path.join(file_path, csv_files[0])
            df = pd.DataFrame(csv_file_path)

            return df
        
    ## Implementing Factory Class
    class DataIngestorFactory:
        @staticmethod
        def get_data_ingestor(file_extension: str) -> DataIngestor:
            if file_extension == ".zip":
                return ZipDataIngestor()
            else:
                raise ValueError("No ingestor available for extension {file_extension}") 

# if __name__ == 'main':