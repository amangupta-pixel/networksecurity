from dataclasses import dataclass
# Dataclass is used for creating vars for anempty classes

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str

