from pathlib import Path

from transit_toolkit.gtfs import GTFSReader

# Project root
project_root = Path(__file__).resolve().parents[1]

# GTFS folder
gtfs_folder = project_root / "datasets" / "sample_gtfs"

reader = GTFSReader(gtfs_folder)

stops = reader.load_stops()

print("===== GTFS Stops =====")
print(stops)