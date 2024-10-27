import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    try:
        import pygame
    except ImportError:
        print("pygame not found, installing...")
        install("pygame")

if __name__ == "__main__":
    main()