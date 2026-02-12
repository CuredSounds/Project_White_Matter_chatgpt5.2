from docx import Document
import os

DOCS_DIR = "documents"

def convert_docx_to_md():
    for filename in os.listdir(DOCS_DIR):
        if filename.endswith(".docx") and not filename.startswith("~"):
            docx_path = os.path.join(DOCS_DIR, filename)
            md_path = os.path.join(DOCS_DIR, filename.replace(".docx", ".md"))
            
            try:
                doc = Document(docx_path)
                text = []
                for para in doc.paragraphs:
                    text.append(para.text)
                
                md_content = "\n\n".join(text)
                
                with open(md_path, "w", encoding="utf-8") as f:
                    f.write(f"# {filename}\n\n{md_content}")
                print(f"Converted: {filename} -> {md_path}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
    convert_docx_to_md()
