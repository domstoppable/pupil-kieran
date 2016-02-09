
if __name__ == '__main__':
    import subprocess as sp
    python_includes = sp.check_output("python-config --includes",shell=True ).strip('\n')
    python_ldflags= sp.check_output("python-config --ldflags",shell=True ).strip('\n')

    s = "g++ -std=c++11 " +python_includes + python_ldflags+"  -g loggerTest.cpp -o test"
    sp.call(s,shell=True)


    print "BUILD COMPLETE ______________________"
    sp.call("./test",shell=True)

