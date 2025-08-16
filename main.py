import argparse
import sys
import os
import pathlib

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str, help="Input file")
    parser.add_argument("output", type=str, help="Output file")
    args = parser.parse_args()

    input_path = pathlib.Path(args.input)
    output_path = pathlib.Path(args.output)

    if not input_path.exists():
        print(f"Input file {input_path} does not exist")
        return
    
    # パスがファイルかディレクトリかを判定
    if input_path.is_file():
        print(f"{input_path} はファイルです")
    elif input_path.is_dir():
        print(f"{input_path} はディレクトリです")
    else:
        print(f"{input_path} はファイルでもディレクトリでもありません（シンボリックリンクなど）")

    print(f"Converting {args.input} to {args.output}")


if __name__ == "__main__":
    main()
