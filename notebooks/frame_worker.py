"""Worker side of a parallel globe movie.

Each worker process builds its globe once (`start`), then draws and saves one day per task (`render`).
Workers are started fresh ("spawn"): copying ("forking") a notebook kernel with running threads can deadlock.
The notebook's functions and data arrive pickled with cloudpickle, since a fresh process can't import them.
"""
import warnings

import cloudpickle
import pyvista as pv

_worker = {}


def start(payload):
    """Unpack (build_globe, add_layer, land_mesh, data, frame_dir) and build this worker's globe."""
    warnings.filterwarnings("ignore")
    pv.vtk_verbosity("off")
    build_globe, add_layer, land_mesh, data, frame_dir = cloudpickle.loads(payload)
    _worker.update(plotter=build_globe(land_mesh), add_layer=add_layer, data=data, frame_dir=frame_dir)


def render(frame):
    """Load one day of `data`, draw it and save it as frame_NNNN.png."""
    frame_number, date = frame
    _worker["add_layer"](_worker["plotter"], _worker["data"].sel(time=date).load())
    _worker["plotter"].screenshot(f"{_worker['frame_dir']}/frame_{frame_number:04d}.png")
