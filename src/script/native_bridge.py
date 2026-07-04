import os
import ctypes

_DLL = None  # cached handle so the DLL loads only once per session


def load_dll():
    """Load curve_sort.dll (once) and declare the sort_curves signature."""
    global _DLL
    if _DLL is not None:
        return _DLL

    here = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(here, "native", "curve_sort.dll")
    lib = ctypes.CDLL(dll_path)

    # void sort_curves(const double*, int, const double*, int, int, int, int*, int*)
    lib.sort_curves.argtypes = [
        ctypes.POINTER(ctypes.c_double),  # endpoints (6*n)
        ctypes.c_int,                     # n
        ctypes.POINTER(ctypes.c_double),  # start_pt (3)
        ctypes.c_int,                     # use_two_opt
        ctypes.c_int,                     # two_opt_max_passes
        ctypes.c_int,                     # knn_k
        ctypes.c_int,                     # if_flip
        ctypes.POINTER(ctypes.c_int),     # out_order (n)
        ctypes.POINTER(ctypes.c_int),     # out_reversal (n)
    ]
    lib.sort_curves.restype = None

    _DLL = lib
    return lib
