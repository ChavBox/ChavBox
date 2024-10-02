## Heirarchy
- Hard Drive
- Memory (on chip)
- L2 Cache (on chip)
- L1 Cache (direct cpu access)
- Registers (direct cpu access)
- ALU (direct cpu access)

Each process has a base and limit value to hold starting and ending memory addresses. 
Only the kernel can access all other program data (outside of base/limit range)

### Memory Allocation
