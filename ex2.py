def skip_elements(elements):
	# Initialize variables
	new_list = []
	a = len(elements)+1
	if a ==1:
		return new_list
	else:
		for i in range(0, a):

            if i%2==0:

                new_list.append(elements[i])

        return new_list

	

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []
