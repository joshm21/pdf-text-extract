import pdfplumber

with pdfplumber.open("data.pdf") as pdf:
    output = ""
    
    WIDTH = 612
    HEIGHT = 792
    VERTICAL_CUTOFF = 300

    for page in pdf.pages:
        left = page.within_bbox((0, 0, VERTICAL_CUTOFF, HEIGHT))
        right = page.within_bbox((VERTICAL_CUTOFF+1, 0, WIDTH, HEIGHT))

        output = output + left.extract_text() + "\nColumn Break\n"
        output = output + right.extract_text() + "\nPage Break\n"

with open('output.txt', 'w') as f:
    f.write(output)