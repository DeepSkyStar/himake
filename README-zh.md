# himake

himake，用于提供一系列方便管理CMake和进行跨平台编译的方法。
目录组织逻辑和CMakeLists参考<<Modern CMake>>.

[Relase Notes](release-notes.md)

## 使用方法

### 创建模版工程
创建模版工程，`himake create [name]`

### 编译
编译工程，`himake build`

#### 编译并输出到某个目录
使用命令，`himake build -o output_path`

#### 执行测试用例
执行所有测试用例，`himake test`

#### 运行main工程
运行main工程，`himake run`

