import re
import os

file_path = r"c:\Users\Cliente\nicolegrazzioli\resumo\README.md"
# Read file
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
buffer = []
in_code = False

def is_code(line):
    s_line = line.strip()
    if not s_line: return False
    
    # Check for keywords
    keywords = ["class ", "def ", "import ", "from ", "print(", "return ", "pass", "raise ", "yield ", "if ", "else:", "elif ", "for ", "while ", "try:", "except:", "finally:", "with ", "global ", "del ", "break", "continue"]
    if s_line.startswith(tuple(keywords)):
        return True
    
    # Comments: # or *#
    if s_line.startswith("#") or s_line.startswith("*#"):
        if s_line.startswith("##"): return False # Markdown headers
        return True
    
    # Indented lines (2+ spaces or tab) AND not list items
    is_indented = line.startswith("  ") or line.startswith("\t")
    # List items: - text, * text, 1. text
    # Note: s_line strips leading spaces so we check s_line for -, *, 1.
    is_list_item = s_line.startswith("- ") or s_line.startswith("* ") or re.match(r"^\d+\.\s", s_line)
    
    if is_indented and not is_list_item:
        # Check if it looks like text?
        # If it's pure text indented, it might be a blockquote or just formatting.
        # But in this file, indented code is common.
        # Let's assume yes, unless it looks strictly like prose? 
        # Hard to tell. But "mais de uma linha" implies blocks.
        return True

    # Assignment: var = value or var \= value
    # Regex: Start with identifier, optional space, optional backslash, equal sign
    if re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*\s*\\?=\s*", s_line):
        return True
    if re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*\s*\+=\s*", s_line): # +=
        return True

    # Function calls: obj.method() or func()
    # Identifier (dot identifier)* (
    if re.match(r"^[a-zA-Z_][a-zA-Z0-9_\.]*\s*\(", s_line):
         # Check if it's a known non-code pattern? "ex: ..."
         if s_line.lower().startswith("ex:"): return False
         return True
    
    return False

for line in lines:
    # Existing code blocks detection?
    if line.strip().startswith("```"):
         if buffer:
             real_code_lines = [l for l in buffer if l.strip()]
             if len(real_code_lines) > 1:
                  new_lines.append("```\n")
                  new_lines.extend(buffer)
                  new_lines.append("```\n")
             else:
                  new_lines.extend(buffer)
             buffer = []
             in_code = False
         new_lines.append(line)
         # We are now in a pre-existing code block (or ending one). 
         # But wait, this script logic assumes we process the file once.
         # If we find ``` it means existing formatting.
         # We should treat content inside ``` as just text to pass through?
         # Or does this flip a state?
         # The file has some existing blocks.
         # I should track if I am inside an EXISTING block to avoid double wrapping.
         # But my simple logic just flushes buffer and passes line.
         # The next lines will be processed.
         # If I am in an existing block, the next lines will look like code and I will try to buffer them.
         # Then I wrap them again! capture ` ``` code ``` ` -> ` ``` ``` code ``` ``` ` .
         # Bad.
         # So I need `in_existing_block` state.
         continue

    if not line.strip():
        if in_code:
            buffer.append(line)
        else:
            new_lines.append(line)
        continue

    # Handling existing blocks properly:
    # If we hit ```, we flip 'in_existing_block'.
    # While in_existing_block, just append lines.
    # But I can't detect state easily if I just continued loop.
    # Let's rewrite the loop slightly.
    pass

# Refined Loop with existing block handling
new_lines = []
buffer = []
in_code = False
in_existing_block = False

for line in lines:
    s_line = line.strip()
    
    if s_line.startswith("```"):
        if in_code:
            # We were building a detected block, but hit an explicit fence.
            # Close detected block first?
            # Or merge?
            # Likely the detected block should end before this fence.
            real_code_lines = [l for l in buffer if l.strip()]
            if len(real_code_lines) > 1:
                new_lines.append("```\n")
                new_lines.extend(buffer)
                new_lines.append("```\n")
            else:
                new_lines.extend(buffer)
            buffer = []
            in_code = False
        
        new_lines.append(line)
        in_existing_block = not in_existing_block
        continue

    if in_existing_block:
        new_lines.append(line)
        continue

    # Normal processing
    if not s_line:
        if in_code:
            buffer.append(line)
        else:
            new_lines.append(line)
        continue

    if is_code(line):
        if not in_code:
            in_code = True
        buffer.append(line)
    else:
        if in_code:
             real_code_lines = [l for l in buffer if l.strip()]
             if len(real_code_lines) > 1:
                  new_lines.append("```\n")
                  new_lines.extend(buffer)
                  new_lines.append("```\n")
             else:
                  new_lines.extend(buffer)
             buffer = []
             in_code = False
        new_lines.append(line)

# Flush final buffer
if in_code and buffer:
     real_code_lines = [l for l in buffer if l.strip()]
     if len(real_code_lines) > 1:
          new_lines.append("```\n")
          new_lines.extend(buffer)
          new_lines.append("```\n")
     else:
          new_lines.extend(buffer)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
