"""Convert an explicitly selected JSON file without machine-specific paths."""
import argparse
from pathlib import Path


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Input JSON file")
    parser.add_argument("output", type=Path, help="Output CSV file")
    args = parser.parse_args(argv)

    import pandas as pd

    frame = pd.read_json(args.input)
    frame.to_csv(args.output, index=False)


if __name__ == "__main__":
    main()
