# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.9

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.9.0/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.9.0/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/ryota/Documents/programming/OpenGLProjects/cpp-game-project

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/ryota/Documents/programming/OpenGLProjects/cpp-game-project

# Include any dependencies generated for this target.
include CMakeFiles/cpp-game-project.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/cpp-game-project.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/cpp-game-project.dir/flags.make

CMakeFiles/cpp-game-project.dir/sample.c.o: CMakeFiles/cpp-game-project.dir/flags.make
CMakeFiles/cpp-game-project.dir/sample.c.o: sample.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/ryota/Documents/programming/OpenGLProjects/cpp-game-project/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/cpp-game-project.dir/sample.c.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/cpp-game-project.dir/sample.c.o   -c /Users/ryota/Documents/programming/OpenGLProjects/cpp-game-project/sample.c

CMakeFiles/cpp-game-project.dir/sample.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/cpp-game-project.dir/sample.c.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/ryota/Documents/programming/OpenGLProjects/cpp-game-project/sample.c > CMakeFiles/cpp-game-project.dir/sample.c.i

CMakeFiles/cpp-game-project.dir/sample.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/cpp-game-project.dir/sample.c.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/ryota/Documents/programming/OpenGLProjects/cpp-game-project/sample.c -o CMakeFiles/cpp-game-project.dir/sample.c.s

CMakeFiles/cpp-game-project.dir/sample.c.o.requires:

.PHONY : CMakeFiles/cpp-game-project.dir/sample.c.o.requires

CMakeFiles/cpp-game-project.dir/sample.c.o.provides: CMakeFiles/cpp-game-project.dir/sample.c.o.requires
	$(MAKE) -f CMakeFiles/cpp-game-project.dir/build.make CMakeFiles/cpp-game-project.dir/sample.c.o.provides.build
.PHONY : CMakeFiles/cpp-game-project.dir/sample.c.o.provides

CMakeFiles/cpp-game-project.dir/sample.c.o.provides.build: CMakeFiles/cpp-game-project.dir/sample.c.o


CMakeFiles/cpp-game-project.dir/draw_function.c.o: CMakeFiles/cpp-game-project.dir/flags.make
CMakeFiles/cpp-game-project.dir/draw_function.c.o: draw_function.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/ryota/Documents/programming/OpenGLProjects/cpp-game-project/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object CMakeFiles/cpp-game-project.dir/draw_function.c.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/cpp-game-project.dir/draw_function.c.o   -c /Users/ryota/Documents/programming/OpenGLProjects/cpp-game-project/draw_function.c

CMakeFiles/cpp-game-project.dir/draw_function.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/cpp-game-project.dir/draw_function.c.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/ryota/Documents/programming/OpenGLProjects/cpp-game-project/draw_function.c > CMakeFiles/cpp-game-project.dir/draw_function.c.i

CMakeFiles/cpp-game-project.dir/draw_function.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/cpp-game-project.dir/draw_function.c.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/ryota/Documents/programming/OpenGLProjects/cpp-game-project/draw_function.c -o CMakeFiles/cpp-game-project.dir/draw_function.c.s

CMakeFiles/cpp-game-project.dir/draw_function.c.o.requires:

.PHONY : CMakeFiles/cpp-game-project.dir/draw_function.c.o.requires

CMakeFiles/cpp-game-project.dir/draw_function.c.o.provides: CMakeFiles/cpp-game-project.dir/draw_function.c.o.requires
	$(MAKE) -f CMakeFiles/cpp-game-project.dir/build.make CMakeFiles/cpp-game-project.dir/draw_function.c.o.provides.build
.PHONY : CMakeFiles/cpp-game-project.dir/draw_function.c.o.provides

CMakeFiles/cpp-game-project.dir/draw_function.c.o.provides.build: CMakeFiles/cpp-game-project.dir/draw_function.c.o


CMakeFiles/cpp-game-project.dir/get_clock_now.c.o: CMakeFiles/cpp-game-project.dir/flags.make
CMakeFiles/cpp-game-project.dir/get_clock_now.c.o: get_clock_now.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/ryota/Documents/programming/OpenGLProjects/cpp-game-project/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building C object CMakeFiles/cpp-game-project.dir/get_clock_now.c.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/cpp-game-project.dir/get_clock_now.c.o   -c /Users/ryota/Documents/programming/OpenGLProjects/cpp-game-project/get_clock_now.c

CMakeFiles/cpp-game-project.dir/get_clock_now.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/cpp-game-project.dir/get_clock_now.c.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/ryota/Documents/programming/OpenGLProjects/cpp-game-project/get_clock_now.c > CMakeFiles/cpp-game-project.dir/get_clock_now.c.i

CMakeFiles/cpp-game-project.dir/get_clock_now.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/cpp-game-project.dir/get_clock_now.c.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/ryota/Documents/programming/OpenGLProjects/cpp-game-project/get_clock_now.c -o CMakeFiles/cpp-game-project.dir/get_clock_now.c.s

CMakeFiles/cpp-game-project.dir/get_clock_now.c.o.requires:

.PHONY : CMakeFiles/cpp-game-project.dir/get_clock_now.c.o.requires

CMakeFiles/cpp-game-project.dir/get_clock_now.c.o.provides: CMakeFiles/cpp-game-project.dir/get_clock_now.c.o.requires
	$(MAKE) -f CMakeFiles/cpp-game-project.dir/build.make CMakeFiles/cpp-game-project.dir/get_clock_now.c.o.provides.build
.PHONY : CMakeFiles/cpp-game-project.dir/get_clock_now.c.o.provides

CMakeFiles/cpp-game-project.dir/get_clock_now.c.o.provides.build: CMakeFiles/cpp-game-project.dir/get_clock_now.c.o


# Object files for target cpp-game-project
cpp__game__project_OBJECTS = \
"CMakeFiles/cpp-game-project.dir/sample.c.o" \
"CMakeFiles/cpp-game-project.dir/draw_function.c.o" \
"CMakeFiles/cpp-game-project.dir/get_clock_now.c.o"

# External object files for target cpp-game-project
cpp__game__project_EXTERNAL_OBJECTS =

cpp-game-project: CMakeFiles/cpp-game-project.dir/sample.c.o
cpp-game-project: CMakeFiles/cpp-game-project.dir/draw_function.c.o
cpp-game-project: CMakeFiles/cpp-game-project.dir/get_clock_now.c.o
cpp-game-project: CMakeFiles/cpp-game-project.dir/build.make
cpp-game-project: CMakeFiles/cpp-game-project.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/ryota/Documents/programming/OpenGLProjects/cpp-game-project/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking C executable cpp-game-project"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/cpp-game-project.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/cpp-game-project.dir/build: cpp-game-project

.PHONY : CMakeFiles/cpp-game-project.dir/build

CMakeFiles/cpp-game-project.dir/requires: CMakeFiles/cpp-game-project.dir/sample.c.o.requires
CMakeFiles/cpp-game-project.dir/requires: CMakeFiles/cpp-game-project.dir/draw_function.c.o.requires
CMakeFiles/cpp-game-project.dir/requires: CMakeFiles/cpp-game-project.dir/get_clock_now.c.o.requires

.PHONY : CMakeFiles/cpp-game-project.dir/requires

CMakeFiles/cpp-game-project.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/cpp-game-project.dir/cmake_clean.cmake
.PHONY : CMakeFiles/cpp-game-project.dir/clean

CMakeFiles/cpp-game-project.dir/depend:
	cd /Users/ryota/Documents/programming/OpenGLProjects/cpp-game-project && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/ryota/Documents/programming/OpenGLProjects/cpp-game-project /Users/ryota/Documents/programming/OpenGLProjects/cpp-game-project /Users/ryota/Documents/programming/OpenGLProjects/cpp-game-project /Users/ryota/Documents/programming/OpenGLProjects/cpp-game-project /Users/ryota/Documents/programming/OpenGLProjects/cpp-game-project/CMakeFiles/cpp-game-project.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/cpp-game-project.dir/depend

