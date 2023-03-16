from io import TextIOWrapper
from pathlib import Path

import vt

id = 0
file_handle: TextIOWrapper = None


def _init_results_csv() -> TextIOWrapper:
    """
    Returns a handle to the CSV file. Creates a new file if it doesn't already
    exist, and adds the headings.
    """
    csv_filepath = str(Path(__file__).parent.parent.parent / "data" / "results.csv")

    if Path(csv_filepath).is_file():
        return open(csv_filepath, "a")

    else:
        file = open(csv_filepath, "w")
        file.write(
            ",".join(["id", "original", "file", "av", "category", "result"]) + "\n"
        )
        return file


def write_result_to_file(
    original_name: str, binary_name: str, analysis: vt.object.Object
):
    global id, file_handle

    for result in analysis.results.items():
        file_handle.write(
            ",".join(
                [
                    str(id),
                    original_name,
                    binary_name,
                    result[0],
                    result[1]["category"],
                    str(result[1]["result"]),
                ]
            )
            + "\n"
        )

        id += 1


def result_csv_start():
    global file_handle
    file_handle = _init_results_csv()


def result_csv_end():
    file_handle.close()
