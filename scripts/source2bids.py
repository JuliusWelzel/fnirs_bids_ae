import mne
from mne_bids import BIDSPath, write_raw_bids

from src.config import DIR_DATA_SOURCE, DIR_BIDS_ROOT

all_files = list(DIR_DATA_SOURCE.rglob("*.snirf"))
file_path = all_files[0]  # just pick the first file for this example

# Load the data
raw = mne.io.read_raw_snirf(file_path, preload=False)
raw.info["line_freq"] = 50  # specify power line frequency as required by BIDS

# Sanity check, show the optode positions
raw.plot_sensors()

subject_id = "01"
task = "rest"

bids_path = BIDSPath(subject=subject_id, task=task, root=DIR_BIDS_ROOT)
write_raw_bids(raw, bids_path, overwrite=True)