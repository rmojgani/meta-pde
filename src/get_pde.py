from absl import flags
from .poisson import poisson_def
from .stokes import stokes_def



FLAGS = flags.FLAGS


def get_pde(pde_name):
    if pde_name == "poisson":
        return poisson_def

    elif pde_name == "linear_stokes":
        FLAGS.stokes_nonlinear = False
        return stokes_def

    elif pde_name == "nonlinear_stokes":
        FLAGS.stokes_nonlinear = True
        return stokes_def

    else:
        raise Exception("Invalid PDE {}".format(pde_name))
