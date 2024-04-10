### Records (Structures)
Also known as struct in C and it's descendants

When storing data, the memory layout follows alignment restrictions, creating "holes" 
- some types, like integers need to be word aligned, so bytes in memory will be skipped and left empty to make that possible

Some languages, like C and Ada allow a record to be specified as "packed"
- When this is the case, memory is saved and "holes" are not used to align certain data types. 

A union, is a memory efficient use of variables that would not be used at the same time, and are allocated "on top of" each other.
```
union{
  int i;
  double d;
  _Bool b;
} 
``` 


The overall size would be that of it's largest member.

### Arrays


### Strings


### Recursive Types

