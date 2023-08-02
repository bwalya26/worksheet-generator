import PyPDF2

class SequenceSolver:
    def __init__(self, pdf_file):
        self.pdf_file = pdf_file
        self.pdf_writer = PyPDF2.PdfWriter()
    
    def find_nth_term_arithmetic(self, first_term, common_diff, n):
        nth_term = first_term + (n - 1) * common_diff
        return nth_term

    def find_sum_arithmetic(self, first_term, common_diff, n):
        sum_seq = (n / 2) * (2 * first_term + (n - 1) * common_diff)
        return sum_seq

    def find_nth_term_geometric(self, first_term, common_ratio, n):
        nth_term = first_term * (common_ratio ** (n - 1))
        return nth_term

    def find_sum_geometric(self, first_term, common_ratio, n):
        if common_ratio == 1:
            sum_seq = first_term * n
        else:
            sum_seq = first_term * ((common_ratio ** n) - 1) / (common_ratio - 1)
        return sum_seq

    def generate_sequence_pdf(self):
        # Arithmetic sequence
        first_term_arithmetic = 2
        common_diff_arithmetic = 3
        n_arithmetic = 5

        nth_term_arithmetic = self.find_nth_term_arithmetic(first_term_arithmetic, common_diff_arithmetic, n_arithmetic)
        sum_arithmetic = self.find_sum_arithmetic(first_term_arithmetic, common_diff_arithmetic, n_arithmetic)

        # Geometric sequence
        first_term_geometric = 2
        common_ratio_geometric = 3
        n_geometric = 5

        nth_term_geometric = self.find_nth_term_geometric(first_term_geometric, common_ratio_geometric, n_geometric)
        sum_geometric = self.find_sum_geometric(first_term_geometric, common_ratio_geometric, n_geometric)

        # Write questions and solutions to the PDF
        with open(self.pdf_file, "wb") as file:
            self.pdf_writer.addPage(PyPDF2.PageObject(title="Arithmetic Sequence", contents=f"First term: {first_term_arithmetic}\nCommon difference: {common_diff_arithmetic}\nNth term (n = {n_arithmetic}): {nth_term_arithmetic}\nSum (n = {n_arithmetic}): {sum_arithmetic}"))
            self.pdf_writer.addPage(PyPDF2.PageObject(title="Geometric Sequence", contents=f"First term: {first_term_geometric}\nCommon ratio: {common_ratio_geometric}\nNth term (n = {n_geometric}): {nth_term_geometric}\nSum (n = {n_geometric}): {sum_geometric}"))
            self.pdf_writer.write(file)

        print("PDF file created successfully:", self.pdf_file)

# Example usage:
pdf_file = "sequence_questions.pdf"
sequence_solver = SequenceSolver(pdf_file)
sequence_solver.generate_sequence_pdf()
