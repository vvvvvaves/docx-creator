from clause_model import Clause

def set_header_and_footer(doc, header_text, footer_text):
    from docx.shared import Pt
    header = doc.sections[0].header
    footer = doc.sections[0].footer
    
    # Set header text and font size
    header_para = header.paragraphs[0]
    header_para.text = header_text
    header_para.runs[0].font.size = Pt(8)

    # Get the existing table in the footer
    table = footer.tables[0]
    left_cell = table.cell(0, 0)
    left_para = left_cell.paragraphs[0]
    left_para.text = footer_text
    for run in left_para.runs:
        run.font.size = Pt(8)

    right_para = table.cell(0, 1).paragraphs[0]
    for run in right_para.runs:
        run.font.size = Pt(8)

    return doc  

def add_heading(doc, heading_text):
    from docx import Document
    from docx.shared import Pt, RGBColor
    from docx.enum.text import WD_LINE_SPACING
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn

    # Create and configure custom heading style
    custom_style = doc.styles['Title']
    custom_style.font.size = Pt(24)
    custom_style.font.name = 'Arial'
    custom_style.font.color.rgb = RGBColor(0, 166, 80)
    custom_style.paragraph_format.space_after = Pt(7.5)  # 10px bottom padding
    custom_style.paragraph_format.space_before = Pt(0)

    # Remove border by setting it to none using the proper XML structure
    pPr = custom_style._element.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    for border in ['top', 'left', 'bottom', 'right', 'between', 'bar']:
        border_elem = OxmlElement(f'w:{border}')
        border_elem.set(qn('w:val'), 'none')
        border_elem.set(qn('w:sz'), '0')
        border_elem.set(qn('w:space'), '0')
        border_elem.set(qn('w:color'), 'auto')
        pBdr.append(border_elem)
    pPr.append(pBdr)

    # Remove empty paragraphs at the start of the document
    if doc.paragraphs and not doc.paragraphs[0].text.strip():
        p = doc.paragraphs[0]._element
        p.getparent().remove(p)
        p._p = p._element = None

    # Add heading using the custom style
    paragraph = doc.add_paragraph(style='Title')
    run = paragraph.add_run(heading_text)
    # Ensure the run also has Arial font
    run.font.name = 'Arial'

    return doc

def define_styles(doc):
    from docx import Document
    from docx.shared import Pt, RGBColor, Cm
    from docx.enum.text import WD_LINE_SPACING, WD_TAB_ALIGNMENT
    from docx.enum.style import WD_STYLE_TYPE
    from docx.shared import Twips

    # Create paragraph style for the list
    custom_style = doc.styles['Heading 1']
    custom_style.font.size = Pt(14)
    custom_style.font.color.rgb = RGBColor(0, 176, 80)
    custom_style.font.name = 'Arial'
    custom_style.paragraph_format.space_after = Pt(0)
    custom_style.paragraph_format.space_before = Pt(0)
    custom_style.paragraph_format.left_indent = Cm(0)
    custom_style.paragraph_format.right_indent = Cm(0)
    custom_style.paragraph_format.first_line_indent = Cm(0)


    # style = doc.styles.add_style('Clause 1', WD_STYLE_TYPE.PARAGRAPH)
    # style.font.name = 'Arial'
    # style.font.size = Pt(14)
    # style.font.color.rgb = RGBColor(0, 176, 80)  # Standard green

    style = doc.styles.add_style('Clause 2', WD_STYLE_TYPE.PARAGRAPH)
    style.font.name = 'Arial'
    style.font.size = Pt(10)
    indent_coef = 1.26
    style.paragraph_format.first_line_indent = Cm(-indent_coef*1)
    style.paragraph_format.left_indent = Cm(indent_coef*2)  # Set left indent to 0.63 cm

    style = doc.styles.add_style('Clause 3', WD_STYLE_TYPE.PARAGRAPH)
    style.font.name = 'Arial'
    style.font.size = Pt(10)
    style.paragraph_format.first_line_indent = Cm(indent_coef*(-0.5))
    style.paragraph_format.left_indent = Cm(indent_coef*2.5)

    return doc

def add_clauses(doc, clauses: list[dict]):
    from docx.enum.text import WD_LINE_SPACING
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    
    clauses = [Clause.model_validate(clause) for clause in clauses]

    # Enable line numbering using XML elements
    section = doc.sections[-1]._sectPr
    line_num = OxmlElement('w:lnNumType')
    line_num.set(qn('w:start'), '0')  # Start at 1
    line_num.set(qn('w:countBy'), '1')  # Number every line
    line_num.set(qn('w:distance'), '360')  # ~0.5 inch from text
    line_num.set(qn('w:restart'), 'continuous')  # Continuous numbering
    section.append(line_num)

    for i, clause in enumerate(clauses):
        # Add the list item with custom numbering
        paragraph = doc.add_paragraph(style='Heading 1')
        run = paragraph.add_run(f"{i+1}\t")  # Add number
        run = paragraph.add_run(f"{clause.clause_title}")  # Add tab and text

        for j, content in enumerate(clause.clause_content):
            paragraph = doc.add_paragraph(style='Clause 2')
            run = paragraph.add_run(f"{i+1}.{j+1}\t")  # Add number
            run = paragraph.add_run(f"{content.clause_content}")  # Add tab and text

            for k, subclause in enumerate(content.subclauses):
                paragraph = doc.add_paragraph(style='Clause 3')
                letter = chr(ord('a') + k)
                run = paragraph.add_run(f"{letter})\t")  # Add letter and tab
                run = paragraph.add_run(f"{subclause}")  # Add tab and text

    return doc

def set_updatefields_true(doc):
    import lxml
    namespace = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    # add child to doc.settings element
    element_updatefields = lxml.etree.SubElement(
        doc.settings.element, f"{namespace}updateFields"
    )
    element_updatefields.set(f"{namespace}val", "true")
    return doc

def add_table_of_contents(doc):
    from docx.shared import Pt, Inches
    from docx.oxml import OxmlElement, register_element_cls
    from docx.oxml.ns import qn
    from docx.oxml.xmlchemy import BaseOxmlElement
    from docx.enum.section import WD_SECTION
    from docx.enum.style import WD_STYLE_TYPE
    
    # Register the TOC element
    class CT_SdtToc(BaseOxmlElement):
        """Table of contents element class."""
        sdtContent = None
    register_element_cls('w:sdt', CT_SdtToc)
    
    # Create custom TOC styles
    try:
        toc1_style = doc.styles.add_style('toc 1', WD_STYLE_TYPE.PARAGRAPH)
        toc1_style.font.name = 'Arial'
        toc1_style.font.size = Pt(10)
    except:
        # Style might already exist
        toc1_style = doc.styles['toc 1']
        toc1_style.font.name = 'Arial'
        toc1_style.font.size = Pt(10)
    
    # Create a new section for TOC
    new_section = doc.add_section()
    
    # Set section type to continuous and add two columns
    type_element = OxmlElement('w:type')
    type_element.set(qn('w:val'), 'continuous')
    new_section._sectPr.append(type_element)
    
    # Add columns configuration
    cols = OxmlElement('w:cols')
    cols.set(qn('w:num'), '2')
    cols.set(qn('w:space'), '708')  # 0.5 inch in twentieths of a point
    new_section._sectPr.append(cols)
    
    # Create the TOC
    paragraph = doc.add_paragraph()
    # Set paragraph font to Arial and 10pt
    paragraph.style.font.name = 'Arial'
    paragraph.style.font.size = Pt(10)
    
    # Create structured document tag
    sdt = OxmlElement('w:sdt')
    
    # Create SDT properties
    sdtPr = OxmlElement('w:sdtPr')
    
    # Create SDT ID
    sdtId = OxmlElement('w:id')
    sdtId.set(qn('w:val'), '-1202456363')
    sdtPr.append(sdtId)
    
    # Create SDT title
    sdtTitle = OxmlElement('w:docPartObj')
    docPartGallery = OxmlElement('w:docPartGallery')
    docPartGallery.set(qn('w:val'), 'Table of Contents')
    sdtTitle.append(docPartGallery)
    sdtPr.append(sdtTitle)
    
    sdt.append(sdtPr)
    
    # Create SDT content
    sdtContent = OxmlElement('w:sdtContent')
    
    # Create TOC paragraph
    p = OxmlElement('w:p')
    
    # Add paragraph properties for font formatting
    pPr = OxmlElement('w:pPr')
    
    # Create paragraph run properties
    rPr = OxmlElement('w:rPr')
    
    # Set font name to Arial
    rFonts = OxmlElement('w:rFonts')
    rFonts.set(qn('w:ascii'), 'Arial')
    rFonts.set(qn('w:hAnsi'), 'Arial')
    rPr.append(rFonts)
    
    # Set font size to 10pt (20 half-points)
    sz = OxmlElement('w:sz')
    sz.set(qn('w:val'), '20')
    rPr.append(sz)
    
    # Set font size for complex scripts
    szCs = OxmlElement('w:szCs')
    szCs.set(qn('w:val'), '20')
    rPr.append(szCs)
    
    pPr.append(rPr)
    p.append(pPr)
    
    # Create TOC run
    r = OxmlElement('w:r')
    
    # Create TOC field begin
    fldChar1 = OxmlElement('w:fldChar')
    fldChar1.set(qn('w:fldCharType'), 'begin')
    r.append(fldChar1)
    
    # Create TOC instruction text
    instrText = OxmlElement('w:instrText')
    instrText.set(qn('xml:space'), 'preserve')
    # Add \t switch to use built-in TOC heading
    instrText.text = 'TOC \\o "1-3" \\h \\z \\u \\t "TOC Heading,1"'
    r.append(instrText)
    
    # Create TOC field end
    fldChar2 = OxmlElement('w:fldChar')
    fldChar2.set(qn('w:fldCharType'), 'end')
    r.append(fldChar2)
    
    p.append(r)
    sdtContent.append(p)
    sdt.append(sdtContent)
    
    # Add the TOC to the document
    paragraph._p.append(sdt)
    
    # Create another section for the main content with a page break
    final_section = doc.add_section(WD_SECTION.NEW_PAGE)  # This creates a new page
    
    # Reset to single column for the main content
    cols = OxmlElement('w:cols')
    cols.set(qn('w:num'), '1')
    final_section._sectPr.append(cols)
    
    return doc

def add_part_i(doc, rows: list[dict]):
    """
    rows: list[dict]
    keys: query, answer, answer_type
    """
    from docx import Document
    from docx.shared import Pt
    from docx.enum.section import WD_SECTION
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_ALIGN_VERTICAL
    
    # Create individual tables for each row
    from docx.shared import Pt
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    
    for i, row_data in enumerate(rows):
        # Determine which columns to include based on non-empty data
        query = row_data.get('query', '').strip()
        answer = row_data.get('answer', '').strip()
        answer_type = row_data.get('answer_type', '').strip()
        
        # Build list of columns to include
        columns_data = []
        column_alignments = []
        
        is_query = False
        if query:
            columns_data.append(query)
            column_alignments.append(WD_ALIGN_PARAGRAPH.LEFT)
            is_query = True

        if answer:
            columns_data.append(answer)
            column_alignments.append(WD_ALIGN_PARAGRAPH.CENTER)
        
        if answer_type:
            columns_data.append(answer_type)
            column_alignments.append(WD_ALIGN_PARAGRAPH.RIGHT)
        
        # Skip if no data to display
        if not columns_data:
            continue
            
        # Create table with dynamic number of columns
        table = doc.add_table(rows=1, cols=len(columns_data))
        table.style = 'Table Grid'
        
        # Customize table borders
        tbl = table._tbl
        tblPr = tbl.tblPr
        tblBorders = OxmlElement('w:tblBorders')
        
        
        for border_name in ['bottom', 'insideH']:
            border = OxmlElement(f'w:{border_name}')
            border.set(qn('w:val'), 'single')
            border.set(qn('w:sz'), '8')  # 1px = 8 eighths of a point
            border.set(qn('w:space'), '0')
            border.set(qn('w:color'), 'b8b9bb')  # rgb(184, 185, 187) in hex
            tblBorders.append(border)
        
        # Remove vertical borders (left, right, insideV)
        for border_name in ['left', 'right', 'insideV', 'top']:
            border = OxmlElement(f'w:{border_name}')
            border.set(qn('w:val'), 'none')
            border.set(qn('w:sz'), '0')
            border.set(qn('w:space'), '0')
            border.set(qn('w:color'), 'auto')
            tblBorders.append(border)
        
        
        tblPr.append(tblBorders)
        
        row = table.rows[0]
        
        # Set cell margins (10px top and bottom padding)
        for cell in row.cells:
            tc = cell._tc
            tcPr = tc.get_or_add_tcPr()
            tcMar = OxmlElement('w:tcMar')
            
            # Set top margin
            top = OxmlElement('w:top')
            top.set(qn('w:w'), '150')  # 10px in twentieths of a point
            top.set(qn('w:type'), 'dxa')
            tcMar.append(top)
            
            # Set bottom margin
            bottom = OxmlElement('w:bottom')
            bottom.set(qn('w:w'), '150')  # 10px in twentieths of a point
            bottom.set(qn('w:type'), 'dxa')
            tcMar.append(bottom)
            
            tcPr.append(tcMar)
        
        # Fill cells with data and apply formatting
        for j, (data, alignment) in enumerate(zip(columns_data, column_alignments)):
            cell = row.cells[j]
            cell.text = data
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            
            for paragraph in cell.paragraphs:
                paragraph.alignment = alignment
                for run in paragraph.runs:
                    run.font.name = 'Arial'
                    run.font.size = Pt(10)
                    if is_query and j == 0: 
                        run.font.bold = True
        
        # Add some spacing between tables
        # doc.add_paragraph()

    doc.add_section(WD_SECTION.NEW_PAGE)
    
    return doc

def create_docx_file(input_file_name, output_file_name, clauses: list[dict], preamble_rows: list[dict]):
    from docx import Document
    doc = Document(input_file_name)
    doc = define_styles(doc)
    doc = set_header_and_footer(doc, "Header of my document", "Footer of my document")
    doc = add_heading(doc, "Clause Index")
    doc = add_table_of_contents(doc)  # Add TOC after heading
    doc = add_heading(doc, "Preamble")
    doc = add_part_i(doc, preamble_rows)
    doc = add_heading(doc, "Part 2")
    doc = add_clauses(doc, clauses)
    doc = set_updatefields_true(doc)
    doc.save(output_file_name)


if __name__ == "__main__":
    clauses = [
        {
            "clause_number": "1",
            "clause_title": "Lorem Ipsum Dolor",
            "clause_content": [
                {
                    "clause_content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                    "subclauses": ["Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."]
                }
            ]
        },
        {
            "clause_number": "2",
            "clause_title": "Lorem ipsum Dolor",
            "clause_content": [
                {
                    "clause_content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                    "subclauses": ["Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."]
                }
            ]
        }, 
        {
            "clause_number": "3",
            "clause_title": "Lorem ipsum Dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
            "clause_content": [
                {
                    "clause_content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                    "subclauses": ["Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."]
                }
            ]
        },
        
        {
            "clause_number": "4",
            "clause_title": "Lorem ipsum Dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
            "clause_content": [
                {
                    "clause_content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                    "subclauses": ["Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."]
                }
            ]
        },
        {
            "clause_number": "5",
            "clause_title": "Lorem ipsum Dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
            "clause_content": [
                {
                    "clause_content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                    "subclauses": ["Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."]
                }
            ]
        },
        {
            "clause_number": "6",
            "clause_title": "Lorem ipsum Dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
            "clause_content": [
                {
                    "clause_content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                    "subclauses": ["Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."]
                }
            ]
        }
    ]*7

    preamble_rows = [
        {
            "query": "Date:",
            "answer": "2025-06-25",
            "answer_type": ""
        },
        {
            "query": "It is this day agreed between:",
            "answer": "John Doe and Jane Doe",
            "answer_type": ""
        },
        {
            "query": "of (registered address):",
            "answer": "123 Main St, Anytown, USA",
            "answer_type": "(“Owners”)"
        },
        {
            "query": "being the: ",
            "answer": "Owners",
            "answer_type": "(“Owner/Disponent Owner”)"
        },
        {
            "query": "of the Vessel called:",
            "answer": "John Doe and Jane Doe",
            "answer_type": "(“Vessel”)"
        },
        {
            "query": "and",
            "answer": "John Doe and Jane Doe",
            "answer_type": "(“Vessel”)"
        },
        {
            "query": "of",
            "answer": "John Doe and Jane Doe",
            "answer_type": "(“Charterers”)"
        },
        {
            "query": "",
            "answer": "That the service as described below shall be performed subject to the terms and conditions of this Charter, which consists of Part 1 and Part 2 and the completed questionnaire on the latest version of Intertanko Standard Tanker Voyage Chartering Questionnaire 1988 (“the Q88”) attached to this Charter. ",
            "answer_type": ""
        },
    ]*5
    create_docx_file("header_and_footer_empty.docx", "part_ii.docx", clauses, preamble_rows)