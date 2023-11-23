# README.md for Advanced Makefiles

## Overview
This README covers advanced topics in Makefiles, building on the basics of Makefile usage. Advanced Makefiles provide greater flexibility and automation in managing complex C projects, including handling dependencies, generating files, and more.

## Table of Contents
1. [Automatic Variables](#automatic-variables)
2. [Pattern Rules](#pattern-rules)
3. [Wildcard Expansion](#wildcard-expansion)
4. [Managing Dependencies](#managing-dependencies)
5. [Phony Targets](#phony-targets)
6. [Conditional Statements](#conditional-statements)
7. [Include Directives](#include-directives)
8. [Generating Files](#generating-files)

## 1. Automatic Variables
Automatic variables simplify Makefile recipes by providing easy access to common values. Some commonly used automatic variables include:
- `$@`: The target file name.
- `$<`: The first prerequisite (dependency).
- `$^`: All prerequisites.
- `$?`: Prerequisites that are newer than the target.
- `$*`: The stem (base name) of the target file.

Example:
```makefile
%.o: %.c
    $(CC) -c $< -o $@
```

## 2. Pattern Rules
Pattern rules allow you to define generic rules for compiling files based on their extensions. They simplify Makefile maintenance by reducing the need for repetitive rules.

Example:
```makefile
%.o: %.c
    $(CC) -c $< -o $@
```

## 3. Wildcard Expansion
You can use wildcard expansion to include multiple files in your rules without specifying each file individually. This is useful when you have many source files.

Example:
```makefile
SRC_FILES := $(wildcard src/*.c)
OBJ_FILES := $(patsubst src/%.c,obj/%.o,$(SRC_FILES))

app: $(OBJ_FILES)
    $(CC) $^ -o $@
```

## 4. Managing Dependencies
Makefiles can automatically generate dependency information to ensure that changes in header files trigger recompilation of affected source files. Tools like `gcc -M` can help generate dependency rules.

Example:
```makefile
%.o: %.c
    $(CC) -MMD -c $< -o $@
    
-include $(OBJ_FILES:.o=.d)
```

## 5. Phony Targets
Declare targets as `.PHONY` to indicate they are not files and should always be executed. Common phony targets include `clean`, `all`, and `test`.

Example:
```makefile
.PHONY: clean

clean:
    rm -f $(OBJ_FILES) app
```

## 6. Conditional Statements
Makefiles support conditional statements that allow you to define rules based on conditions like the target platform, compiler, or build type.

Example:
```makefile
ifeq ($(DEBUG), 1)
CFLAGS += -g
endif
```

## 7. Include Directives
You can include external Makefiles or configuration files using `include` directives. This makes your Makefiles more modular and easier to maintain.

Example:
```makefile
include config.mk
```

## 8. Generating Files
Makefiles can generate files automatically using rules. This is useful for generating header files, documentation, or other artifacts.

Example:
```makefile
docs: README.md
    doxygen Doxyfile
```


# Advanced Makefiles - Tasks

Here are some tasks to practice and test your knowledge of advanced Makefiles. These tasks build on the basics and cover more advanced features of Makefiles:

### Task 1: Automatic Variables
**Objective**: Create a Makefile that compiles multiple C source files (`*.c`) into object files (`*.o`) using automatic variables.

**Requirements**:
- Use automatic variables like `$@`, `$<`, and `$^`.
- Write a generic pattern rule to compile any `.c` file into an `.o` file.

### Task 2: Dependency Generation
**Objective**: Enhance the Makefile from Task 1 to automatically generate dependency files (`.d`) for each source file.

**Requirements**:
- Use `gcc -MMD` to generate dependency files.
- Include the dependency files using the `-include` directive.

### Task 3: Phony Targets
**Objective**: Create a Makefile with phony targets for building, cleaning, and running tests.

**Requirements**:
- Declare targets `all`, `clean`, and `test` as phony.
- Implement the `clean` target to remove object files and the executable.
- Implement the `test` target to run tests if applicable.

### Task 4: Conditional Compilation
**Objective**: Modify the Makefile to conditionally compile with or without debugging information based on a variable.

**Requirements**:
- Define a variable (e.g., `DEBUG`) to control compilation options.
- Add a conditional statement to add debugging flags (`-g`) when `DEBUG` is set.

### Task 5: Include Directives
**Objective**: Refactor your Makefile to include an external configuration file (`config.mk`) for build settings.

**Requirements**:
- Create a `config.mk` file with variables for compiler, compiler flags, and other build settings.
- Include the `config.mk` file in your Makefile using the `include` directive.

### Task 6: Generating Documentation
**Objective**: Extend your Makefile to generate documentation using Doxygen.

**Requirements**:
- Define a target `docs` for generating documentation.
- Use Doxygen to generate documentation from source code comments.




## References

Here are some references and resources to help you dive deeper into advanced Makefiles:

1. [GNU Make Manual](https://www.gnu.org/software/make/manual/make.html) - The official GNU Make manual provides comprehensive documentation on Makefile syntax and features.

2. [Makefile Tutorial](https://makefiletutorial.com/) - A beginner-friendly tutorial on Makefiles that covers both basics and advanced topics.

3. [Managing Projects with GNU Make](https://oreilly.com/library/view/managing-projects-with/0596006101/) - A book by Robert Mecklenburg that explores advanced Makefile techniques.

4. [Advanced Makefile Tricks](https://www.olioapps.com/blog/advanced-makefile-tricks/) - A blog post with advanced Makefile examples and explanations.

5. [Automatic Variables in GNU Make](https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html) - Details about automatic variables in GNU Make.

6. [Pattern Rules in GNU Make](https://www.gnu.org/software/make/manual/html_node/Pattern-Rules.html) - Information about pattern rules in GNU Make.

7. [Wildcard Function in GNU Make](https://www.gnu.org/software/make/manual/html_node/Wildcard-Function.html) - Explanation of the wildcard function in GNU Make.

8. [Managing Dependencies in Make](https://mad-scientist.net/make/autodep.html) - A tutorial on managing dependencies in Makefiles.

9. [Conditional Directives in Makefiles](https://www.gnu.org/software/make/manual/html_node/Conditional-Directives.html) - Information about conditional statements in Makefiles.

10. [Include Directive in GNU Make](https://www.gnu.org/software/make/manual/html_node/Include.html) - Details on how to include other Makefiles.

11. [Generating Prerequisites Automatically in GNU Make](https://www.gnu.org/software/make/manual/html_node/Automatic-Prerequisites.html) - Information on generating dependency information automatically.

12. [Advanced Makefile Examples](https://github.com/mbcrawfo/GNUMakeForC) - A GitHub repository with advanced Makefile examples for C projects.

Explore these resources to gain a deeper understanding of advanced Makefile concepts and techniques.

---


## Conclusion
Advanced Makefiles are a powerful tool for managing complex C projects efficiently. They provide automation, dependency tracking, and flexibility, making them a valuable asset in software development.

