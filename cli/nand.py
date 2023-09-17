#!/usr/bin/env python3

import argparse
import subprocess
from pathlib import Path

nand2tetris_path = Path(__file__).resolve().parent.parent


def run_shell_script(script_name):
    script_path = nand2tetris_path / "tools" / script_name
    subprocess.run(["bash", str(script_path)])


def main():
    parser = argparse.ArgumentParser(description="Nand command line utility")
    subparsers = parser.add_subparsers(dest="command", title="Commands")

    # Define subparsers for each command
    subparsers.add_parser("help", help="Display this help message")
    subparsers.add_parser("hardware", help="Runs HardwareSimulator.sh")
    subparsers.add_parser("cpu", help="Runs CPUEmulator.sh")
    subparsers.add_parser("assembler", help="Runs Assembler.sh")
    subparsers.add_parser("vm", help="Runs VMEmulator.sh")
    subparsers.add_parser("jackcompiler", help="Runs JackCompiler.sh")

    args = parser.parse_args()

    if not args.command or args.command == "help":
        parser.print_help()
    elif args.command == "hardware":
        run_shell_script("HardwareSimulator.sh")
    elif args.command == "cpu":
        run_shell_script("CPUEmulator.sh")
    elif args.command == "assembler":
        run_shell_script("Assembler.sh")
    elif args.command == "vm":
        run_shell_script("VMEmulator.sh")
    elif args.command == "jackcompiler":
        run_shell_script("JackCompiler.sh")
    else:
        print(
            f"Unknown command '{args.command}', please run 'nand help' for a list of commands."
        )


if __name__ == "__main__":
    main()
