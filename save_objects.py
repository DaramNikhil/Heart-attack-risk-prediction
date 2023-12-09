import pickle
import os
import logging

def object_saving(file, file_path: str):

    try:
        """_summary_

        Args:
            file_path (str): pickle file was stored in this location
            file (pickle): it returns the pickle file
        """

        with open(file_path, "wb") as f:

            pickle.dump(file, f)

    except Exception as e:
        logging.info("Failed to save objects: {}".format(e))

        





