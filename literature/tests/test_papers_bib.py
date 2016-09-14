import subprocess


def test_papersbib():
    command = "pdflatex -halt-on-error citeall.tex"

    # We should allow for the test to time out; latex does that in
    # extreme circumstances (such as article.cls missing or latex
    # file not found).
    
    retcode, output = subprocess.getstatusoutput(command)

    print("Output from command '{}'".format(command))
    print(output)
    assert retcode == 0


def test_bibtex():
    

    # setup system: need to call latex once before running bibtex
    command = "pdflatex -halt-on-error citeall.tex"
    retcode, output = subprocess.getstatusoutput(command)
    if retcode is not 0:
        message = "Compiling latex document fails, so we can't check bibtex call.)"
        print(message)
        raise RuntimeError(message)
        return   # stop testing here
    
    # actual tests for bibtex
    command = "bibtex citeall"
    retcode, output = subprocess.getstatusoutput(command)

    print("Output from command '{}'".format(command))
    print(output)
    assert retcode == 0



