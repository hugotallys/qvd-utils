import os
from qvd import qvd_reader


class TestReadQVDChunk():

    @staticmethod
    def load_qvd_file(file_path):
        try:
            data = qvd_reader.read(file_path)
            if data.shape[0] == 0:
                return None
            return data
        except Exception as e:
            print(f"Error loading QVD file: {e}")
            return None

    def test_qvd_file_loading(self):
        # Replace 'your_qvd_file.qvd' with the path to your QVD file
        qvd_file_path = f'{os.path.dirname(__file__)}/test_files/AAPL.qvd'

        # Try to load the QVD file
        loaded_data = self.load_qvd_file(qvd_file_path)

        print("Loaded data:", loaded_data)

        # Check if the data was successfully loaded
        error_msg = f"Failed to load QVD file: {qvd_file_path}"

        assert loaded_data is not None, error_msg

        # You can add more assertions here to check the structure or
        # content of the loaded data if needed
        # For example, assert len(loaded_data) > 0, "Loaded data is empty"
