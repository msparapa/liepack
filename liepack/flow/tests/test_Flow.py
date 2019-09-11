import numpy as np
from liepack.domain.liealgebras import so
from liepack.domain.liegroups import SO
from liepack.domain.hspaces import HManifold
from liepack.field import VectorField
from liepack.flow import RKMK, Flow

tol = 1e-4


def test_Flow_full1():
    # Solves a differential equation on SO(3). Taken from Kenthe Engo's `diffman` MATLAB repo github.com/kenthe/diffman
    y0 = np.eye(3)
    tspan = [0, 2.5]

    def M2eom(t, y):
        return t ** 2, 1, -t

    def eom2g(t, y):
        x, y, z = M2eom(t, y)
        out = so(3)
        out.set_vector([x, y, z])
        return out

    dim = y0.shape[0]
    y = HManifold(SO(dim, y0))
    vf = VectorField(y)
    vf.set_M2g(eom2g)
    ts = RKMK()
    f = Flow(ts, vf)
    ti, yi = f(y, tspan[0], tspan[-1], 0.1)
    init = np.array([0, 0, 1])
    # gamma = Trajectory(ti, np.array([np.dot(_, init) for _ in yi]))
    assert ti[0] == tspan[0]
    assert ti[-1] == tspan[-1]
    assert np.dot(yi[0], init)[0] == init[0]
    assert np.dot(yi[0], init)[1] == init[1]
    assert np.dot(yi[0], init)[2] == init[2]
    assert np.dot(yi[-1], init)[0] - 0.45901073 < tol
    assert np.dot(yi[-1], init)[1] + 0.22656862 < tol
    assert np.dot(yi[-1], init)[2] - 0.85905518 < tol
