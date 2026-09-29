import time 
import subprocess
import pyautogui
import core.keys as keys
from core.wyrm_manager import BaseWyrmManager

class PyAutoGuiWyrmManager(BaseWyrmManager):
    """Manage Wyrm via subprocesses and pyautogui
    Cross platform, but it globally takes over the input, so you need the terminal 
    constantly on focus during test run
    """
    Wyrm_START_DELAY : float = 0.5
    def __init__(self, wyrm_path : str):
        super().__init__(wyrm_path)
        self.wyrm_process = None


    def start_wyrm(self, start_dir : str = None, args : list[str] = None) -> None:
        wyrm_args = [self.wyrm_path]
        if args :
            wyrm_args += args
        wyrm_args.append(start_dir)

        self.wyrm_process = subprocess.Popen(wyrm_args,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(PyAutoGuiWyrmManager.Wyrm_START_DELAY)

        # Need to send a sample keypress otherwise it ignores first keypress
        self.send_text_input('x')
        
    
    def send_text_input(self, text : str, all_at_once : bool = False) -> None:
        if all_at_once :
            pyautogui.write(text)
        else:
            for c in text:
                pyautogui.write(c)

    def send_special_input(self, key : keys.Keys) -> None:
        if isinstance(key, keys.CtrlKeys):
            pyautogui.hotkey('ctrl', key.char)
        elif isinstance(key, keys.SpecialKeys):
            pyautogui.press(key.key_name.lower())
        else:
            raise Exception(f"Unknown key : {key}") 

    def get_rendered_output(self) -> str:
        return "[Not supported yet]" 
    
    
    def is_wyrm_running(self) -> bool:
        self._is_wyrm_running = (self.wyrm_process is not None) and (self.wyrm_process.poll() is None)
        return self._is_wyrm_running
    
    def close_wyrm(self) -> None:
        if self.wyrm_process is not None:
            self.wyrm_process.terminate()
    
    # Override
    def runtime_info(self) -> str:
        if self.wyrm_process is None:
            return "[No process]"
        else:
            return f"[PID : {self.wyrm_process.pid}, poll : {self.wyrm_process.poll()}]"  



