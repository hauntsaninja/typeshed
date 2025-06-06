from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

__all__ = ["is_valid_joint_degree", "is_valid_directed_joint_degree", "joint_degree_graph", "directed_joint_degree_graph"]

@_dispatchable
def is_valid_joint_degree(joint_degrees): ...
@_dispatchable
def joint_degree_graph(joint_degrees, seed: Incomplete | None = None): ...
@_dispatchable
def is_valid_directed_joint_degree(in_degrees, out_degrees, nkk): ...
@_dispatchable
def directed_joint_degree_graph(in_degrees, out_degrees, nkk, seed: Incomplete | None = None): ...
