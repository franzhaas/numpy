import os
import sys
from pathlib import Path
import pytest

import numpy as np
from numpy.testing import assert_

FILES = [
    ("py.typed"),
    ("__init__.pyi"),
    ("ctypeslib.pyi"),
    ("core" , "__init__.pyi"),
    ("distutils" , "__init__.pyi"),
    ("f2py" , "__init__.pyi"),
    ("fft" , "__init__.pyi"),
    ("lib" , "__init__.pyi"),
    ("linalg" , "__init__.pyi"),
    ("ma" , "__init__.pyi"),
    ("matrixlib" , "__init__.pyi"),
    ("polynomial" , "__init__.pyi"),
    ("random" , "__init__.pyi"),
    ("testing" , "__init__.pyi"),
]


class TestIsFile:
    @pytest.mark.skipif(getattr(sys, "oxidized", False),
                    reason="__file__ not defined this module is pro, file system checks dont make sense")
    def test_isfile(self):
        """Test if all ``.pyi`` files are properly installed."""
        ROOT = Path(np.__file__).parents[0]
        for file in FILES:
            file = ROOT / "/".join(file)
            assert_(os.path.isfile(file))

    def test_isResource(self):
        for file in FILES:
            file = ["numpy"] + file
            with importlib.resources.path(".".join(file[:-1]), file[-1]) as filename:
                assert_(os.path.isfile(filename))
