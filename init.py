import os
import sys

from pathlib import Path


if __name__ == "__main__":
    number = sys.argv[1]
    folder = f"code/{number}"
    script = f"{folder}/{number}.py"
    readme = f"{folder}/README.md"
    txt = f"""


#datanalytics #datascience #dataengineering #machinelearning #devops

------
🗣 If you like this post, follow me for daily #python tips, and hit that like button so the algorithms help others see it, too. For full code and data on this and earlier exercises, visit https://www.github.com/bryangoodrich/python-exercises
------

<img src="../../static/{number}.png" />

"""
    os.makedirs(folder, exist_ok=True)
    Path(script).touch()
    Path(readme).touch()
    with open(readme, 'w', encoding="utf-16") as fh:
        fh.write(txt)
