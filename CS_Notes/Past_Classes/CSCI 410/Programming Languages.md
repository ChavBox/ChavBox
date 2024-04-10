### Assignment 1 (done)
Game of life (voters problem)
80x24 window
Count up neighborhood, vote for the majority vote 

### Assignment 2 (Due 2/2)

Same thing but now in fortran
- slice arrays
- forall(i = min:max, j = min:max)
- sum slices of array
Main loop:
```
  implicit none
  write format: "(100I1,2X)"
```

returning from subroutine:
```
FUNCTION example()
IMPLICIT NONE
do some stuff
...
example = sum(a+b)
```
## Puzzle
huge array