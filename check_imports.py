def check_imports():
    try:
        import docx
    except ImportError:
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "python-docx"])

if __name__ == "__main__":
    check_imports()