
%%
% __init__.pl is consulted to load several rosprolog modules
% such that exported predicates are available to the user.
%
:- use_module('./ros.pl').
:- use_module('./package.pl').
:- use_module('./query.pl').
:- use_module('./logging.pl').

:- register_ros_package(rosprolog).
