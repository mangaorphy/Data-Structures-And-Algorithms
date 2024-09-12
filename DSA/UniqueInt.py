class UniqueIntegerProcessor:
    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.unique_integers = []

    def is_integer(self, s):
        """Check if the string is a valid integer."""
        if s.startswith('-'):
            return s[1:].isdigit()
        return s.isdigit()

    def insert_sorted(self, number):
        """Insert a number into the sorted list of unique integers."""
        if not self.unique_integers:  # If the list is empty
            self.unique_integers.append(number)
            return
        
        for i in range(len(self.unique_integers)):
            if self.unique_integers[i] > number:
                self.unique_integers.insert(i, number)
                return
        
        self.unique_integers.append(number)  # Insert at the end if larger than all

    def process_file(self):
        """Process the input file to extract unique integers."""
        with open(self.input_filename, 'r') as infile:
            for line in infile:
                line = line.strip()  # Remove leading and trailing whitespace
                if not line:  # Skip empty lines
                    continue
                parts = line.split()  # Split on whitespace
                
                if len(parts) != 1 or not self.is_integer(parts[0]):
                    continue  # Skip invalid lines
                    
                number = int(parts[0])  # Convert to integer
                self.insert_sorted(number)  # Insert while maintaining order

        # Write the unique sorted integers to the output file
        self.write_output()

    def write_output(self):
        """Write the unique integers to the output file."""
        with open(self.output_filename, 'w') as outfile:
            for number in self.unique_integers:
                outfile.write(f"{number}\n")


# Example usage with specified input and output files
input_filename = 'sample_01.txt'  # Input file name
output_filename = 'sample_02.txt'  # Output file name
processor = UniqueIntegerProcessor(input_filename, output_filename)
processor.process_file()