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
    parser.add_argument("command", nargs="?", default="help", help="Command to execute")
    args = parser.parse_args()

    if args.command == "help":
        parser.print_help()
        print("\nCommands:")
        print("  hardware: Runs HardwareSimulator.sh")
        print("  cpu: Runs CPUEmulator.sh")
        print("  assembler: Runs Assembler.sh")
        print("  vm: Runs VMEmulator.sh")
        print("  jackcompiler: Runs JackCompiler.sh")
        print("\n")

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
        print(f"Unknown command '{args.command}', please run 'nand help' for a list of commands.")

if __name__ == "__main__":
    main()
