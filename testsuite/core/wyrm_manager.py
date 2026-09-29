from abc import ABC, abstractmethod
import core.keys as keys

class BaseWyrmManager(ABC):

    def __init__(self, wyrm_path : str):
        self.wyrm_path = wyrm_path
        # _ denotes the internal variables, anyone should not directly read/modify
        self._is_wyrm_running : bool = False

    @abstractmethod
    def start_wyrm(self, start_dir : str = None, args : list[str] = None) -> None:
        pass 
    
    @abstractmethod
    def send_text_input(self, text : str, all_at_once : bool = False) -> None:
        pass 

    @abstractmethod
    def send_special_input(self, key : keys.Keys) -> None:
        pass 

    @abstractmethod
    def get_rendered_output(self) -> str:
        pass
    
    
    @abstractmethod
    def is_wyrm_running(self) -> bool:
        """
        We allow using _is_wyrm_running variable for efficiency
        But this method should give the true state, although this might have some calculations
        """
        return self._is_wyrm_running
    
    @abstractmethod
    def close_wyrm(self) -> None:
        """
        Close wyrm if its running and cleanup any other resources
        """
    
    def runtime_info(self) -> str:
        return "[No runtime info]"

