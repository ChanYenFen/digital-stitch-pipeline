import sys
import array
 
 
def unload_modules(top_level_module_name):
    """
    Unloads all modules named starting with the specified string.
 
    This is adapted from COMPAS to facilitate dynamic reloading in Rhino/GH.
 
    Args:
        top_level_module_name (str): The name of the library (e.g., 'd2m')
    """
    # 1. Identify all related modules
    modules_to_remove = [
        m for m in sys.modules.keys()
        if m.startswith(top_level_module_name)
    ]
 
    # 2. Remove them from memory
    for module_name in modules_to_remove:
        del sys.modules[module_name]
 
    # 3. Return list of unloaded modules (useful for debugging)
    return modules_to_remove
 
 
# --- Marshaling helpers for the native curve_sort DLL (CPython 3) ---
 
 
def curves_to_endpoint_buffer(curves):
    """Flatten endpoints to a flat double buffer: [sx,sy,sz, ex,ey,ez, ...]. Returns (buffer, n)."""
    buf = array.array('d')
    for c in curves:
        s = c.PointAtStart
        e = c.PointAtEnd
        buf.append(s.X)
        buf.append(s.Y)
        buf.append(s.Z)
        buf.append(e.X)
        buf.append(e.Y)
        buf.append(e.Z)
    return buf, len(curves)
 
 
def start_pt_to_buffer(start_pt):
    """Flatten the reference start point to a 3-double buffer [X, Y, Z]."""
    return array.array('d', (start_pt.X, start_pt.Y, start_pt.Z))
 
 
def apply_order(curves, order, reversal):
    """Rebuild ordered curves from native result. Duplicate/Reverse deferred to here."""
    out = []
    for idx, rev in zip(order, reversal):
        c = curves[idx].Duplicate()
        if rev:
            c.Reverse()
        out.append(c)
    return out
 