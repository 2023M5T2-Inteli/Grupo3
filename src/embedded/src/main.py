import sys

sys.path.append('Script')  # Add the path to the script folder

if __name__ == '__main__':
    import modules.controller as Controller

    # Controller.main()
    from base.api import *
    from DobotEDU import *

    m_lite.set_ptpcmd(ptp_mode=0, x=250, y=0, z=50, r=0)
    m_lite.set_homecmd()
