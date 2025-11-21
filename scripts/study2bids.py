from mne_bids import BIDSPath, make_dataset_description
import json
from pprint import pprint

from src.config import DIR_BIDS_ROOT

subject_id = "01"
task = "rest"
bids_path = BIDSPath(subject=subject_id, task=task, root=DIR_BIDS_ROOT)

make_dataset_description(
    path=bids_path.root,
    name="FNIRS study UOL",
    authors=["Aykut Eken", "Cornelia Kranczioch"],
    data_license="CC0",
    ethics_approvals=["ID UOL"],
    funding=[
        "DFG NNNNN",
    ],
    overwrite=True,
)
desc_json_path = bids_path.root / "dataset_description.json"
with open(desc_json_path, encoding="utf-8-sig") as fid:
    pprint(json.loads(fid.read()))
