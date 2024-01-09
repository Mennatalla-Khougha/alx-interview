# 0x01-lockboxes

- Start with a hash set that contain the key to the first lockbox since it's always open 

- Closed is an empty array to keep track of the unopened lockboxes

### loop through the boxes array:
- if the index of the box in the hash then add the keys inside the box to the hash
- else we can't open the box and we add the index of the locked box to the closed array 
---

- we keep a count of our closed array 

### loop through the unopened boxes:
- if the index of the box in the hash then add the keys inside the box to the hash and we decrease our count by one 
---

## if our count is 0 then we opened all our boxes else we have unopened boxes
