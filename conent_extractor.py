import os
import re

def generate_table_of_content(file_path, content_dict):
    table_of_content = ""
    for title, anchor in content_dict.items():
        table_of_content += f"- [{title}]({file_path}#{anchor})\n"
    return table_of_content

def process_md_file(file_path):
    content_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            match = re.match(r'^#{1,6}\s+(.+)$', line)
            if match:
                title = match.group(1).strip()
                anchor = re.sub(r'\s+', '-', title.lower())
                content_dict[title] = anchor
    return content_dict

def main():
    folder_path = "./BTB's Heroes III Modding Guide"  # Change this to the path where your .md files are located
    output_file_path = 'tableofcontent.md'

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write("# Table of Content\n")

        for filename in os.listdir(folder_path):
            if filename.endswith('.md'):
                file_path = os.path.join(folder_path, filename)
                content_dict = process_md_file(file_path)
                if content_dict:
                    output_file.write(generate_table_of_content(file_path, content_dict))
                    output_file.write('\n')

if __name__ == "__main__":
    main()
