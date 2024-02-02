#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

def run_checked(command, return_output:bool=False) -> bool|tuple[bool, str, str]:
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)    
    if result.returncode != 0:
        if return_output:
            return (False, result.stdout, result.stderr)
        return False
    if return_output:
        return (True, result.stdout, result.stderr)
    return True