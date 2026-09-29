from core.wyrm_manager import BaseWyrmManager
from core.fs_manager import TestFSManager

class Environment:
    """Manage test environment
    Manage cleanup of environment and other stuff at a single place
    """    
    def __init__(self, wyrm_manager : BaseWyrmManager, fs_manager : TestFSManager ):
        self.wyrm_mgr = wyrm_manager
        self.fs_mgr = fs_manager

    def cleanup(self) -> None:
        self.wyrm_mgr.close_wyrm()
        self.fs_mgr.cleanup()