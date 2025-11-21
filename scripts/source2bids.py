import mne
from mne_bids import BIDSPath, write_raw_bids

from src.config import DIR_DATA_SOURCE, DIR_BIDS_ROOT

all_files = list(DIR_DATA_SOURCE.rglob("**/*.snirf"))
file_path = all_files[0]  # just pick the first file for this example

# loop over all files
for file_path in all_files:
    print(f"Converting file: {file_path}")
    # Load the data
    raw = mne.io.read_raw_snirf(file_path, preload=False)

    subject_id = file_path.parts[-3].replace("_", "")  # assuming filename starts with subject ID
    task = file_path.parts[-2]     # assuming task name is the parent folder name

    bids_path = BIDSPath(subject=subject_id, task=task, root=DIR_BIDS_ROOT)
    write_raw_bids(raw, bids_path, overwrite=True)