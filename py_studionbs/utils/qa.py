###################################################
# qa
###################################################
# a submodule for ease-of-life quality assurance 
# methods
###################################################

import os

# assert and print
def aap(test_val, true_val, suc_msg: str, fail_msg: str) -> None:
    fmtstr = '\nAssertion {0}\n > {1}\n > {2}'

    try:
        assert(test_val == true_val)
        print(fmtstr.format('Successful', suc_msg, os.path.realpath(__file__)))
    except:
        print(fmtstr.format('Successful', fail_msg, os.path.realpath(__file__)))