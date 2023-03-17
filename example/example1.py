"""
An example of using the library to check if appropriate versions of blastn and 
samtools are installed.
"""

import sys
import os
import vezzo

path = os.path.dirname(os.path.realpath(__file__))
config = os.path.join(path, "config.yaml")

fails = 0
for is_match, obs_version, exp_version, tool in vezzo.verify_from_config(config):
    if is_match:
        sys.stderr.write(
            f"\033[32m {tool} version {obs_version} matches requirements {exp_version}.... \u2714 \033[0m\n"
        )
    else:
        sys.stderr.write(
            f"\033[31m {tool} version {obs_version} DOES NOT match requirements {exp_version}.... \u274C \033[0m\n"
        )
        fails += 1

if fails > 0:
    sys.stderr.write(
        f"\033[31m There {'was' if fails == 1 else 'were'} {fails} tool{'s' if fails > 0 else ''} that failed the version requirements. Please ensure these are corrected before proceeding. \U0001F622 \033[0m\n"
    )
    sys.exit(1)
