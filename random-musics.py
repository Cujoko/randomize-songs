import math
import random
import shutil
from pathlib import Path

files_portion_size = 255

source_dir_fullpath = Path("c:\\Users\\Cujoko\\Music\\Favorites")

source_dir_name = source_dir_fullpath.stem

for dest_dir_fullpath in [
    x for x in source_dir_fullpath.parent.glob(f"{source_dir_name} # *") if x.is_dir()
]:
    for file_fullpath in dest_dir_fullpath.iterdir():
        shutil.move(file_fullpath, source_dir_fullpath)

    shutil.rmtree(dest_dir_fullpath)

file_fullpaths = [
    x for x in source_dir_fullpath.iterdir() if x.is_file() and x.suffix == ".mp3"
]

files_len = len(file_fullpaths)

dirs_len = math.ceil(
    files_len / files_portion_size,
)

files_to_move_len = files_len

dir_lens = []

for k in range(dirs_len):
    dirs_to_move_to = dirs_len - k

    files_to_move_to_dir_len = math.ceil(files_to_move_len / dirs_to_move_to)

    dir_lens.append(files_to_move_to_dir_len)

    files_to_move_len -= files_to_move_to_dir_len

for file_fullpath in file_fullpaths:
    max_dir_indices = [x for x, y in enumerate(dir_lens) if y == max(dir_lens)]

    random_index = random.choice(max_dir_indices)

    dest_dir_fullpath = (
        source_dir_fullpath.parent / f"{source_dir_name} # {random_index + 1}"
    )
    dest_dir_fullpath.mkdir(exist_ok=True)

    shutil.move(file_fullpath, dest_dir_fullpath)

    dir_lens[random_index] = dir_lens[random_index] - 1
