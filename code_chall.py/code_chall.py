# Print out all of the strings in the following array in alphabetical order, each on a separate line.

# The expected output is:
# 'Cha Cha'
# 'Foxtrot'
# 'Jive'
# 'Paso Doble'
# 'Rumba'
# 'Samba'
# 'Tango'
# 'Viennese Waltz'
# 'Waltz'
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code.
# Run through the UPER problem solving framework while
# going through your thought process.

# my_list = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']

# def alph_list(my_list):
#   n = len(my_list)

#   for i in range(n-1):
#     for j in range(0, n-i-1):

#       if my_list[j][0] > my_list[j+1][0]:
#         my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
#       else:
#         if my_list[j][0] < my_list[j+1][0]:
#           my_list[j], my_list[j+1] = my_list[j], my_list[j+1]

# print(alph_list(my_list))

my_list = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
def alph_list(my_list):
  my_list.sort()
  for i in my_list:
    print(i)
print(alph_list(my_list))


