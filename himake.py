#!/usr/bin/env python3
# coding=utf-8

from hi_basic import *
from cmake_project import *
import os
import argparse
import textwrap

def __info(args):
    curpath = os.path.dirname(os.path.abspath(__file__))
    appinfo = HiAppInfo(curpath)
    print(appinfo.name + " " + appinfo.version + " by " + appinfo.owner if appinfo.owner else "Unknown")
    # NOTE: Remember edit the "hikit-info.json" file, especially the "owner" and "remote"!
    pass


def __create(args):
    HiLog.warning(HiText("menu_create_warning", "Not Yet Support!"))
    pass

def __build(args):
    is_force = args["force"]
    project = CMakeProject()
    if is_force:
        project.clean()
    project.build()
    pass

def __run(args):
    target = args["target"]
    is_force = args["force"]
    nobuild = args["nobuild"]
    project = CMakeProject()
    if is_force:
        project.clean()
    project.run(name=target, nobuild=nobuild)
    pass

def __test(args):
    pass

def __clean(args):
    CMakeProject().clean()
    pass

def __setup_parser():
    # Define the menu.
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(HiText("menu_desc", """
        himake
        This the make project for himake.
        Thank you for used.
        """)),
        epilog=textwrap.dedent("""
        """)
        )

    # Create sub commands.
    subparsers = parser.add_subparsers(
        title=HiText("menu_list_title", "Command List")
    )

    # Add command for show app info.
    parser_info = subparsers.add_parser(
        name="info",
        help=HiText("menu_info_help", "View tool's version."),
        description=textwrap.dedent(HiText("menu_info_desc", """
        View tool's version.
        """)),
        )

    parser_info.set_defaults(func=__info)

    # Create Apps.
    parser_create = subparsers.add_parser(
        name="create",
        help=HiText("menu_create_help", "Provide template for create crossplatform c project.")
        )

    parser_create.add_argument(
        'name',
        help=HiText("menu_create_name_desc", "The project name."),
        )

    parser_create.set_defaults(func=__create)

    # Build Apps.
    parser_build = subparsers.add_parser(
        name="build",
        help=HiText("menu_build_help", "Build a project output to build dir, --output can install to other dir. --type can select the type. --platform can select platform."),
        )
    
    parser_build.add_argument(
        '-f',
        '--force',
        help=HiText("menu_build_force_desc", "Rebuild all."),
        action="store_true"
        )

    parser_build.set_defaults(func=__build)

    # Run Tests.
    parser_run = subparsers.add_parser(
        name="run",
        help=HiText("menu_run_help", "Run program in apps dir."),
        )

    parser_run.add_argument(
        'target',
        help=HiText("menu_run_target_help", "The target name, default is main."),
        nargs="?",
        default="main"
        )

    parser_run_group = parser_run.add_mutually_exclusive_group()

    parser_run_group.add_argument(
        '-n',
        '--nobuild',
        help=HiText("menu_run_nobuild_desc", "Direct run no build."),
        action="store_true"
        ) 
    
    parser_run_group.add_argument(
        '-f',
        '--force',
        help=HiText("menu_run_force_desc", "Run and rebuild all."),
        action="store_true"
        )

    parser_run.set_defaults(func=__run)

    # Test Apps.
    parser_test = subparsers.add_parser(
        name="test",
        help=HiText("menu_test_help", "Run tests in tests dir."),
        )

    parser_test.set_defaults(func=__test)

    # Test Apps.
    parser_clean = subparsers.add_parser(
        name="clean",
        help=HiText("menu_clean_help", "Clean all build."),
        )

    parser_clean.set_defaults(func=__clean)

    # parse the input.
    args = parser.parse_args()

    if len(vars(args)) == 0:
        # if no input print help.
        parser.print_help()
    else:
        # select the function
        args.func(vars(args))
    pass


def main():
    """Entry."""
    __setup_parser()
    pass


if __name__ == "__main__":
    main()
    pass
