# himake

himake provides a series of convenient methods for managing CMake and performing cross-platform compilation.
The directory organization logic and CMakeLists refer to "Modern CMake".

[中文说明](README-zh.md)
[Release Notes](release-notes.md)

## Usage

### Create Template Project
Create a template project: `himake create [name]`

### Build
Build the project: `himake build`

#### Build and Output to a Specific Directory
Use the command: `himake build -o output_path`

#### Run Test Cases
Run all test cases: `himake test`

#### Run Main Project
Run the main project: `himake run`
