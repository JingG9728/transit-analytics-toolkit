"""
GTFS Reader Module

This module provides functions to read GTFS files.
"""

"""
GTFS Reader Module
==================

This module provides tools for reading GTFS files.

Author: Jing
Project: Transit Analytics Toolkit
"""

from pathlib import Path
import pandas as pd


class GTFSReader:
    """
    A simple GTFS reader.
    """

    def __init__(self, gtfs_folder):
        """
        Parameters
        ----------
        gtfs_folder : str
            Folder containing GTFS txt files.
        """

        self.gtfs_folder = Path(gtfs_folder)

    def load_stops(self):
        """
        Read stops.txt
        """

        file = self.gtfs_folder / "stops.txt"

        return pd.read_csv(file)