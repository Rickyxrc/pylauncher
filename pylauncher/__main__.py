import os, rich, time
from os.path import dirname
from rich.console import Console
# import survey
import pathlib
import random
from simple_term_menu import TerminalMenu

def rnd():
    charset = "1234567890qwertyuiopasdfghjklzxcvbnm"
    return ''.join([random.choice(charset) for _ in range(8)])

console = Console()
# console.log("hello!")

homePath = pathlib.Path(os.path.expanduser("~"))
dirPath = homePath / "active"
archivePath = homePath / "archive"

files = [ str(dirPath / f) for f in os.listdir(dirPath) ] + \
    [ str(archivePath / f) for f in os.listdir(archivePath) ] + \
    [ str(homePath / "nix-config") ]

# console.print(files)

# result = survey.routines.select("project to open: ", options=files)
Terminal = TerminalMenu(files)
result = Terminal.show()

resPath = files[result]

console.log(f"selected {resPath}")

session_name = f"launcher_{rnd()}"

console.log(f"session name {session_name}")

os.system(f"tmux new-session -d -s {session_name}")
# debug only.
# os.system(f"kitty tmux attach-session -t {session_name} &")

time.sleep(0.3)

os.system(f"tmux send-keys -t {session_name} cd space \"{resPath}\" enter")
os.system(f"tmux send-keys -t {session_name} neovide enter")
os.system(f"tmux send-keys -t {session_name} exit enter")

