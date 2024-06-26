etn## Contiguous Allocation
Issues:
- Can't extent size of file
- 
## Linked Allocation
	A file is a linked list of blocks
If a block is size x, you can store x-p data (p being pointer to next block)

## File Allocation Table
	Reserve a single (or two or three) blocks, to hold a table of all blocks.
**Directory Entry**: fileName, ...other..., int(block reference number)
Index Allocation
- A single block contains ALL of the pointers for the blocks in use by a file. 
Linked index blocks:
- A block contains references to data blocks, and the last reference in a block refers to ANOTHER index block
- The last index block in the list of index blocks contains -1s to indicate "no more"

How does the system keep track of available (free) blocks?
- Bit vector approach: keep a single bit to specify if the block is free (0) or not free(1)
	- Advantages: easy to implement
	- Disadvantage: need algorithm to find contiguous space if contiguous allocation is used. 
- Linked List: Link together all of the free blocks