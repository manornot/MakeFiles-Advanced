
import subprocess
import os

def test_automatic_variables():
    # Compile source files into object files
    subprocess.run(["make"], check=True)

    # Check if object files (*.o) are created
    for filename in os.listdir('.'):
        if filename.endswith('.c'):
            object_file = filename.replace('.c', '.o')
            assert os.path.isfile(object_file), f"Object file {object_file} not created"

# Call the test function
test_automatic_variables()

def test_dependency_generation():
    # Run Makefile with dependency generation
    subprocess.run(["make"], check=True)

    # Check if dependency files (*.d) are created for each source file
    for filename in os.listdir('.'):
        if filename.endswith('.c'):
            dep_file = filename.replace('.c', '.d')
            assert os.path.isfile(dep_file), f"Dependency file {dep_file} not created"

# Call the test function
test_dependency_generation()

def test_phony_targets():
    # Run Makefile to build project
    subprocess.run(["make"], check=True)
    
    # Check if `clean` target works as expected
    subprocess.run(["make", "clean"], check=True)
    for filename in os.listdir('.'):
        assert not filename.endswith('.o'), "Object files not cleaned up"

    # Optionally, test `test` target if applicable
    # subprocess.run(["make", "test"], check=True)
    # Add assertions based on the expected behavior of the test target

# Call the test function
test_phony_targets()

def test_conditional_compilation():
    # Compile with DEBUG set
    os.environ["DEBUG"] = "1"
    subprocess.run(["make"], check=True)

    # Assertions here would depend on the specific behavior or outputs
    # when compiling with debugging flags

# Call the test function
test_conditional_compilation()

def test_include_directives():
    # Run Makefile with external config
    subprocess.run(["make"], check=True)

    # Assertions here would depend on the specific settings from config.mk
    # and how they affect the build process

# Call the test function
test_include_directives()

def test_generating_documentation():
    # Run Makefile to generate documentation
    subprocess.run(["make", "docs"], check=True)

    # Check if documentation (e.g., HTML files) is generated
    # Assertions here would depend on the specific output of Doxygen

# Call the test function
test_generating_documentation()
