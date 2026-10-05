# CMPE 255 — Assignment 3

Executed Colab notebooks for K-Means, AutoGluon, RAPIDS, and PyCaret. Each part is kept in its own folder with the notebook code and saved outputs.

| Part | Topic | Notebook |
| --- | --- | --- |
| 1 | K-Means concepts, algorithm variants, and choosing K | [K-Means](Part-1-KMeans/CK_final_kmeans_zero_to_hero.ipynb) |
| 2 | AutoGluon capabilities tour | [AutoGluon capabilities](Part-2-AutoGluon-Capabilities/CK_final_autogluon_capabilities_tour.ipynb) |
| 3 | AutoGluon end-to-end workflow | [AutoGluon end-to-end](Part-3-AutoGluon-EndToEnd/CK_of_final_autogluon_zero_to_hero.ipynb) |
| 4 | RAPIDS: CPU and GPU workflows | [RAPIDS](Part-4-RAPIDS-CPU-vs-GPU/CK_final_nvidia_rapids_zero_to_hero.ipynb) |
| 5 | PyCaret capabilities tour | [PyCaret capabilities](Part-5-PyCaret-Capabilities/CK_final_pycaret_capabilities_tour.ipynb) |
| 6 | PyCaret end-to-end ML and MLOps | [PyCaret zero to hero](Part-6-PyCaret-MLOps/CK_final_pycaret_zero_to_hero.ipynb) |

## Running the notebooks

Open a notebook in Google Colab and follow its installation and runtime instructions from the top. Package installation may require a session restart; after restarting, continue at the import or setup cell indicated in that notebook. GPU examples require a compatible NVIDIA GPU runtime. Saved outputs reflect the environment in which each notebook was run and may differ on a fresh runtime.

The Part 6 notebook uses Python 3.11 and PyCaret 3.3.2. Its Task 25 GPU cell checks PyCaret GPU setup and model availability in an isolated process; completing that registry check alone does not demonstrate GPU model training. If TabPFN and TabICL are unavailable, the custom-estimator example uses a labelled histogram gradient boosting stand-in.

## Walkthrough videos

Video links will be added after the recordings are uploaded. The notebooks and their saved outputs are available above in the meantime.
