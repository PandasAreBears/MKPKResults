from pathlib import Path

from file_system import get_standard_bins

i: int = 0
for bin_filepath in get_standard_bins(100):
    bin_name = Path(bin_filepath).name
    if (bin_name) == "dpkg-maintscript-helper":
        print(i)
        break

    i += 1
