#!/usr/bin/env python3
# coding=utf-8
'''
Author: Cosmade
Date: 2024-05-10 20:27:52
LastEditors: deepskystar deepskystar@outlook.com
LastEditTime: 2024-05-22 22:09:59
FilePath: /himake/cmake_project.py
Description: 

Copyright 2024 Cosmade

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import os
import shutil
import time
from hi_basic import *


class CMakeProject():
    def __init__(self, path: str = None) -> None:
        self._path = path
        if self._path is None:
            self._path = os.getcwd()
        self._build_path = os.path.join(self._path, "build")
        self._test_path = os.path.join(self._path, "tests")
        self._test_build_path = os.path.join(self._test_path, "build")
        self._run_path = os.path.join(self._path, "apps")
        self._run_build_path = os.path.join(self._run_path, "build")
        pass

    @property
    def path(self) -> str:
        return self._path

    def check_rebuild(self, run_path: str) -> bool:
        source_cmakefile = os.path.join(self._path, "CMakeLists.txt")
        build_cmakefile = os.path.join(run_path, "CMakeLists.txt")
        build_checkfile = os.path.join(run_path, "build/CMakeCache.txt")

        if not os.path.exists(build_checkfile) or not os.path.isfile(build_checkfile):
            return True
        last_build_time = os.path.getmtime(build_checkfile)
        
        modify_time = os.path.getmtime(build_cmakefile)
        modify_time = modify_time if os.path.getmtime(source_cmakefile) > modify_time else os.path.getmtime(source_cmakefile)

        if modify_time > last_build_time:
            return True
        return False

    @classmethod
    def check_project(cls, path: str) -> bool:
        check_files = [
            "CMakeLists.txt",
            "apps/CMakeLists.txt",
        ]
        check_dirs = [
            "include",
            "src",
            "apps",
        ]

        for file in check_files:
            if not os.path.exists(os.path.join(path, file)):
                HiLog.error(os.path.join(path, file) + " not found!")
                return False
            if not os.path.isfile(os.path.join(path, file)):
                HiLog.error(os.path.join(path, file) + " not a file!")
                return False
            pass

        for file in check_dirs:
            if not os.path.exists(os.path.join(path, file)):
                HiLog.error(os.path.join(path, file) + " not found!")
                return False
            if not os.path.isdir(os.path.join(path, file)):
                HiLog.error(os.path.join(path, file) + " not a file!")
                return False
            pass

        return True

    def build_dir(self, path: str) -> None:
        build_path = os.path.join(path, "build")
        if not os.path.exists(build_path):
            os.mkdir(build_path)
        if not os.path.isdir(build_path):
            raise FileExistsError(build_path + " is not a dir!")

        if self.check_rebuild(path):
            os.system("cmake -S " + path + " -B " + build_path)
        os.system("cmake --build " + build_path)
        pass

    def build(self) -> None:
        self.build_dir(self._path)
        # -DCMAKE_SYSTEM_NAME=<system>
        # -DCMAKE_SYSTEM_PROCESSOR=<processor>
        # cmake -G Xcode -DCMAKE_TOOLCHAIN_FILE=<ios-cmake-toolchain> -DIOS_PLATFORM=<platform> <source-dir>
        pass

    def clean(self) -> None:
        clean_list = [
            self._build_path,
            self._test_build_path,
            self._run_build_path
        ]
        for path in clean_list:
            if os.path.exists(path):
                # os.remove(path)
                shutil.rmtree(path)
        pass

    def run(self, name: str = "main", nobuild: bool = False, args: str = "") -> None:
        if not nobuild:
            self.build_dir(self._run_path)
        os.system("./apps/build/" + name + " " + args)
        pass

    def test(self) -> None:
        pass

    pass
