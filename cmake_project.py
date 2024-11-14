#!/usr/bin/env python3
# coding=utf-8
'''
Author: Cosmade
Date: 2024-05-10 20:27:52
LastEditors: deepskystar deepskystar@outlook.com
LastEditTime: 2024-11-14 17:12:35
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
from hi_basic import *

class CMakeProjectAppTemplate(HiTemplate):
    def __init__(self, project_name: str, template_dir: str, app_name: str):
        self._app_name = app_name
        super().__init__(project_name, template_dir)
        pass

    def _replace_content(self, content: str) -> str:
        """Override Point."""
        return super()._replace_content(content).replace(
            "<APP_NAME>", self._app_name
        )
    
    def generate_to_path(self, path: str = os.getcwd(), is_force: bool = False) -> None:
        """Generate to path."""
        path = os.path.join(path, self._app_name)
        self._legal_check(path, is_force)
        if not os.path.exists(path):
            os.mkdir(path)
        self._deploy_template(path)
        pass
    pass

class CMakeProject():
    def __init__(self, path: str = None) -> None:
        self._path = path
        if self._path is None:
            self._path = os.getcwd()
        self._build_path = os.path.join(self._path, "build")
        self._test_path = os.path.join(self._path, "tests")
        self._run_path = os.path.join(self._path, "apps")
        pass

    @property
    def path(self) -> str:
        return self._path

    @property
    def runpath(self) -> str:
        return self._run_path

    @property
    def apps(self) -> list:
        return os.listdir(self._run_path)

    @property
    def testpath(self) -> str:
        return self._test_path

    def check_rebuild(self, run_path: str) -> bool:
        source_cmakefile = os.path.join(self._path, "CMakeLists.txt")
        build_cmakefile = os.path.join(run_path, "CMakeLists.txt")
        build_checkfile = os.path.join(run_path, "build/CMakeCache.txt")

        if not os.path.exists(build_checkfile) or not os.path.isfile(build_checkfile):
            return True
        last_build_time = os.path.getmtime(build_checkfile)

        modify_time = os.path.getmtime(build_cmakefile)
        modify_time = modify_time if os.path.getmtime(source_cmakefile) < modify_time else os.path.getmtime(source_cmakefile)

        if modify_time > last_build_time:
            return True
        return False

    @classmethod
    def check_project(cls, path: str) -> bool:
        check_files = [
            "CMakeLists.txt",
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

    def build_dir(self, path: str, args: str) -> None:
        need_rebuild = self.check_rebuild(path)
        if need_rebuild:
            self.clean()

        build_path = os.path.join(path, "build")
        if not os.path.exists(build_path):
            os.mkdir(build_path)
        if not os.path.isdir(build_path):
            raise FileExistsError(build_path + " is not a dir!")

        if need_rebuild:
            os.system("cmake "+ args + " -S " + path + " -B " + build_path)
        # else:
            # os.remove(os.path.join(path, "build/CMakeCache.txt"))
        os.system("cmake" + " --build " + build_path + " -- -j")
        pass

    def build(self) -> None:
        self.build_dir(self._path, args="")
        # -DCMAKE_SYSTEM_NAME=<system>
        # -DCMAKE_SYSTEM_PROCESSOR=<processor>
        # cmake -G Xcode -DCMAKE_TOOLCHAIN_FILE=<ios-cmake-toolchain> -DIOS_PLATFORM=<platform> <source-dir>
        pass

    def clean(self) -> None:
        clean_list = [
            self._build_path,
            os.path.join(self._test_path, "build"),
            # self._run_build_path
        ]
        
        for name in os.listdir(self._run_path):
            path = os.path.join(self._run_path, name)
            build_path = os.path.join(path, "build")
            clean_list.append(build_path)

        for path in clean_list:
            if os.path.exists(path):
                # os.remove(path)
                shutil.rmtree(path)
        pass

    def run(self, name: str = "main", nobuild: bool = False, args: str = "", build_args: str = "") -> None:
        app_path = os.path.join(self._run_path, name)
        if not nobuild:
            self.build_dir(app_path, args=build_args)
        os.system("./apps/" + name + "/build/" + name + " " + args)
        pass

    def test(self) -> None:
        pass

    pass
