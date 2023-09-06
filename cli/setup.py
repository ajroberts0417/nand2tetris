import os
import sys
from pathlib import Path


def main():
    cli_script_name = "nand.py"
    cli_path = Path(__file__).resolve().parent / cli_script_name
    bin_dir = Path.home() / "bin"
    symlink_path = bin_dir / "nand"

    # Make the Python script executable
    os.chmod(cli_path, os.stat(cli_path).st_mode | 0o111)

    # Create ~/bin directory if it doesn't exist
    bin_dir.mkdir(exist_ok=True)

    # Create symbolic link in ~/bin
    if symlink_path.exists():
        symlink_path.unlink()
    symlink_path.symlink_to(cli_path)

    # Check if ~/bin is in PATH. If not, add it to the shell startup file
    if str(bin_dir) not in os.environ["PATH"].split(":"):
        default_shell = os.path.basename(os.environ["SHELL"])

        if default_shell == "bash":
            startup_file = Path.home() / ".bashrc"
        elif default_shell == "zsh":
            startup_file = Path.home() / ".zshrc"
        else:
            print(
                f"Unsupported shell: {default_shell}. Manually add {bin_dir} to your PATH."
            )
            sys.exit(1)

        with open(startup_file, "a") as file:
            file.write(f"\nexport PATH=$PATH:{bin_dir}\n")

    print(
        "CLI has been added to your path. Restart your terminal or source your shell's startup file to start using 'nand' command."
    )


if __name__ == "__main__":
    main()
