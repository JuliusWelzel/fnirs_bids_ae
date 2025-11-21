from pathlib import Path


def define_dir(root, *names):
    """define_dir create path handle and creates dir if not existend.

    Args:
        root (str): root to directory of interest
        names (tuple): subdirectories as separate arguments

    Returns:
        pathlib.Path: Pathlib handle of dir
    """
    path = Path(root)
    for name in names:
        path = path / name 
    path.mkdir(parents=True, exist_ok=True)
    return path

# If the user is not known, assume that the project is in the current working directory
DIR_PROJ = Path.cwd().parent


###############################################################################
# These are relevant directories which are used in the analysis.

DIR_DATA = define_dir(DIR_PROJ, "data")
DIR_DATA_SOURCE = Path(r"W:\data\projects\ae_fnirs_phy\source\AllSubjects\fNIRS_Data")
DIR_BIDS_ROOT = Path(r"W:\data\projects\ae_fnirs_phy\bids")