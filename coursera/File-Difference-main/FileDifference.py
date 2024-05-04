"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1


def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    shorter_line = min(len(line1), len(line2))

    for i in range(shorter_line):
        if line1[i] != line2[i]:
            return i

    if len(line1) == len(line2):
        return IDENTICAL

    elif len(line1) != len(line2):
        return shorter_line


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """

    shorter_line = min(len(line1), len(line2))
    if idx not in range(0, shorter_line + 1):
        return ""

    if '\n' in line1 or '\n' in line2:
        return ""
    if '\r' in line1 or '\r' in line2:
        return ""

    the_drawing = "=" * idx + "^"
    the_picture = line1 + "\n" + the_drawing + "\n" + line2 + "\n"

    return the_picture


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """

    short = min(len(lines1), len(lines2))

    for despair in range(0, short):
        first = lines1[despair]
        second = lines2[despair]
        index = singleline_diff(first, second)
        if index != -1:
            return (despair, index)

    if len(lines1) != len(lines2):
        return (short, 0)
    return (IDENTICAL, IDENTICAL)

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    openfile = open(filename, "rt")
    lines = openfile.read()
    happy_lines = lines.split("\n")
    if "" in happy_lines:
        happy_lines.remove("")

    openfile.close()

    return happy_lines

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    list_one = get_file_lines(filename1)
    list_two = get_file_lines(filename2)
    #I asked Python to open files and create lists of strings

    short = min(len(list_one), len(list_two))

    for sad_string in range(0, short):
        first = list_one[sad_string]
        second = list_two[sad_string]
        index = singleline_diff(first, second)
        if index != -1:
            line_number = str(sad_string)
            the_drawing = "="*index + "^"
            the_picture = "Line " + line_number + ":" + "\n" + \
                          list_one[sad_string] + "\n" + the_drawing + "\n" + \
                          list_two[sad_string] + "\n"

            return the_picture


    return "No difference\n"










