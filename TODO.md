# To do

- [ ] Clean up `notebooks/ross_section_movie.ipynb` the same way as the compute notebook
  - Settings: clear names, `Path.home()` for the model data, movie speed as months per second
  - Read `seafloor_depth` from the section file instead of re-interpolating `HT` itself
  - Remove references to the old `Untitled1`/`Untitled2` names
- [ ] Add `seafloor_depth` to `data/Ross_section.zarr` (re-run `ross_section_compute.ipynb`, or append just that variable)
- [ ] Re-run `ross_section_movie.ipynb` end to end and check the preview and movie
- [ ] Re-run `ross_section_compute.ipynb` end to end once (only the parts before the save cell have been tested)
- [ ] Decide whether to move the globe notebook (`~/Untitled1.ipynb`) and its outputs into this project
- [ ] First git commit
