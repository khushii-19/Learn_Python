# Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.

# Function to generate the multiplication table of a given number
def table(n):
    table = ""  # This will store the entire table as a string

    # Loop from 1 to 10 to generate the multiplication table
    for i in range(1, 11):
        # Add each line of the multiplication table to the 'table' string
        table += f"{n} X {i} = {n*i}\n"

    # Open a file to write the table (creates the file if it doesn't exist)
    # The file will be saved as 'table_<n>.txt' inside the 'tables' folder
    with open(f"Chapter 9/practice set/tables/table_{n}.txt", "w") as f:
        f.write(table)  # Write the entire table string to the file

# This loop will generate multiplication tables from 2 to 20
for i in range(2, 21):
    table(i)  # Call the table function for each number from 2 to 20

