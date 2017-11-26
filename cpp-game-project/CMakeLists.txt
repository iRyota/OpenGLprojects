cmake_minimum_required (VERSION 3.0)

project(cpp-game-project)

find_package(GLUT)
find_package(OpenGL)

set(CMAKE_CXX_FLAGS "-g -Wall")

add_executable(cpp-game-project sample.c draw_function.c get_clock_now.c)
target_link_libraries(cpp-game-project ${GLUT_LIBRARY} ${OPENGL_LIBRARY} m)