import pickle
from typing import Any

class PersistentPickleStorageMixin(object):
    """
    Enables basic persistent storage using pickle, just make sure to manually save

    Parameters
    ----------
    fn:str
      Name of the file that you're going to write data to, should preferably end in .pkl

    Attributes
    ----------
    fn:str
      Name of the file that you're going to write data to, should preferably end in .pkl

    data:dict
      Dictionary containing the data
    """

    def __init__(self, fn:str) -> None:
        self.fn = fn
        self.data = {}

    def save(self) -> None:
        """
        Saves the data in a pickle file
        """
        with open(self.fn, 'wb') as f:
            pickle.dump(self.data, f)

    def load(self) -> None:
        """
        Loads the data of the pickle file
        """
        with open(self.fn, 'rb') as f:
            self.data = pickle.load(f)

    def __getitem__(self, key:Any) -> Any:
        return self.data[key]

    def __setitem__(self, key:Any, value:Any) -> None:
        self.data[key] = value

    def __delitem__(self, key:Any) -> None:
        del self.data[key]
